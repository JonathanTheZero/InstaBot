from instabot import Bot
from config import INSTA_TAG, USERNAME, PASSWORD
import os
from PIL import Image

def upload():
    os.system('rmdir /S /Q config')

    bot = Bot()
    bot.login(
        username=USERNAME,
        password=PASSWORD
    )

    dir = 'img/'

    for img in os.listdir(dir):
        im = Image.open(dir + img)
        width, height = im.size
        if .85 < width / height > 1.15: #not quadratic or similiar
            continue

        bot.upload_photo(dir + img, caption=INSTA_TAG)
        break
    
