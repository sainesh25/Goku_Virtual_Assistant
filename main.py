import speech_recognition as sr
import webbrowser
import pyttsx3

import musicLibrary
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processRequest(c):
    if 'open google' in c.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://youtube.com')
    elif 'open my linkedin profile' in c.lower():
        webbrowser.open('https://linkedin.com/in/sainesh-patil/')
    elif 'open SP Gmail' in c.lower():
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    elif 'open whatsapp' in c.lower():
        webbrowser.open('https://web.whatsapp.com/')
    elif c.lower().startswith('play'):
        song = c.lower().split(' ')[1]
        link = musicLibrary.music[song]
        print(link)
        webbrowser.open(link)    
    
        
if __name__ == "__main__":
    speak('Initializing Goku......')
    