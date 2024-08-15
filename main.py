import speech_recognition as sr 
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) # Use female voice

def talk(goo):
    engine.say("Hello sir")
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Speak Anything: ")
        audio = listener.listen(source)
        text = listener.recognize_google(audio)
        text = text.lower()
        if "orange" in text:  
            print("You said: ", text)

except:
    pass    
