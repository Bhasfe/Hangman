## A Hangman Game implementation in Python<br>
**Game Play**<br>
![start](https://github.com/Bhasfe/Hangman/blob/master/images/gameplay.gif?raw=true)
<br>
Hangman is the one of the most popular puzzles which has been created long time ago. The aim of the game is finding the world which is asked. To help you to find the word, its definition will be given for you. You will try a letter, and if the word contains it, the letter will be visible in the corresponding place.

You can see your preceding guesses at the ‘so far’ list. If you guess one of your preceding guesses, the program will inform you about that as well.

### Requirements
To use *Pyqt5* and *requests* you need to install<br>
`pip3 install pyqt5`<br>
`pip install requests`<br>
 
### Some Details
The project contains two python file which are **main.py** and **getwords.py**<br>
<br>
In *getwords.py*, I used Oxford Dictionaries API to get words. You can find further information at [https://developer.oxforddictionaries.com](https://developer.oxforddictionaries.com).
I also created a text file which contains the top 1000 words in English.
The program searches the definitions of the 5 words that are in the **top1000words.txt** at **Oxford Dictionaries** and insert words and their definitions into word_database.db for each execution
To be able to use **getwords.py**, you can change these parts with your own
<br>*line 28 29*<br>
`app_id = "your_app_id"`<br>
`app_key = "your_app_key"`

In *main.py*, the askWord function selects a random word in word_database and asks it to user.

I am looking forward to your suggestions and comments :)
