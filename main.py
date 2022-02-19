import pyttsx3
import speech_recognition as sr

#Install Pyaudio : https://www.youtube.com/watch?v=mlrxIQRK3SE


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)


def speak(audio):
    print("     ")
    Assistant.say(audio)
    print("     ")
    Assistant.runAndWait()


def takecommad():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognising")
            quary = command.recognize_google(audio)
            print(f"You said : {quary}")
        except Exception as Error:
            return "none"

        return quary.lower()


quary = takecommad()

if 'Hello' in quary:
    speak("Hello Sir")
else:
    quary = takecommad()
