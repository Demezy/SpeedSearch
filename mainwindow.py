# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(758, 625)
        Mainwindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputpath = QtWidgets.QLineEdit(self.centralwidget)
        self.inputpath.setGeometry(QtCore.QRect(130, 10, 381, 31))
        self.inputpath.setStyleSheet("")
        self.inputpath.setObjectName("inputpath")
        self.path = QtWidgets.QLabel(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.path.setFont(font)
        self.path.setStyleSheet("")
        self.path.setObjectName("path")
        self.outputTV = QtWidgets.QPushButton(self.centralwidget)
        self.outputTV.setGeometry(QtCore.QRect(560, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.outputTV.setFont(font)
        self.outputTV.setStyleSheet("p {\n"
"    font-size: 3em;\n"
"    color: #f00;\n"
"    -webkit-transition: color 1s ease-out;\n"
"    -moz-transition: color 1s ease-out;\n"
"    transition: color 1s ease-out;\n"
"}\n"
"p:hover {\n"
" color: #ff0;   \n"
"}")
        self.outputTV.setObjectName("outputTV")
        self.outputfolder = QtWidgets.QPushButton(self.centralwidget)
        self.outputfolder.setGeometry(QtCore.QRect(560, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.outputfolder.setFont(font)
        self.outputfolder.setStyleSheet("p {\n"
"    font-size: 3em;\n"
"    color: #f00;\n"
"    -webkit-transition: color 1s ease-out;\n"
"    -moz-transition: color 1s ease-out;\n"
"    transition: color 1s ease-out;\n"
"}\n"
"p:hover {\n"
" color: #ff0;   \n"
"}")
        self.outputfolder.setObjectName("outputfolder")
        self.searching = QtWidgets.QLineEdit(self.centralwidget)
        self.searching.setGeometry(QtCore.QRect(130, 70, 381, 31))
        self.searching.setStyleSheet("")
        self.searching.setObjectName("searching")
        self.search = QtWidgets.QLabel(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(50, 60, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.search.setFont(font)
        self.search.setStyleSheet("")
        self.search.setObjectName("search")
        self.outputSQL = QtWidgets.QPushButton(self.centralwidget)
        self.outputSQL.setGeometry(QtCore.QRect(560, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.outputSQL.setFont(font)
        self.outputSQL.setStyleSheet("p {\n"
"    font-size: 3em;\n"
"    color: #f00;\n"
"    -webkit-transition: color 1s ease-out;\n"
"    -moz-transition: color 1s ease-out;\n"
"    transition: color 1s ease-out;\n"
"}\n"
"p:hover {\n"
" color: #ff0;   \n"
"}")
        self.outputSQL.setObjectName("outputSQL")
        self.inputSQL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSQL.setGeometry(QtCore.QRect(130, 130, 381, 31))
        self.inputSQL.setStyleSheet("")
        self.inputSQL.setObjectName("inputSQL")
        self.searchsql = QtWidgets.QLabel(self.centralwidget)
        self.searchsql.setGeometry(QtCore.QRect(10, 100, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.searchsql.setFont(font)
        self.searchsql.setStyleSheet("")
        self.searchsql.setObjectName("searchsql")
        self.outputText = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(70, 218, 551, 341))
        self.outputText.setAutoFillBackground(False)
        self.outputText.setStyleSheet("")
        self.outputText.setObjectName("outputText")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 180, 551, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sorted_name = QtWidgets.QPushButton(self.layoutWidget)
        self.sorted_name.setStyleSheet(" background-image: \n"
"url(kod\\down.png);")
        self.sorted_name.setObjectName("sorted_name")
        self.horizontalLayout.addWidget(self.sorted_name)
        self.created_data = QtWidgets.QPushButton(self.layoutWidget)
        self.created_data.setObjectName("created_data")
        self.horizontalLayout.addWidget(self.created_data)
        self.last_edit_data = QtWidgets.QPushButton(self.layoutWidget)
        self.last_edit_data.setObjectName("last_edit_data")
        self.horizontalLayout.addWidget(self.last_edit_data)
        self.sorted_weight = QtWidgets.QPushButton(self.layoutWidget)
        self.sorted_weight.setObjectName("sorted_weight")
        self.horizontalLayout.addWidget(self.sorted_weight)
        self.sorted_path = QtWidgets.QPushButton(self.layoutWidget)
        self.sorted_path.setObjectName("sorted_path")
        self.horizontalLayout.addWidget(self.sorted_path)
        Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName("menubar")
        Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mainwindow)
        self.statusbar.setObjectName("statusbar")
        Mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "MainWindow"))
        self.path.setText(_translate("Mainwindow", "Путь:"))
        self.outputTV.setText(_translate("Mainwindow", "Записать"))
        self.outputfolder.setText(_translate("Mainwindow", "Выполнить"))
        self.search.setText(_translate("Mainwindow", "Поиск:"))
        self.outputSQL.setText(_translate("Mainwindow", "Выполнить(sql)"))
        self.searchsql.setText(_translate("Mainwindow", "Поиск(sql):"))
        self.sorted_name.setText(_translate("Mainwindow", "Имя"))
        self.created_data.setText(_translate("Mainwindow", "Дата создания"))
        self.last_edit_data.setText(_translate("Mainwindow", "Дата изменения"))
        self.sorted_weight.setText(_translate("Mainwindow", "Размер"))
        self.sorted_path.setText(_translate("Mainwindow", "Путь"))
