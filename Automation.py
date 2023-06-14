from datetime import datetime
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from time import sleep

import webbrowser as web
import os
import geocoder
import pyttsx3
import speech_recognition as sr

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


def Notepad():
    speak("Tell Me The Query")
    speak("I Am Ready To Write")
    writes = takeCommand()
    time = datetime.now().strftime("%H:%M")
    filename = str(time).replace(":","-") + "-note.txt"
    with open(filename,"w") as file:
        file.write(writes)
    path_1 = "D:\\BCA III final draft project\\" + str(filename)
    path_2 = "D:\\BCA III final draft project\\DataBase\\Notes\\" + str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)


def GoogleMaps(Place):
    Url_Place = "https://www.google.com/maps/place/" + str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place , addressdetails= True)
    target_latlon = location.latitude , location.longitude
    web.open(url=Url_Place)
    location = location.raw['address']
    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    speak(f"Sir ,{Place} is {distance} kilometre away from your location")


def CloseNotepad():
    os.system("TASKKILL /F /im Notepad.exe")






