from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import re

def Search(videoName, list):
    Sfile = open("Stopword-List.txt", "r")
    SW = Sfile.readlines()
    stopwords = []
    for x in SW:
        stopwords.append(x.strip())

    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    searchlist = []
    for word in list:
        lema = lemmatizer.lemmatize(word)
        stem = stemmer.stem(lema)
        if stem not in stopwords:
            searchlist.append(stem)


    name = videoName.split(".")[0]
    path = "Translation/T-" + name + ".txt"
    file = open(path, "r")
    file = file.readlines()
    sampleSearch = []
    for line in file:
        data = line.split()
        for x in data:
            sampleSearch.append(x)

    print(sampleSearch)
    offset = []
    lastoff = 0
    first = searchlist[0]
    for i in range(0, len(sampleSearch)):
        word = sampleSearch[i]
        if word == "offset":
            j = i + 1
            lastoff = sampleSearch[j]

        elif word == first:
            print("First word match ", word)
            j = i + 1
            checker = True
            # for k in range(1,len(searchlist)):
            k = 1
            while checker == True:
                if k >= len(searchlist):
                    break
                search = searchlist[k]
                word = sampleSearch[j]
                print("new word ", word, " searching word", search)
                if word == "offset":
                    print(" word == offset")
                    j = j + 2

                elif word == search:
                    print(" word == search")
                    j = j + 1
                    k = k + 1
                else:
                    print("checker false")
                    checker = False
                # print("k = ", k)

            if checker == True:
                offset.append(lastoff)

    print(offset)
    return offset
    # [2654, 2901, 3163]
    # with offset [2957, 3228, 3526]

