from pydub import AudioSegment
import speech_recognition as sr

#sound = AudioSegment.from_mp3("/path/to/file.mp3")
#sound.export("/output/path/file.wav", format="wav")

r = sr.Recognizer()
h = sr.AudioFile('/output/path/file.wav')
with h as s:
  a = r.record(s)
  tupe(a)
  t = r.recognize_google(audio, language= 'ru-RU')
  print({t.lower()})
