import speech_recognition as sr
import os
from openai import OpenAI
from gtts import gTTS
import pygame

# Initialize Pygame mixer once at startup
pygame.mixer.init()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis. Give short and helpful responses."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    r = sr.Recognizer()
    while True:
        print("Listening...")
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                speak(aiProcess(command))
        except Exception as e:
            print(f"Error: {e}")
