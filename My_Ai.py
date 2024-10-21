# ------IM_VYADAW------
from re import Pattern
from bs4 import BeautifulSoup
import psutil
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import speedtest
import wikipedia
import webbrowser
import os
import smtplib
import os  # For environment variables

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        greeting = "Good Morning"


    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    strTime=datetime.datetime.now().strftime("%H:%M")

    print(f"{greeting} Vishal! the current time is {strTime}. i am  your virtual assistant, How can I help you ?")
    speak(f"{greeting} Vishaal the current time is {strTime}. I am  your virtual assistant, how can I help you ?")


#
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.operation_timeout=None
        r.non_speaking_duration=0.1
        audio = r.listen(source)



    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User  said: {query}\n")
        return query.lower()
    except Exception:
        speak("sir say that again...")
        return "None"




def executeCommand(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'net' in query:
        speak("Checking internet speed...")
        speed = speedtest()
        speak(f"Your internet speed is {speed} Mbps")


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")


    elif 'open code' in query:
        code_path = r"C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(code_path)
        speak("sir vs code open ho gaya hai")
    
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")

    elif 'movie' in query:
        movie_path=r"E:\movie"
        os.startfile(movie_path)

    elif 'open chrome' in query:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(chrome_path)
        speak("sir chrome open ho gaya hai")

    elif 'open brave' in query:
        brave_path = r"C:\Users\Lenovo\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
        os.startfile(brave_path)
        speak("sir brave open ho gaya hai")

    elif 'youtube' in query:
        speak("Sir, what do you want to search on youtube?")
        content = takeCommand()
        url = f"https://www.youtube.com/results?search_query={content}"
        webbrowser.open(url)
        speak("Here is what I found on youtube")
        print(url)

    elif 'google' in query:
        speak("Sir, what do you want to search on google?")
        content = takeCommand()
        url = f"https://www.google.com/search?q={content}"
        webbrowser.open(url)
        
        speak("Here is what I found on google")


    elif 'wikipedia' in query:
        speak("Sir, what do you want to search on wikipedia?")
        content = takeCommand()
        url = f"https://en.wikipedia.org/wiki/{content}"
        webbrowser.open(url)


    elif "temperature" in query:
        search = "temperature in noida "
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current{search} is {temp}")
        print(f"current{search} is {temp}")


    elif "weather" in query:
        search = "temperature in noida"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current{search} is {temp}")
        print(f"current{search} is {temp}")



    elif "exit" in query:
        speak("Goodbye Vishal.")
        return True
    
 
    elif 'set alarm' in query:
        speak("Sir, please tell me the time to set an alarm")
        alarm_time = takeCommand()
        print(alarm_time)
        speak("Sir, I have set an alarm for " + alarm_time + ".")
        return True
    
    elif 'play music' in query:
        music_dir = r"A:\song"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Sir, I am playing music for you.")
    

    elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

    elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

    return False

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if executeCommand(query):
            break