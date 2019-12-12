from BaseEditor import SQLWorker as DBase
from Searcher import FileWorker as Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from mainwindow import *
import sys

app = QApplication([])

# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

# The rest of the code is the same as for the "normal" text editor.

text = QPlainTextEdit()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.button_list = {'created_data': 'create_date', 'sorted_weight': 'weight', 'sorted_name': 'name',
                            'last_edit_data': 'last_edit_date', 'sorted_path': 'path'}

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)
        self.condition = True  # сортируем по возратанию или убывнию
        self.ui.outputTV.clicked.connect(self.output)
        self.ui.outputfolder.clicked.connect(self.search)
        self.ui.outputSQL.clicked.connect(self.sql)
        self.ui.sorted_name.clicked.connect(self.sorting_by_smt)
        self.ui.sorted_path.clicked.connect(self.sorting_by_smt)
        self.ui.sorted_weight.clicked.connect(self.sorting_by_smt)
        self.ui.created_data.clicked.connect(self.sorting_by_smt)
        self.ui.last_edit_data.clicked.connect(self.sorting_by_smt)

    def output(self):
        path = self.ui.inputpath.text()
        try:
            self.file = Files(path)
            self.database = DBase()
            self.database.fill_the_table(self.file.list_of_files)
            self.ui.outputText.setText(self.pretty_output(self.database.sort_and_search("")))
        except FileNotFoundError:
            self.ui.outputText.setText('Такого пути не существует')

    def sorting_by_smt(self):
        self.condition = not (self.condition)
        self.arrow_clear()
        name = self.ui.searching.text()
        if self.condition:
            self.sender().setIcon(QtGui.QIcon("down1.ico"))
            data1 = self.pretty_output(
                self.database.sort_and_search(name,
                                              order_by=self.button_list[self.sender().objectName()],
                                              direction='DESC'))
        else:
            self.sender().setIcon(QtGui.QIcon("upper1.ico"))
            data1 = self.pretty_output(
                self.database.sort_and_search(name,
                                              order_by=self.button_list[self.sender().objectName()],
                                              direction='ASC'
                                              ))
        self.ui.outputText.setText(data1)

    def arrow_clear(self):
        self.ui.created_data.setIcon(QIcon())
        self.ui.sorted_weight.setIcon(QIcon())
        self.ui.sorted_name.setIcon(QIcon())
        self.ui.last_edit_data.setIcon(QIcon())
        self.ui.sorted_path.setIcon(QIcon())

    def search(self):
        self.arrow_clear()
        # print(self.ui.searching.text())
        self.ui.outputText.setText(self.pretty_output(
            self.database.sort_and_search(self.ui.searching.text())))

    def sql(self):
        self.ui.outputText.setText(self.pretty_output(
            self.database.search_by_sql_request(self.ui.inputSQL.text)))

    def pretty_output(self, data):
        answ = ''
        for i in data:
            answ += str(i[0]).ljust(7) + str(i[1]).ljust(17) + ' '.join(str(j).ljust(15) for j in i[2:]) + '\n'
            # answ += str(i[0]).ljust(5, '\t') + str(i[1]).ljust(7, '\t') + ' '.join(str(j).ljust(5, '\t') for j in i[2:]) + '\n'
        return answ


if __name__ == '__main__':
    window = MyWin()
    window.show()
    sys.exit(app.exec_())
