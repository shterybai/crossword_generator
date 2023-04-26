import requests
import time
import numpy as np
import csv
from flask import Flask, request
import logging
import csv

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"
EMPTY_CHAR = "_"
EMPTY_CLUE = ""
MAX_RUN_TIME = 2000
inserted_words = []

# Word list initialization
eleven_char_words = []
ten_char_words = []
six_char_words = []
four_char_words = []

grid_length = 11

word_model_return = 50000

# Grid creation
# black_square = "#"
# grid = [
#     [black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square],
#     [white_square, white_square, white_square, white_square, black_square, white_square, white_square, white_square, white_square, white_square, white_square],
#     [black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square],
#     [black_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square],
#     [black_square, black_square, black_square, white_square, black_square, white_square, black_square, black_square, black_square, white_square, black_square],
#     [white_square, white_square, white_square, white_square, black_square, white_square, black_square, white_square, white_square, white_square, white_square],
#     [black_square, white_square, black_square, black_square, black_square, white_square, black_square, white_square, black_square, black_square, black_square],
#     [white_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square, white_square, black_square],
#     [black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square],
#     [white_square, white_square, white_square, white_square, white_square, white_square, black_square, white_square, white_square, white_square, white_square],
#     [black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square, white_square, black_square]
# ]

app = Flask(__name__)
# start_time = time.time()


@app.route('/request', methods=['GET', 'POST'])
def request_page():
    start_time = time.time()

    reset_states()

    user_words = str(request.args.get('user_words'))
    word2vec(user_words)

    execute()

    crossword = draw_grid()

    create_clues()

    result = {
        "grid_length": grid_length,
        "crossword": crossword,
        "words": [
            {'slot': states["a6"].name, 'word': states["a6"].word, 'clue': states["a6"].clue, 'orientation': states["a6"].orientation, 'number': states["a6"].number},
            {'slot': states["a7"].name, 'word': states["a7"].word, 'clue': states["a7"].clue, 'orientation': states["a7"].orientation, 'number': states["a7"].number},
            {'slot': states["a8"].name, 'word': states["a8"].word, 'clue': states["a8"].clue, 'orientation': states["a8"].orientation, 'number': states["a8"].number},
            {'slot': states["a9"].name, 'word': states["a9"].word, 'clue': states["a9"].clue, 'orientation': states["a9"].orientation, 'number': states["a9"].number},
            {'slot': states["a11"].name, 'word': states["a11"].word, 'clue': states["a11"].clue, 'orientation': states["a11"].orientation, 'number': states["a11"].number},
            {'slot': states["a12"].name, 'word': states["a12"].word, 'clue': states["a12"].clue, 'orientation': states["a12"].orientation, 'number': states["a12"].number},
            {'slot': states["a15"].name, 'word': states["a15"].word, 'clue': states["a15"].clue, 'orientation': states["a15"].orientation, 'number': states["a15"].number},
            {'slot': states["a16"].name, 'word': states["a16"].word, 'clue': states["a16"].clue,'orientation': states["a16"].orientation, 'number': states["a16"].number},
            {'slot': states["d1"].name, 'word': states["d1"].word, 'clue': states["d1"].clue, 'orientation': states["d1"].orientation, 'number': states["d1"].number},
            {'slot': states["d2"].name, 'word': states["d2"].word, 'clue': states["d2"].clue, 'orientation': states["d2"].orientation, 'number': states["d2"].number},
            {'slot': states["d3"].name, 'word': states["d3"].word, 'clue': states["d3"].clue, 'orientation': states["d3"].orientation, 'number': states["d3"].number},
            {'slot': states["d4"].name, 'word': states["d4"].word, 'clue': states["d4"].clue, 'orientation': states["d4"].orientation, 'number': states["d4"].number},
            {'slot': states["d5"].name, 'word': states["d5"].word, 'clue': states["d5"].clue, 'orientation': states["d5"].orientation, 'number': states["d5"].number},
            {'slot': states["d10"].name, 'word': states["d10"].word, 'clue': states["d10"].clue, 'orientation': states["d10"].orientation, 'number': states["d10"].number},
            {'slot': states["d11"].name, 'word': states["d11"].word, 'clue': states["d11"].clue, 'orientation': states["d11"].orientation, 'number': states["d11"].number},
            {'slot': states["d13"].name, 'word': states["d13"].word, 'clue': states["d13"].clue, 'orientation': states["d13"].orientation, 'number': states["d13"].number},
            {'slot': states["d14"].name, 'word': states["d14"].word, 'clue': states["d14"].clue, 'orientation': states["d14"].orientation, 'number': states["d14"].number},
        ]
    }

    eleven_char_words.clear()
    ten_char_words.clear()
    six_char_words.clear()
    four_char_words.clear()
    inserted_words.clear()

    execution_time = time.time() - start_time

    print("\nFinished. Total execution time: ", execution_time, " seconds")

    # with open('time_data.csv', 'a', newline='') as time_file:
    #     time_writer = csv.writer(time_file)
    #     time_writer.writerow([word_model_return, execution_time])
    #     time_file.flush()

    return result


def reset_states():
    global states
    states = {
        "d3": D3Insertion(),
        "a8": A8Insertion(),
        "a12": A12Insertion(),
        "d2": D2Insertion(),
        "d5": D5Insertion(),
        "d10": D10Insertion(),
        "d11": D11Insertion(),
        "a7": A7Insertion(),
        "a15": A15Insertion(),
        "d1": D1Insertion(),
        "d4": D4Insertion(),
        "a6": A6Insertion(),
        "a9": A9Insertion(),
        "a11": A11Insertion(),
        "d13": D13Insertion(),
        "d14": D14Insertion(),
        "a16": A16Insertion()
    }


def word2vec(user_words):
    print("Retrieving sim_list for words " + user_words)
    sim_list = requests.get('http://127.0.0.1:7777/request/?user_words=' + user_words)

    word_list = [i[0] for i in sim_list.json()]

    print("sim_list successfully retrieved for words " + user_words)

    dictionaries(word_list)


def dictionaries(word_list):
    # Populate word lists
    print("Populating word lists...")

    for word in word_list:
        if len(word) == 11 and all(c not in BANNED_CHARACTERS for c in word):
            eleven_char_words.append(word.upper())
        if len(word) == 10 and all(c not in BANNED_CHARACTERS for c in word):
            ten_char_words.append(word.upper())
        if len(word) == 6 and all(c not in BANNED_CHARACTERS for c in word):
            six_char_words.append(word.upper())
        if len(word) == 4 and all(c not in BANNED_CHARACTERS for c in word):
            four_char_words.append(word.upper())

    print("Done")

    # print("\nEleven character words:")
    # for word in eleven_char_words:
    #     print(word)
    #
    # print("\nTen character words:")
    # for word in ten_char_words:
    #     print(word)
    #
    # print("\nSix character words:")
    # for word in six_char_words:
    #     print(word)
    #
    # print("\nFour character words:")
    # for word in four_char_words:
    #     print(word)


class WordInsertions:
    def __init__(self):
        self.word = EMPTY_WORD

    def set_word(self, word):
        self.word = word
        return self.next_state

    def ban_current_word(self):
        if self.word != EMPTY_WORD:
            self.banned_words.append(self.word)

    def ban_word(self, word):
        self.banned_words.append(word)


# D3 assignment
class D3Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d3"
        self.orientation = "down"
        self.number = 3
        self.word_length = 11
        self.next_state = "a8"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word not in self.banned_words:
            eleven_char_nytcrosswords = csv.DictReader(open("eleven_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in eleven_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A8 assignment
class A8Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a8"
        self.orientation = "across"
        self.number = 8
        self.word_length = 10
        self.next_state = "a12"
        self.backtrack_state = "d3"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[4] == states[self.backtrack_state].word[3] and \
                word not in inserted_words and \
                word not in self.banned_words:
            ten_char_nytcrosswords = csv.DictReader(open("ten_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in ten_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A12 assignment
class A12Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a12"
        self.orientation = "across"
        self.number = 12
        self.word_length = 10
        self.next_state = "d2"
        self.backtrack_state = "d3"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[5] == states[self.backtrack_state].word[7] and \
                word not in inserted_words and \
                word not in self.banned_words:
            ten_char_nytcrosswords = csv.DictReader(open("ten_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in ten_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D2 assignment
class D2Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d2"
        self.orientation = "down"
        self.number = 2
        self.word_length = 6
        self.next_state = "d5"
        self.backtrack_state = "a8"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[3] == states[self.backtrack_state].word[2] and \
                word not in inserted_words and \
                word not in self.banned_words:
            six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in six_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D5 assignment
class D5Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d5"
        self.orientation = "down"
        self.number = 5
        self.word_length = 6
        self.next_state = "d10"
        self.backtrack_state = "a8"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[3] == states[self.backtrack_state].word[8] and \
                word not in inserted_words and \
                word not in self.banned_words:
            six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in six_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D10 assignment
class D10Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d10"
        self.orientation = "down"
        self.number = 10
        self.word_length = 6
        self.next_state = "d11"
        self.backtrack_state = "a12"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[2] == states[self.backtrack_state].word[1] and \
                word not in inserted_words and \
                word not in self.banned_words:
            six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in six_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D11 assignment
class D11Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d11"
        self.orientation = "down"
        self.number = 11
        self.word_length = 6
        self.next_state = "a7"
        self.backtrack_state = "a12"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[2] == states[self.backtrack_state].word[7] and \
                word not in inserted_words and \
                word not in self.banned_words:
            six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in six_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A7 assignment
class A7Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a7"
        self.orientation = "across"
        self.number = 7
        self.word_length = 6
        self.next_state = "a15"
        self.backtrack_state = "d3"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[0] == states[self.backtrack_state].word[1] and \
                word[4] == states["d5"].word[1] and \
                word not in inserted_words and \
                word not in self.banned_words:
            six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in six_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A15 assignment
class A15Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a15"
        self.orientation = "across"
        self.number = 15
        self.word_length = 6
        self.next_state = "d1"
        self.backtrack_state = "d10"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[1] == states[self.backtrack_state].word[4] and \
                word[5] == states["d3"].word[9] and \
                word not in inserted_words and \
                word not in self.banned_words:
            six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in six_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D1 assignment
class D1Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d1"
        self.orientation = "down"
        self.number = 1
        self.word_length = 4
        self.next_state = "d4"
        self.backtrack_state = "a8"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[3] == states[self.backtrack_state].word[0] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D4 assignment
class D4Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d4"
        self.orientation = "down"
        self.number = 4
        self.word_length = 4
        self.next_state = "a6"
        self.backtrack_state = "a7"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[1] == states[self.backtrack_state].word[2] and \
                word[3] == states["a8"].word[6] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A6 assignment
class A6Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a6"
        self.orientation = "across"
        self.number = 6
        self.word_length = 4
        self.next_state = "a9"
        self.backtrack_state = "d1"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[1] == states[self.backtrack_state].word[1] and \
                word[3] == states["d2"].word[1] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A9 assignment
class A9Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a9"
        self.orientation = "across"
        self.number = 9
        self.word_length = 4
        self.next_state = "a11"
        self.backtrack_state = "d10"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[1] == states[self.backtrack_state].word[0] and \
                word[3] == states["d2"].word[5] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A11 assignment
class A11Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a11"
        self.orientation = "across"
        self.number = 11
        self.word_length = 4
        self.next_state = "d13"
        self.backtrack_state = "d11"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[0] == states[self.backtrack_state].word[0] and \
                word[2] == states["d5"].word[5] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D13 assignment
class D13Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d13"
        self.orientation = "down"
        self.number = 13
        self.word_length = 4
        self.next_state = "d14"
        self.backtrack_state = "a12"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[0] == states[self.backtrack_state].word[3] and \
                word[2] == states["a15"].word[3] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D14 assignment
class D14Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d14"
        self.orientation = "down"
        self.number = 14
        self.word_length = 4
        self.next_state = "a16"
        self.backtrack_state = "a12"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[0] == states[self.backtrack_state].word[9] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A16 assignment
class A16Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a16"
        self.orientation = "across"
        self.number = 16
        self.word_length = 4
        self.next_state = ""
        self.backtrack_state = "d11"
        self.clue = EMPTY_CLUE

    def is_valid(self, word):
        if word[0] == states[self.backtrack_state].word[4] and \
                word[2] == states["d14"].word[2] and \
                word not in inserted_words and \
                word not in self.banned_words:
            four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
            for row in four_char_nytcrosswords:
                if word == row["Word"]:
                    self.set_word(word)
                    return True
        return False


# Tracking states
cargo = ["d3", "a8", "a12", "d2", "d5", "d10", "d11", "a7", "a15", "d1", "d4", "a6", "a9", "a11", "d13", "d14", "a16"]

states = {
    "d3": D3Insertion(),
    "a8": A8Insertion(),
    "a12": A12Insertion(),
    "d2": D2Insertion(),
    "d5": D5Insertion(),
    "d10": D10Insertion(),
    "d11": D11Insertion(),
    "a7": A7Insertion(),
    "a15": A15Insertion(),
    "d1": D1Insertion(),
    "d4": D4Insertion(),
    "a6": A6Insertion(),
    "a9": A9Insertion(),
    "a11": A11Insertion(),
    "d13": D13Insertion(),
    "d14": D14Insertion(),
    "a16": A16Insertion()
}

wordlists = {
    11: eleven_char_words,
    10: ten_char_words,
    6: six_char_words,
    4: four_char_words
}


def next_state(current_state):
    match current_state:
        case "d3":
            return "a8"
        case "a8":
            return "a12"
        case "a12":
            return "d2"
        case "d2":
            return "d5"
        case "d5":
            return "d10"
        case "d10":
            return "d11"
        case "d11":
            return "a7"
        case "a7":
            return "a15"
        case "a15":
            return "d1"
        case "d1":
            return "d4"
        case "d4":
            return "a6"
        case "a6":
            return "a9"
        case "a9":
            return "a11"
        case "a11":
            return "d13"
        case "d13":
            return "d14"
        case "d14":
            return "a16"


def backtrack_state(current_state):
    match current_state:
        case "a8":
            return "d3"
        case "a12":
            return "d3"
        case "d2":
            return "a8"
        case "d5":
            return "a8"
        case "d10":
            return "a12"
        case "d11":
            return "a12"
        case "a7":
            return "d3"
        case "a15":
            return "d10"
        case "d1":
            return "a8"
        case "d4":
            return "a7"
        case "a6":
            return "d1"
        case "a9":
            return "d10"
        case "a11":
            return "d11"
        case "d13":
            return "a12"
        case "d14":
            return "a12"
        case "a16":
            return "d11"


def execute():
    inserted_words.clear()

    i = 0
    backtracks = 0
    print("Beginning insertions...")
    while i < MAX_RUN_TIME:
        if i >= len(cargo):
            print("End of cargo reached")


            with open('success_failure_data.csv', 'a', newline='') as success_failure_file:
                success_failure_writer = csv.writer(success_failure_file)
                success_failure_writer.writerow([word_model_return, "Success"])
                success_failure_file.flush()

            break

        current_state = cargo[i]
        state = states[current_state]
        word_list = wordlists[state.word_length]

        state.word = EMPTY_WORD

        for word in word_list:
            if state.is_valid(word):
                print("Insert Success: inserting the word " + "\"" + state.word + "\"" + " into " + current_state)
                state.word = word
                inserted_words.append(word)
                # i += 1
                break

        if state.word == EMPTY_WORD:
            n_state = backtrack_state(current_state)
            i = cargo.index(n_state)
            states[n_state].ban_current_word()
            inserted_words.remove(states[n_state].word)
            print("Insertion for " + current_state + " failed: backtracking to " + cargo[i])
            backtracks += 1
            print_words()
            continue

        if state.word in state.banned_words:
            print("No valid words remaining for " + current_state + "; crossword construction failed")

            with open('success_failure_data.csv', 'a', newline='') as success_failure_file:
                success_failure_writer = csv.writer(success_failure_file)
                success_failure_writer.writerow([word_model_return, "Failure"])
                success_failure_file.flush()

            break

        i += 1

    with open('backtrack_data.csv', 'a', newline='') as backtrack_file:
        backtrack_writer = csv.writer(backtrack_file)
        backtrack_writer.writerow([word_model_return, backtracks])
        backtrack_file.flush()


def print_words():
    print("3-down = " + states["d3"].word)
    print("8-across = " + states["a8"].word)
    print("12-across = " + states["a12"].word)
    print("2-down = " + states["d2"].word)
    print("5-down = " + states["d5"].word)
    print("10-down = " + states["d10"].word)
    print("11-down = " + states["d11"].word)
    print("7-across = " + states["a7"].word)
    print("15-across = " + states["a15"].word)
    print("1-down = " + states["d1"].word)
    print("4-down = " + states["d4"].word)
    print("6-across = " + states["a6"].word)
    print("9-across = " + states["a9"].word)
    print("11-across = " + states["a11"].word)
    print("13-down = " + states["d13"].word)
    print("14-down = " + states["d14"].word)
    print("16-across = " + states["a16"].word)


def draw_grid():
    black_square = "#"
    grid = [
        [black_square, states["d1"].word[0], black_square, states["d2"].word[0], black_square, states["d3"].word[0], black_square, states["d4"].word[0], black_square, states["d5"].word[0], black_square],
        [states["a6"].word[0], states["d1"].word[1], states["a6"].word[2], states["d2"].word[1], black_square, states["d3"].word[1], states["a7"].word[1], states["a7"].word[2], states["a7"].word[3], states["d5"].word[1], states["a7"].word[5]],
        [black_square, states["d1"].word[2], black_square, states["d2"].word[2], black_square, states["d3"].word[2], black_square, states["d4"].word[2], black_square, states["d5"].word[2], black_square],
        [black_square, states["a8"].word[0], states["a8"].word[1], states["a8"].word[2], states["a8"].word[3], states["d3"].word[3], states["a8"].word[5], states["a8"].word[6], states["a8"].word[7], states["a8"].word[8], states["a8"].word[9]],
        [black_square, black_square, black_square, states["d2"].word[4], black_square, states["d3"].word[4], black_square, black_square, black_square, states["d5"].word[4], black_square],
        [states["a9"].word[0], states["d10"].word[0], states["a9"].word[2], states["d2"].word[5], black_square, states["d3"].word[5], black_square, states["d11"].word[0], states["a11"].word[1], states["d5"].word[5], states["a11"].word[3]],
        [black_square, states["d10"].word[1], black_square, black_square, black_square, states["d3"].word[6], black_square, states["d11"].word[1], black_square, black_square, black_square],
        [states["a12"].word[0], states["a12"].word[1], states["a12"].word[2], states["a12"].word[3], states["a12"].word[4], states["d3"].word[7], states["a12"].word[6], states["a12"].word[7], states["a12"].word[8], states["a12"].word[9], black_square],
        [black_square, states["d10"].word[3], black_square, states["d13"].word[1], black_square, states["d3"].word[8], black_square, states["d11"].word[3], black_square, states["d14"].word[1], black_square],
        [states["a15"].word[0], states["d10"].word[4], states["a15"].word[2], states["a15"].word[3], states["a15"].word[4], states["d3"].word[9], black_square, states["d11"].word[4], states["a16"].word[1], states["d14"].word[2], states["a16"].word[3]],
        [black_square, states["d10"].word[5], black_square, states["d13"].word[3], black_square, states["d3"].word[10], black_square, states["d11"].word[5], black_square, states["d14"].word[3], black_square]
    ]

    print(np.matrix(grid))
    return grid


def create_clues():
    # 1. CSV File Clues
    print("Begininng CSV clues")
    eleven_char_nytcrosswords = csv.DictReader(open("eleven_char_nytcrosswords.csv", 'r', encoding="utf8"))
    for row in eleven_char_nytcrosswords:
        if states["d3"].word == row["Word"]:
            states["d3"].clue = row["Clue"]

    ten_char_nytcrosswords = csv.DictReader(open("ten_char_nytcrosswords.csv", 'r', encoding="utf8"))
    for row in ten_char_nytcrosswords:
        if states["a8"].word == row["Word"]:
            states["a8"].clue = row["Clue"]
        if states["a12"].word == row["Word"]:
            states["a12"].clue = row["Clue"]

    six_char_nytcrosswords = csv.DictReader(open("six_char_nytcrosswords.csv", 'r', encoding="utf8"))
    for row in six_char_nytcrosswords:
        if states["d2"].word == row["Word"]:
            states["d2"].clue = row["Clue"]
        if states["d5"].word == row["Word"]:
            states["d5"].clue = row["Clue"]
        if states["d10"].word == row["Word"]:
            states["d10"].clue = row["Clue"]
        if states["d11"].word == row["Word"]:
            states["d11"].clue = row["Clue"]
        if states["a7"].word == row["Word"]:
            states["a7"].clue = row["Clue"]
        if states["a15"].word == row["Word"]:
            states["a15"].clue = row["Clue"]

    four_char_nytcrosswords = csv.DictReader(open("four_char_nytcrosswords.csv", 'r', encoding="utf8"))
    for row in four_char_nytcrosswords:
        if states["d1"].word == row["Word"]:
            states["d1"].clue = row["Clue"]
        if states["d4"].word == row["Word"]:
            states["d4"].clue = row["Clue"]
        if states["a6"].word == row["Word"]:
            states["a6"].clue = row["Clue"]
        if states["a9"].word == row["Word"]:
            states["a9"].clue = row["Clue"]
        if states["a11"].word == row["Word"]:
            states["a11"].clue = row["Clue"]
        if states["d13"].word == row["Word"]:
            states["d13"].clue = row["Clue"]
        if states["d14"].word == row["Word"]:
            states["d14"].clue = row["Clue"]
        if states["a16"].word == row["Word"]:
            states["a16"].clue = row["Clue"]
    print("Finished CSV clues")

    print("\nAcross Clues:")
    print("6: " + str(states["a6"].clue) + ": " + states["a6"].word)
    print("7: " + str(states["a7"].clue) + ": " + states["a7"].word)
    print("8: " + str(states["a8"].clue) + ": " + states["a8"].word)
    print("9: " + str(states["a9"].clue) + ": " + states["a9"].word)
    print("11: " + str(states["a11"].clue) + ": " + states["a11"].word)
    print("12: " + str(states["a12"].clue) + ": " + states["a12"].word)
    print("15: " + str(states["a15"].clue) + ": " + states["a15"].word)
    print("16: " + str(states["a16"].clue) + ": " + states["a16"].word)

    print("\nDown Clues:")
    print("1: " + str(states["d1"].clue) + ": " + states["d1"].word)
    print("2: " + str(states["d2"].clue) + ": " + states["d2"].word)
    print("3: " + str(states["d3"].clue) + ": " + states["d3"].word)
    print("4: " + str(states["d4"].clue) + ": " + states["d4"].word)
    print("5: " + str(states["d5"].clue) + ": " + states["d5"].word)
    print("10: " + str(states["d10"].clue) + ": " + states["d10"].word)
    print("11: " + str(states["d11"].clue) + ": " + states["d11"].word)
    print("13: " + str(states["d13"].clue) + ": " + states["d13"].word)
    print("14: " + str(states["d14"].clue) + ": " + states["d14"].word)


app.run(port=7776)
