# utils/affirmations.py (you can create this file)

import random
from datetime import date

AFFIRMATIONS = [
    "You are doing the best you can, and that is enough.",
    "You are capable of handling anything that comes your way.",
    "Peace begins with a deep breath.",
    "You are worthy of love and compassion.",
    "Your feelings are valid.",
    "Growth is not linear, but it is always happening.",
    "Today is a fresh start.",
    "You deserve time to rest and heal.",
    "Your presence makes a difference in the world."
]

def get_daily_affirmation():
    seed = int(date.today().strftime('%Y%m%d'))  # Ensure one affirmation per day
    random.seed(seed)
    return random.choice(AFFIRMATIONS)
