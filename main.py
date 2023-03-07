import requests
import time
import numpy as np
from better_profanity import profanity
import csv

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"
EMPTY_CHAR = "_"
MAX_RUN_TIME = 2000
inserted_words = []

eleven_char_file = open("eleven_char_nytcrosswords.csv", 'r')
ten_char_file = open("ten_char_nytcrosswords.csv", 'r')
six_char_file = open("six_char_nytcrosswords.csv", 'r')
four_char_file = open("four_char_nytcrosswords.csv", 'r')

eleven_char_nytcrosswords = csv.DictReader(eleven_char_file)
ten_char_nytcrosswords = csv.DictReader(ten_char_file)
six_char_nytcrosswords = csv.DictReader(six_char_file)
four_char_nytcrosswords = csv.DictReader(four_char_file)

# Word list initialization
eleven_char_words = []
ten_char_words = []
six_char_words = []
four_char_words = []

# Grid creation
# black_square = "#"
# white_square = "-"
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


def word2vec(user_words: list[str]):
    print(time.time() - start_time, "seconds: Retrieving sim_list")
    sim_list = requests.get('http://4e86-109-255-231-194.ngrok.io/request/?user_words=' + words)

    word_list = [i[0] for i in sim_list.json()]

    print(time.time() - start_time, "seconds: sim_list successfully retrieved")

    dictionaries(word_list)


def dictionaries(word_list):
    # Populate word lists
    print(time.time() - start_time, "seconds: Populating word lists...")
    # file = open("nytcrosswords.csv", 'r')
    # nytcrosswords = csv.DictReader(file)

    for word in word_list:
        if len(word) == 11 and all(c not in BANNED_CHARACTERS for c in word):
            # print(time.time() - start_time, "seconds: Adding " + word + " to the list")
            eleven_char_words.append(word.upper())
        if len(word) == 10 and all(c not in BANNED_CHARACTERS for c in word):
            # print(time.time() - start_time, "seconds: Adding " + word + " to the list")
            ten_char_words.append(word.upper())
        if len(word) == 6 and all(c not in BANNED_CHARACTERS for c in word):
            # print(time.time() - start_time, "seconds: Adding " + word + " to the list")
            six_char_words.append(word.upper())
        if len(word) == 4 and all(c not in BANNED_CHARACTERS for c in word):
            # print(time.time() - start_time, "seconds: Adding " + word + " to the list")
            four_char_words.append(word.upper())

    # new_eleven_char_words = []
    # for row in eleven_char_nytcrosswords:
    #     for word in eleven_char_words:
    #         if word == row["Word"]:
    #             print(time.time() - start_time, "seconds: Common word " + word + " found; adding")
    #             new_eleven_char_words.append(word)
    #             break
    #
    # eleven_char_words.clear()
    #
    # for word in new_eleven_char_words:
    #     print(time.time() - start_time, "seconds: Adding " + word + " to eleven_char_words")
    #     eleven_char_words.append(word)
    #
    # new_ten_char_words = []
    # for row in ten_char_nytcrosswords:
    #     for word in ten_char_words:
    #         if word == row["Word"]:
    #             print(time.time() - start_time, "seconds: Common word " + word + " found; adding")
    #             new_ten_char_words.append(word)
    #             break
    #
    # ten_char_words.clear()
    #
    # for word in new_ten_char_words:
    #     print(time.time() - start_time, "seconds: Adding " + word + " to ten_char_words")
    #     ten_char_words.append(word)
    #
    # new_six_char_words = []
    # for row in six_char_nytcrosswords:
    #     for word in six_char_words:
    #         if word == row["Word"]:
    #             print(time.time() - start_time, "seconds: Common word " + word + " found; adding")
    #             new_six_char_words.append(word)
    #             break
    #
    # six_char_words.clear()
    #
    # for word in new_six_char_words:
    #     print(time.time() - start_time, "seconds: Adding " + word + " to six_char_words")
    #     six_char_words.append(word)
    #
    # new_four_char_words = []
    # for row in four_char_nytcrosswords:
    #     for word in four_char_words:
    #         if word == row["Word"]:
    #             print(time.time() - start_time, "seconds: Common word " + word + " found; adding")
    #             new_four_char_words.append(word)
    #             break
    #
    # four_char_words.clear()
    #
    # for word in new_four_char_words:
    #     print(time.time() - start_time, "seconds: Adding " + word + " to four_char_words")
    #     four_char_words.append(word)

    print(time.time() - start_time, "seconds: Done")

    # print("Eleven character words:")
    # for word in eleven_char_words:
    #     print(word)

    # print("Ten character words:")
    # for word in ten_char_words:
    #     print(word)

    # print("Six character words:")
    # for word in six_char_words:
    #     print(word)

    # print("Four character words:")
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
        self.word_length = 11
        self.next_state = "a8"

    def is_valid(self, word):
        if word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# A8 assignment
class A8Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a8"
        self.word_length = 10
        self.next_state = "a12"
        self.backtrack_state = "d3"

    def is_valid(self, word):
        if word[4].casefold() == states[self.backtrack_state].word[3].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# A12 assignment
class A12Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a12"
        self.word_length = 10
        self.next_state = "d2"
        self.backtrack_state = "d3"

    def is_valid(self, word):
        if word[5].casefold() == states[self.backtrack_state].word[7].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# D2 assignment
class D2Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d2"
        self.word_length = 6
        self.next_state = "d5"
        self.backtrack_state = "a8"

    def is_valid(self, word):
        if word[3].casefold() == states[self.backtrack_state].word[2].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# D5 assignment
class D5Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d5"
        self.word_length = 6
        self.next_state = "d10"
        self.backtrack_state = "a8"

    def is_valid(self, word):
        if word[3].casefold() == states[self.backtrack_state].word[8].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# D10 assignment
class D10Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d10"
        self.word_length = 6
        self.next_state = "d11"
        self.backtrack_state = "a12"

    def is_valid(self, word):
        if word[2].casefold() == states[self.backtrack_state].word[1].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# D11 assignment
class D11Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d11"
        self.word_length = 6
        self.next_state = "a7"
        self.backtrack_state = "a12"

    def is_valid(self, word):
        if word[2].casefold() == states[self.backtrack_state].word[7].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# A7 assignment
class A7Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a7"
        self.word_length = 6
        self.next_state = "a15"
        self.backtrack_state = "d3"

    def is_valid(self, word):
        if word[0].casefold() == states[self.backtrack_state].word[1].casefold() and word[4].casefold() == \
                states["d5"].word[
                    1].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# A15 assignment
class A15Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a15"
        self.word_length = 6
        self.next_state = "d1"
        self.backtrack_state = "d10"

    def is_valid(self, word):
        if word[1].casefold() == states[self.backtrack_state].word[4].casefold() and word[5].casefold() == \
                states["d3"].word[
                    9].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# D1 assignment
class D1Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d1"
        self.word_length = 4
        self.next_state = "d4"
        self.backtrack_state = "a8"

    def is_valid(self, word):
        if word[3].casefold() == states[self.backtrack_state].word[0].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # print("big memes")
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"], "for d1")
            #     if word == row["Word"]:
            #         print("Found Word!")
            #         self.set_word(word)
            #         break
            # if self.word != EMPTY_WORD:
            #     return True
            self.set_word(word)
            return True
        return False


# D4 assignment
class D4Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d4"
        self.word_length = 4
        self.next_state = "a6"
        self.backtrack_state = "a7"

    def is_valid(self, word):
        if word[1].casefold() == states[self.backtrack_state].word[2].casefold() and word[3].casefold() == \
                states["a8"].word[
                    6].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A6 assignment
class A6Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a6"
        self.word_length = 4
        self.next_state = "a9"
        self.backtrack_state = "d1"

    def is_valid(self, word):
        if word[1].casefold() == states[self.backtrack_state].word[1].casefold() and word[3].casefold() == \
                states["d2"].word[
                    1].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
            #         print("Found Word!")
                    self.set_word(word)
                    return True
        return False


# A9 assignment
class A9Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a9"
        self.word_length = 4
        self.next_state = "a11"
        self.backtrack_state = "d10"

    def is_valid(self, word):
        if word[1].casefold() == states[self.backtrack_state].word[0].casefold() and word[3].casefold() == \
                states["d2"].word[
                    5].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A11 assignment
class A11Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a11"
        self.word_length = 4
        self.next_state = "d13"
        self.backtrack_state = "d11"

    def is_valid(self, word):
        if word[0].casefold() == states[self.backtrack_state].word[0].casefold() and word[2].casefold() == \
                states["d5"].word[
                    5].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D13 assignment
class D13Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d13"
        self.word_length = 4
        self.next_state = "d14"
        self.backtrack_state = "a12"

    def is_valid(self, word):
        if word[0].casefold() == states[self.backtrack_state].word[3].casefold() and word[2].casefold() == \
                states["a15"].word[
                    3].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
                    self.set_word(word)
                    return True
        return False


# D14 assignment
class D14Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "d14"
        self.word_length = 4
        self.next_state = "a16"
        self.backtrack_state = "a12"

    def is_valid(self, word):
        if word[0].casefold() == states[self.backtrack_state].word[9].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
                    self.set_word(word)
                    return True
        return False


# A16 assignment
class A16Insertion(WordInsertions):
    def __init__(self):
        super().__init__()
        self.banned_words = []
        self.name = "a16"
        self.word_length = 4
        self.next_state = ""
        self.backtrack_state = "d11"

    def is_valid(self, word):
        if word[0].casefold() == states[self.backtrack_state].word[4].casefold() and word[2].casefold() == \
                states["d14"].word[
                    2].casefold() and not profanity.contains_profanity(word) and word not in inserted_words and word not in self.banned_words:
            # for row in four_char_nytcrosswords:
            #     print("Checking if " + word + " is the same as", row["Word"])
            #     if word in row["Word"]:
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
    print(time.time() - start_time, "seconds: Beginning insertions...")
    while i < MAX_RUN_TIME:
        if i >= len(cargo):
            print("End of cargo reached")
            break

        current_state = cargo[i]
        state = states[current_state]
        word_list = wordlists[state.word_length]

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
            print("Insertion for " + current_state + " failed: backtracking to " + cargo[i])
            print_words()
            continue

        if state.word in state.banned_words:
            print("No valid words remaining for " + current_state + "; crossword construction failed")
            break

        i += 1

    draw_grid()

    create_clues()


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
    white_square = "-"
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


def create_clues():
    a6_clue = a7_clue = a8_clue = a9_clue = a11_clue = a12_clue = a15_clue = a16_clue = ""
    d1_clue = d2_clue = d3_clue = d4_clue = d5_clue = d10_clue = d11_clue = d13_clue = d14_clue = ""

    for row in eleven_char_nytcrosswords:
        if states["d11"].word == row["Word"]:
            d11_clue = row["Clue"]

    for row in ten_char_nytcrosswords:
        if states["a8"].word == row["Word"]:
            a8_clue = row["Clue"]
        if states["a12"].word == row["Word"]:
            a12_clue = row["Clue"]

    for row in six_char_nytcrosswords:
        if states["d2"].word == row["Word"]:
            d2_clue = row["Clue"]
        if states["d5"].word == row["Word"]:
            d5_clue = row["Clue"]
        if states["d10"].word == row["Word"]:
            d10_clue = row["Clue"]
        if states["d11"].word == row["Word"]:
            d11_clue = row["Clue"]
        if states["a7"].word == row["Word"]:
            a7_clue = row["Clue"]
        if states["a15"].word == row["Word"]:
            a15_clue = row["Clue"]

    for row in four_char_nytcrosswords:
        if states["d1"].word == row["Word"]:
            d1_clue = row["Clue"]
        if states["d4"].word == row["Word"]:
            d4_clue = row["Clue"]
        if states["a6"].word == row["Word"]:
            a6_clue = row["Clue"]
        if states["a9"].word == row["Word"]:
            a9_clue = row["Clue"]
        if states["a11"].word == row["Word"]:
            a11_clue = row["Clue"]
        if states["d13"].word == row["Word"]:
            d13_clue = row["Clue"]
        if states["d14"].word == row["Word"]:
            d14_clue = row["Clue"]
        if states["a16"].word == row["Word"]:
            a16_clue = row["Clue"]

    print("\nAcross Clues:")
    print("6: " + a6_clue)
    print("7: " + a7_clue)
    print("8: " + a8_clue)
    print("9: " + a9_clue)
    print("11: " + a11_clue)
    print("12: " + a12_clue)
    print("15: " + a15_clue)
    print("16: " + a16_clue)

    print("\nDown Clues:")
    print("1: " + d1_clue)
    print("2: " + d2_clue)
    print("3: " + d3_clue)
    print("4: " + d4_clue)
    print("5: " + d5_clue)
    print("10: " + d10_clue)
    print("11: " + d11_clue)
    print("13: " + d13_clue)
    print("14: " + d14_clue)

# bad_word = "shit"

# print(profanity.contains_profanity(bad_word))

user_word_1 = input("Enter a word: ")
user_word_2 = input("Enter another word: ")
user_word_3 = input("Enter a final word: ")

start_time = time.time()

words = user_word_1 + "," + user_word_2 + "," + user_word_3
word2vec(words.split(','))

execute()

print("Finished. Total execution time: ", time.time() - start_time, " seconds")
