import gensim
from gensim.models import Word2Vec
# from statemachine import StateMachine, State
import requests
import time

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"

# model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/GoogleNews-vectors-negative300.bin', binary=True)


def word2vec(user_words: list[str]):
    print(time.time() - start_time, "seconds: Retrieving sim_list")
    sim_list = requests.get('http://8b0f-109-255-34-132.ngrok.io/request/?user_words=' + words)

    word_list = [i[0] for i in sim_list.json()]

    print(time.time() - start_time, "seconds: sim_list successfully retrieved")

    dictionaries(word_list)


def dictionaries(word_list):
    # Word list initialization
    eleven_char_words = []
    ten_char_words = []
    six_char_words = []
    four_char_words = []

    # Populate word lists
    print(time.time() - start_time, "seconds: Populating word lists...")
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

    print(time.time() - start_time, "seconds: Done")

    # print("Eleven character words: " + eleven_char_words[0])
    # print("Ten character words: " + ten_char_words[0])
    # print("Six character words: " + six_char_words[0])
    # print("Four character words: " + four_char_words[0])

    print(time.time() - start_time, "seconds: Beginning insertions...")
    insertions(eleven_char_words, ten_char_words, six_char_words, four_char_words)


def insertions(eleven_char_words, ten_char_words, six_char_words, four_char_words):
    # a6 = a7 = a8 = a9 = a11 = a12 = a15 = a16 = d1 = d2 = d3 = d4 = d5 = d10 = d11 = d13 = d14 = EMPTY_WORD

    a6_banned = a7_banned = a8_banned = a9_banned = a11_banned = a12_banned = a15_banned = a16_banned = d1_banned = \
        d2_banned = d3_banned = d4_banned = d5_banned = d10_banned = d11_banned = d13_banned = d14_banned = []

    d3 = d3_insertion(d3_banned, eleven_char_words)
    a8 = a8_insertion(a8_banned, d3, ten_char_words)
    a12 = a12_insertion(a12_banned, d3, ten_char_words)
    d2 = d2_insertion(d2_banned, a8, six_char_words)
    d5 = d5_insertion(d5_banned, a8, six_char_words)
    d10 = d10_insertion(d10_banned, a12, six_char_words)
    d11 = d11_insertion(d11_banned, a12, six_char_words)
    a7 = a7_insertion(a7_banned, d3, six_char_words)
    a15 = a15_insertion(a15_banned, d10, d3, six_char_words)
    d1 = d1_insertion(d1_banned, a8, four_char_words)
    d4 = d4_insertion(d4_banned, a7, a8, four_char_words)
    a6 = a6_insertion(a6_banned, d1, d2, four_char_words)
    a9 = a9_insertion(a9_banned, d10, d2, four_char_words)
    a11 = a11_insertion(a11_banned, d11, d5, four_char_words)
    d13 = d13_insertion(d13_banned, a12, a15, four_char_words)
    d14 = d14_insertion(d14_banned, a12, four_char_words)
    a16 = a16_insertion(a16_banned, d11, d14, four_char_words)

    print("3-down = " + d3)
    print("8-across = " + a8)
    print("12-across = " + a12)
    print("2-down = " + d2)
    print("5-down = " + d5)
    print("10-down = " + d10)
    print("11-down = " + d11)
    print("7-across = " + a7)
    print("15-across = " + a15)
    print("1-down = " + d1)
    print("4-down = " + d4)
    print("6-across = " + a6)
    print("9-across = " + a9)
    print("11-across = " + a11)
    print("13-down = " + d13)
    print("14-down = " + d14)
    print("16-across = " + a16)

    print("Finished. Total execution time: ", time.time() - start_time)


# D3 assignment
def d3_insertion(d3_banned, eleven_char_words):
    print(time.time() - start_time, "seconds: D3 assignment")
    for word in eleven_char_words:
        if word not in d3_banned:
            d3 = word
            return d3
    return EMPTY_WORD


# A8 assignment
def a8_insertion(a8_banned, d3, ten_char_words):
    print(time.time() - start_time, "seconds: A8 assignment")
    for word in ten_char_words:
        if word[4] == d3[3] and word not in a8_banned:
            a8 = word
            return a8
    return EMPTY_WORD


# A12 assignment
def a12_insertion(a12_banned, d3, ten_char_words):
    print(time.time() - start_time, "seconds: A12 assignment")
    for word in ten_char_words:
        if word[5] == d3[7] and word not in a12_banned:
            a12 = word
            return a12
    return EMPTY_WORD


# D2 assignment
def d2_insertion(d2_banned, a8, six_char_words):
    print(time.time() - start_time, "seconds: D2 assignment")
    for word in six_char_words:
        if word[3] == a8[2] and word not in d2_banned:
            d2 = word
            return d2
    return EMPTY_WORD


# D5 assignment
def d5_insertion(d5_banned, a8, six_char_words):
    print(time.time() - start_time, "seconds: D5 assignment")
    for word in six_char_words:
        if word[3] == a8[8] and word not in d5_banned:
            d5 = word
            return d5
    return EMPTY_WORD


# D10 assignment
def d10_insertion(d10_banned, a12, six_char_words):
    print(time.time() - start_time, "seconds: D10 assignment")
    for word in six_char_words:
        if word[2] == a12[1] and word not in d10_banned:
            d10 = word
            return d10
    return EMPTY_WORD


# D11 assignment
def d11_insertion(d11_banned, a12, six_char_words):
    print(time.time() - start_time, "seconds: D11 assignment")
    for word in six_char_words:
        if word[2] == a12[7] and word not in d11_banned:
            d11 = word
            return d11
    return EMPTY_WORD


# A7 assignment
def a7_insertion(a7_banned, d3, six_char_words):
    print(time.time() - start_time, "seconds: A7 assignment")
    for word in six_char_words:
        if word[0] == d3[1] and word[5] == d3[9] and word not in a7_banned:
            a7 = word
            return a7
    return EMPTY_WORD


# A15 assignment
def a15_insertion(a15_banned, d10, d3, six_char_words):
    print(time.time() - start_time, "seconds: A15 assignment")
    for word in six_char_words:
        if word[1] == d10[4] and word[5] == d3[9] and word not in a15_banned:
            a15 = word
            return a15
    return EMPTY_WORD


# D1 assignment
def d1_insertion(d1_banned, a8, four_char_words):
    print(time.time() - start_time, "seconds: D1 assignment")
    for word in four_char_words:
        if word[3] == a8[0] and word not in d1_banned:
            d1 = word
            return d1
    return EMPTY_WORD


# D4 assignment
def d4_insertion(d4_banned, a7, a8, four_char_words):
    print(time.time() - start_time, "seconds: D4 assignment")
    for word in four_char_words:
        if word[1] == a7[2] and word[3] == a8[6] and word not in d4_banned:
            d4 = word
            return d4
    return EMPTY_WORD


# A6 assignment
def a6_insertion(a6_banned, d1, d2, four_char_words):
    print(time.time() - start_time, "seconds: A6 assignment")
    for word in four_char_words:
        if word[1] == d1[1] and word[3] == d2[1] and word not in a6_banned:
            a6 = word
            return a6
    return EMPTY_WORD


# A9 assignment
def a9_insertion(a9_banned, d10, d2, four_char_words):
    print(time.time() - start_time, "seconds: A9 assignment")
    for word in four_char_words:
        if word[1] == d10[0] and word[3] == d2[5] and word not in a9_banned:
            a9 = word
            return a9
    return EMPTY_WORD


# A11 assignment
def a11_insertion(a11_banned, d11, d5, four_char_words):
    print(time.time() - start_time, "seconds: A11 assignment")
    for word in four_char_words:
        if word[0] == d11[0] and word[2] == d5[5] and word not in a11_banned:
            a11 = word
            return a11
    return EMPTY_WORD


# D13 assignment
def d13_insertion(d13_banned, a12, a15, four_char_words):
    print(time.time() - start_time, "seconds: D13 assignment")
    for word in four_char_words:
        if word[0] == a12[3] and word[0] == a15[3] and word not in d13_banned:
            d13 = word
            return d13
    return EMPTY_WORD


# D14 assignment
def d14_insertion(d14_banned, a12, four_char_words):
    print(time.time() - start_time, "seconds: D14 assignment")
    for word in four_char_words:
        if word[0] == a12[9] and word not in d14_banned:
            d14 = word
            return d14
    return EMPTY_WORD


# A16 assignment
def a16_insertion(a16_banned, d11, d14, four_char_words):
    print(time.time() - start_time, "seconds: A16 assignment")
    for word in four_char_words:
        if word[0] == d11[4] and word[2] == d14[2] and word not in a16_banned:
            a16 = word
            return a16
    return EMPTY_WORD


user_word_1 = input("Enter a word: ")
user_word_2 = input("Enter another word: ")
user_word_3 = input("Enter a final word: ")

start_time =  time.time()

words = user_word_1 + "," + user_word_2 + "," + user_word_3
word2vec(words.split(','))
