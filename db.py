import psycopg2 as p
import config
import telebot
import datetime
import timetable
import timetable1
import requests, bs4
import weather

bot = telebot.TeleBot(config.token)
con = p.connect(database='dfq6banncblc4l', user='vtudqaibjctcaw', host='ec2-23-23-142-5.compute-1.amazonaws.com',
                password='d9dcd45b804a1510e232ff7b13f9ff260332692b9328bef3e21b8a752ffb389c')
cur = con.cursor()
a = []


def start(message, fuc, kurs):
    cur.execute("select * from users")
    a.clear()
    for row in cur:
        a.append(row[0])
    print(a)
    if message.from_user.id in a:
        print("УЖЕ СУЩЕСТВУЕТ")
        return "УЖЕ СУЩЕСТВУЕТ"

        a.clear()
    else:
        cur.execute(
            'INSERT INTO users VALUES (' + str(message.from_user.id) + ',' + "'" + fuc + "'" + ',' + str(kurs) + ');')

        con.commit()
        a.clear()
        return "Упешно добавлена"


def rassilka():
    cur.execute("select * from users")
    dn = datetime.date.today().isoweekday()
    if dn == 7:
        dn = 1

    else:
        dn=dn+1
    d= datetime.date.today().day
    m = datetime.date.today().month
    privet=weather.start(d,m)
    privet1 = "Добрый вечер!!! " + '\n' + 'Расписание на завтра:'
    for row in cur:
        print(row[1])
        print(row[2])
        if row[1] in ("МО", "ГМУ", "Лингвистика", "Реклама"):
            if row[1] == 'МО':
                z = timetable1.get_day("МО", int(row[2]), dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'

            elif row[1] == 'ГМУ':
                z = timetable1.get_day("ГМУ", row[2], dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'

            elif row[1] == "Лингвистика":
                z = timetable1.get_day("ЛИНГВ", row[2], dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'

            elif row[1] == "Реклама":
                z = timetable1.get_day("РЕКС", row[2], dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'

            z = privet1 + '\n' + z + '\n' + privet
            z = z.replace("*", "")
            #z = "Прошу прощения за неудобства!!!"
            try:
                bot.send_message(row[0], z)
            except Exception:
                pass
        elif row[1] in ("ПМИ", "Геология", "Химия"):
            if row[1] == 'ПМИ':
                z = timetable.get_day("ПМИИ", int(row[2]), dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'
            elif row[1] == 'Геология':

                z = timetable.get_day("ГЕОЛ", row[2], dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'
                print(z)
            elif row[1] == 'Химия':
                z = timetable.get_day("ХИМФ", row[2], dn)
                k = z.rindex('\n', 0, 21)
                z = z[k + 1:]
                if 'ВЫХОДНОЙ' in z:
                  z='У вас нет пар 😊, ВЫХОДНОЙ 🎉'
            z = z.replace("*", "")
            z = privet1 + '\n' + z + '\n' + privet
            #z="Прошу прощения за неудобства!!!"
            try: bot.send_message(row[0], z)
            except Exception:
                pass
def new_week():
    cur.execute('update config set  name1 = ' + str(int(config.week)+1) + ', name =' + str(int(config.file)+1) + '')
    con.commit()
    cur.execute("select * from config")
    m = cur.fetchall()

    #print(m)
    config.week=m[0][1]
    config.file=m[0][0]
def get_week():
    cur.execute("select * from config")
    m = cur.fetchall()

    # print(m)
    config.week = m[0][1]
    config.file = m[0][0]
def send_me():
    dn = datetime.date.today().isoweekday()
    if dn == 7:
        dn = 1
        config.file= int(config.file)+ 1
        a = str(config.file) + '.xlsx'
        timetable.start(a)
    else:
        dn = dn + 1
    privet1 = "Добрый вечер!!! " + '\n' + 'Рассписание на завтра:'
    a=timetable.get_day("ПМИИ", 3, dn)
    print(a)
