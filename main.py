import speech_recognition as sr
import pyttsx3
import datetime
import os
import time
import subprocess
import webbrowser
import json
import requests
from subprocess import Popen
from AppOpener import run
from spotify_local import SpotifyLocal


print('Loading your AI personal assistant - spot e')
#set up speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant spot e")




if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "okay bye" in statement or "stop" in statement:
            speak('your personal assistant spot e is shutting down,Good bye')
            print('your personal assistant spot e is shutting down,Good bye')
            break
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open spotify' in statement:
            run("spotify")
            speak("spotify is open now")
            time.sleep(5)
        elif 'pause spotify' in statement:
            with SpotifyLocal() as s:
                s.pause()
            speak("spotify paused")
            time.sleep(5)


        
