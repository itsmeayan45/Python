print("Welcome to rollercoster!")
height=int(input("Enter your height in cm "))
age=int(input("Enter your age "))
if(height>=120):
    if(age>=18):
        print("You have to pay 12 dollar")
    else:
        print("You have to pay 7 dollar")
else:
    print("Sorry you can't take a rollercoster ride ")