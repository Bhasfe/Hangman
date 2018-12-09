import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

button_Font = QFont("Century Gothic",20)
word_Font = QFont("Times",25)
text_Font = QFont("Times",12)

class main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.left = 500
        self.top = 300
        self.width = 700
        self.height = 330

        self.title = "Hangman Game V1"

        self.interface()
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
        change_font = QAction("Font",self)

        view.addAction(change_bg)
        view.addAction(change_font)

        about = QAction("About Me",self)
        helpme = QAction("Help",self)

        help.addAction(about)
        help.addAction(helpme)

        exit.triggered.connect(self.quit)


        # Hangman

        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.gallow = QLabel(self)
        self.gallow.setPixmap(QPixmap("mistake0.jpg"))
        self.gallow.resize(200,200)

        self.gallow.move(470,75)


        self.meaning = QLabel("Meaning Of the word: ",self)
        self.meaning.move(30,70)
        self.meaning.resize(300,20)
        self.meaning.setFont(text_Font)

        self.word = QLabel("The word",self)
        self.word.move(30,130)
        self.word.resize(300,50)
        self.word.setFont(word_Font)

        self.guess = QLineEdit(self)
        self.guess.setPlaceholderText("Place enter your guess")
        self.guess.resize(160,30)
        self.guess.move(30,190)

        self.answer_button = QPushButton("Try",self)
        self.answer_button.move(30,225)
        self.answer_button.resize(100,50)
        self.answer_button.setFont(button_Font)




    def quit(self):
        sure = QMessageBox.question(self,"See you soon","Are you sure ?",QMessageBox.Yes | QMessageBox.No)
        if sure == QMessageBox.Yes:
            qApp.quit()



application = QApplication(sys.argv)
main_window = main()
sys.exit(application.exec_())
