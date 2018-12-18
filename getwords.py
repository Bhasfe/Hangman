import requests
import random
import sqlite3

con = sqlite3.connect("word_database.db")
cursor = con.cursor()

def addtodb(word,meaning):

    if meaning != "Error":
        cursor.execute("SELECT * FROM words")
        word_database = cursor.fetchall()
        con.commit()
        if word not in word_database:
            cursor.execute("INSERT INTO words(word,definition) VALUES (?,?)",(word,meaning))
            con.commit()

def gettingwords():

    for i in range(5):

        with open("top1000words.txt","r") as word_list:

            words = word_list.readlines()
            the_word = random.sample(words,1)
            the_word = the_word[0].replace("\n","")

        app_id = "698028c0"
        app_key = "800bcc3a296d14a1731da7b6b12b2641"
        language = 'en'
        get_word = the_word


        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + get_word.lower()
        r_meaning = requests.get(url, headers= {'app_id': app_id, 'app_key': app_key})

        if r_meaning:
            meaning_json = r_meaning.json()
            meaning_list = []

            for result in meaning_json['results']:
                for lexicalEntry in result['lexicalEntries']:
                    for entry in lexicalEntry['entries']:
                        for sense in entry['senses']:
                            try:
                                meaning_list.append(sense['definitions'][0])
                            except KeyError:
                                meaning_list.append("Error")
        else:
            meaning_list = "Not Found"


        addtodb(the_word,meaning_list[0])
