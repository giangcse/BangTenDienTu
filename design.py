# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 736)
        MainWindow.setStyleSheet("background-image: url(bangten.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setStatusTip("")
        self.logo.setStyleSheet("background: transparent;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setLineWidth(0)
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setPixmap(QtGui.QPixmap(""))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.dong_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dong_1.sizePolicy().hasHeightForWidth())
        self.dong_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(50)
        self.dong_1.setFont(font)
        self.dong_1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dong_1.setStyleSheet("background: transparent;\n"
"color: rgb(255, 0, 0);")
        self.dong_1.setScaledContents(False)
        self.dong_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.dong_1.setWordWrap(False)
        self.dong_1.setObjectName("dong_1")
        self.verticalLayout.addWidget(self.dong_1)
        self.dong_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.dong_2.setFont(font)
        self.dong_2.setStyleSheet("background: transparent;\n"
"color: rgb(255, 0, 0);")
        self.dong_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dong_2.setObjectName("dong_2")
        self.verticalLayout.addWidget(self.dong_2)
        self.dong_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.dong_3.setFont(font)
        self.dong_3.setStyleSheet("background: transparent;\n"
"color: rgb(255, 0, 0);")
        self.dong_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.dong_3.setObjectName("dong_3")
        self.verticalLayout.addWidget(self.dong_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BangTenDienTu"))
        MainWindow.setWindowFlags(MainWindow.windowFlags() | Qt.FramelessWindowHint)
        # Phóng to cửa sổ
        MainWindow.showFullScreen()
        
# Run PyQt5 UI
# if __name__=='__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
