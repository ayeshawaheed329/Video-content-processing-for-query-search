import os
from mutagen.mp3 import MP3
import speech_recognition as sr
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

def DurationOfMP3(file):
    path = file+".mp3"
    audio = MP3(path)
    return audio.info.length

def FindPointOfTime(filename):
    file = filename
    # print("Data set Translation called")
    # print("filename is ",file)
    command2mp3 = "ffmpeg -i "+file+".mp4 "+file+".mp3 "
    command2wav = "ffmpeg -i "+file+".mp3 "+file+".wav "
    os.system(command2mp3)
    os.system(command2wav)
    Tpath = "T-"+file+".txt"
    file = open(Tpath,"w+")
    voc = open("vocabulary.txt","a+")
    voc2 = open("vocabulary.txt", "r")
    vocab = voc2.readlines()
    voc2.close()
    vocabulary = []
    for x in vocab:
        vocabulary.append(x.strip())
    # print("vocabulary ",vocabulary)
    Sfile = open("Stopword-List.txt", "r")
    SW = Sfile.readlines()
    stopwords = []
    for x in SW:
        stopwords.append(x.strip())

    # print("stop words ", stopwords)
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    # print("lemmatizer ")
    r= sr.Recognizer()
    # print("recognizer ")
    Wpath = filename+".wav"
    # print("wav path ",Wpath)
    audio = sr.AudioFile(Wpath)
    Timesup = DurationOfMP3(filename)
    # print("timesup ",Timesup)
    off = 0
    dur = 10
    temp = ""
    while True:
        with audio as source:
            audio1 = r.record(source, offset=off, duration=dur)
            try:

                val = r.recognize_google(audio1)
                val = val.lower()
                val2= val
                features = []
                features = val.split()
                for i in features:
                    # print("x : {0} ".format(i))
                    lema = lemmatizer.lemmatize(i)
                    stem = stemmer.stem(lema)
                    if stem not in stopwords:
                        if stem not in vocabulary:
                            voc.write(stem)
                            vocabulary.append(stem)
                            voc.write("\n")
                        # print( i, "replacing with ",stem)
                        val= val.replace(i,stem)
                        # print("after replacing ", val)

                    else:
                        # print("stop words ",i)
                        i = " "+i+" "
                        val = val.replace(i," ")
                        # print("after replacing ", val)

                file.write("offset\t")
                file.write(str(off))
                file.write("\n")
                file.write(val)
                file.write("\n")
                print(val2)
                # print("offset {0}".format(off))
                # temp = temp + (str(off))
                # temp = temp + "\n"
                temp = temp + val2 + " "
                # temp = temp + "\n"
                off = off + 10
            except:
                off = off + 10
        if off >  Timesup:
            break

    return temp

# inp=input("Enter Video no")
# print(FindPointOfTime("16"))
# command2mp3 = "ffmpeg -i vid15.mp4 vid15.mp3 "
# command2wav = "ffmpeg -i vid15.mp3 vid15.wav "
# os.system(command2mp3)
# os.system(command2wav)
# file = open("vid15-Translation.txt","a+")
# r= sr.Recognizer()
# audio = sr.AudioFile('vid15.wav')
# duration = DurationOfMP3()
# duration = 20
# off = 60
# dur = 20
# with audio as source:
#      audio1 = r.record(source,offset=off, duration=dur)
#      val = r.recognize_google(audio1)
#      file.write(val)
#      print(val)
