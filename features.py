from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
from time import sleep

import smtplib
import pyperclip
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as pp
import subprocess
import webbrowser as web
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)


def speak(audio):
    print(" ")
    print(f"{audio}")
    print(" ")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning!")
    elif hour>=0 and hour<4:
        speak("It's soo Late!")
    elif hour>=12 and hour<18:
        speak("Good Noon!")
    else:
        speak("Good Evening!")
    speak("Sir I am Jaarvis, Tell me How can I help you")


def takeCommand():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except :
        speak("Say that Again Please...")
        print("Say that Again Please...")
        return "None"
    return query


def intro():
    speak("I am Jaarvis, a Artificial Intelligence and Desktop assistant for you, I can perform any Task, Regarding your PC, just on your voice Command")


def day():
    day = datetime.datetime.now()
    strDay = (day.strftime("%A"))
    speak(f": Today is {strDay}")    


def ipadd():
    ip = requests.get('https://api.ipify.org').text
    speak(f'your IP address is {ip}')


def close():
    speak("OK Sir, Quitting, Have a Nice Day")
    exit()


def youtube(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    speak("This is what I found")
    pp.playonyt(term)
    speak("This may also help you")


def time():
    hour =  int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H %M")
    if hour>=0 and hour <12:
        speak(f": The Time is:{strTime} AM")
    else:
        speak(f": The Time is: {strTime} PM")


def date():
    date = datetime.datetime.now()
    strDate = (date.strftime("%B%d %Y"))
    speak(f":Today's Date is {strDate}")


def wikip(query):
    results =  wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)


def google(query):
    speak("I found this")
    pp.search(query)


def alarm(query):
    TimeHere = open('D:\\BCA III final draft project\\data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    cmd = 'python alarm.py'
    p = subprocess.Popen(cmd, shell=True)
    out, err = p.communicate()
    print(err)
    print(out)


def DownloadYoutube():
    sleep(2)
    click(x=1270,y=65)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('D:\\BCA III final draft project\\DataBase\\Youtube Downloads\\')
    Download(Link)
    speak("Done Sir, I have downloaded the video")
    speak("You can Go and check it out")


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sonironak284@gmail.com','soni284ronak')
    server.sendmail('sonironak284@gmail.com',to,content)
    server.close


def My_Location():
    
    #web.open(op)
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f"Sir, You're now in {state , country}")
