import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import getwords
import random

button_Font = QFont("Century Gothic",20)
word_Font = QFont("Times",25)
text_Font = QFont("Times",10)

class main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.left = 500
        self.top = 300
        self.width = 700
        self.height = 330

        self.title = "Hangman Game V1"

        self.setAutoFillBackground(True)
        self.colorpalette = self.palette()


        getwords.gettingwords()

        self.mistakes = 0
        self.words_sofar = []

        self.interface()
        self.askWord()
        self.show()

    def interface(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle(self.title)

        # MENU

        menubar = self.menuBar()
        game = menubar.addMenu("Game")
        view = menubar.addMenu("View")
        help = menubar.addMenu("Help")

        newGame = QAction("New Came",self)
        newGame.setShortcut("Ctrl+N")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        game.addAction(newGame)
        game.addAction(exit)

        change_bg = QAction("Background",self)

        view.addAction(change_bg)

        about = QAction("About Me",self)
        helpme = QAction("Help",self)

        help.addAction(about)
        help.addAction(helpme)

        exit.triggered.connect(self.quit)
        newGame.triggered.connect(self.newGame)
        about.triggered.connect(self.aboutMe)
        helpme.triggered.connect(self.howtoplay)
        change_bg.triggered.connect(self.Change_bg)

        # Hangman

        self.gallow = QLabel(self)
        self.gallow.setPixmap(QPixmap("mistake0.jpg"))
        self.gallow.resize(200,200)

        self.gallow.move(470,75)


        self.meaning = QLabel("Meaning Of the word: ",self)
        self.meaning.move(30,10)
        self.meaning.resize(400,200)
        self.meaning.setWordWrap(True)
        self.meaning.setFont(text_Font)

        self.word = QLabel("The word",self)
        self.word.move(30,150)
        self.word.resize(300,50)
        self.word.setFont(word_Font)

        self.guess = QLineEdit(self)
        self.guess.setPlaceholderText("Your guess")
        self.guess.resize(100,30)
        self.guess.move(30,235)

        self.answer_button = QPushButton("Try",self)
        self.answer_button.move(30,270)
        self.answer_button.resize(100,50)
        self.answer_button.setFont(button_Font)

        self.answer_button.clicked.connect(self.answer)

        self.sofar = QLabel("So far: ",self)
        self.sofar.move(470,280)
        self.sofar.resize(160,30)
        self.sofar.setFont(text_Font)


    def quit(self):
        sure = QMessageBox.question(self,"See you soon","Are you sure ?",QMessageBox.Yes | QMessageBox.No)
        if sure == QMessageBox.Yes:
            qApp.quit()

    def askWord(self):

        getwords.cursor.execute("SELECT COUNT(id) FROM words")
        word_number = getwords.cursor.fetchall()
        getwords.con.commit()
        word_id = random.randint(1,word_number[0][0]+1)
        getwords.cursor.execute("SELECT * FROM words WHERE id=?",(word_id,))
        the_word_data = getwords.cursor.fetchall()
        getwords.con.commit()

        try:
            self.the_word = the_word_data[0][1]
            self.the_meaning = the_word_data[0][2]
        except IndexError:
            self.askWord()

        print(self.the_word)
        print(self.the_meaning)

        self.meaning.setText("Definition: " + self.the_meaning)

        self.question =""
        for i in self.the_word:
            self.question = self.question + " _"

        self.word.setText(self.question)

    def answer(self):

        wrong_input = "0123456789-_*=()[]/{}?'\+^#!."
        if len(self.guess.text())==1 and self.guess.text() not in wrong_input:
            l_guess = self.guess.text()
            l_guess = l_guess.lower()
            if l_guess not in self.words_sofar:
                if l_guess in self.the_word:
                    self.newquestion = ""
                    self.question = list(self.question)

                    for i in range(0,len(self.the_word)):
                        if self.the_word[i] == l_guess:
                            self.question[i*2+1] = l_guess
                            print(self.question)
                            print(self.newquestion)
                    for j in self.question:
                        self.newquestion +=j
                    self.word.setText(self.newquestion)
                    self.guess.clear()

                    if "_" not in self.newquestion:
                        again = QMessageBox.question(self,"Congratulations","You Won ! Would you like to play again ?",QMessageBox.Yes | QMessageBox.No)
                        if again == QMessageBox.Yes:
                            self.askWord()

                else:
                    self.words_sofar.append(self.guess.text())
                    self.sofar.setText(self.sofar.text() + self.guess.text() + ", ")
                    self.mistakes += 1
                    if self.mistakes ==1:
                        self.gallow.setPixmap(QPixmap("mistake1.jpg"))
                    elif self.mistakes ==2:
                        self.gallow.setPixmap(QPixmap("mistake2.jpg"))
                    elif self.mistakes ==3:
                        self.gallow.setPixmap(QPixmap("mistake3.jpg"))
                    elif self.mistakes ==4:
                        self.gallow.setPixmap(QPixmap("mistake4.jpg"))
                    elif self.mistakes ==5:
                        self.gallow.setPixmap(QPixmap("mistake5.jpg"))
                    elif self.mistakes ==6:
                        self.gallow.setPixmap(QPixmap("mistake6.jpg"))

                    self.guess.clear()

                    if self.mistakes == 6:
                        again = QMessageBox.question(self,"Game Over","Game Over ! Would you like to play again ?",QMessageBox.Yes | QMessageBox.No)
                        if again == QMessageBox.Yes:
                            self.askWord()

            else:
                QMessageBox.question(self,"Repetation","You have already tried this letter",QMessageBox.Ok)

        else:
            QMessageBox.question(self,"Wrong Input","Your input is not in the correct form",QMessageBox.Ok)

    def newGame(self):
        self.askWord()

    def aboutMe(self):
        self.whoami = AboutMe()
        self.whoami.show()

    def howtoplay(self):
        self.help = Help()
        self.help.show()

    def Change_bg(self):
        color = QColorDialog.getColor()
        self.colorpalette.setColor(self.backgroundRole(),color)
        self.setPalette(self.colorpalette)



class AboutMe(QWidget):
    def __init__(self):
        super().__init__()

        horizontal_layout = QHBoxLayout()
        self.description = QLabel("I am a computer engineering student who has written this program to improve himself in python")
        self.description.setWordWrap(True)
        self.description.setFont(text_Font)

        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.description)
        horizontal_layout.addStretch()
        self.setLayout(horizontal_layout)
        self.setGeometry(600,400,400,100)
        self.setWindowTitle("About Me")

class Help(QWidget):
    def __init__(self):
        super().__init__()

        horizontal_layout = QHBoxLayout()
        self.howtoplay = QLabel("To find the word, use the definition and enter your guess (as a letter) into textbox")
        self.howtoplay.setWordWrap(True)
        self.howtoplay.setFont(text_Font)

        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.howtoplay)
        horizontal_layout.addStretch()
        self.setLayout(horizontal_layout)
        self.setGeometry(600,400,400,100)
        self.setWindowTitle("Help")

application = QApplication(sys.argv)
main_window = main()
sys.exit(application.exec_())
