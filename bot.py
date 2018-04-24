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
        if dn==7 and today.hour==23 and today.minute>51:
            config.file += 1
            a = str(config.file) + '.xlsx'
            timetable.start(a)
            config.week+=1
            a = str(config.week) + '.xlsx'
            timetable1.start(a)
        if today.hour==2:

            db.rassilka()
            time.sleep(3600)
        else:
            time.sleep(600)

print(today.hour)
print(today.minute)
print(today.second)
if __name__ == '__main__':
    main()

