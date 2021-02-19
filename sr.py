import telebot
import requests
import speech_recognition as sr
import os.path


if os.path.exists("voice.ogg")==0:
    token = ''
    bot = telebot.TeleBot(token)

    @bot.message_handler(content_types=['voice','text'])
    def repeat_all_message(message):
        file_info = bot.get_file(message.voice.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

        with open('voice.ogg','wb') as f:
            f.write(file.content)

    if __name__ == '__main__':
        bot.polling(none_stop=True)

a = 1

#Скачивание FFMpeg        https://github.com/BtbN/FFmpeg-Builds/releases 
#скачивать только   (ffmpeg-n4.3.1-221-gd08bcbffff-win64-gpl-4.3)
#инструкция https://www.youtube.com/watch?v=qjtmgCb8NcE&t=335s
#


while a==1:
    if os.path.exists("voice.ogg")==1:
        if os.path.exists("voice2.wav") == 0:
            print(os.path.exists("voice.ogg"))
            cd = r"C:\Users\admin\PycharmProjects\untitled2"
            command = "ffmpeg -i voice.ogg voice2.wav"        #
            #subprocess.run(cd)
            #subprocess.run(command)
            os.system(cd)
            os.system(command)
        else:
            while a == 1:
                if os.path.exists("voice2.wav") == 1:
                    if os.path.exists("voice2.wav") == 1:
                        r = sr.Recognizer()
                        harvard = sr.AudioFile('voice2.wav')
                        with harvard as source:
                            audio = r.record(source)
                            type(audio)
                            a = r.recognize_google(audio, language='ru-RU')
                        tex = {a.lower()}
                        print(tex)
                        os.remove('/Users/admin/PycharmProjects/untitled2/voice.ogg')
                        os.remove('/Users/admin/PycharmProjects/untitled2/voice2.wav')
