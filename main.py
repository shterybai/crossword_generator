import gensim
from gensim.models import Word2Vec
from statemachine import StateMachine, State
import requests

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"

# Word list initialization
eleven_char_words = []
ten_char_words = []
six_char_words = []
four_char_words = []


# model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/GoogleNews-vectors-negative300.bin', binary=True)


def word2vec(user_words: list[str]):
    sim_list = requests.get('http://ecc1-109-255-34-132.ngrok.io/request/?user_words=' + words)

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


# D3 assignment
class D3Insertion:
    def __init__(self):
        self.banned_words = []
        self.name = "d3"
        self.word = EMPTY_WORD
        self.word_length = 11
        self.next_state = "a8"

    def set_word(self, word):
        self.word = word
        return self.next_state

    def ban_current_word(self):
        if self.word != EMPTY_WORD:
            self.banned_words.append(self.word)

    def ban_word(self, word):
        self.banned_words.append(word)

    def is_valid(self, word):
        if word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# A8 assignment
class A8Insertion:
    def __init__(self):
        self.banned_words = []
        self.name = "a8"
        self.word = EMPTY_WORD
        self.word_length = 10
        self.next_state = "a12"
        self.backtrack_state = "d3"

    def set_word(self, word):
        self.word = word
        return self.next_state

    def ban_current_word(self):
        if self.word != EMPTY_WORD:
            self.banned_words.append(self.word)

    def ban_word(self, word):
        self.banned_words.append(word)

    def is_valid(self, word):
        # for word in ten_char_words:
        if word[4] == states["d3"].word[3] and word not in self.banned_words:
            self.set_word(word)
            return True
        return False


# # A12 assignment
# def a12_insertion(a12_banned, d3, ten_char_words):
#     for word in ten_char_words:
#         if word[5] == d3[7] and word not in a12_banned:
#             a12 = word
#             newState = "d2_insertion"
#         else:
#             newState = "d3_insertion"
#     return (newState, a12)
#
# # D2 assignment
# def d2_insertion(d2_banned, a8, six_char_words):
#     for word in six_char_words:
#         if word[3] == a8[2] and word not in d2_banned:
#             d2 = word
#             return d2
#     return EMPTY_WORD
#
# # D5 assignment
# def d5_insertion(d5_banned, a8, six_char_words):
#     for word in six_char_words:
#         if word[3] == a8[8] and word not in d5_banned:
#             d5 = word
#             return d5
#     return EMPTY_WORD
#
# # D10 assignment
# def d10_insertion(d10_banned, a12, six_char_words):
#     for word in six_char_words:
#         if word[2] == a12[1] and word not in d10_banned:
#             d10 = word
#             return d10
#     return EMPTY_WORD
#
# # D11 assignment
# def d11_insertion(d11_banned, a12, six_char_words):
#     for word in six_char_words:
#         if word[2] == a12[7] and word not in d11_banned:
#             d11 = word
#             return d11
#     return EMPTY_WORD
#
# # A7 assignment
# def a7_insertion(a7_banned, d3, six_char_words):
#     for word in six_char_words:
#         if word[0] == d3[1] and word[5] == d3[9] and word not in a7_banned:
#             a7 = word
#             return a7
#     return EMPTY_WORD
#
# # A15 assignment
# def a15_insertion(a15_banned, d10, d3, six_char_words):
#     for word in six_char_words:
#         if word[1] == d10[4] and word[5] == d3[9] and word not in a15_banned:
#             a15 = word
#             return a15
#     return EMPTY_WORD
#
# # D1 assignment
# def d1_insertion(d1_banned, a8, four_char_words):
#     for word in four_char_words:
#         if word[3] == a8[0] and word not in d1_banned:
#             d1 = word
#             return d1
#     return EMPTY_WORD
#
# # D4 assignment
# def d4_insertion(d4_banned, a7, a8, four_char_words):
#     for word in four_char_words:
#         if word[1] == a7[2] and word[3] == a8[6] and word not in d4_banned:
#             d4 = word
#             return d4
#     return EMPTY_WORD
#
# # A6 assignment
# def a6_insertion(a6_banned, d1, d2, four_char_words):
#     for word in four_char_words:
#         if word[1] == d1[1] and word[3] == d2[1] and word not in a6_banned:
#             a6 = word
#             return a6
#     return EMPTY_WORD
#
# # A9 assignment
# def a9_insertion(a9_banned, d10, d2, four_char_words):
#     for word in four_char_words:
#         if word[1] == d10[0] and word[3] == d2[5] and word not in a9_banned:
#             a9 = word
#             return a9
#     return EMPTY_WORD
#
# # A11 assignment
# def a11_insertion(a11_banned, d11, d5, four_char_words):
#     for word in four_char_words:
#         if word[0] == d11[0] and word[1] == d5[5] and word not in a11_banned:
#             a11 = word
#             return a11
#     return EMPTY_WORD
#
# # D13 assignment
# def d13_insertion(d13_banned, a12, four_char_words):
#     for word in four_char_words:
#         if word[0] == a12[3] and word not in d13_banned:
#             d13 = word
#             return d13
#     return EMPTY_WORD
#
# # D14 assignment
# def d14_insertion(d14_banned, a12, four_char_words):
#     for word in four_char_words:
#         if word[0] == a12[9] and word not in d14_banned:
#             d14 = word
#             return d14
#     return EMPTY_WORD
#
# # A16 assignment
# def a16_insertion(a16_banned, d11, d14, four_char_words):
#     for word in four_char_words:
#         if word[0] == d11[4] and word[2] == d14[2] and word not in a16_banned:
#             a16 = word
#             return a16
#     return EMPTY_WORD

# Tracking states
# cargo = ["d3", "a8", "a12", "d2", "d5", "d10", "d11", "a7", "a15", "d1", "d4", "a6", "a9", "a11", "d13", "d14", "a16"]
cargo = ["d3", "a8"]

states = {
    "d3": D3Insertion(),
    "a8": A8Insertion()
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


def backtrack_state(current_state):
    match current_state:
        case "a8":
            return "d3"


def execute():
    i = 0
    while i < 20000:
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
            n_state = next_state(current_state)
            i = cargo.index(n_state)
            states[n_state].ban_current_word()
            print("Insert for " + current_state + " failed: backtracking to " + cargo[i])
            continue


user_word_1 = input("Enter a word: ")
user_word_2 = input("Enter another word: ")
user_word_3 = input("Enter a final word: ")

words = user_word_1 + "," + user_word_2 + "," + user_word_3
word2vec(words.split(','))

execute()

print("3-down = " + states["d3"].word)
print("8-across = " + states["a8"].word)
# print("12-across = " + a12)
# print("2-down = " + d2)
# print("5-down = " + d5)
# print("10-down = " + d10)
# print("11-down = " + d11)
# print("7-across = " + a7)
# print("15-across = " + a15)
# print("1-down = " + d1)
# print("4-down = " + d4)
# print("6-across = " + a6)
# print("9-across = " + a9)
# print("11-across = " + a11)
# print("13-down = " + d13)
# print("14-down = " + d14)
# print("16-across = " + a16)
