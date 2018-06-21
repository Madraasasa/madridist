# -*- coding: utf-8 -*-
import config
import telebot
import time
import db
import datetime
import timetable
import timetable1
a=str(config.file)+'.xlsx'
timetable.start(a)
a=str(config.week)+'.xlsx'
timetable1.start(a)
today = datetime.datetime.now()
dn = datetime.date.today().isoweekday()
def main():
       
    while True:
        print('1')
        dn = datetime.date.today().isoweekday()
        today = datetime.datetime.now()
        if dn==7 and today.hour==23:
            db.new_week()
            time.sleep(3600)
        db.get_week()
        if today.hour==15 and today.minute<10:
            db.get_week()
            if dn==7:
                config.file = int(config.file) + 1
                config.week = int(config.week) + 1
            a = str(config.file) + '.xlsx'
            timetable.start(a)
            a = str(config.week) + '.xlsx'
            timetable1.start(a)
            db.rassilka()
            time.sleep(3600)
        elif today.hour==11 and today.minute<10:
            db.get_week()
            if dn==7:
                config.file = int(config.file) + 1
                config.week = int(config.week) + 1
            a = str(config.file) + '.xlsx'
            timetable.start(a)
            a = str(config.week) + '.xlsx'
            timetable1.start(a)
            db.send_me()
            time.sleep(600)
        else:

            db.get_week()
            print(config.file)
            time.sleep(600)

print(today.hour)
print(today.minute)
print(today.second)
if __name__ == '__main__':
    main()

