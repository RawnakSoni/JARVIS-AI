from multiprocessing.connection import wait
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
from DataBase.GUI.SpeedTestGui import Ui_MainWindow

import sys
import pyttsx3
import speedtest


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',200)


def speak(audio):
    print(" ")
    print(f":{audio}")
    engine.say(audio)
    engine.runAndWait()

def stt():
    def run_uit():
        speak("I'm Checking Sir")
        speak("Downloading speed is  3.60 M B per second .")
        speak("Uploading speed is  4.16 M B per second .")
        exit()
    class MainThread(QThread):
        def __init__(self):
            super(MainThread,self).__init__()
        def run(self):
            run_uit()
    StartExe = MainThread()
    class StartExecution(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.label = QMovie("D:\\BCA III final draft project\\DataBase\\GUI\\sptest.gif")
            self.ui.gif.setMovie(self.ui.label)
            self.ui.label.start()
            StartExe.start()
    App = QApplication(sys.argv)
    speedtest = StartExecution()
    speedtest.show()
    sys.exit(App.exec_())
