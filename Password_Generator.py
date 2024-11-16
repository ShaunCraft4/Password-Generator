import random

def Check(password):
    score=0
    advice=""
    if len(password)>12:
        score+=1
    else:
        advice+="Try having more than 12 characters.\n"  
    d={"UpperCase":0,"LowerCase":0,"Digits":0,"SpecialCharacters":0}
    for i in password:
        if i.isupper():
            d["UpperCase"]+=1
        if i.islower():
            d["LowerCase"]+=1
        if i.isdigit():
            d["Digits"]+=1
        if i.isalnum()==False:
            d["SpecialCharacters"]+=1
    for i in d:
        if d[i]>0:
            score+=1
        elif i=="UpperCase":
            advice+="Try having more uppercase letters.\n"
        elif i=="LowerCase":
            advice+="Try having more lowercase letters.\n"
        elif i=="Digits":
            advice+="Try having more numbers.\n"
        elif i=="SpecialCharacters":
            advice+="Try having more special characters.\n"
    return (score,advice)
    
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
            
        
            
