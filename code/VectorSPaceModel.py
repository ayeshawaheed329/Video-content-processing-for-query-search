import math
import os
class BooleanModel:

    def __init__(self):
        self.features = []
        DIR = 'F:/pycharmProjects/HCI-Project/Mp4Files/'
        self.NoFiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        # self.NoFiles = self.NoFiles + 1
        self.arr = os.listdir("F:/pycharmProjects/HCI-Project/Translation/")
        voc = open("vocabulary.txt", "r")
        vocab = voc.readlines()
        for x in vocab:
            self.features.append(x.strip())

        # for i in range(0, self.NoFiles):
       #     j = self.arr[i]
        #     path = "Translation/"+j
        #     file = open(path, "r")
        #     data = file.readlines()
        #     for x in data:
        #         l = x.split()
        #         if l[0] != "offset":
        #             for z in l:
        #                 self.features.append(z)

    def CreatingIndexes(self):
        # noOfFiles = self.NoFiles - 1
        print("index creation")
        model = open("VectorSpaceModel.txt", "w+")
        for x in self.features:
            print(x)
            idf = 0
            model.write(x)
            model.write("\t")
            tf = []
            for i in range(0, self.NoFiles):
                j = self.arr[i]
                path = "Translation/" + j
                file = open(path, "r")
                data = file.read()
                tf.append(data.count(x))

            df = self.NoFiles - tf.count(0)
            if(df==0):
                df = 1
            # print("x = {0} docFrq = {1}".format(x, df))
            idf = math.log10((self.NoFiles / df))
            for j in tf:
                f = j * idf
                model.write(str(f)[:7])
                model.write("\t")

            model.write(str(idf))
            model.write("\n")


# obj = BooleanModel()
# obj.CreatingIndexes()


