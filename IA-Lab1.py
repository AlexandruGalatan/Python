#Biggest 2 different values
def ex1():
    n = int(input("n = "))
    v = []
    for i in range(0, n):
        v.append(int(input()))
    v = sorted(v)

    last = v[len(v) - 1]
    for i in range(len(v) - 2, -1, -1):
        if v[i] != last:
            print(v[i], last)
            return

    print("Impossible")

#Anagrams
def ex2():
    s1 = input()
    s2 = input()

    print(sorted(s1) == sorted(s2))

#Words in s that are formed using all the letters of w and only the letters of w
def ex3():
    s = input()
    w = input()

    for remove in ",.;!?":
        s = s.replace(remove, '')

    def swcmp(word, inside):
        for letter in word:
            if not (letter in inside):
                return False
        return True

    total = 0

    for word in s.split(" "):
        if swcmp(word, w) and swcmp(w, word):
            total += 1
            print(word)

    if total == 0:
        print("None found")

#Different string manipulation operations
def ex4():
    text = input()

    print("Length of text:", len(text))

    notAlNum = []
    for char in text:
        if not char.isalnum() and not (char in notAlNum) and char != "-" and char != " ":
            notAlNum.append(char)

    print("Not alphanumeric:", notAlNum)

    words = []
    for rmv in notAlNum:
        text = text.replace(rmv, '')

    for word in text.split(" "):
        words.append(word.lower())

    mWords = []

    for word in words:
        if word.endswith("ul"):
            mWords.append(word)

    print("Masculine words:", mWords)

    crWords = []
    for word in words:
        if word.find("-") >= 0:
            crWords.append(word)

    print("Contains '-':", crWords)

ex4()
