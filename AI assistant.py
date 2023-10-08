import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, sir")

    elif 12 <= hour < 18:
        speak("Good afternoon, sir")

    else:
        speak("Good evening, sir")

    speak("I am Steve, your personal AI assistant. How may I help you?")

# Function to recognize user's voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, sir. I couldn't catch that. Can you please say that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'what' in query:
            speak('Searching Google...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Please wait")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Please wait")
            webbrowser.open("https://www.google.com")

        elif 'open prime video' in query:
            speak("Please wait")
            webbrowser.open("https://www.primevideo.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'hey steve' in query:
            speak("Hello, sir")

        elif 'who are you' in query:
            speak("I am Steve, your personal AI assistant. How may I help you?")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")

        elif 'how are you' in query:
            speak("I am fine, sir. Let me know your thoughts, please")

        # Add more commands here...

        elif 'thank you' in query:
            speak("It's my job to get you out of trouble, sir.")
            exit()

        elif 'bye' in query:
            exit()

        elif 'exit' in query:
            exit()

            
