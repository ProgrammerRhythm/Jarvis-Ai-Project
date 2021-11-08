import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 100)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning! Rhythm")

    elif hour>=12 and hour<18:
        talk("Good Afternoon! Rhythm")

    else:
        talk("Good Evening! Rhythm")

    talk("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-bd')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        command = takeCommand().lower()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)




        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'open google' in command:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in command:
            webbrowser.open("facebook.com")



        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'say something about' in command:
            person = command.replace('say something about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)



        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'boss' in command:
            talk("Sorry I Don't have boss , But Rhythm Make me")
        elif 'open code' in command:
            codePath = "C:\\Users\\Rhythm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in command:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'open the website' in command:
            codePath = "E:\\Rezwan.com\\index.html"
            os.startfile(codePath)
        elif 'open spotify' in command:
            codePath = "C:\\Users\\Rhythm\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
        elif "is you" in command:
            talk('I am jarvis')
        elif 'what is your name' in command:
            talk('I am jarvis')
        elif 'are you virgin' in command:
            talk('No Rezwan Take it from me')
        elif 'good morning' in command:
            talk('Thank You')
        elif 'good afternoon' in command:
            talk('Thank You')
        elif 'good evening' in command:
            talk('Thank You')
        elif 'good night' in command:
            talk('Thank You')
        elif 'know me' in command:
            talk('who are you')
        elif 'i am' in command:
            talk('Oh,Ok I will try to remember you')
        elif 'My name is' in command:
            talk('Oh,Nice name')
        elif 'thanks' in command:
            talk('welcome')
        elif 'thank you' in command:
            talk('Welcome')
        elif 'welcome' in command:
            talk('Guluglu,Human')
        elif 'am i looking' in command:
            talk('Boss ! You are looking beautiful ')
        elif 'rhythm' in command:
            talk('Rhythm Munshi is a Web Developer from Bangladesh. He is 14 Years Old. He Is Learning Web development for 	the last 1 year.'
                 'By Oneself, I believe someday He will be the most successful in this field. Holder of a big company.')
        elif 'hi' in command:
            talk('Hello boss')
        elif 'hello' in command:
            talk('Hi,How is your day')
        elif 'fine' in command:
            talk('Oh , I see')
        else:
            talk('Please Say me again')
