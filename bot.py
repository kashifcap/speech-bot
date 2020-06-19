import speech_recognition as sr 
import pyttsx3

r = sr.Recognizer()
sample_rate = 48000
chunk_size = 2048

reply = {
    "hi" : "Hi",
    "hello" : "hello",
    "hey" : "hey",
    "your name" : "pybot",
    "who" : "pybot"
} #anytopic

with sr.Microphone(sample_rate= sample_rate, chunk_size= chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    audio = r.listen(source)

try:
    for k,v in reply:
        if k in r.recognize_google(audio).lower():
            engine = pyttsx3.init()
            engine.say(v)
            engine.runAndWait()
        else:
            engine = pyttsx3.init()
            engine.say("Sorry I couldn't understand that")
            engine.runAndWait()

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
