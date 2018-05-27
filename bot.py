# -*- coding: utf-8 -*-
import config
import telebot
import datetime
import timetable
import timetable1
import db
from telebot import types
a=str(config.file)+'.xlsx'
timetable.start(a)
a=str(config.week)+'.xlsx'
timetable1.start(a)
today = datetime.datetime.now()
bot = telebot.TeleBot(config.token)
if (today.day==1 and today.hour==0):
    config.file=config.file+1
    config.week=config.week+1
@bot.message_handler(commands=["start"])
def handle_start(message):

    user_makeup=telebot.types.ReplyKeyboardMarkup(True,False)
    user_makeup.row('вначало')
    user_makeup.row('расписание')
    user_makeup.row('Моё расписание на сегодня')
    user_makeup.row('регистрация на подписку')

    bot.send_message(message.chat.id, 'Добро пожаловать ' + str(message.from_user.first_name),
                     reply_markup=user_makeup)
'''def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)'''


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'расписание':
        a=config.file
        b=config.week
        db.new_week()
        if config.file!= a :
            print("да")
            a = str(config.file) + '.xlsx'
            timetable.start(a)
            a = str(config.week) + '.xlsx'
            timetable1.start(a)
        keyboard=types.ReplyKeyboardMarkup()
        keyboard.add('ЕНФ')
        keyboard.add('ГФ')
        message1=bot.send_message(message.chat.id,'выберите факультет',reply_markup=keyboard)
        bot.register_next_step_handler(message1, fuc)
        #rasp_type(message)
    elif message.text =='вначало':
        handle_start(message)
        #bot.send_message(message.chat.id, "Подписка разрабатывается")
    elif message.text=="регистрация на подписку":
        regist(message)
    elif message.text=='Моё расписание на сегодня':
        res=db.search_my(message)
        if res!=[]:
            my_time(message, res)
        else:
            bot.send_message(message.chat.id, "Вы не подписаны на расписание 😣 \nнажмите на кнопку  \n'регистрация на подписку'")
            handle_start(message);
    else:
        bot.send_message(message.chat.id,"НЕПРАВИЛЬНАЯ КОМАНДА ")
        handle_start(message);
def my_time(message, res):
    print(res)
    pr= res[0][1]
    kr=res[0][2]
    print(pr)
    print(kr)
    dn = datetime.date.today().isoweekday()
    if pr in ("МО", "ГМУ", "Лингвистика", 'Реклама'):
        z=timetable1.get_day(pr,kr, dn)
    else:
        z=timetable.get_day(pr,kr, dn)
    bot.send_message(message.chat.id, z)
    bot.send_message(message.chat.id, "для продолжения нажмите на /start")

def regist(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    today = datetime.date.today().isoweekday()
    keyboard1.add("МО", "ГМУ","Лингвистика", "Реклама")
    keyboard1.add("ПМИ","Геология", "Химия")
    message1 = bot.send_message(message.chat.id, 'выберите направление', reply_markup=keyboard1)
    bot.register_next_step_handler(message, regist1)
def regist1(message):
    from telebot import types
    config.pod_pr=message.text
    pr=message.text
    if pr in ("МО", "ГМУ","Лингвистика","ПМИ","Геология", "Химия"):
        keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard2.add("1-ый курс", '2-ой курс')
        keyboard2.add('3-ий курс', '4-ый курс')
        bot.send_message(message.chat.id, 'выберите направление', reply_markup=keyboard2)
        bot.register_next_step_handler(message,start)
    elif pr=="Реклама":
        start(message)
def start(message):
    pr=config.pod_pr
    kr=message.text
    if pr in ("МО", "ГМУ", "Лингвистика","ПМИ","Геология", "Химия"):
        z=db.start(message,pr,kr[0])
        bot.send_message(message.chat.id,z)
        handle_start(message)
    elif pr=="Реклама":
        z=db.start(message, pr, 0)
        bot.send_message(message.chat.id, z)
        handle_start(message)
def fuc(message):
    if message.text=='ЕНФ':
        rasp_type(message)
    elif message.text=='ГФ':
        rasp_type1(message)
def rasp_type1(message):
    from telebot import types
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    today = datetime.datetime.now()
    keyboard1.add("Расписание на сегодня")
    keyboard1.add("Расписание на оставшиеся дни")
    if (today.isoweekday() == 7) or (today.isoweekday() == 6 and today.hour >= 15):
        keyboard1.add("Расписание на след неделю")
    keyboard1.add("Назад")

    message1 = bot.send_message(message.chat.id, 'выберите тип расписания', reply_markup=keyboard1)
    bot.register_next_step_handler(message1, start_m1)
def start_m1(message):
    if message.text in ("Расписание на сегодня","Расписание на оставшиеся дни","Расписание на след неделю"):
        config.rasp_type=message.text
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today = datetime.date.today().isoweekday()
        keyboard1.add("МО","ГМУ")
        keyboard1.add("Лингвистика","Реклама")
        keyboard1.add("Назад")
        message1 = bot.send_message(message.chat.id, 'выберите направление', reply_markup=keyboard1)
        bot.register_next_step_handler(message1, start_nap1)
    elif message.text=="Назад":
        fuc(message)

    else:
        bot.send_message(message.chat.id, "выбран неправельный тип расписания")
        rasp_type1(message)
def start_nap1(message1):
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    pr = (message1.text)
    if pr in ("МО", "ГМУ", "Лингвистика", 'Реклама'):
        config.pr = pr
        keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard2.add("1-ый курс", '2-ой курс')
        keyboard2.add('3-ий курс', '4-ый курс')
        keyboard2.add("Назад")
        if pr =='Реклама':
            if (config.rasp_type == 'Расписание на сегодня'):
                 start_kur1(message1)
                 return 0
            elif (config.rasp_type == "Расписание на оставшиеся дни"):
                pasp_ned1(message1)
                return 0
            elif (config.rasp_type == "Расписание на след неделю"):
                a = config.file
                # print(z)
                config.file = a

                past_nex_ned1(message1)
                return 0
        bot.send_message(message1.chat.id, 'Теперь выбери курс', reply_markup=keyboard2)
        if (config.rasp_type == 'Расписание на сегодня'):
            bot.register_next_step_handler(message1, start_kur1)
        elif (config.rasp_type == "Расписание на оставшиеся дни"):
            bot.register_next_step_handler(message1, pasp_ned1)
        elif (config.rasp_type == "Расписание на след неделю"):
            a = config.file
            # print(z)
            config.file = a

            bot.register_next_step_handler(message1, past_nex_ned1)


    elif pr == "Назад":
        rasp_type1(message1)

    else:
        bot.send_message(message1.chat.id, 'ошибка выберите направление')
        bot.register_next_step_handler(message1, start_nap1)
def start_kur1(message1):
    pr = config.pr
    f = open('text.txt', 'r')
    a = f.read()
    f.close()
    # print(a)
    a = a.split()
    if str(message1.chat.id) not in a:
        f = open('text.txt', 'a')
        f.write(
            str(message1.chat.id) + ' ' + str(message1.from_user.first_name) + ' ' + str(message1.from_user.last_name))
    f.close()
    print(message1.chat.id)
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    kr = message1.text
    # print(kr)
    if pr =="Реклама":
        dn = datetime.date.today().isoweekday()
        bot.send_message(message1.chat.id, 'загрузка с файла...')
        z = timetable1.get_day("РЕКС",0, dn)
        bot.send_message(message1.chat.id, z, reply_markup=user_makeup, parse_mode='markdown')
        bot.send_message(message1.chat.id, "для продолжения нажмите на /start")
        return 0
    if kr[0] in ("1", "2", "3", "4") :
        dn = datetime.date.today().isoweekday()
        bot.send_message(message1.chat.id, 'загрузка с файла...')
        # rasp.start()
        if pr == 'МО':
            z = timetable1.get_day("МО", int(kr[0]), dn)
        elif pr == 'ГМУ':

            z = timetable1.get_day("ГМУ", int(kr[0]), dn)
        elif pr =="Лингвистика":
            z=timetable1.get_day("ЛИНГВ",int(kr[0]), dn)
        try:
            bot.send_message(message1.chat.id, z, reply_markup=user_makeup, parse_mode='markdown')
        # bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        except:
            bot.send_message(message1.chat.id, z, reply_markup=user_makeup)
        # handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на /start")

    elif kr == "Назад":
        start_nap1(message1)
    else:
        bot.send_message(message1.chat.id, 'ошибка выберите курс')
        bot.register_next_step_handler(message1, start_kur1)
def pasp_ned1(message1):
    pr = config.pr
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    kr = message1.text
    print(kr)
    z = ''
    dn = datetime.date.today().isoweekday()
    if kr[0] in ("1", "2", "3", "4"):
        bot.send_message(message1.chat.id, 'загрузка расписания...')
        # rasp.start()
        if pr == 'МО':
            z = timetable1.get_last_day("МО", int(kr[0]), dn)
        elif pr == 'ГМУ':

            z = timetable1.get_last_day("ГМУ", int(kr[0]), dn)
            print(z)
        elif pr == 'Лингвистика':
            z = timetable1.get_last_day("ЛИНГВ", int(kr[0]), dn)


        bot.send_message(message1.chat.id, z, parse_mode='markdown', reply_markup=user_makeup)
        # bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        # rasp_t=config.rasp_type

        # bot.send_message(message1.chat.id, z, parse_mode='markdown')
        # handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на  /start")
    elif pr == "Реклама":
        z = timetable1.get_last_day("РЕКС", 0, dn)
        bot.send_message(message1.chat.id, z, parse_mode='markdown', reply_markup=user_makeup)
        # bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        # rasp_t=config.rasp_type

        # bot.send_message(message1.chat.id, z, parse_mode='markdown')
        # handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на  /start")
    elif kr == "Назад":
        start_nap1(message1)
    else:
        bot.send_message(message1.chat.id, 'ошибка выберите курс')
        bot.register_next_step_handler(message1, start_kur1)
def past_nex_ned1(message1):
    pr = config.pr
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    kr = message1.text
    print(kr)
    z = ''
    bot.send_message(message1.chat.id, '*Расписание загружется, подождите...*', parse_mode='markdown')
    a = str(config.week + 1) + '.xlsx'
    timetable1.start(a)

    dn = datetime.date.today().isoweekday()
    if kr[0] in ("1", "2", "3", "4"):
        bot.send_message(message1.chat.id, 'загрузка расписания...')
        # rasp.start()
        if pr == 'МО':
            z = timetable1.get_week("МО", int(kr[0]))
        elif pr == 'ГМУ':

            z = timetable1.get_week("ГМУ", int(kr[0]))
            print(z)
        elif pr == 'Лингвистика':
            z = timetable1.get_week("ЛИНГВ", int(kr[0]))

        bot.send_message(message1.chat.id, z, parse_mode='markdown', reply_markup=user_makeup)
        # bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        # rasp_t=config.rasp_type

        # bot.send_message(message1.chat.id, z, parse_mode='markdown')
        # handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на  /start")
    elif pr == "Реклама":
        z = timetable1.get_week("РЕКС", 0)
        bot.send_message(message1.chat.id, z, parse_mode='markdown', reply_markup=user_makeup)
        # bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        # rasp_t=config.rasp_type

        # bot.send_message(message1.chat.id, z, parse_mode='markdown')
        # handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на  /start")
    elif kr == "Назад":
        start_nap1(message1)
    else:
        bot.send_message(message1.chat.id, 'ошибка выберите курс')
        bot.register_next_step_handler(message1, start_kur1)
def rasp_type(message):
    from telebot import types
    keyboard1=types.ReplyKeyboardMarkup(resize_keyboard=True)
    today=datetime.datetime.now()
    keyboard1.add("Расписание на сегодня")
    keyboard1.add("Расписание на оставшиеся дни")
    if(today.isoweekday()==7) or (today.isoweekday()==6 and today.hour>=15):
        keyboard1.add("Расписание на след неделю")
    keyboard1.add("Назад")

    message1=bot.send_message(message.chat.id, 'выберите тип расписания', reply_markup=keyboard1)
    bot.register_next_step_handler(message1,start_m)
def start_m(message):
    if message.text in ("Расписание на сегодня","Расписание на оставшиеся дни","Расписание на след неделю"):
        config.rasp_type=message.text
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today = datetime.date.today().isoweekday()
        keyboard1.add("ПМИ","Геология")
        keyboard1.add("Химия")
        keyboard1.add("Назад")
        message1 = bot.send_message(message.chat.id, 'выберите направление', reply_markup=keyboard1)
        bot.register_next_step_handler(message1, start_nap)
    elif message.text=="Назад":
        handle_start(message)

    else:
        bot.send_message(message.chat.id, "выбран неправельный тип расписания")
        rasp_type(message)
def start_nap(message1):
    #print(message1.text)
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    pr=(message1.text)
    if pr in ("ПМИ", "Геология","Химия"):
        config.pr=pr
        keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard2.add("1-ый курс",'2-ой курс')
        keyboard2.add('3-ий курс','4-ый курс')
        keyboard2.add("Назад")
        bot.send_message(message1.chat.id, 'Теперь выбери курс', reply_markup=keyboard2)

        if (config.rasp_type == 'Расписание на сегодня'):
            bot.register_next_step_handler(message1, start_kur)
        elif (config.rasp_type=="Расписание на оставшиеся дни"):
            bot.register_next_step_handler(message1,pasp_ned)
        elif (config.rasp_type=="Расписание на след неделю"):
                a=config.file
                #print(z)
                config.file=a

                bot.register_next_step_handler(message1,past_nex_ned)
    elif pr=="Назад":
       rasp_type(message1)

    else:
        bot.send_message(message1.chat.id, 'ошибка выберите направление')
        bot.register_next_step_handler(message1,start_nap)



    #bot.send_message(message1.chat.id,'',reply_markup=user_makeup)
def start_kur(message1):
    pr=config.pr
    f = open('text.txt', 'r')
    a=f.read()
    f.close()
    #print(a)
    a=a.split()
    if str(message1.chat.id) not in a:
        f = open('text.txt', 'a')
        f.write(str(message1.chat.id) +' '+ str(message1.from_user.first_name) +' ' +str(message1.from_user.last_name))
    f.close()
    print(message1.chat.id)
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    kr=message1.text
    #print(kr)
    if kr[0] in ("1","2","3","4"):
        dn=datetime.date.today().isoweekday()
        bot.send_message(message1.chat.id, 'загрузка с файла...')
        #rasp.start()
        if pr=='ПМИ':
            z = timetable.get_day("ПМИИ",int(kr[0]),dn)
        elif pr=='Геология':

            z = timetable.get_day("ГЕОЛ",int(kr[0]),dn)
            print(z)
        elif pr=='Химия':
            z = timetable.get_day("ХИМФ",int(kr[0]), dn)
        try:
            bot.send_message(message1.chat.id, z, reply_markup=user_makeup, parse_mode='markdown')
        #bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        except:
            bot.send_message(message1.chat.id, z, reply_markup=user_makeup)
        #handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на /start")
    elif kr=="Назад":
        start_nap(message1)
    else:
        bot.send_message(message1.chat.id, 'ошибка выберите курс')
        bot.register_next_step_handler(message1, start_kur)

def pasp_ned(message1):
    pr = config.pr
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    kr = message1.text
    print(kr)
    z=''
    dn = datetime.date.today().isoweekday()
    if kr[0] in ("1", "2", "3", "4"):
        bot.send_message(message1.chat.id, 'загрузка расписания...')
        #rasp.start()
        if pr == 'ПМИ':
            z = timetable.get_last_day("ПМИИ", int(kr[0]),dn)
        elif pr == 'Геология':
            z = timetable.get_last_day("ГЕОЛ", int(kr[0]),dn)
        elif  pr == 'Химия':
            z = timetable.get_last_day("ХИМФ", int(kr[0]),dn)

        bot.send_message(message1.chat.id, z, parse_mode='markdown', reply_markup=user_makeup)
        #bot.send_message(message1.chat.id, '*продолжим?*', parse_mode='markdown')
        #rasp_t=config.rasp_type

        #bot.send_message(message1.chat.id, z, parse_mode='markdown')
        #handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на  /start")
    elif kr=="Назад":
        start_nap(message1)
    else:
        bot.send_message(message1.chat.id, 'ошибка выберите курс')
        bot.register_next_step_handler(message1, start_kur)
def past_nex_ned(message1):
    pr = config.pr
    from telebot import types
    user_makeup = telebot.types.ReplyKeyboardRemove()
    kr = message1.text
    #print(kr)
    z = ''
    dn = datetime.date.today().isoweekday()
    if kr[0] in ("1", "2", "3", "4"):
        bot.send_message(message1.chat.id, '*Расписание загружется, подождите...*', parse_mode='markdown')
        a = str(config.file+1) + '.xlsx'
        timetable.start(a)

        if pr == 'ПМИ':
            z = z + timetable.get_week("ПМИИ", int(kr[0]))
        elif pr == 'Геология':
            z = z + timetable.get_week("ГЕОЛ", int(kr[0]))
        elif pr == 'Химия':
            z = z+timetable.get_week("ХИМФ", int(kr[0]))
        #bot.send_message(message1.chat.id, z, parse_mode='markdown', reply_markup=user_makeup)
        #z.replace('*','')
        #rasp_t = config.rasp_type

        bot.send_message(message1.chat.id, z, parse_mode='markdown',reply_markup=user_makeup)

        a = str(config.file) + '.xlsx'
        timetable.start(a)
        #handle_start(message1)
        bot.send_message(message1.chat.id, "для продолжения нажмите на  /start")
    elif kr=="Назад":
        start_nap(message1)
    else:
        bot.send_message(message1.chat.id, 'ошибка выберите курс')
        bot.register_next_step_handler(message1, start_kur)
if __name__ == '__main__':
    bot.polling(none_stop=True)


