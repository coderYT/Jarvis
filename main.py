import pyttsx3
import speech_recognition as sr

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except Exception as e:
    print(e)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def read_voice_cmd():
    print('Speak...')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        return speech.recognize_google(audio_data=audio).lower()
    except Exception as e:
        print(e)


while True:
    voice_input = read_voice_cmd()
    print('Voice Input : ', voice_input)
    if 'jarvis' in voice_input:
        speak('Hello Sir, How may i help you?')
        continue
    else:
        speak('Command not found.')
        continue
