import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
synbols=['!','@','$','#','%','^','&','*','(',')','{','}','[',']','<','>','?','/',':','|']
print("Welcome to the Pypassword Generator! ")
n=int(input("How many letters would you like in your password? "))
s=int(input(f"How many symbols would you like?\n "))
num=int(input(f"How many numbers would you like?\n"))
passwd=[]
for char in range(1,n+1):
    passwd+=random.choice(letters)
for char in range(1,s+1):
    passwd+=random.choice(synbols)
for char in range(1,num+1):
    passwd+=random.choice(numbers)
random.shuffle(passwd)
pas="0"
for i in passwd:
    pas+=i
print(f"Your password is {pas} ")