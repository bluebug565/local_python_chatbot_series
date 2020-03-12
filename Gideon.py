# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gideon.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from chatterbot import ChatBot
from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 695)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/ChatterBot-master/graphics/ad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.926136, y1:0.04, x2:0.960227, y2:0, stop:1 rgba(0, 0, 0, 225));")
        self.centralwidget.setObjectName("centralwidget")
        self.container_frame = QtWidgets.QFrame(self.centralwidget)
        self.container_frame.setGeometry(QtCore.QRect(0, 0, 811, 661))
        self.container_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_frame.setObjectName("container_frame")
        self.conversition = QtWidgets.QTextBrowser(self.container_frame)
        self.conversition.setGeometry(QtCore.QRect(30, 120, 741, 401))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.conversition.setFont(font)
        self.conversition.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.conversition.setObjectName("conversition")
        self.user_input = QtWidgets.QTextEdit(self.container_frame)
        self.user_input.setGeometry(QtCore.QRect(30, 560, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_input.setFont(font)
        self.user_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(12, 44, 255);\n"
"\n"
"")
        #self.user_input = QtGui.Entry(self, state='normal')
        self.user_input.setObjectName("user_input")
        self.send_frame = QtWidgets.QFrame(self.container_frame)
        self.send_frame.setGeometry(QtCore.QRect(620, 560, 151, 52))
        self.send_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.send_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.send_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.send_frame.setObjectName("send_frame")
        self.get_response = QtWidgets.QPushButton(self.send_frame)
        self.get_response.setGeometry(QtCore.QRect(0, 0, 152, 53))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.get_response.setFont(font)
        self.get_response.setAcceptDrops(True)
        self.get_response.setAutoFillBackground(False)
        self.get_response.setStyleSheet("color: qconicalgradient(cx:0, cy:0, angle:135, stop:0.198864 rgba(3, 0, 255, 255), stop:0.607955 rgba(3, 0, 255, 164), stop:0.704545 rgba(255, 255, 0, 69), stop:0.857955 rgba(255, 218, 71, 130), stop:0.892045 rgba(255, 244, 71, 130), stop:0.920455 rgba(255, 255, 0, 255), stop:0.977273 rgba(255, 203, 0, 130), stop:0.994318 rgba(251, 255, 0, 145), stop:1 rgba(255, 255, 0, 69));")
        self.get_response.setCheckable(True)
        self.get_response.setAutoDefault(False)
        self.get_response.setDefault(True)
        self.get_response.setFlat(True)
        self.get_response.setObjectName("get_response")
        self.g_intro = QtWidgets.QLabel(self.container_frame)
        self.g_intro.setGeometry(QtCore.QRect(30, 20, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.g_intro.setFont(font)
        self.g_intro.setMouseTracking(True)
        self.g_intro.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0.198864 rgba(3, 0, 255, 255), stop:0.607955 rgba(3, 0, 255, 164), stop:0.704545 rgba(255, 255, 0, 69), stop:0.857955 rgba(255, 218, 71, 130), stop:0.892045 rgba(255, 244, 71, 130), stop:0.920455 rgba(255, 255, 0, 255), stop:0.977273 rgba(255, 203, 0, 130), stop:0.994318 rgba(251, 255, 0, 145), stop:1 rgba(255, 255, 0, 69));")
        self.g_intro.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.g_intro.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.g_intro.setWordWrap(False)
        self.g_intro.setOpenExternalLinks(False)
        self.g_intro.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.g_intro.setObjectName("g_intro")
        self.conversitio_title = QtWidgets.QLabel(self.container_frame)
        self.conversitio_title.setGeometry(QtCore.QRect(280, 90, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.conversitio_title.setFont(font)
        self.conversitio_title.setObjectName("conversitio_title")
        self.reply_gideon = QtWidgets.QLabel(self.container_frame)
        self.reply_gideon.setGeometry(QtCore.QRect(310, 530, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reply_gideon.setFont(font)
        self.reply_gideon.setObjectName("reply_gideon")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.container_frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(760, 120, 16, 401))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(170, 170, 127);")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_m = QtWidgets.QAction(MainWindow)
        self.action_m.setObjectName("action_m")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def get_response(self, MainWindow):
        """
        Get a response from the chatbot and display it.
        """
        usr_input = self.user_input.get()
        self.user_input.delete(0, QtGui.End)

        response = self.chatbot.get_response(usr_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            QtGui.End, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gideon v1.0"))
        self.get_response.setText(_translate("MainWindow", "GET RESPONSE"))
        self.g_intro.setText(_translate("MainWindow", "  Welcome friend, my name is Gideon v1.0. I am an A.I chatbot "))
        self.conversitio_title.setText(_translate("MainWindow", "      Conversition"))
        self.reply_gideon.setText(_translate("MainWindow", "Reply Gideon"))
        self.action_m.setText(_translate("MainWindow", " m "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

