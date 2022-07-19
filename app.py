import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead?: " %get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word dosen't exist. Check it again."
        else:
            return "We didn't understand your entry."
    else:
        return "Word dosen't exists. Check it again."

word = input("Enter a word: ")

output = translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



