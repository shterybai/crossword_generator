import gensim
from gensim.models import Word2Vec

BANNED_CHARACTERS = "\"!@#$%^&.`*()-+?_=,<>/123456789\'"
EMPTY_WORD = "___________"

model = gensim.models.KeyedVectors.load_word2vec_format('venv/data/GoogleNews-vectors-negative300.bin', binary=True)


def word2vec(user_words: list[str]):
    # print(model.most_similar(positive=words, topn=5000))

    sim_list = model.most_similar(positive=user_words, topn=20000)

    word_list = [i[0] for i in sim_list]

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

    word_initialization(eleven_char_words, ten_char_words, six_char_words, four_char_words)


def word_initialization(eleven_char_words, ten_char_words, six_char_words, four_char_words):
    # Entries initialization
    a6 = a7 = a8 = a9 = a11 = a12 = a15 = a16 = d1 = d2 = d3 = d4 = d5 = d10 = d11 = d13 = d14 = EMPTY_WORD

    # D3 assignment
    d3 = eleven_char_words[0]

    # A8 assignment
    for word in ten_char_words:
        if word[4] == d3[3]:
            a8 = word
            break
    # A12 assignment
    for word in ten_char_words:
        if word[5] == d3[7]:
            a12 = word
            break

    # D2 assignment
    for word in six_char_words:
        if word[3] == a8[2]:
            d2 = word
            break
    # D5 assignment
    for word in six_char_words:
        if word[3] == a8[8]:
            d5 = word
            break
    # D10 assignment
    for word in six_char_words:
        if word[2] == a12[1]:
            d10 = word
            break
    # D11 assignment
    for word in six_char_words:
        if word[2] == a12[7]:
            d11 = word
            break
    # A7 assignment
    for word in six_char_words:
        if word[0] == d3[1] and word[5] == d3[9]:
            a7 = word
            break
    # A15 assignment
    for word in six_char_words:
        if word[1] == d10[4] and word[5] == d3[9]:
            a15 = word
            break

    # D1 assignment
    for word in four_char_words:
        if word[3] == a8[0]:
            d1 = word
            break
    # D4 assignment
    for word in four_char_words:
        if word[1] == a7[2] and word[3] == a8[6]:
            d4 = word
            break
    # A6 assignment
    for word in four_char_words:
        if word[1] == d1[1] and word[3] == d2[1]:
            a6 = word
            break
    # A9 assignment
    for word in four_char_words:
        if word[1] == d10[0] and word[3] == d2[5]:
            a9 = word
            break
    # A11 assignment
    for word in four_char_words:
        if word[0] == d11[0] and word[1] == d5[5]:
            a11 = word
            break
    # D13 assignment
    for word in four_char_words:
        if word[0] == a12[3]:
            d13 = word
            break
    # D14 assignment
    for word in four_char_words:
        if word[0] == a12[9]:
            d14 = word
            break
    # A16 assignment
    for word in four_char_words:
        if word[0] == d11[4] and word[2] == d14[2]:
            a16 = word
            break

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


user_word_1 = input("Enter a word: ")
user_word_2 = input("Enter another word: ")
user_word_3 = input("Enter a final word: ")

words = user_word_1 + "," + user_word_2 + "," + user_word_3
word2vec(words.split(','))
