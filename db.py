import psycopg2 as p
import config
import telebot
import datetime
import timetable
import timetable1
bot = telebot.TeleBot(config.token)
con = p.connect(database='dfq6banncblc4l', user='vtudqaibjctcaw', host='ec2-23-23-142-5.compute-1.amazonaws.com', password='d9dcd45b804a1510e232ff7b13f9ff260332692b9328bef3e21b8a752ffb389c')
cur=con.cursor()
a=[]
def start(message,fuc,kurs):
    cur.execute('select * from users')
    con.commit()
    a.clear()
    for row in cur:
        a.append(row[0])
    print(a)
    if message.from_user.id in a:
        cur.execute('update  users set name = ' + str(message.from_user.id) + ', fuck = ' + "'" + fuc + "'" + ', kurs = ' + str(kurs) + ', username = ' + "'" + str(message.from_user.username) + "'" + ' where name = ' + str(message.from_user.id)+';')
        con.commit()
        return "Подписка обновлена"
        a.clear()
    else:
        cur.execute('INSERT INTO users VALUES ('+str(message.from_user.id)+','+"'"+fuc+"'"+','+str(kurs)+','+ "'" + str(message.from_user.username) + "'"+');')
        con.commit()
        a.clear()
        return "Успешно добавлена"
def rassilka():
    cur.execute("select * from users")
    dn = datetime.date.today().isoweekday()
    for row in cur:
        print(row[1])
        print(row[2])
        if row[1] in ("МО", "ГМУ","Лингвистика", "Реклама"):
            if row[1] == 'МО':
                z = timetable1.get_day("МО", int(row[2]), dn)
            elif row[1] == 'ГМУ':

                z = timetable1.get_day("ГМУ", row[2], dn)
            elif row[1] == "Лингвистика":
                z = timetable1.get_day("ЛИНГВ", row[2], dn)
            bot.send_message(row[0], z,  parse_mode='markdown')
        elif row[1] in ("ПМИ", "Геология","Химия"):
            if row[1] == 'ПМИ':
                z = timetable.get_day("ПМИИ",int(row[2]), dn)
            elif row[1] == 'Геология':

                z = timetable.get_day("ГЕОЛ", row[2], dn)
                print(z)
            elif row[1] == 'Химия':
                z = timetable.get_day("ХФММ", row[2], dn)
            bot.send_message(row[0], z, parse_mode='markdown')
def new_week():
    cur.execute("select * from config")
    m = cur.fetchall()

    #print(m)
    config.week=m[0][1]
    config.file=m[0][0]
def search_my(message):
    cur.execute('select * from users where name='+str(message.from_user.id))
    m=cur.fetchall()
    return m