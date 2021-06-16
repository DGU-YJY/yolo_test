from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests



def get_weather():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = bs(html.text,'html.parser')
    data1 = soup.find('div',{'class':'info_data'})

    temperature = data1.find('span',{'class':'todaytemp'}).text
    cast = data1.find('p',{'class':'cast_txt'}).text
    temp_min = data1.find('span',{'class':'min'}).find('span',{'class':'num'}).text
    temp_max = data1.find('span',{'class':'max'}).find('span',{'class':'num'}).text
    feel = data1.find('span',{'class':'sensible'}).find('span',{'class':'num'}).text
    
    data = {
        'temp':int(temperature), 'min':int(temp_min), 'max':int(temp_max), 'feel':int(feel),
        'cast':cast
    }
    if '비' in cast or '소나기' in cast :
        data['rain'] = True
    else:
        data['rain'] = False

    return data

def weather_talk(data):
    talk = "현재 온도는 " + str(data["temp"]) + "도로 "
    talk += data["cast"] +". \n"
    talk += "최저 " + str(data['min'])+"도, "
    talk += "최고 " + str(data['max'])+"도, "
    talk += "체감 온도 "+ str(data['feel'])+"도 입니다. \n"
    #talk += cloth(data)
    
    return talk

def cloth(data):
    temperature= data['temp']
    rain = data['rain']

    if temperature > 28:
        res = '기온이 높으므로 민소매, 반팔, 반바지를 입기에 적당합니다. '
    elif temperature > 23:
        res = '반팔, 반바지, 면바지, 얇은 셔츠를 입기에 적당합니다. '
    elif temperature > 20:
        res = '긴팔티, 면바지, 슬랙스를 입기에 적당합니다. '
    elif temperature > 17:
        res = '가디건, 니트, 맨투맨, 후드, 긴바지를 입기에 적당합니다. '
    elif temperature > 12:
        res = '자켓, 가디건, 니트, 긴바지를 입기에 적당합니다. '
    elif temperature > 9:
        res = '트렌치 코트, 야상, 점퍼를 입기에 적당합니다. '
    elif temperature > 5:
        res = '코트, 기모옷, 가죽옷을 입기 적당합니다.'
    elif temperature <= 5:
        res = '날씨가 추우므로 패딩, 기모옷, 목도리, 두꺼운 코트를 입기 적당합니다.'
    if rain:
        res = res +'또한 비가 올 수 있으므로 밝은 옷을 입고, 우산을 챙기세요.'
    return res

