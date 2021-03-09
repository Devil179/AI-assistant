import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say (audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour>=12 and hour<18:
        speak("good afternoon sir")  

    else:       
        speak("good evening sir")

    speak("I am steve, your personal AI assistant, suggest me, how may i help you")    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")   

    except Exception as e:
        speak("sorry sir cannot catch that , can you please say that again")
        return "None"    
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'what' in query:
            speak('searching google...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("please wait")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("please wait")
            webbrowser.open("google.com")

        elif 'open prime video' in  query:
            speak("please wait")
            webbrowser.open("primevideo.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open call of duty' in query:
           codePath = "C:\\Users\\devil\\Desktop\\Call of Duty Modern Warfare\\iw3sp.exe"  
           os.startfile(codePath)

        elif 'open among us' in query:
            codePath = "C:\\Users\\devil\\Desktop\\Among.Us.v2020.10.22s\\Among.Us.v2020.10.22s\\Among Us\\Among Us.exe"
            os.startfile(codePath)

        elif 'hey steve' in query:
            speak("hello sir")

        elif 'who are you' in query:
            speak("i am steve, your personal AI assistant, suggest me how may i help you")   

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'how are you' in query:
            speak("i am fine sir, let me know your thoughts, please")

        elif 'do you know about cortana' in query:
            speak("yes i know her , and she is a good friend to me")

        elif 'open edge' in query:
            webbrowser.open("bing.com")

        elif 'hey, how are you doing' in query:
            speak("i am doin' great sir")  

        elif 'hello steve' in query:
            speak("hi there, sir")   

        elif 'what about alexa' in query:
            speak("she's also my friend , but not cool")

        elif 'what about cortana' in query:
            speak("she's also my friend , on windows")

        elif 'do you know about assistant' in query:
            speak("yes i know her , and she is also a good friend to me")

        elif 'do you know google assistant , whats about google assistant' in query:
            speak("yes she is also like the others but much better") 

        elif 'do you know about cortana' in query:
            speak("yes i know her")

        elif 'whats about google assistant' in query:
            speak("she is my friend from google") 

        elif 'tell me ' in query: 
            speak('searching google...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("so, it goes like this sir")
            print(results)
            speak(results) 
        
        elif 'thank you' in query:
            speak("it's my job to get you out of trouble sir ")
            exit()

        elif 'bye' in query:
            exit()

        elif 'exit' in query:
            exit()



            
