import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
import os
import urllib.request
from workers.logs import write_to_log, get_log
from workers.subs import get_sub


def fetch():
    reddit = praw.Reddit(
        user_agent=USER_AGENT,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    for hot in reddit.subreddit(get_sub()).hot(limit=5):
        print(hot.url)
        if hot.url.endswith('.jpg') and hot.id not in get_log():
            save(hot.url, hot.id)
            break


def save(url: str, localName: str) -> None:
    urllib.request.urlretrieve(url, 'img/' + localName + '.jpg')
    write_to_log(localName + '\n')
