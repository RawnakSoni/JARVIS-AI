from multiprocessing.connection import wait
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie 
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindowgui
from features import *
from DataBase.GUI.SpeedTestGraphics import *
from Automation import *
from keyboard import press
from keyboard import press_and_release

import pyttsx3
import speech_recognition as sr
import os
import random
import sys
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',200)


def speak(audio):
    print(" ")
    print(f":{audio}")
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


def taskexe():
    wishMe()

    while True:
        query = takeCommand().lower()
        
        if 'tell me about' in query:
            query = query.replace("tell me about", "")
            wikip(query)


        elif 'who are you' in query or 'introduce yourself' in query:
            intro()
            

        elif 'what is' in query or 'what are' in query or 'google search' in query or 'what do you mean by' in query or 'meaning of' in query or 'who is' in query:
            try:
                query = query.replace("what is", "")
                query = query.replace("google search", "")
                query = query.replace("what do you mean by", "")
                query = query.replace("what are", "")
                query = query.replace("who is", "")
                google(query)
               
            except:
                speak("Sorry sir, I can't found")


        elif 'open command' in query:
            os.system("start cmd")

        
        elif 'on youtube' in query or 'video' in query:
            query = query.replace("play", "")
            query = query.replace("video", "")
            query = query.replace("on youtube", "")
            youtube(query) 


        elif 'the time' in query:                                                                                                                       
            time()

            
        elif 'date' in query:
            date()


        elif 'day' in query:
            day()


        elif 'ip address' in query:
            ipadd()


        elif 'windows' in query:
            cPath = "C:\\"
            os.startfile(cPath)


        elif 'social' in query:
            ePath = "E:\\"
            os.startfile(ePath)


        elif 'games' in query:
            fPath = "F:\\"
            os.startfile(fPath)

    
        elif 'data' in query:
            dPath = "D:\\"
            os.startfile(dPath)

        
        elif 'copy' in query:
            press_and_release('ctrl + c')

        
        elif 'paste' in query:
            press_and_release('ctrl + v')


        elif 'cut' in query:
            press_and_release('ctrl + x')


        
        elif 'WhatsApp' in query:
            Path = "C:\\Users\\HP\\Desktop\\WhatsApp.lnk"
            os.startfile(Path)


        elif 'play music' in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,100)]))


        elif 'play movies' in query:
            movpath = "E:\\Movies"
            os.startfile(movpath)
            speak("You can select your Favorite Movie from here")


        elif 'code' in query:
            gPath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(gPath)


        elif 'home screen' in query or 'minimise' in query:
            press_and_release('windows + m')


        elif 'start' in query:    
            press_and_release('windows')


        elif 'send email' in query:
            try:
                speak("what to send?")
                content = takeCommand()
                to = "inifd.bhilwara@gmail.com"
                sendEmail(to,content)
                speak("Email Sent")
            except Exception as e:
                print(e)
                speak("sorry i can't send")


        elif 'open setting' in query:
            press_and_release('windows + i')


        elif 'close' in query:
            press_and_release('alt + f4')


        elif 'news' in query:
            press_and_release('windows + w')


        elif 'open search' in query:
            press_and_release('windows + s')


        elif 'screenshot' in query:
            press_and_release('windows + SHIFT + s')


        elif 'exit' in query or 'quit' in query:
            close()


        elif 'set alarm' in query:
            alarm(query)

        
        elif 'download' in query:
            DownloadYoutube()


        elif 'note' in query:
            Notepad()


        elif 'dismiss' in query:
            CloseNotepad()

        
        elif 'speed test' in query:
            stt()


        elif 'my location' in query:
            My_Location()


        elif 'where is' in query:
            Place = query.replace("where is", "")
            GoogleMaps(Place)


        elif 'open' in query:
            name = query.replace("open ","")
            NameA = str(name)
            if 'youtube' in NameA:
                web.open("https://www.youtube.com/")
            elif 'instagram' in NameA:
                web.open("https://www.instagram.com/")
            else:
                string = "https://www." + NameA + ".com"
                string_2 = string.replace(" ","")
                web.open(string_2)


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        taskexe()

StartExe = MainThread()
class StartExecution(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindowgui()
        self.gui.setupUi(self)
        self.gui.START.clicked.connect(self.startFunc)
        self.gui.STOP.clicked.connect(self.close)

    def startFunc(self):
        self.gui.label1 = QtGui.QMovie("D:\\BCA III final draft project\\DataBase\\GUI\\gui2.gif")
        self.gui.side1.setMovie(self.gui.label1)
        self.gui.label1.start()
        self.gui.label2 = QtGui.QMovie("D:\\BCA III final draft project\\DataBase\\GUI\\gui7.gif")
        self.gui.side2.setMovie(self.gui.label2)
        self.gui.label2.start()
        StartExe.start()

App = QApplication(sys.argv)
jarvisai = StartExecution()
jarvisai.show()
sys.exit(App.exec_())  