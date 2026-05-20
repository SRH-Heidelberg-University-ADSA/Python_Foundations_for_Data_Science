import sys

import utils

# import db
# from utils.db.db import insert_db


# print(sys.path)
print(__name__)


class Stackoverflow:
    def __init__(self, rating, questions_answered):
        self.ratings = rating
        self.questions_answered = questions_answered

    def fetch_data(self):
        # fetch the data
        # db.insert_db()
        utils.insert_db()
        # i()


s = Stackoverflow(1, 2)
s1 = Stackoverflow(3, 4)
s.fetch_data()

people = [s, s1]
print(s.__dict__)

import pandas as pd

df = pd.DataFrame([p.__dict__ for p in people])
print(df["ratings"].mean())
