from flask import Flask, request, jsonify, render_template, send_from_directory
from gtts import gTTS
import os
import whisper
from google.cloud import translate_v2 as conversion
from werkzeug.utils import secure_filename
import yt_dlp

app = Flask(__name__)

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'project.json'

# Initialize the Google Cloud Translation client
translate_client = conversion.Client()

# Load the Whisper model
model = whisper.load_model("base")

UPLOAD_FOLDER = 'uploads'
TRANSLATE_FOLDER = 'translated'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSLATE_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

def download_audio_from_youtube(youtube_url, output_path='downloads'):
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        # Set up yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        # Find the downloaded file
        for file in os.listdir(output_path):
            if file.endswith(".mp3"):
                return os.path.join(output_path, file)

    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None

def transcribe_translated(audio_file_path, target_language):
    try:
        # Transcribe the audio file using Whisper
        result = model.transcribe(audio_file_path, beam_size=5)
        transcribed_text = result["text"]
        print("Transcribed text:", transcribed_text)
        # Translate the transcribed text using Google Cloud Translate
        translation = translate_client.translate(transcribed_text, target_language=target_language)
        translated_text = translation['translatedText']
        print("Translated text:", translated_text)
        return translated_text
    except Exception as e:
        print(f"Error in transcribe_and_translate: {e}")
    return None

@app.route('/translate', methods=['POST'])
def translate():
    try:
        audio_file = request.files.get('audioFile')
        youtube_url = request.form.get('youtubeUrl')
        language = request.form.get('language')

        if not language:
            return jsonify({'error': 'Language parameter is required'}), 400

        if audio_file:
            if audio_file.filename:
                filename = secure_filename(audio_file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                audio_file.save(file_path)
            else:
                return jsonify({'error': 'Invalid audio file'}), 400
        elif youtube_url:
            file_path = download_audio_from_youtube(youtube_url, output_path=app.config['UPLOAD_FOLDER'])
            if not file_path:
                return jsonify({'error': 'Failed to download audio from YouTube URL'}), 400
            filename = os.path.basename(file_path)
        else:
            return jsonify({'error': 'No audio file or YouTube URL provided'}), 400

        # Perform transcription and translation
        translated_text = transcribe_translated(file_path, language)
        if translated_text is None:
            return jsonify({'error': 'Failed to transcribe and translate the audio file'}), 500

        # Convert translated text to audio using gTTS
        tts = gTTS(translated_text, lang=language)
        translated_audio_path = os.path.join(TRANSLATE_FOLDER, f"{os.path.splitext(filename)[0]}_translated.mp3")
        tts.save(translated_audio_path)

        return jsonify({'audioUrl': f"/translated/{os.path.basename(translated_audio_path)}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/translated/<filename>')
def download_file(filename):
    try:
        return send_from_directory(TRANSLATE_FOLDER, filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


