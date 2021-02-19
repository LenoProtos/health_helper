import telebot
import requests
import speech_recognition as sr
import os.path
#import pandas
#import subprocess
#import soundfile as sf

token = '1566451163:AAGZ7duum1_kPdppyZ3HaXxyPh3zaQpxaT8'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['voice','text'])
def repeat_all_message(message):
  file_info = bot.get_file(message.voice.file_id)
  file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

  with open('voice.ogg','wb') as f:
    f.write(file.content)

if __name__ == '__main__':
   bot.polling(none_stop=True)

if os.path.exists("voice.ogg")==1:
    print(os.path.exists("voice.ogg"))
    cd = r"C:\Users\admin\PycharmProjects\untitled2"  #ffmpeg-n4.3.1-221-gd08bcbffff-win64-gpl-4.3
    command = "ffmpeg -i voice.ogg voice3.wav"        #https://www.youtube.com/watch?v=qjtmgCb8NcE&t=335s
    #subprocess.run(cd)                               #https://www.youtube.com/watch?v=3oNWzAsfZQg
    #subprocess.run(command)
    os.system(cd)
    os.system(command)




while os.path.exists("2voice.wav")==1:
    r = sr.Recognizer()
    harvard = sr.AudioFile('2voice.wav')
    with harvard as source:
        audio = r.record(source)
        type(audio)
        a = r.recognize_google(audio, language= 'ru-RU')
    tex = {a.lower()}
    print(tex)
