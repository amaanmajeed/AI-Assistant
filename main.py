# install Pyaudio: https://www.youtube.com/watch?v=mlrxIQRK3SE
import speech_recognition  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
import pywhatkit  # pip install
import random
import os
import wikipedia
import datetime
import pyautogui
from time import sleep


listener = speech_recognition.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def get_audio():
    command = ''
    while command == '':
        try:
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                print('.')
                r.pause_threshold = 1
                # audio = r.listen(source, timeout=4, phrase_time_limit=7)
                audio = r.listen(source, 0, 4)
                command = r.recognize_google(audio, language='en-in').lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                if 'can you' in command:
                    command = command.replace('can you', '')
                if 'please' in command:
                    command = command.replace('please', '')
        except speech_recognition.UnknownValueError:
            command = get_audio()
    return command


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    print('Welcome back sir!')
    talk('Welcome back sir!')
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        print('Good Morning!')
        talk('Good Morning!')
    elif 12 <= hour <= 24:
        print('Good Evening!')
        talk('Good Evening!')

    print('How may I help you?')
    talk('How may I help you!')


def greet():
    try:
        print('I am splendid, Thank you for asking!')
        talk('I am splendid, Thank you for asking!')

        print('What can I do for you?')
        talk('What can I do for you?')
        run_alexa()
    except Exception as ep:
        print(ep)


def play_youtube(command):
    if 'music' in command:
        talk('Playing some music')
        music_dir = "C:/Users/Hp/Music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))
        print('Playing on music')
    else:
        talk('searching..')
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
        print('playing on youtube')


def wiki_search(command):
    try:
        talk('Searching...')
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        print('searching on wikipedia')
        talk(info)
    except Exception as ep:
        print(ep)
        talk('Unable to find result')


def time():
    this_time = datetime.datetime.now().strftime('%I:%M %p')
    print('The time is ' + this_time)
    talk('The time is ' + this_time)


def date():
    x = datetime.datetime.now()
    talk('Today is ' + x.strftime("%A %d %B %Y"))
    print('Today is ' + x.strftime("%A %d %B %Y"))


def open_app(command):
    print('Opening apps')
    if 'open' in command:
        app = command.replace('open', '')
        if 'task manager' in app:
            pyautogui.hotkey('ctrl', 'shift', 'esc')
            talk('Opening task manager')
        else:
            talk(f'Opening {app}')
            pyautogui.hotkey('win')
            sleep(0.5)
            pyautogui.write(app, interval=0.02)
            pyautogui.hotkey('enter')


def run_alexa():
    while True:
        command = get_audio()
        print(command)

        if 'hello' in command:
            talk("Hello Sir, How may I help you")

        elif 'play' in command:
            play_youtube(command)

        elif 'who' in command:
            if 'made' in command or 'created' in command:  # Who created you
                talk('I was created by Amaan')
                print('who made you')
            else:
                wiki_search(command)

        elif 'time' in command:  # what is the time right now
            time()

        elif 'what' in command:  # what is te date today
            if 'date' in command:
                date()
            elif 'do' in command:
                print('I can tell the time, the date, search the web, play a youtube video, tell you who made me.')
                talk('I can tell the time, the date, search the web, play a youtube video, tell you who made me.')
                print('I can open any app on your system, tell you a joke, toggle between apps, close the apps or ')
                print('close the current tab')
                talk('I can open any app on your system, tell you a joke, toggle between apps, close the apps or '
                     'close the current tab')
                print("you say it, I'll do it.")
                talk("you say it, I'll do it.")
                print('And when you are done, just send me to sleep')
                talk('And when you are done, just send me to sleep')

        elif 'open' in command:  # Open and app
            open_app(command)

        elif 'how are you' in command:                      # Greetings
            greet()

        elif 'sleep' in command:
            talk("Ok Sir")
            break

        elif 'bye bye' in command:
            talk("Byie")
            break

        elif 'close' in command:  # Close
            talk('Sure!')
            if 'app' in command:
                pyautogui.hotkey('alt', 'f4')  # Close this app
                print('closing this app')
            elif 'tab' in command:
                pyautogui.hotkey('ctrl', 'w')  # Close this tab
                print('closing this tab')

        else:
            talk("Can you say that again")


wish_me()
print('Listening...')
try:
    run_alexa()
except Exception as e:
    print(e)
    pass
