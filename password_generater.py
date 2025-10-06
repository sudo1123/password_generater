import json
import random
while True:
    try:
        password_length=int(input("Please enter the length of the password you want:"))
        break
    except ValueError:
        print("There is an error occurred, please try again.")
message=[]
with open("alphabet.json","r") as a:
    alphabet=json.load(a)
def pick_letter():
    cache=[]
    cache.append(random.randint(0,1))
    cache.append(random.randint(0,25))
    message.append(cache)

def Main(number_of_circulation):
    result=""
    for i in range(number_of_circulation):
        pick_letter()
    for element in message:
        if element[0]==0:
            result+=alphabet["uppercase"][element[1]]
        else:
            result+=alphabet["lowercase"][element[1]]
    return result

print("Here is your password:"+Main(password_length))