import random


def get_sub() -> str:
    subs = [
        'wholesomememes',
        'wholesomememes',
        'wholesomememes',
        'wholesomememes',  # weight of 4
        'memes',
        'memes'  # weight of 2
    ]
    return random.choice(subs)
