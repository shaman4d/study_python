import logging
import random
import glob
import ctypes
import os
import pickle
import requests
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SPI_SETDESKWALLPAPER = 20
WEATHER_APPID = 'cfa3e4ee304ebb8210c87409a03ab66a'
WEATHER_UNITS = 'metric'
WEATHER_CITY = 'simferopol'

logging.basicConfig(filename='errors.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

currConfig = {'updated':'', 'photo':-1}
if os.path.exists('config.pkl'):
    file = open('config.pkl', 'rb')
    currConfig = pickle.load(file)

def processing_weather_data(weatherData={}):
    return {'city': weatherData['name'], 'temp': weatherData['main']['temp'],
            'humidity': weatherData['main']['humidity'], 'wind': weatherData['wind'],
            'clouds': weatherData['clouds']['all'], 'icon':
                weatherData['weather'][0]['icon']}


def get_weather_info():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={WEATHER_CITY}&appid={WEATHER_APPID}&units={WEATHER_UNITS}'
    response = requests.get(url).json()
    processedData = None
    if response is None:
        print('! Something went wrong with getting data !')
        logging.error('Something went wrong with getting weather info')
    elif response['cod'] != 200:
        print('Error: {}'.format(response['message']))
        logging.error('Error: {}'.format(response['message']))
    else:
        logging.info('Weather full data: {}'.format(response))
        processedData = processing_weather_data(response)
    return processedData


def make_wallpaper(weatherData={}):
    global currConfig
    user32 = ctypes.windll.user32
    screenW, screenH = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    now = datetime.now()
    currDate = now.strftime("%d/%m/%Y")

    photos = glob.glob('photos/*.jpg')
    # photo = photos[0]
    if currConfig['photo'] == -1 or currConfig['updated'] != currDate:
        photo_idx = random.randint(0, len(photos)-1)
        photo = photos[photo_idx]
        currConfig['photo'] = photo_idx
        currConfig['updated'] = currDate
    else:
        photo = photos[currConfig['photo']]

    script_path = os.getcwd()
    photo_full_path = os.path.join(script_path, photo)
    img = Image.open(photo_full_path)
    imgW = img.size[0]
    imgH = img.size[1]
    # wRatio = screenW/float(imgW)
    # hRatio = screenH/float(imgH)
    if screenW / float(screenH) < imgW / float(imgH):
        print('Squeeze by Vertical')
        img = img.resize((int(imgW * screenH / float(imgH)), screenH), Image.BICUBIC)
    else:
        print('Squeeze by Horizontal')
        img = img.resize((screenW, int(imgH * screenW / float(imgW))), Image.BICUBIC)
    imgW = img.size[0]
    imgH = img.size[1]

    overlay = Image.new('RGB', (imgW, imgH), 0)
    img = Image.blend(img, overlay, 0.2)

    draw = ImageDraw.Draw(img)
    # draw city weather
    font = ImageFont.truetype('djvu_bold.ttf',40)
    text = '{} {}C°'.format(weatherData['city'], int(weatherData['temp']))
    textW, textH = font.getsize(text)
    offsetY = imgH/2 - screenH/2 + 10
    draw.text((screenW - textW - 10 + 2, offsetY + 2), text, (0,0,0), font=font)
    draw.text((screenW - textW - 10, offsetY), text, (255,255,255), font=font)



    # draw wind and humidity
    font = ImageFont.truetype('djvu_bold.ttf',20)
    text = 'wspd.{} clds.{} hum.{}'.format(weatherData['wind']['speed'], weatherData['clouds'], int(weatherData['humidity']))
    textW, textH = font.getsize(text)
    offsetY += textH*2 + 10
    draw.text((screenW - textW - 35 + 2, offsetY + 2), text, (0,0,0), font=font)
    draw.text((screenW - textW - 35, offsetY), text, (255,255,255), font=font)

    # draw update timestamp
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    font = ImageFont.truetype('djvu_bold.ttf',16)
    text = 'last update: {}'.format(timestamp)
    textW, textH = font.getsize(text)
    draw.text((screenW - textW - 10, imgH/2 + screenH/2 - 50), text, (215,215,215), font=font)


    img.save('tmp.jpg')
    # img.show()
    w_full_path = os.path.join(script_path, 'tmp.jpg')
    user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, w_full_path, 0)
    file = open('config.pkl', 'wb')
    pickle.dump(currConfig, file)


make_wallpaper(get_weather_info())

'''
weatherData = {'coord': {'lon': 34.1, 'lat': 44.95},
               'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],
               'base': 'stations',
               'main': {'temp': 30.07, 'pressure': 1012.62, 'humidity': 22, 'temp_min': 30.07, 'temp_max': 30.07,
                        'sea_level': 1012.62, 'grnd_level':
                            988.43}, 'wind': {'speed': 3.44, 'deg': 336.517}, 'clouds': {'all': 18},
               'dt': 1567592108,
               'sys': {'message': 0.007, 'country': 'UA', 'sunrise': 1567566525, 'sunset': 1567613837},
               'timezone': 10800, 'id': 693805, 'name': 'Simferopol', 'cod': 200}
make_wallpaper(processing_weather_data(weatherData))
'''

