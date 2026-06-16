import speech_recognition as sr
import webbrowser
import requests
import musicLibrary
import os
from openai import OpenAI
from gtts import gTTS
import pygame

newsapi = "<Your Key Here>"

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
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in the music library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)


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
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
