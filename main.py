import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engin = pyttsx3.init()

def speak(text):
    engin.say(text)
    engin.runAndWait()

if __name__ == "__main__":
    speak('Initializing Goku......')
    