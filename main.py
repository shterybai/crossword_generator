import gensim
from gensim.models import Word2Vec
from statemachine import StateMachine, State
import requests

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"

# model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/GoogleNews-vectors-negative300.bin', binary=True)


def word2vec(user_words: list[str]):
    # print(model.most_similar(positive=words, topn=5000))

    # sim_list = model.most_similar(positive=user_words, topn=100000)

    sim_list = requests.get('http://744f-109-255-34-132.ngrok.io/request/?user_words=' + words)

    word_list = [i[0] for i in sim_list.json()]

    # print(word_list)

    dictionaries(word_list)


def dictionaries(word_list):
    # Word list initialization
    eleven_char_words = []
    ten_char_words = []
    six_char_words = []
    four_char_words = []

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


class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self):
        # try:
        handler = self.handlers[self.startState]
        # except:
        #     raise InitializationError("must call .set_start() before .run()")
        # if not self.endStates:
        #     raise InitializationError("at least one state must be an end_state")

        while True:
            (newState) = handler()
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break
            else:
                handler = self.handlers[newState.upper()]



    # D3 assignment
    def d3_insertion(d3_banned, eleven_char_words):
        for word in eleven_char_words:
            if word not in d3_banned:
                d3 = word
                newState = "a8_insertion"
                return (newState)

    # A8 assignment
    def a8_insertion(a8_banned, d3, ten_char_words):
        for word in ten_char_words:
            if word[4] == d3[3] and word not in a8_banned:
                a8 = word
                newState = "a12_insertion"
                break
        if a8 == EMPTY_WORD:
            newState = "d3_insertion"
        return (newState)

    # A12 assignment
    def a12_insertion(a12_banned, d3, ten_char_words):
        for word in ten_char_words:
            if word[5] == d3[7] and word not in a12_banned:
                a12 = word
                newState = "d2_insertion"
            else:
                newState = "d3_insertion"
        return (newState, a12)

    # D2 assignment
    def d2_insertion(d2_banned, a8, six_char_words):
        for word in six_char_words:
            if word[3] == a8[2] and word not in d2_banned:
                d2 = word
                return d2
        return EMPTY_WORD

    # D5 assignment
    def d5_insertion(d5_banned, a8, six_char_words):
        for word in six_char_words:
            if word[3] == a8[8] and word not in d5_banned:
                d5 = word
                return d5
        return EMPTY_WORD

    # D10 assignment
    def d10_insertion(d10_banned, a12, six_char_words):
        for word in six_char_words:
            if word[2] == a12[1] and word not in d10_banned:
                d10 = word
                return d10
        return EMPTY_WORD

    # D11 assignment
    def d11_insertion(d11_banned, a12, six_char_words):
        for word in six_char_words:
            if word[2] == a12[7] and word not in d11_banned:
                d11 = word
                return d11
        return EMPTY_WORD

    # A7 assignment
    def a7_insertion(a7_banned, d3, six_char_words):
        for word in six_char_words:
            if word[0] == d3[1] and word[5] == d3[9] and word not in a7_banned:
                a7 = word
                return a7
        return EMPTY_WORD

    # A15 assignment
    def a15_insertion(a15_banned, d10, d3, six_char_words):
        for word in six_char_words:
            if word[1] == d10[4] and word[5] == d3[9] and word not in a15_banned:
                a15 = word
                return a15
        return EMPTY_WORD

    # D1 assignment
    def d1_insertion(d1_banned, a8, four_char_words):
        for word in four_char_words:
            if word[3] == a8[0] and word not in d1_banned:
                d1 = word
                return d1
        return EMPTY_WORD

    # D4 assignment
    def d4_insertion(d4_banned, a7, a8, four_char_words):
        for word in four_char_words:
            if word[1] == a7[2] and word[3] == a8[6] and word not in d4_banned:
                d4 = word
                return d4
        return EMPTY_WORD

    # A6 assignment
    def a6_insertion(a6_banned, d1, d2, four_char_words):
        for word in four_char_words:
            if word[1] == d1[1] and word[3] == d2[1] and word not in a6_banned:
                a6 = word
                return a6
        return EMPTY_WORD

    # A9 assignment
    def a9_insertion(a9_banned, d10, d2, four_char_words):
        for word in four_char_words:
            if word[1] == d10[0] and word[3] == d2[5] and word not in a9_banned:
                a9 = word
                return a9
        return EMPTY_WORD

    # A11 assignment
    def a11_insertion(a11_banned, d11, d5, four_char_words):
        for word in four_char_words:
            if word[0] == d11[0] and word[1] == d5[5] and word not in a11_banned:
                a11 = word
                return a11
        return EMPTY_WORD

    # D13 assignment
    def d13_insertion(d13_banned, a12, four_char_words):
        for word in four_char_words:
            if word[0] == a12[3] and word not in d13_banned:
                d13 = word
                return d13
        return EMPTY_WORD

    # D14 assignment
    def d14_insertion(d14_banned, a12, four_char_words):
        for word in four_char_words:
            if word[0] == a12[9] and word not in d14_banned:
                d14 = word
                return d14
        return EMPTY_WORD

    # A16 assignment
    def a16_insertion(a16_banned, d11, d14, four_char_words):
        for word in four_char_words:
            if word[0] == d11[4] and word[2] == d14[2] and word not in a16_banned:
                a16 = word
                return a16
        return EMPTY_WORD

# class Insertions(StateMachine):
#     d3 = State('Empty', initial=True)
#     a6 = a7 = a8 = a9 = a11 = a12 = a15 = a16 = d1 = d2 = d3 = d4 = d5 = d10 = d11 = d13 = d14 = State('Empty')
#
#     d3found = d3.to(a8)
#
#     a8found = a8.to(a12)
#     a8notfound = a8.to(d3)
#
#     a12found = a12.to(d2)
#     a12notfound = a12.to(d3)
#
#     d2found = d2.to(d5)
#     d2notfound = d2.to(a8)
#
#     d5found = d5.to(d10)
#     d5notfound = d5.to(a8)
#
#     d10found = d10.to(d11)
#     d10notfound = d10.to(a12)
#
#     d11found = d11.to(a7)
#     d11notfound = d11.to(a12)
#
#     a7found = a7.to(a15)
#     a7notfound = a7.to(d3)
#
#     a15found = a15.to(d1)
#     a15notfound = a15.to(d3)
#
#     d1found = d1.to(d4)
#     d1notfound = d1.to(a8)
#
#     d4found = d4.to(a6)
#     d4notfound = d4.to(a8)
#
#     a6found = a6.to(a9)
#     a6notfound = a6.to(d2)
#
#     a9found = a9.to(a11)
#     a9notfound = a9.to(d2)
#
#     a11found = a11.to(d13)
#     a11notfound = a11.to(d5)
#
#     d13found = d13.to(d14)
#     d13notfound = d13.to(a12)
#
#     d14found = d14.to(a16)
#     d14notfound = d14.to(a12)
#
#     a16notfound = a16.to(d14)
#
#     def insertions(eleven_char_words, ten_char_words, six_char_words, four_char_words):
#         # a6 = a7 = a8 = a9 = a11 = a12 = a15 = a16 = d1 = d2 = d3 = d4 = d5 = d10 = d11 = d13 = d14 = EMPTY_WORD
#
#         a6_banned = a7_banned = a8_banned = a9_banned = a11_banned = a12_banned = a15_banned = a16_banned = d1_banned = \
#             d2_banned = d3_banned = d4_banned = d5_banned = d10_banned = d11_banned = d13_banned = d14_banned = []
#
#         d3 = d3_insertion(d3_banned, eleven_char_words)
#         a8 = a8_insertion(a8_banned, d3, ten_char_words)
#         a12 = a12_insertion(a12_banned, d3, ten_char_words)
#         d2 = d2_insertion(d2_banned, a8, six_char_words)
#         d5 = d5_insertion(d5_banned, a8, six_char_words)
#         d10 = d10_insertion(d10_banned, a12, six_char_words)
#         d11 = d11_insertion(d11_banned, a12, six_char_words)
#         a7 = a7_insertion(a7_banned, d3, six_char_words)
#         a15 = a15_insertion(a15_banned, d10, d3, six_char_words)
#         d1 = d1_insertion(d1_banned, a8, four_char_words)
#         d4 = d4_insertion(d4_banned, a7, a8, four_char_words)
#         a6 = a6_insertion(a6_banned, d1, d2, four_char_words)
#         a9 = a9_insertion(a9_banned, d10, d2, four_char_words)
#         a11 = a11_insertion(a11_banned, d11, d5, four_char_words)
#         d13 = d13_insertion(d13_banned, a12, four_char_words)
#         d14 = d14_insertion(d14_banned, a12, four_char_words)
#         a16 = a16_insertion(a16_banned, d11, d14, four_char_words)
#
#         print("3-down = " + d3)
#         print("8-across = " + a8)
#         print("12-across = " + a12)
#         print("2-down = " + d2)
#         print("5-down = " + d5)
#         print("10-down = " + d10)
#         print("11-down = " + d11)
#         print("7-across = " + a7)
#         print("15-across = " + a15)
#         print("1-down = " + d1)
#         print("4-down = " + d4)
#         print("6-across = " + a6)
#         print("9-across = " + a9)
#         print("11-across = " + a11)
#         print("13-down = " + d13)
#         print("14-down = " + d14)
#         print("16-across = " + a16)
#
#
    # # D3 assignment
    # def d3_insertion(d3_banned, eleven_char_words):
    #     for word in eleven_char_words:
    #         if word not in d3_banned:
    #             d3 = word
    #             return d3
    #     return EMPTY_WORD
    #
    #
    # # A8 assignment
    # def a8_insertion(a8_banned, d3, ten_char_words):
    #     for word in ten_char_words:
    #         if word[4] == d3[3] and word not in a8_banned:
    #             a8 = word
    #             return a8
    #     return EMPTY_WORD
    #
    #
    # # A12 assignment
    # def a12_insertion(a12_banned, d3, ten_char_words):
    #     for word in ten_char_words:
    #         if word[5] == d3[7] and word not in a12_banned:
    #             a12 = word
    #             return a12
    #     return EMPTY_WORD
    #
    #
    # # D2 assignment
    # def d2_insertion(d2_banned, a8, six_char_words):
    #     for word in six_char_words:
    #         if word[3] == a8[2] and word not in d2_banned:
    #             d2 = word
    #             return d2
    #     return EMPTY_WORD
    #
    #
    # # D5 assignment
    # def d5_insertion(d5_banned, a8, six_char_words):
    #     for word in six_char_words:
    #         if word[3] == a8[8] and word not in d5_banned:
    #             d5 = word
    #             return d5
    #     return EMPTY_WORD
    #
    #
    # # D10 assignment
    # def d10_insertion(d10_banned, a12, six_char_words):
    #     for word in six_char_words:
    #         if word[2] == a12[1] and word not in d10_banned:
    #             d10 = word
    #             return d10
    #     return EMPTY_WORD
    #
    #
    # # D11 assignment
    # def d11_insertion(d11_banned, a12, six_char_words):
    #     for word in six_char_words:
    #         if word[2] == a12[7] and word not in d11_banned:
    #             d11 = word
    #             return d11
    #     return EMPTY_WORD
    #
    #
    # # A7 assignment
    # def a7_insertion(a7_banned, d3, six_char_words):
    #     for word in six_char_words:
    #         if word[0] == d3[1] and word[5] == d3[9] and word not in a7_banned:
    #             a7 = word
    #             return a7
    #     return EMPTY_WORD
    #
    #
    # # A15 assignment
    # def a15_insertion(a15_banned, d10, d3, six_char_words):
    #     for word in six_char_words:
    #         if word[1] == d10[4] and word[5] == d3[9] and word not in a15_banned:
    #             a15 = word
    #             return a15
    #     return EMPTY_WORD
    #
    #
    # # D1 assignment
    # def d1_insertion(d1_banned, a8, four_char_words):
    #     for word in four_char_words:
    #         if word[3] == a8[0] and word not in d1_banned:
    #             d1 = word
    #             return d1
    #     return EMPTY_WORD
    #
    #
    # # D4 assignment
    # def d4_insertion(d4_banned, a7, a8, four_char_words):
    #     for word in four_char_words:
    #         if word[1] == a7[2] and word[3] == a8[6] and word not in d4_banned:
    #             d4 = word
    #             return d4
    #     return EMPTY_WORD
    #
    #
    # # A6 assignment
    # def a6_insertion(a6_banned, d1, d2, four_char_words):
    #     for word in four_char_words:
    #         if word[1] == d1[1] and word[3] == d2[1] and word not in a6_banned:
    #             a6 = word
    #             return a6
    #     return EMPTY_WORD
    #
    #
    # # A9 assignment
    # def a9_insertion(a9_banned, d10, d2, four_char_words):
    #     for word in four_char_words:
    #         if word[1] == d10[0] and word[3] == d2[5] and word not in a9_banned:
    #             a9 = word
    #             return a9
    #     return EMPTY_WORD
    #
    #
    # # A11 assignment
    # def a11_insertion(a11_banned, d11, d5, four_char_words):
    #     for word in four_char_words:
    #         if word[0] == d11[0] and word[1] == d5[5] and word not in a11_banned:
    #             a11 = word
    #             return a11
    #     return EMPTY_WORD
    #
    #
    # # D13 assignment
    # def d13_insertion(d13_banned, a12, four_char_words):
    #     for word in four_char_words:
    #         if word[0] == a12[3] and word not in d13_banned:
    #             d13 = word
    #             return d13
    #     return EMPTY_WORD
    #
    #
    # # D14 assignment
    # def d14_insertion(d14_banned, a12, four_char_words):
    #     for word in four_char_words:
    #         if word[0] == a12[9] and word not in d14_banned:
    #             d14 = word
    #             return d14
    #     return EMPTY_WORD
    #
    #
    # # A16 assignment
    # def a16_insertion(a16_banned, d11, d14, four_char_words):
    #     for word in four_char_words:
    #         if word[0] == d11[4] and word[2] == d14[2] and word not in a16_banned:
    #             a16 = word
    #             return a16
    #     return EMPTY_WORD


user_word_1 = input("Enter a word: ")
user_word_2 = input("Enter another word: ")
user_word_3 = input("Enter a final word: ")

words = user_word_1 + "," + user_word_2 + "," + user_word_3
word2vec(words.split(','))
