import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
import os


def fetch():
    reddit = praw.Reddit(
        user_agent=USER_AGENT, 
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    for hot in reddit.subreddit("dankmemes").hot(limit=5):
        print(hot.__dict__)
        print("\n")
