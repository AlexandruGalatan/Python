# List comprehension
def ex1():
    # 1. Odd numbers from 0 to 10
    nr = [i for i in range(11) if i % 2 == 1]
    print("1", nr)

    # 2. a -> z
    lwr = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    print("2", lwr)

    # 3. 1, -2, 3, -4, ...
    n = 7  # int(input())
    l = [(-1) ** (i + 1) * i for i in range(1, n + 1)]
    print("3", l)

    # 4. Find odd numbers
    lst = [1, 2, 3, 4, 5, 6]
    oddNr = [i for i in lst if i % 2 == 1]
    print("4", oddNr)

    # 5. Find numbers on odd positions
    lst = [1, 2, 3, 4, 5, 6]
    oddNr = [lst[i] for i in range(len(lst)) if i % 2 == 1]
    print("5", oddNr)

    # 6. Numbers that have the same parity as their ind
    lst = [2, 4, 1, 7, 5, 1, 8, 10]
    prt = [lst[i] for i in range(len(lst)) if i % 2 == lst[i] % 2]
    print("6", prt)

    # 7. Tuples of adjacent numbers
    lst = [1, 2, 3, 4]
    tpl = [(lst[i - 1], lst[i]) for i in range(1, len(lst))]
    print("7", tpl)

    # 8. List of n lists, multiplication table
    n = 3
    m = [[str(i + 1) + "*" + str(j + 1) + "=" + str((i + 1) * (j + 1)) for j in range(n)] for i in range(n)]
    print("8", m)

    # 9. abc - > bca -> cab
    word = "abcde"
    res = [word[i:] + word[:i] for i in range(len(word))]
    print("9", res)

    # 10. [[], [1], [2, 2], [3, 3, 3], ...]
    n = 4
    m = [[i] * i for i in range(n)]
    print("10", m)


# Sorting
def ex2():
    # a) sort using lambda as string
    nr = [745, 236, 856, 333, 1009]
    nr = sorted(nr, key=lambda x: str(x))
    print("a", nr)

    # b) sort using lambda as reversed string
    nr = [745, 236, 856, 333, 1009]
    nr = sorted(nr, key=lambda x: str(x)[::-1])
    print("b", nr)

    # c) sort using lambda as reversed string
    nr = [745, 236, 856, 333, 1009]
    nr = sorted(nr, key=lambda x: len(str(x)))
    print("c", nr)

    # d) sort using lambda by nr of different characters
    nr = [745, 236, 855, 333, 1009]
    nr = sorted(nr, key=lambda x: len(set(str(x))))
    print("d", nr)


# Set of (x, y) where x has been found at least n times right before y
def ex3():
    n = 2
    cuvinte = ["papagal", "pisica", "soarece", "bolovan", "soparla", "catel", "pasare"]

    def gen_matrice():
        m = [[0]]
        for i in range(ord("a"), ord("z") + 1):
            m[0].append(chr(i))
        for i in range(ord("a"), ord("z") + 1):
            new = [chr(i)]
            new.extend([0] * (ord("z") - ord("a") + 1))
            m.append(new)
        return m

    def completeaza_matrice(cuv, mtr):
        for cuvant in cuv:
            for i in range(1, len(cuvant)):
                x = ord(cuvant[i - 1]) - ord("a") + 1
                y = ord(cuvant[i]) - ord("a") + 1
                mtr[x][y] += 1
        print(mtr)
        return mtr

    m = completeaza_matrice(cuvinte, gen_matrice())
    i = 1
    while i < len(m):
        rmv = True
        for j in range(1, len(m[i])):
            if m[i][j] != 0:
                rmv = False
        if rmv:
            del m[i]
            i -= 1
            print(i)
        i += 1
    print("-------------")

    print(m)

    prs = set()
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            if m[i][j] >= n:
                prs.add((m[i][0], m[0][j]))

    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            m[i][j] = str(m[i][j])
    print(*m, sep = '\n')
    print(prs)

#Count how many times a word is found in l (not case sensitive)
def ex4():
    l = ["haha", "poc", "Poc", "POC", "haHA", "hei", "hey", "HahA", "poc", "Hei"]
    d = dict()
    for cuv in l:
        key = cuv.lower();

        if not (key in d):
            d[key] = 0
        d[key] += 1
    print(d)


#For each character, find all entries that contain it and include it in a category
def ex5():
    l =  ["bau-bau", "bobocel", "14 pisici", "1pitic", "pisicel", "botosel", "414", "ham", "-hau", "bob", "bocceluta"]
    d = dict()
    ap = dict()

    #a
    for x in ((1,4),"mic"), ((4,8), "mediu"), ((8,15),"mare"):
        d[x[0]] = x[1]

    #b
    for cuv in l:
        for c in cuv:
            if not (c in ap):
                ap[c] = []
                for cuvant in l:
                    if c in cuvant:
                        ap[c].append(cuvant)

    print(ap)

    #c
    for c, val in ap.items():
        for wrd in val:
            if not (wrd.isalnum()): #or '-' in wrd:
                val.remove(wrd)
                print("Sters", c, wrd)

    print(ap)

    #d
    print(len(ap))

    #e
    for c, val in ap.items():
        l = len(val)
        for interv in d:
            if l >= interv[0] and l < interv[1]:
                print(c, d[interv])
                break

    print(d)

#List comprehension
def ex6():
    #a
    '''
    0 1 2
    1 2 3
    2 3 4
    '''
    n = 4
    m = [[i + j for j in range(n)] for i in range(n)]
    print("a", *m, sep = '\n')

    #b
    #clone of all lines with sum > n
    n = 5
    m = [[1, 2, 3],
         [10, 2, 9],
         [1, 1, 1]]

    rez = [[m[i][j] for j in range(len(m[i]))] for i in range(len(m)) if sum(m[i]) > n]

    print("b", *rez, sep = '\n')

    #c
    #matrix that compares all elements of 2 lists
    l1 = [i for i in range(4)]
    l2 = [i for i in range(2)]

    def getit(i, j):
        if l1[i] < l2[j]:
            return "<"
        elif l1[i] > l2[j]:
            return ">"
        return "=="

    rez = [[getit(i, j) for j in range(len(l2))] for i in range(len(l1))]

    print("c", *rez, sep = '\n')

ex6()