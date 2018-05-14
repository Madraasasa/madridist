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
        today = datetime.datetime.now()
        today = datetime.datetime.now()
        dn = datetime.date.today().isoweekday()
        if dn==7 and today.hour==23:
            db.new_week()
            print(config.file)
        if today.hour==14 and today.minute<30:
            if dn==7:
                config.file += 1
                a = str(config.file) + '.xlsx'
                timetable.start(a)
                config.week += 1
                a = str(config.week) + '.xlsx'
                timetable1.start(a)

            db.rassilka()
            time.sleep(23*3600)
        else:
            time.sleep(600)

print(today.hour)
print(today.minute)
print(today.second)
if __name__ == '__main__':
    main()

