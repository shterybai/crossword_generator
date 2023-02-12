import gensim
from gensim.models import Word2Vec
from statemachine import StateMachine, State
import requests

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"
EMPTY_CHAR = "_"
MAX_RUN_TIME = 20000

# Word list initialization
eleven_char_words = []
ten_char_words = []
six_char_words = []
four_char_words = []


def word2vec(user_words: list[str]):
    sim_list = requests.get('http://5e4c-109-255-34-132.ngrok.io/request/?user_words=' + words)

    word_list = [i[0] for i in sim_list.json()]

    # print(word_list)

    dictionaries(word_list)


def dictionaries(word_list):
    # Populate word lists
    for word in word_list:
        if len(word) == 11:
            if all(c not in BANNED_CHARACTERS for c in word):
                eleven_char_words.append(word)
        if len(word) == 10:
            if all(c not in BANNED_CHARACTERS for c in word):
                ten_char_words.append(word)
        if len(word) == 6:
            if all(c not in BANNED_CHARACTERS for c in word):
                six_char_words.append(word)
        if len(word) == 4:
            if all(c not in BANNED_CHARACTERS for c in word):
                four_char_words.append(word)

    # print("Eleven character words: " + eleven_char_words[0])
    # print("Ten character words: " + ten_char_words[0])
    # print("Six character words: " + six_char_words[0])
    # print("Four character words: " + four_char_words[0])

    # insertions(eleven_char_words, ten_char_words, six_char_words, four_char_words)
    # D3Insertion()


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
        if word[4] == states[self.backtrack_state].word[3] and word not in self.banned_words:
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
        if word[5] == states[self.backtrack_state].word[7] and word not in self.banned_words:
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
        if word[3] == states[self.backtrack_state].word[2] and word not in self.banned_words:
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
        if word[3] == states[self.backtrack_state].word[8] and word not in self.banned_words:
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
        if word[2] == states[self.backtrack_state].word[1] and word not in self.banned_words:
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
        if word[2] == states[self.backtrack_state].word[7] and word not in self.banned_words:
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
        if word[0] == states[self.backtrack_state].word[1] and word[4] == states["d5"].word[
            1] and word not in self.banned_words:
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
        if word[1] == states[self.backtrack_state].word[4] and word[5] == states["d3"].word[
            9] and word not in self.banned_words:
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
        if word[3] == states[self.backtrack_state].word[0] and word not in self.banned_words:
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
        if word[1] == states[self.backtrack_state].word[2] and word[3] == states["a8"].word[
            6] and word not in self.banned_words:
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
        if word[1] == states[self.backtrack_state].word[1] and word[3] == states["d2"].word[
            1] and word not in self.banned_words:
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
        if word[1] == states[self.backtrack_state].word[0] and word[3] == states["d2"].word[
            5] and word not in self.banned_words:
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
        if word[0] == states[self.backtrack_state].word[0] and word[2] == states["d5"].word[
            5] and word not in self.banned_words:
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
        if word[0] == states[self.backtrack_state].word[3] and word[2] == states["a15"].word[
            3] and word not in self.banned_words:
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
        if word[0] == states[self.backtrack_state].word[9] and word not in self.banned_words:
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
        if word[0] == states[self.backtrack_state].word[4] and word[2] == states["d14"].word[
            2] and word not in self.banned_words:
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
    i = 0
    while i < MAX_RUN_TIME:
        if i >= len(cargo):
            print("End of cargo reached")
            break

        current_state = cargo[i]
        state = states[current_state]
        word_list = wordlists[state.word_length]

        for word in word_list:
            if state.is_valid(word):
                state.word = word
                print("Insert Success: inserting into " + current_state + " \"" + state.word + "\"")
                i += 1
                break

        if state.word == EMPTY_WORD:
            n_state = backtrack_state(current_state)
            i = cargo.index(n_state)
            states[n_state].ban_current_word()
            print("Insert for " + current_state + " failed: backtracking to " + cargo[i])
            print_words()
            continue

    print_words()


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


user_word_1 = input("Enter a word: ")
user_word_2 = input("Enter another word: ")
user_word_3 = input("Enter a final word: ")

words = user_word_1 + "," + user_word_2 + "," + user_word_3
word2vec(words.split(','))

execute()
