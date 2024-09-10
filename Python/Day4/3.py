import random
name=input("Enter some name seperated by a comma : ")
names=name.split(", ")
num=len(names)
choice=random.randint(0,num-1)
person=names[choice]
print(f"{person} is going to buy the meal today!")