# AudioTranslator Using Whisper.

### I USED REPLIT TO COMPLETE THIS PROJECT AND PYTHON(LANGUAGE)

#### 1.WHISPER AI
#### 2.GOOGLE TRANSLATOR
#### 3.TEXT TO SPEECH
#### 4.FULL STACK
####       --html,css,js and Flask(backend)

Main Purpose of this project is to translate a youtube video to different Languages using Whisper

There are few Steps to do this project

# 1 . Transcribing The Audio

TRANSCRIBING -- It is used to get the text from the audio 

To transcribe we use whisper (There are many which I used still there is no other transcribing AI which is like whisper)

##### To install whisper  :  
      pip install git+https://github.com/openai/whisper.git
##### To get Audio or video we use ffmpeg :  
      pip install ffmpeg

### CODE 

       import whisper
       model = whisper.load_model("base")
       result = model.transcribe(audio_file_path)
       transcribed_text = result["text"]
       print("Transcribed text:", transcribed_text)


# 2 . Translating Audio 

TRANSLATING -- It is the technique which is used to translate To Specific Language

To Translate we can also use whisper but it wont give accurate results 
<br>
To Translate I Used Google Translator.To use this we use the Google Cloud API
<br>
#### STEPS TO GET GOOGLE CLOUD API

###### 1 . Create a Google Cloud Project:
   Go to the Google Cloud Console.
<br>
   Create a new project.

###### 2 . Enable the Translation API:
   In the Google Cloud Console, navigate to the API Library.
<br>
   Search for "Cloud Translation API" and enable it for your project.

###### 3 . Set Up Authentication:
   Create service account credentials:
<br>
   Go to the "IAM & Admin" > "Service Accounts" page in the Google Cloud Console.
<br>
   Create a new service account.
<br>
   Grant it the "Editor" role.
<br>
   Create a JSON key for the service account and download it.

###### 4 . Upload the JSON Key File to Replit

Upload the JSON key file:
        In your Replit project, click on the "Files" tab on the left sidebar.
        Click the "Upload File" button and upload the JSON key file you downloaded.

Set the GOOGLE_APPLICATION_CREDENTIALS environment variable:
        In the "Secrets" section of your Replit project (found in the left sidebar), add a new secret named GOOGLE_APPLICATION_CREDENTIALS.
        Set the value to the path of your JSON key file. For example, if your file is named service-account-file.json, set the value to service-account-file.json.

###### To Translate we use some libraries they are :
      pip install google-cloud-translate

### CODE

      from google.cloud import translate_v2 as translate
      import os
      os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'project.json' // update your json file
      translate_client = translate.Client()
      translation = translate_client.translate(transcribed_text, target_language='te') //telugu
      translated_text = translation['translatedText']
      print("Translated text:", translated_text)

# 3 . TEXT TO SPEECH 

Text-to-Speech -- It is used to convert the translated text to the audio

###### To install it we use GOOGLE TEXT TO SPEECH (GTTS)

      pip install gtts

### CODE

      from gtts import gTTS
      tts = gTTS(translated_text, lang='en')
      tts.save(translated_audio_path)

# 4 . EXTRACTING AUDIO FROM YOUTUBE VIDEO (By URL)

We can use pytube but the audio is not extracting correctly as it shows throtling error
<br>
To not get that error we use yt-dlp PACKAGE

###### To install yt-dlp package :
      pip install yt-dlp

###### To extract Audio From YOUTUBE URL we use
### CODE
      import yt_dlp
       URL of the video you want to download
      video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
      # Define download options
      ydl_opts = {
          'format': 'best',
          'outtmpl': 'downloaded_video.%(ext)s',
      }

      # Download the video
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([video_url])


##### THESE ARE THE STEPS TO CONVERT THE VIDEO TO AUDIO IN DIFFERENT LANGUAGE



## ERRORS WHILE USING FLASK

###### 1 .  we're having trouble while finding this site
<br>
To solve this we should whitlelist that particular domain (This occurs when firewall is blocking this)

###### 2 . Method Not defined
<br>
Check you're code ,  we use @app.route('/')
<br>
if it is app.route('/') and
<br>
@app.route('<foldername>')
<br>

Change it to the @app.route('/') AS IT SHOULD BE CURRENT DIRECTORY

###### 3 . REQUEST URL NOT DEFINED

if there is no folder name which we are using in app.route then it returns this error

# OUTPUT

## The UI is like this

![IMG_20240716_222733](https://github.com/user-attachments/assets/3a73f5b7-0a26-46c2-9a3b-80889dac6e1f)


### Filling the details like the url and giving input language
            
![IMG_20240716_222532](https://github.com/user-attachments/assets/aedbe229-0f88-4534-80da-f22ec85e3edb)

### Giving The Language To Convert

![IMG_20240716_223538](https://github.com/user-attachments/assets/4d097127-72db-468d-9e7e-c4d59da0ffe6)



###  THE FINAL OUTPUT AFTER GIVING THE DETAILS


![IMG_20240716_222600](https://github.com/user-attachments/assets/a75383e9-08b6-4cc2-b648-f43005028ede)
