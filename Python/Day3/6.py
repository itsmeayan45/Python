print("Welcome to rollercoster!")
bill=0
height=int(input("Enter your height in cm: "))
age=int(input("Enter your age: "))
pic=input("Do you want to take a picture? type yes or no ")
if(height>=120):
    if(age>18):
        bill=12
        print("You can ride and your fare will be $12 ")
    elif(12<=age<=18):
        bill=7
        print("You can ride and your fare will be $7 ")
    else:
        bill=5
        print("You can ride and your fare will be $5")
    if(pic=="yes"):
        bill+=3
        print(f"Your bill will be ${bill}")
else:
    print("You can't ride ")