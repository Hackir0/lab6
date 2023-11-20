import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dbio import DB

import os

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.result = QtWidgets.QLabel(self)
        self.result.setGeometry(250, 50, 200, 200)

        self.index = 0
        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(150, 100, 300, 25)
        self.title.setText("Викторина на знания Python")
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.title.setFont(self.font)
        self.title.setStyleSheet("color:black")

        self.setWindowTitle("Викторина")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color:rgb(90,169,95)")

        self.startbutton = QtWidgets.QPushButton(self)
        self.startbutton.setGeometry(170, 280, 280, 20)
        self.startbutton.setFont(self.font)
        self.startbutton.setText("Ну что,погнали?")
        self.startbutton.setStyleSheet("background-color:rgb(90,169,89)")
        self.startbutton.clicked.connect(self.start_button)

        db = DB()
        self.questions = db.load_data()

        self.correct = 0
        self.number = len(self.questions)

        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: rgb(78,87,101")

        self.font = QtGui.QFont()
        self.font.setPointSize(18)
        self.question_text = QtWidgets.QLabel(self)
        self.question_text.setGeometry(190, 50, 200, 200)
        self.question_text.setStyleSheet("color: black")
        self.question_text.setWordWrap(True)
        self.question_text.hide()

        self.line = QtWidgets.QLineEdit(self)
        self.line.setFocus()

        self.line.setGeometry(225, 200, 150, 35)
        self.line.setStyleSheet("background-color:white")
        self.font.setPointSize(12)
        self.line.setFont(self.font)
        self.line.hide()

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(260, 280, 80, 20)
        self.font.setPointSize(9)
        self.pushButton.setFont(self.font)
        self.pushButton.setText("Следующий")
        self.pushButton.setStyleSheet("background-color:green")
        self.pushButton.clicked.connect(self.show_questions)

        self.pushButton.hide()

    def show_questions(self):

        if self.index < len(self.questions):
            self.questions[self.index]['answer'] = self.line.text().lower()
            print(self.questions[self.index]['correct_answer'], self.line.text().lower())

            if self.questions[self.index]['correct_answer'] == self.line.text().lower():
                self.correct += 1
            self.line.clear()

            self.index += 1

            if self.index < len(self.questions):
                self.question_text.setText(self.questions[self.index]['question'])
            else:
                self.line.hide()
                self.pushButton.hide()
                self.question_text.hide()
                print(self.correct, self.number)
                self.result.setText(f"Ваш результат: {(self.correct / self.number) * 100} %")
                self.result.setWordWrap(True)

    def start_button(self):
        self.startbutton.hide()
        self.question_text.show()
        self.line.show()
        self.pushButton.show()
        self.question_text.setText(self.questions[0]['question'])
        self.title.hide()
