import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def keytovalue(k):
        k=k.lower()
        if k in data:
            return data[k]
        elif k.title() in data:
            return data[k.title()]
        elif k.upper() in data:
            return data[k.upper()]
        elif len(get_close_matches(k,data.keys()))>0:
            a=input("Did you mean %s if yes press 'Y' or NO 'N' : " %get_close_matches(k,data.keys())[0])
            if a=="Y" or a=="y":
                return data[get_close_matches(k,data.keys())[0]]
            elif a=="N" or a=="n":
                return "Word doesn't exist"
            else:
                return "Didn't catch what you said"
        else:
            return "Word doesn't exist"


print("Program for Dictionary")
key=input("Please enter the KEY: ")
output=keytovalue(key)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
