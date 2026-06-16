import speech_recognition as sr
import os
from gtts import gTTS
import pygame
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Pygame mixer once at startup
pygame.mixer.init()

# Configure Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


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
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"You are a virtual assistant named Jarvis. Give short and helpful responses.\n\nUser: {command}"
    )
    return response.text


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
