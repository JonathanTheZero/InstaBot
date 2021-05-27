from instabot import Bot
from config import USERNAME, PASSWORD
import os

def upload():
    os.system("rmdir /S /Q config")

    bot = Bot()
    bot.login(
        username=USERNAME,
        password=PASSWORD
    )

    dir = "img/"

    for img in os.listdir(dir):
        bot.upload_photo(dir + img, caption="Test2222")
        os.system("del img\\" + img)
    
