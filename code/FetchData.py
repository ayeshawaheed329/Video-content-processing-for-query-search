from Playvideobypyglet import playVideos
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
# import speech_recognition as sr
import numpy as np
import operator
import math
import os
search = ""



def FetchingRecords(par):
    DIR = 'F:/pycharmProjects/HCI-Project/Mp4Files/'
    NoFiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    NoFiles = NoFiles + 1
    print("Fetching Related Ranked Videos ..............")
    search = par
    Sfile = open("Stopword-List.txt", "r")
    SW = Sfile.readlines()
    stopwords = []
    question = ["what","when","how","where","define","explain","why"]
    for x in SW:
        stopwords.append(x.strip())

    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    searchlist = []
    for x in search.split():
        lema = lemmatizer.lemmatize(x)
        stem = stemmer.stem(lema)
        if stem not in stopwords:
            if stem not in question:
                stem = stem.lower()
                searchlist.append(stem)

    print("final search list ",searchlist)
    file = open("VectorSpaceModel.txt", "r")
    VSM = file.readlines()
    QueryVector = []
    DocVector = []
    for i in range(0, NoFiles):
        DocVector.append([])

    for line in VSM:
        data = line.split()
        tf = searchlist.count(data[0])
        QueryVector.append(str(tf * float(data[NoFiles])))
        for i in range(1, NoFiles):
            DocVector[i].append(data[i])

    FinalResults = {}
    QueryVector = [float(j) for j in QueryVector]
    QueryVector = np.array(QueryVector)
    print("query vector ", QueryVector)
    norma = np.linalg.norm(QueryVector)
    for i in range(1, NoFiles):
        b = [float(j) for j in DocVector[i]]
        b = np.array(b)
        normb = np.linalg.norm(b)
        dot = np.dot(QueryVector, b)
        cos = dot / (norma * normb)
        if cos > 0.09:
            # print("{0} cosine = {1}".format(i, cos))
            FinalResults[i] = cos

    sorted_d = dict(sorted(FinalResults.items(), key=operator.itemgetter(1), reverse=True))
    ret = []
    arr = os.listdir("F:/pycharmProjects/HCI-Project/Translation/")
    for key in FinalResults:
        i= key-1
        name = arr[i]
        name =  name.split("-",1)[1]
        name = name.split(".")[0] + ".mp4"
        ret.append(name)
    return ret

