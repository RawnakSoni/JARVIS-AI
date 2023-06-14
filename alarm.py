from fileinput import close
from sqlite3 import Time
from playsound import playsound
from requests import delete

import os
import datetime

extracted_time = open('D:\\BCA III final draft project\\data.txt','rt')
time = extracted_time.read()
Time = str(time)

delete_time = open("D:\\BCA III final draft project\\data.txt",'r+')
delete_time.truncate(0)
delete_time.close()


def RingerNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis","")
    time_now = time_now.replace("set alarm for","")
    time_now = time_now.replace("and",":")
    time_now = time_now.replace(" ","")
    Alarm_Time = str(time_now)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == Alarm_Time:
            print("Wake Up")
            os.startfile("D:\\BCA III final draft project\\DataBase\\sounds\\Alarm.mp3")
        elif current_time>Alarm_Time:
            break

RingerNow(Time)