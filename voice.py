import pyttsx3
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that.")
            return None
        except sr.RequestError as e:
            speak("There was a problem with the request.")
            return None

speak("Hello, I am your voice assistant. What can I do for you?")
while True:
    text = get_audio()
    if text:
        print(text)
        if text.lower() == "quit":
            break
        else:
            speak("I don't understand.")