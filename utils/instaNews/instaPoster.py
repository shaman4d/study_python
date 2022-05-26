'''
import InstagramAPI

username = 'shaman4d'
psw = 'CallipsoInsta77'
image = 'ylrn.jpg'

iapi = InstagramAPI.InstagramAPI(username, psw)
iapi.login()

iapi.uploadPhoto(image,caption="Test image")
'''

''' '''
from instapy_cli import client

username = 'shaman4d'
psw = 'CallipsoInsta77'
image = 'ylrn.jpg'
text = 'Новости Lenta.ru за вчера.'+ '\r\n' +'#lentaru #data_art #yesterdaynews'

with client(username, psw) as cli:
    cli.upload(image, text)

''' '''