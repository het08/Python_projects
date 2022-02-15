# All the library should be installed to work this program 
# If not installed you can install by pip install
from urllib import request
from numpy import record, true_divide
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb 
import os
import psutil
import pyjokes
import socket
from tkinter import *
import speedtest
import pyautogui
import cv2
import numpy as np

socket.getaddrinfo('localhost', 8080)

# Command for activation of the voice assistance
machine = pyttsx3.init()
voices = machine.getProperty("voices")
machine.setProperty("voice", voices[1].id)
voicerate = 200
machine.setProperty("rate", voicerate)

# Command for speaking the voice
def speak(audio):
    machine.say(audio)
    machine.runAndWait()

# Command for telling time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)

# Command for telling date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)

# Command for wishing
def wakeup_command():
    speak("Hello")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >=18 and hour <= 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night sir")

    speak("mark at your service, how can i help you")

# Command for accepting command from the users
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        speak("Sorry i cannot understand you please repeat again...")
        return "None"

    return query

# Command for telling the cpu battery percentage
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery
    percentage = battery.percent
    speak("battery is at {percentage}")
    
    if percentage >= 75:
        speak("you have enough battery still you can continue your work")
    elif percentage >= 30 and percentage <= 75:
        speak("you have to plug in your charger to work continuously")
    else :
        speak("you need to charge it immediately, or else it will get shutdown")
        
# Command for telling jokes
def jokes():
    speak(pyjokes.get_joke())
    
# Command for taking screenshot
def screenshot():
    s = pyautogui.screenshot()
    s.save(r'C:\\Users\\hetsh\\OneDrive\\Pictures\\Screenshots\\s.png')
    speak("screenshot has been taken successfully")

# Command for checking internet speed    
def internetspeed():
    speak("wait for few seconds, checking the internet speed")
    st = speedtest.Speedtest()
    dl = st.download()
    dl = dl/(1000000)
    up = st.upload()
    up = up/(1000000)
    speak("we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

# Command for screen recording   
def screenrecord():
    screen_size = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))
    
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        
        if cv2.waitKey(1) == ord("x"):
            break
    cv2.destroyAllWindows()
    out.release()
        
# Main command lines
if __name__ == "__main__":
    clear = lambda: os.system("cls")

    clear()
    wakeup_command()

    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()
        
        elif "date" in query:
            date()
        
        elif "stop" in query or "quit" in query or "go offine" in query:
            quit()

        elif "how are you" in query:
            speak("I am fine, thank you")
            speak("How are you, sir")

        elif "i am good" in query or "i am fine" in query:
            speak("Glad to hear that")
        
        elif "i am bad" in query or "i am sick" in query:
            speak("take care of yourself, sir")
            speak("get well soon")

        elif "who created you" in query or "who made you" in query:
            speak("I was designed by, het")

        elif "log out" in query:
            os.system("shutdown /r /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "battery percentage" in query:
            cpu()
        
        elif "joke" in query:
            jokes()
        
        elif "take screenshot" in query:
            screenshot()
            
        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
       
        elif "search in chrome" in query:
            speak("What should i search")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
        
        elif "play song" in query or "play music" in query:
            speak("Playing songs")
            songs_dir = "S:" # Write down your song folder path here
            songs = os.listdir(songs_dir)
            random = os.startfile(os.path.join(songs_dir, songs[1]))
            
        elif "check internet speed" in query or "internet speed" in query:
            internetspeed()
        
        elif "remember this" in query:
            speak("What should i remember")
            note = takecommand()
            file = open("note.txt", "w")
            speak("should i inlcude date and time")
            snfm = takecommand()
            if "yes" in snfm or "sure" in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write("  :-  ")
                file.write(note)
            else:
                file.write(note)
        
        elif "what did you remember" in query:
            speak("You told me this to remember")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "open youtube" in query:
            speak("opening youtube")
            wb.open_new_tab("https://www.youtube.com")

        elif "open google" in query:
            speak("opening google")
            wb.open_new_tab("https://www.google.com")

        elif "open instagram" in query:
            speak("opening instagram")
            wb.open_new_tab("https://www.instagram.com")

        elif "open facebook" in query:
            speak("opening facebook")
            wb.open_new_tab("https://www.facebook.com")

        elif "open whatsapp" in query:
            speak("opening whatsapp")
            wb.open_new_tab("https://www.whatsapp.com")

        elif "open spotify" in query:
            speak("opening spotify")
            wb.open_new_tab("https://www.spotify.com")
            
        elif "start screen recording" in query:
            screenrecord()

        elif "weather report" in query:
            api_key = "" #Enter your API key
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takecommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = request.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                
        