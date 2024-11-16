import random
from Password_Checker import Check

def Create_Password():
    length=int(input("Enter how long thee password should be: "))
    Cases=["ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz","1234567890","!@#$%^&*(){}[];':\|<>?,./"]
    password=""
    if length>12:
        while True:
            for i in range(length):
                Case=random.choice(Cases)
                password+=random.choice(Case)
            Score=Check(password)[0]
            if Score==5:
                print("Here is a new password for you:")
                print(password)
                break
            else:
                password=""
    else:
        print("Please choose the length of the password to be more than 12 characters!")

Create_Password()
            
        
            