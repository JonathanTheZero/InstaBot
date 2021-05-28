from workers.upload import upload
from workers.fetch_images import fetch
from workers.logs import clean_log, print_log
import time
import random
import threading


def post_loop():
    print('Posting loop started')
    upload()
    offset = 3600 + random.uniform(1, 2) * 3600
    print(offset)
    time.sleep(offset)
    post_loop()


def fetch_loop():
    print('Fetching loop started')
    fetch()
    time.sleep(3600)
    fetch_loop()


if __name__ == '__main__':
    fetch_thread = threading.Thread(target=fetch_loop, name='Fetch')
    fetch_thread.start()
    time.sleep(10)
    post_loop()
