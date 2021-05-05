import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty(voices, voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Jarvis Sir. Please tell me how may I help you')


def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query} \n')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
