# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import sys
import random
import json

# TODO: replace with your own app_id and app_key
app_id = '698028c0'
app_key = '800bcc3a296d14a1731da7b6b12b2641'

language = 'en'

categories = ["Art","Music","Deneme","Test"]
categories = random.sample(categories,1)

url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/domains=' + categories[0] + '?limit=5'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

#print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))



name_json = r.json()


name_list = []
for name in name_json['results']:
    name_list.append(name['word'])

for i in name_list:
    print(i)
