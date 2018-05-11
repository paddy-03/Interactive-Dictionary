import os
import json
from difflib import get_close_matches
os.chdir('/home/swarup03/Udemy/08 Application 1 Building an Interactive Dictionary')
#print(os.getcwd())

data = json.load(open("076 data.json"))
#print(data.keys())

def meaning(word):
    word=word.lower()
    Word = word.title()
    WORD = word.upper()
    if word in data.keys() or Word in data.keys() or WORD in data.keys():
        if word in data.keys():
            return data[word]
        elif Word in data.keys():
            return data[Word]
        else:
            return data[WORD]
    elif len(get_close_matches(word,data.keys())):
        yn = input("Did you meean %s (Y/N) " %get_close_matches(word,data.keys())[0])
        if yn == 'Y' or yn == 'y':
                return data[get_close_matches(word,data.keys())[0]]
        else:
                return "Word not found"
    else:
        return "Word not found"

word=input("Enter Word: ")
output = meaning(word)

ctr=1
if type(output) == list:
    for meaning in output:
        print(str(ctr) + ". " +meaning)
        ctr+=1

else:
    print(output)

