## AudioTranslator Using Whisper.

# I USED REPLIT TO COMPLETE THIS PROJECT AND PYTHON(LANGUAGE)

#### 1.WHISPER AI
#### 2.GOOGLE TRANSLATOR
#### 3.TEXT TO SPEECH
#### 4.FULL STACK
      -- html,css,js and Flask(backend)

Main Puropose of this project is to translate a youtube video to different Languages using Whisper

There are few Steps to do this project

# 1 . Transcribing The Audio

TRANSCRIBING -- It is used to get the text from the audio 

To transcribe we use whisper (There are many which I used still there is no other transcribing AI which is like whisper)

To install whisper  :  pip install git+https://github.com/openai/whisper.git <br>
To get Audio or video we use ffmpeg :  pip install ffmpeg

### CODE 

##### import whisper
##### model = whisper.load_model("base")
##### result = model.transcribe(audio_file_path)
##### transcribed_text = result["text"]
##### print("Transcribed text:", transcribed_text)


