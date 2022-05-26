import logging
import requests
import random
import sys
import urllib.parse as urlparse
import os
import re
import pickle
import ctypes
from datetime import datetime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from bs4 import BeautifulSoup

logging.basicConfig(
    filename="errors.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# print('args:',sys.argv)
logging.info("Launch args {}".format(sys.argv))

SPI_SETDESKWALLPAPER = 20
POGODA_BG_W = 520
POGODA_BG_H = 200

INFO_COLOR = (235,235,235)

LOCATION = "simferopol"
KEYWORD = "'architecture moscow'"
AMOUNT = 10


def getUsplashImageByKeywords():
    if True:
    # if os.path.exists('tmp.jpg') == False or currConfig['updated'] != currDate:
        # getting list of images
        print(f"Query: https://unsplash.com/napi/search/photos?query={KEYWORD}&per_page=1")
        imgs = requests.get(
            f"https://unsplash.com/napi/search/photos?query={KEYWORD}&per_page=1"
        ).json()
        # get random image
        total = imgs["total"]
        PAGE= random.randint(1,min(int(total),int(AMOUNT)))
        print(f"Query: https://unsplash.com/napi/search/photos?query={KEYWORD}&per_page=1&page={PAGE}")
        imgs = requests.get(
            f"https://unsplash.com/napi/search/photos?query={KEYWORD}&per_page=1&page={PAGE}"
        ).json()

        img = imgs["results"][0]
        img_raw_url = img["urls"]["full"]
        print(img_raw_url)
        responce = requests.get(img_raw_url)
        if responce.status_code == 200:
            with open("tmp.jpg", "wb") as f:
                f.write(responce.content)


def getYPogoda():
    global pogodaInfo
    pogodaInfo = {}

    '''
    if os.path.exists("tmp.html") == False:
        url = f"https://yandex.ru/pogoda/{LOCATION}"
        html = requests.get(url)
        if html.status_code == 200:
            with open("tmp.html", "wb") as f:
                f.write(html.content)

    htmlContent = None
    with open("tmp.html", "rb") as f:
        htmlContent = f.read()
    '''
    url = f"https://yandex.ru/pogoda/{LOCATION}"
    html = requests.get(url)
    htmlContent = html.content

    bsHtml = BeautifulSoup(htmlContent, features="html.parser")
    cssHref = bsHtml.html.head.findAll(
        "link", {"href": re.compile("index\.css")})[0].attrs["href"]
    cssHref = urlparse.urljoin("https://", cssHref)
    print(f'CSS url: {cssHref}')

    css = requests.get(cssHref)
    # if css.status_code == 200:
        # with open("tmp.css", "wb") as f:
            # f.write(css.content)

    cssContent = css.content.decode('utf-8')
    # with open("tmp.css", "rb") as f:
        # cssContent = f.read().decode('utf-8')

    divCard = bsHtml.find('div', {'class':'fact card card_size_big'})
    divCardBg = divCard.findChild()
    divCardBgClass = divCardBg.attrs['class'][1]
    result = re.search( divCardBgClass + '\s*{.*?url\((?P<ulink>.*?)\)', cssContent)
    bgImgPath = urlparse.urljoin('https://', result.group('ulink'))
    print(f'bg image url: {bgImgPath}')

    response = requests.get(bgImgPath)
    if response.status_code == 200:
        with open('tmp_bg.jpg', 'wb') as f:
            f.write(response.content)

    divCity = bsHtml.find('ol', {'class':'breadcrumbs'})
    breadcrums = divCity.findAll('span', {'class':'breadcrumbs__title'})
    city = breadcrums[len(breadcrums)-1].text
    pogodaInfo['city'] = city

    divCurrTemp = bsHtml.find('div', {'class':'temp fact__temp fact__temp_size_s'})
    currTemp = divCurrTemp.find('span', {'class':'temp__value'}).text
    print(f'curr temperature: {currTemp}')
    pogodaInfo['curr_temp'] = currTemp

    divCurrFeelTemp = bsHtml.find('div', {'class':'link__feelings fact__feelings'})
    currFeelTemp = divCurrFeelTemp.find('span', {'class':'temp__value'}).text
    print(f'curr feel temperature: {currFeelTemp}')
    pogodaInfo['curr_fell_temp'] = currFeelTemp

    divYtrTemp = bsHtml.find('dl', {'class':'term term_orient_h term_size_wide fact__yesterday'})
    ytrTemp = divYtrTemp.find('span', {'class':'temp__value'}).text
    print(f'yesterday temperature: {ytrTemp}')
    pogodaInfo['ytr_temp'] = ytrTemp

    # wind
    divWind = bsHtml.find('dl', {'class':'term term_orient_v fact__wind-speed'})
    currWind = divWind.find('span', {'class':'wind-speed'}).text
    currWindDir = divWind.find('abbr').text
    print(f'wind: {currWind} m\s {currWindDir}')
    pogodaInfo['wind'] = currWind

    # humidity
    divHumid = bsHtml.find('dl', {'class':'term term_orient_v fact__humidity'})
    currHumid = divHumid.find('dd').text
    print(f'humidity: {currHumid}')
    pogodaInfo['hum'] = currHumid

    # pressure
    divPres = bsHtml.find('dl', {'class':'term term_orient_v fact__pressure'})
    currPres = divPres.find('dd').text
    print(f'a.pressure: {currPres}')
    pogodaInfo['pres'] = currPres

    # temperature by hour
    divHourlyTemps = bsHtml.find('div', {'class':'swiper-container fact__hourly-swiper'})
    divsHT = divHourlyTemps.findAll('div', {'class':'fact__hour swiper-slide'})
    hourlyTemps = []
    for dht in divsHT:
        currH = dht.find('div',{'class':'fact__hour-label'}).text
        currT = dht.find('div',{'class':'fact__hour-temp'}).text
        # print(f'hour:{currH} temp:{currT}')
        hourlyTemps.append([currH, currT])
    pogodaInfo['hourlyTemp'] = hourlyTemps

def makeWallpaper():
    global currConfig
    user32 = ctypes.windll.user32
    screenW, screenH = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    img = Image.open('tmp.jpg')
    imgW = img.size[0]
    imgH = img.size[1]
    if screenW / float(screenH) < imgW / float(imgH):
        print('Squeeze by Vertical')
        img = img.resize((int(imgW * screenH / float(imgH)), screenH), Image.BICUBIC)
    else:
        print('Squeeze by Horizontal')
        img = img.resize((screenW, int(imgH * screenW / float(imgW))), Image.BICUBIC)
    imgW = img.size[0]
    imgH = img.size[1]

    overlay = Image.new('RGB', (imgW, imgH), 0)
    img = Image.blend(img, overlay, 0.3)

    draw = ImageDraw.Draw(img)

    #draw weather bg
    bgStage = Image.new('RGBA',(POGODA_BG_W, POGODA_BG_H),0)

    tmpBg = Image.open('tmp_bg.jpg')
    tmpBg = tmpBg.resize((POGODA_BG_W, POGODA_BG_H), Image.BICUBIC)
    # tmpBgMask = Image.new('RGBA', (POGODA_BG_W, POGODA_BG_H), (0,0,0,230))
    tmpBgMask = Image.open('bg_mask_white.png')
    tmpBgMask = tmpBgMask.resize((POGODA_BG_W, POGODA_BG_H), Image.BICUBIC)
    
    bgStage.paste(tmpBg, (0,0), mask = tmpBgMask)
    
    img.paste(bgStage, (screenW - POGODA_BG_W - 10, int(imgH/2 - screenH/2) + 10), mask = tmpBgMask)
    
    # draw update timestamp
    offsetY = imgH/2 - screenH/2 + 15
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    font = ImageFont.truetype('kabelbook.otf',16)
    text = 'обновлено: {}'.format(timestamp)
    textW, textH = font.getsize(text)
    draw.text((screenW - POGODA_BG_W + 5, offsetY + 10), text, (215,215,215), font=font)

    # draw city weather
    offsetY = imgH/2 - screenH/2 + 60
    font = ImageFont.truetype('kabelbook.otf',40)
    text = '{} {} C°'.format(pogodaInfo['city'], int(pogodaInfo['curr_temp']))
    textW, textH = font.getsize(text)
    draw.text((screenW - POGODA_BG_W + 5 + 2, offsetY + 2), text, (0,0,0), font=font)
    draw.text((screenW - POGODA_BG_W + 5, offsetY), text, (255,255,255), font=font)
    offsetY += textH

    # draw wind
    font = ImageFont.truetype('kabelbook.otf',18)
    text = 'ветер: {} м/с'.format(pogodaInfo['wind'])
    textW, textH = font.getsize(text)
    draw.text((screenW - POGODA_BG_W + 5, offsetY + 10), text, INFO_COLOR, font=font)
    offsetX = textW

    text = 'влажность: {}'.format(pogodaInfo['hum'])
    textW, textH = font.getsize(text)
    draw.text((screenW - POGODA_BG_W + 20 + offsetX, offsetY + 11), text, INFO_COLOR, font=font)
    offsetX += textW

    text = 'давление: {}'.format(pogodaInfo['pres'])
    textW, textH = font.getsize(text)
    draw.text((screenW - POGODA_BG_W + 40 + offsetX, offsetY + 11), text, INFO_COLOR, font=font)
    offsetY += textH

    #draw hourly
    htRange = pogodaInfo['hourlyTemp']
    htRange = htRange[0:9]

    font = ImageFont.truetype('kabelbook.otf',18)
    offsetY += 30
    counter = 0
    for ht in htRange:
        text = '{}'.format(ht[0])
        textW, textH = font.getsize(text)
        draw.text((screenW - POGODA_BG_W + 5 + counter * 55, offsetY), text, INFO_COLOR, font=font)

        text = '{}'.format(ht[1])
        draw.text((screenW - POGODA_BG_W + 10 + counter * 55, offsetY + 10 + textH), text, INFO_COLOR, font=font)
        counter +=1


    img.save('tmp_wp.jpg')
    # img.show()
    w_full_path = os.path.join(os.getcwd(), 'tmp_wp.jpg')
    user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, w_full_path, 0)


# --------------------------------------------------------------------
print("Number of args {}".format(len(sys.argv)))
if len(sys.argv) > 1:
    LOCATION = sys.argv[1]
    print("LOCATION {}".format(sys.argv[1]))
if len(sys.argv) > 2:
    KEYWORD = sys.argv[2]
    print("KEYWORD {}".format(sys.argv[2]))
if len(sys.argv) > 3:
    AMOUNT = sys.argv[3]
    print("AMOUNT {}".format(sys.argv[3]))

currConfig = {'updated':''}
try:
    if os.path.exists('config.pkl'):
        file = open('config.pkl', 'rb')
        currConfig = pickle.load(file)
except:
    pass

now = datetime.now()
currDate = now.strftime("%d/%m/%Y")

pogodaInfo = None

getUsplashImageByKeywords()
getYPogoda()
makeWallpaper()

currConfig['updated'] = currDate
file = open('config.pkl', 'wb')
pickle.dump(currConfig, file)