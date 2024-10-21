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

#laptop britness 
def setBrightness():
    os.system('brightness 50')
    speak("Brightness set to 50%")
#laptop volume
def setVolume():
    os.system('amixer set Master 50%')
    speak("Volume set to 50%")
# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your-email@gmail.com", "your-password")
    server.sendmail("your-email@gmail.com", to, content)
    server.close()


#vs code close 

def Codeband():
    os.system('taskkill /im code.exe /f')
    speak("Vs code closed")
    #vs code open
def Codeon():
    os.system('code')
    speak("Vs code opened")



#NEW FUNCTIO ADD  KARO 
def add():
    speak("Enter first number")
    num1 = int(input("Enter first number: "))
    speak("Enter second number")
    num2 = int(input("Enter second number: "))
    speak("Adding...")
    ans = num1 + num2
    speak("The answer is ")
    speak(ans)
    return ans

#NEW FUNCTIO SUB  KARO
def sub():
    speak("Enter first number")
    num1 = int(input("Enter first number: "))
    speak("Enter second number")
    num2 = int(input("Enter second number: "))
    speak("Subtracting...")
    ans = num1 - num2
    speak("The answer is ")
    speak(ans)
    return ans
#NEW FUNCTIO MUL  KARO
def mul():
    speak("Enter first number")
    num1 = int(input("Enter first number: "))
    speak("Enter second number")
    num2 = int(input("Enter second number: "))
    speak("Multiplying...")
    ans = num1 * num2
    speak("The answer is ")
    speak(ans)
    return ans
#NEW FUNCTIO DIV  KARO
def div():
    speak("Enter first number")
    num1 = int(input("Enter first number: "))
    speak("Enter second number")
    num2 = int(input("Enter second number: "))
    speak("Dividing...")
    ans = num1 / num2
    speak("The answer is ")
    speak(ans)
    return ans
#NEW FUNCTIO MOD  KARO
def mod():
    speak("Enter first number")
    num1 = int(input("Enter first number: "))
    speak("Enter second number")
    num2 = int(input("Enter second number: "))
    speak("Finding modulus...")
    ans = num1 % num2
    speak("The answer is ")
    speak(ans)
    return ans





# Function to get the weather details
# def getWeather():
#     api_key = " your-api-key"

#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     complete_url = base_url + "appid=" + api_key + "&q=London"
#     response = requests.get(complete_url)
#     x = response.json()
#     if x["cod"] != "404":
#         y = x["main"]
#         current_temperature = y["temp"]
#         current_humidiy = y["humidity"]
#         speak("Temperature in London is " + str(current_temperature) + " degree celcius")
#         speak("Humidity in London is " + str(current_humidiy) + "%")




#battry  percentage
def BatteryPercentage():
    return psutil.sensors_battery().percent
#laptop full charge ho gaya hai
def isFullCharge():
    return psutil.sensors_battery().power_plugged

#laptop charge percentage

def getChargePercentage():
    return psutil.sensors_battery().percent

#laptop ko charge me lagate hi bole 
def laptopCharge():
    speak("Laptop is charging...")
    return psutil.sensors_battery().power_plugged

#laptop ko charge me nahi lagate hi bole
def laptopNotCharge():
    speak("Laptop is not charging...")
    return psutil.sensors_battery().power_plugged

#laptop charge percentage
def laptopChargePercentage():
    speak("Laptop is charging...")
    return psutil.sensors_battery().percent


#laptop battry low

def isLowBattery():
    return psutil.sensors_battery().percent < 20

#agar laptop ke samne koi nahi hai to laptop apne aap lock ho jaye 
def lockLaptop():
    speak("locking laptop")
    os.system('gnome-screensaver-command -l')


def executeCommand(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif "screen britness" in query:
        setBrightness()

    elif "volume" in query:
        setVolume()
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")


    elif 'open code' in query:
    # Define the path to Visual Studio Code
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


    elif 'email to harry' in query:
        speak("What should I say?")
        content = takeCommand()
        to = "harryyourEmail@gmail.com"
        sendEmail(to, content)
    
    elif "temperature" in query:
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current{search} is {temp}")
        print(f"current{search} is {temp}")

    elif "weather" in query:
        search = "temperature in delhi"
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

    elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

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