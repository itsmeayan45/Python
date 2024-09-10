print("Wlcome to love calculator! ")
name1=input("What is your name? ")
name2=input("What is her name? ")
string=name1+name2
low=string.lower()
t=low.count("t")
r=low.count("r")
u=low.count("u")
e=low.count("e")
true=t+r+u+e
l=low.count("l")
o=low.count("o")
v=low.count("v")
e=low.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if(love_score<10 or love_score>90):
    print(f"Your love score is {love_score},you go together like coke and mentos ")
elif(love_score<=40 and love_score>=50):
    print(f"Your score is {love_score},you are alright together.")
else:
    print(f"your love score is {love_score} ")