import datetime
import os
import pyttsx3
import smtplib
import wikipedia 
import speech_recognition as sr 
import webbrowser


engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
# print(voice)
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    time=int(datetime.datetime.now().hour)
    if time<12:
        speak("Good Morning Sir")
    elif time>=12 and time<16:
        speak("Good AfterNoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Swwaraa Satish Sadddaaavartei. How may I help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold=1
        # r.energy_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You Said:{query}")
    except Exception:
        print("Say that again...")
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")