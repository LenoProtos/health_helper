from pydub import AudioSegment
import speech_recognition as sr
import os
import requests

@bot.message_handler(content_types=['voice','text'])       #https://qna.habr.com/q/768647
def repeat_all_message(message):
  file_info = bot.get_file(message.voice.file_id)
  file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

#sound = AudioSegment.from_mp3("/voice/file.mp3")          
#sound.export("/output/path/file.wav", format="wav")

r = sr.Recognizer()
h = sr.AudioFile('/voice/file.wav')
with h as s:
  a = r.record(s)
  tupe(a)
  t = r.recognize_google(audio, language= 'ru-RU')
  print({t.lower()})
  
  
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.mp3')
os.remove(path)
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.wav')
os.remove(path)
