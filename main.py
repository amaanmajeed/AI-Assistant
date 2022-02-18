#install Pyaudio: https://www.youtube.com/watch?v=mlrxIQRK3SE
import speech_recognition       #pip install SpeechRecognition
import pyttsx3                  #pip install pyttsx3


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


def run_alexa():
    while True:
        command = get_audio()
        print(command)

        if 'hello' in command:
            talk("Hello Sir, How may I help you")
        elif 'sleep' or 'bye bye' in command:
            talk("Ok Sir")
            break
        else:
            talk("Can you say that again")


print('Listening...')
try:
    run_alexa()
except Exception as e:
    print(e)
    pass
