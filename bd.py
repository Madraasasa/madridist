# import os
import psycopg2 as p
import telebot
#from PIL import Image

# con = p.connect(database='dfq6banncblc4l', user='vtudqaibjctcaw', host='ec2-23-23-142-5.compute-1.amazonaws.com', password='d9dcd45b804a1510e232ff7b13f9ff260332692b9328bef3e21b8a752ffb389c')
# cur=con.cursor()
# cur.execute("select * from users")
# con.commit()
# for row in cur:
#    print (row[0])
#    try:
#        a=bot.get_chat(row[0])
#    except:
#        a=0
#    print(a)
#    k+=1
# print(k-1)
# cur.execute("select * from users")
# con.commit()
# #cur.execute('CREATE TABLE config( name varchar(25), name1 varchar(25) ) ')
# con.commit()
# #cur.execute('insert into config values( 38,338)')
# #cur.execute('update config set  name1 = '+str(339)+', name ='+ str(39)+'')
# #con.commit()
# cur.execute("select * from config")
# m=cur.fetchall()
#
# print(m)
# coof=m[0][1]
# print(coof)



# import requests
# # from bs4 import BeautifulSoup
# # title=[]
# url = 'index.html'
# html_doc=open(url, 'rb')
#
# # #print(html_doc)
# soup = BeautifulSoup(html_doc, 'lxml')
# table=soup.find('div', class_='mechety').find('tbody')
# # #print(table)
# today=(table.find('tr', class_='today').text).split('\n')
# today=today[4:]
# #print(today)
# # i=2
# today=[]
# table=table.find_all('tr')[7:8]
# # #print(table)
# # for tab in table:
# # #
# tds=(table[0].find_all('td'))
#  # #print(tds)
# for td in tds:
#     today.append(td.text)
# print(today[1])
# # #print(today)
# # if '07.06.2018' in today:
# #     print(today[:9])
# # else:
# #     today.clear()
# from bs4 import BeautifulSoup
# import requests
# r=requests.get('https://pogoda.mail.ru/prognoz/dushanbe/8-june/').text
#     # #print(html_doc)
# html_doc=r
# soup = BeautifulSoup(html_doc, 'lxml')
# table=soup.find('div', class_='cols__column__item cols__column__item_2-1 cols__column__item_2-1_ie8')
# today=table.find_all('div', class_='day day_period')
# temp=[]
# for td in today[:3]:
#     temp.append((td.find('div', class_='day__temperature ').text+''+td.find('div', class_='day__description').text).replace('\n', ' '))
# #print(temp)
# for i in range(0,3):
#     if 'ясно' in temp[i]:
#         temp[i]=temp[i]+'☀️'
#     elif 'малооблачно' in temp[i]:
#         temp[i] = temp[i] + '🌤'
#     elif 'облачность' in temp[i]:
#         temp[i] = temp[i] + '🌥🌥'
#     elif 'дождь' in temp[i]:
#         temp[i] = temp[i]+' возможен' + '🌧'
#     elif 'гроза' in temp[i]:
#         temp[i] = temp[i] + '⚡️'
#     elif 'снегопад' in temp[i]:
#         temp[i] = temp[i] + '🌨'
#
#
# day='днём  : '+ temp[2]
# morning='утром : '+ temp[1]
# nigth='ночью : '+ temp[0]
# print(' '+morning+'\n '+day+'\n',nigth)
# nigth=table.find('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night').text.split('ю')
# nigth[0]=nigth[0]+'ю'
#
# forecast=table.find('div', class_='forecast-briefly__condition').text
# print(forecast)
# if forecast=='Ясно':
#     forecast=forecast +' ☀️'
#
#print(today)
#print(table)
#https://pogoda.mail.ru/prognoz/dushanbe/8-june
#import namoz
#result=namoz.start(day)
# import datetime
# import weather
# dn=datetime.date.today().day
# # months = ["january","febuary","march","april","may","june","july","august","september","october","november","december"]
# month=datetime.date.today().month
# print(dn+1, month)
# a=weather.start(dn+1, month)
# bot.send_message(120929625,a)


#print(b)
# import sys
# import imaplib
# import getpass
#
# IMAP_SERVER = 'imap.mail.ru'
# EMAIL_ACCOUNT = 'afellay_maruf@mail.ru'
# EMAIL_FOLDER = "INBOX"
# OUTPUT_DIRECTORY = 'C:/tmp'
#
# PASSWORD = 'afellay20sb'
#
#
# def process_mailbox(M):
#     """
#     Dump all emails in the folder to files in output directory.
#     """
#
#     rv, data = M.search(None, "ALL")
#     if rv != 'OK':
#         print ("No messages found!")
#         return
#
#     #for num in data[0].split():
#     inbox_list = data[0].split()
#     num=inbox_list[-10]
#     rv, data = M.fetch(num, '(RFC822)')
#     if rv != 'OK':
#         print ("ERROR getting message", num)
#         return
#     print ("Writing message ", num)
#     f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, num), 'wb')
#     f.write(data[0][1])
#     f.close()
#
# def main():
#     M = imaplib.IMAP4_SSL(IMAP_SERVER)
#     M.login(EMAIL_ACCOUNT, PASSWORD)
#     rv, data = M.select(EMAIL_FOLDER)
#     if rv == 'OK':
#         print ("Processing mailbox: ", EMAIL_FOLDER)
#         process_mailbox(M)
#         M.close()
#     else:
#         print ("ERROR: Unable to open mailbox ", rv)
#     M.logout()
#
# if __name__ == "__main__":
#     main()


#import convert
#import timetable

#a=convert.get_email()
#timetable.start(a[1])
#z=timetable.get_day("ПМИИ",3,1)
#print(z)
#import pyaudio

print("Голос")

#print(file)




#f=open('voice.ogg', 'wb')
#f.write(file)
#f.close()
#url = file
import speech_recognition as sr
import io



url = "https://api.telegram.org/file/bot545524762:AAG-pxRB-ZQi2KjDMGwQAyTnmSzl2fBIy0k/voice/file_147.oga"
import pydub
import requests
r=requests.get(url).content


def start():
    import speech_recognition as sr
    sound = pydub.AudioSegment.from_file("apple.wav")
    sound.export("apple.wav", format="wav")
    #data, samplerate = sf.read('/home/fil/music/bang-bang.ogg')
    #sf.write('/home/fil/music/bang-bang.wav', data, samplerate)
    url = "https://api.telegram.org/file/bot545524762:AAG-pxRB-ZQi2KjDMGwQAyTnmSzl2fBIy0k/voice/file_147.oga"


    AUDIO_FILE = "apple.wav"

    # use the audio file as the audio source

    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        # reads the audio file. Here we use record instead of
        # listen
        audio = r.record(source)

    try:
        return ( r.recognize_google(audio, language="ru-RU"))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech  Recognition    service;        {0}        ".format(e))
start()
    # import os
# import shutil
# a=os.listdir('D:')
# dir=[]
# files=[]
# print(a)
# for i in a:
#     if '.' in i:
#          files.append(i)
#     else:
#         dir.append(i)
# print(dir)
# b=open('D:/'+dir[1]+"/1.txt",'rb')
# os.chdir("D:/")
# #os.mkdir('Flash')
# m=os.chdir('D:/Flash')
# print(m)
# a=1
# while (a):
#     try:
#         a=os.listdir('F:/')
#         dir = []
#         files = []
#         #print(a)
#         for i in a:
#     # if i =='#4':
#     #     continue
#     # print(i)
#             if '.doc'  in i:
#                 shutil.copy('F:/'+str(i), 'D:/Flash/'+str(i))
#         ## shutil.move(i,)
#         a=0
#
#     except:
#         #     print('нет флеш')
#         pass
