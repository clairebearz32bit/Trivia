import requests
import json
import random

class Trivia:
    url = 'https://opentdb.com/api.php?amount=1&category={}&difficulty={}&type={}'

    categories = {
                  "Knowledge": "9",
                  "Books": "10",
                  "Movies": "11",
                  "Music": "12",
                  "Theater": "13",
                  "Television": "14",
                  "VideoGames": "15",
                  "BoardGames": "16",
                  "NaturalScience": "17",
                  "ComputerScience": "18",
                  "Math": "19",
                  "Mythology": "20",
                  "Sports": "21",
                  "Geography": "22",
                  "History": "23",
                  "Politics": "24",
                  "Art": "25",
                  "Celebrities": "26",
                  "Animals": "27",
                  "Vehicles": "28",
                  "Comics": "29",
                  "Gadgets": "30",
                  "Anime": "31",
                  "Cartoons": "32"
              }

    question = None
    correct_answer = None
    choices = {}

    def __init__(self, **kwargs):
        self.category = self.categories.get(kwargs['category'])
        self.difficulty = kwargs['difficulty'].lower()
        self.mode = kwargs['mode']

    def getTrivia(self):
        url = self.url.format(self.category, self.difficulty, self.mode)
        self.url = url
        r = requests.get(url)
        return r.json()

    def parseJSON(self, json_obj):
        try:
            json_obj = json.loads(json_obj)

        except:
            pass

        self.question = json_obj['results'][0]['question']
        letters = ['A', 'B', 'C', 'D']
        choices = [i for i in json_obj['results'][0]['incorrect_answers']]
        choices.append(json_obj['results'][0]['correct_answer'])
        choices = random.sample(choices, 4)

        for i in range(4):
            self.choices[letters[i]] = choices[i]

        self.correct_answer = json_obj['results'][0]['correct_answer']

        return json_obj
