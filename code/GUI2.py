# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject, QThread, QThreadPool
from Playvideobypyglet import playVideos
from multiprocessing import Process
from SearchInVideo import Search
import os

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.fn = fn

    @pyqtSlot()
    def run(self):
        self.fn()


class Ui_SubWindow(object):

    def __init__(self, doclist):
        self.doclist = doclist
        print("constructor called")
        self.arr = os.listdir("F:/pycharmProjects/HCI-Project/Mp4Files/")
        print("arr ",self.arr)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(96, 129, 240, 255), stop:0.55 rgba(61, 225, 235, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                                 "color:white;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(240, 40, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setStyleSheet("background:transparent;")
        self.ResultLabel.setObjectName("ResultLabel")
        self.Resultbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.Resultbox.setGeometry(QtCore.QRect(240, 90, 540, 151))
        self.Resultbox.setStyleSheet("background:transparent;\n"
                                     "font-weight:bold;\n"
                                       "font-size:18px;\n"
                                     "border:1px solid white;")
        self.Resultbox.setObjectName("Resultbox")
        self.PlayBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PlayBtn.setGeometry(QtCore.QRect(520, 340, 261, 41))
        # self.PlayBtn.setGeometry(QtCore.QRect(240, 330, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PlayBtn.setFont(font)
        self.PlayBtn.setObjectName("PlayBtn")
        self.PlayBtn.clicked.connect(lambda: self.PlayBtnFunction())
        # self.NextBtn = QtWidgets.QPushButton(self.centralwidget)
        # self.NextBtn.setGeometry(QtCore.QRect(519, 330, 261, 41))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(75)
        # self.NextBtn.setFont(font)
        # self.NextBtn.setObjectName("NextBtn")
        # self.NextBtn.clicked.connect(lambda: self.NextBtnFunction())
        self.SearcLabel = QtWidgets.QLabel(self.centralwidget)
        self.SearcLabel.setGeometry(QtCore.QRect(240, 420, 420, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SearcLabel.setFont(font)
        self.SearcLabel.setStyleSheet("background:transparent;")
        self.SearcLabel.setObjectName("SearcLabel")
        self.VideoNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoNoLabel.setGeometry(QtCore.QRect(240, 475, 271, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VideoNoLabel.setFont(font)
        self.VideoNoLabel.setStyleSheet("background:transparent;")
        self.VideoNoLabel.setObjectName("VideoNoLabel")
        self.VideoNoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VideoNoInput.setGeometry(QtCore.QRect(520, 475, 261, 45))
        self.VideoNoInput.setStyleSheet("background:transparent;\n"
                                       "font-size:18px;\n"
                                        "border:1px solid white;")
        self.VideoNoInput.setObjectName("VideoNoInput")
        self.WordLabel = QtWidgets.QLabel(self.centralwidget)
        self.WordLabel.setGeometry(QtCore.QRect(240, 530, 271, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WordLabel.setFont(font)
        self.WordLabel.setStyleSheet("background:transparent;\n"
                                     "\n"
                                     "")
        self.WordLabel.setObjectName("WordLabel")
        self.WordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.WordInput.setGeometry(QtCore.QRect(520, 530, 261, 45))
        self.WordInput.setStyleSheet("background:transparent;\n"
                                       "font-size:18px;\n"
                                     "border:1px solid white;")
        self.WordInput.setObjectName("WordInput")
        self.SearchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SearchBtn.setGeometry(QtCore.QRect(520, 600, 261, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SearchBtn.setFont(font)
        self.SearchBtn.setObjectName("SearchBtn")
        self.SearchBtn.clicked.connect(lambda: self.SearchBtnFunction())
        self.backLink = QtWidgets.QPushButton(self.centralwidget)
        self.backLink.setGeometry(QtCore.QRect(462, 660, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.backLink.setFont(font)
        self.backLink.setStyleSheet("background:transparent;\n"
                                    "border:none;\n"
                                    "text-decoration:underline;")
        self.backLink.setObjectName("backLink")
        self.backLink.clicked.connect(
            lambda: self.backButtonFunction(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.PlayBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PlayBtn_2.setGeometry(QtCore.QRect(520, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PlayBtn_2.setFont(font)
        self.PlayBtn_2.setObjectName("PlayBtn_2")
        self.PlayBtn_2.clicked.connect(
            lambda: self.PlayOneBtnFunction())
        self.vidToPlay = QtWidgets.QLineEdit(self.centralwidget)
        self.vidToPlay.setGeometry(QtCore.QRect(240, 280, 261, 41))
        self.vidToPlay.setStyleSheet("background:transparent;\n"
                                      "font-size:18px;\n"
                                     "border:1px solid white;")
        self.vidToPlay.setObjectName("vidToPlay")
        self.vidPlayLabel = QtWidgets.QLabel(self.centralwidget)
        self.vidPlayLabel.setGeometry(QtCore.QRect(240, 240, 271, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vidPlayLabel.setFont(font)
        self.vidPlayLabel.setStyleSheet("background:transparent;")
        self.vidPlayLabel.setObjectName("vidPlayLabel")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.displayResult()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ResultLabel.setText(_translate("MainWindow", "Result (Videos )"))
        self.PlayBtn.setText(_translate("MainWindow", "Play All"))
        # self.NextBtn.setText(_translate("MainWindow", "Next"))
        self.SearcLabel.setText(_translate("MainWindow", "Search In Video ?"))
        self.VideoNoLabel.setText(_translate("MainWindow", "Type Video Name :"))
        self.WordLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p>What To Search :</p></body></html>"))
        self.SearchBtn.setText(_translate("MainWindow", "Search"))
        self.backLink.setText(_translate("MainWindow", "Go Back"))
        self.PlayBtn_2.setText(_translate("MainWindow", "Play"))
        self.vidPlayLabel.setText(_translate("MainWindow", "Enter Video Name To Play"))

    def displayResult(self):
        print("New GUI Window")
        print("Results Displayed ")
        if len(self.doclist) == 0:
            print("No Result Found !!!!")
        for x in self.doclist:
            self.Resultbox.append(x)

    def PlayBtnFunction(self):
        print("play Btn")
        self.playVideoInThread(False)

    def PlayOneBtnFunction(self):
        fileno = str(self.vidToPlay.text())
        if fileno:
            name = fileno.split(".")[0]
            name = name + ".mp4"
            if name not in self.arr:
                print("NOT in corpus")
                from dialogueBox import Ui_MainWindow
                global msgWindow9
                msgWindow9 = QtWidgets.QMainWindow()
                lui = Ui_MainWindow("Oops ! Video Not Found")
                lui.setupUi(msgWindow9)
                msgWindow9.show()
            else:
                self.playVideoInThread(True)
        else:
            from dialogueBox import Ui_MainWindow
            global msgWindow
            msgWindow = QtWidgets.QMainWindow()
            lui = Ui_MainWindow("Enter Video Name To Play!!!")
            lui.setupUi(msgWindow)
            msgWindow.show()

    def playVideoInThread(self,one):

        if(one==False):
            process = Process(target=playVideos,
                          args=(self.doclist, False, 0,False,0))
        else:
            fileno = str(self.vidToPlay.text())
            filename = fileno.split(".")[0]
            filename = filename + ".mp4"
            process = Process(target=playVideos,
                          args=(self.doclist, False, 0, True, filename))


        process.start()

    def searchinvid(self):

        filename = str(self.VideoNoInput.text())
        word = str(self.WordInput.text())
        name = filename.split(".")[0]
        name = name + ".mp4"
        print("filename ",name)
        if name not in self.arr and filename != "":
            print("IF true")
            from dialogueBox import Ui_MainWindow
            global msgWindow5
            msgWindow5 = QtWidgets.QMainWindow()
            lui = Ui_MainWindow("Oops ! Video Not Found")
            lui.setupUi(msgWindow5)
            msgWindow5.show()
        elif filename != "" and word !="":
            searchlist = word.split(" ")
            result = Search(filename, searchlist)
            self.VideoNoInput.setText("")
            self.WordInput.setText("")
            if len(result) == 0:
                from dialogueBox import Ui_MainWindow
                global msgWindow2
                msgWindow2 = QtWidgets.QMainWindow()
                lui = Ui_MainWindow("No Result Found ! ")
                lui.setupUi(msgWindow2)
                msgWindow2.show()
            else:
                from GUIPlayvid import Ui_MainWindow
                filename = filename.split(".")[0]
                filename = filename + ".mp4"
                global subWindow
                subWindow = QtWidgets.QMainWindow()
                lui = Ui_MainWindow(result, filename)
                lui.setupUi(subWindow)
                subWindow.show()
        else:
            msg = ""
            if filename == "" and word == "":
                msg = "Enter Video Name And Word You Want To Search "
            elif filename=="":
                msg = "Enter Video Name In Which You Want To Search "
            else:
                msg = "Enter Word You Want To Search  "

            from dialogueBox import Ui_MainWindow
            global msgWindow
            msgWindow = QtWidgets.QMainWindow()
            lui = Ui_MainWindow(msg)
            lui.setupUi(msgWindow)
            msgWindow.show()


    def SearchBtnFunction(self):
        self.searchinvid()


    def backButtonFunction(self, mainWindow):
        from GUI1 import Ui_MainWindow
        global subWindow
        subWindow = QtWidgets.QMainWindow()
        lui = Ui_MainWindow()
        lui.setupUi(subWindow)
        mainWindow.close()
        subWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SubWindow([1])
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
