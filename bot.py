import speech_recognition as sr 

r = sr.Recognizer()
sample_rate = 48000
chunk_size = 2048


with sr.Microphone(sample_rate= sample_rate, chunk_size= chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
