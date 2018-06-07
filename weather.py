def start(dn, month):
    from bs4 import BeautifulSoup
    import requests
    months = ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    month=months[month-1]
    r=requests.get('https://pogoda.mail.ru/prognoz/dushanbe/'+str(dn)+'-'+str(month)+'/')
        # #print(html_doc)
    html_doc=r.text
    #print(html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    table=soup.find('div', class_='cols__column__item cols__column__item_2-1 cols__column__item_2-1_ie8')
    today=table.find_all('div', class_='day day_period')
    temp=[]
    for td in today[:3]:
        temp.append((td.find('div', class_='day__temperature ').text+''+td.find('div', class_='day__description').text).replace('\n', ' '))
    #print(temp)
    for i in range(0,3):
        if 'ясно' in temp[i]:
            temp[i]=temp[i]+'☀️'
        elif 'малооблачно' in temp[i]:
            temp[i] = temp[i] + '🌤'
        elif 'облачность' in temp[i]:
            temp[i] = temp[i] + '🌥🌥'
        elif 'дождь' in temp[i]:
            temp[i] = temp[i]+' возможен' + '🌧'
        elif 'гроза' in temp[i]:
            temp[i] = temp[i] + '⚡️'
        elif 'снегопад' in temp[i]:
            temp[i] = temp[i] + '🌨'


    day='днём  : '+ temp[2]
    morning='утром : '+ temp[1]
    nigth='ночью : '+ temp[0]
    print(' '+morning+'\n '+day+'\n',nigth)
    return (' '+morning+'\n '+day+'\n'+ nigth)
