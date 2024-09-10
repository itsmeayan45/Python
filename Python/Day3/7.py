print("Welcome to Python pizza Deliveries!")
size=input("What size of pizza do you want? S , m or L? ")
pep=input("Do you want pepperoni? Y or N ")
cheese=input("Do you want extra cheese? Y or N? ")
bill=0
if(size=="S"):
    bill=15
    if(pep=="Y"):
        bill+=2
elif(size=="M"):
    bill=20
    if(pep=="Y"):
        bill+=3
elif(size=="L"):
    bill=25
    if(pep=="Y"):
        bill+=3
else:
    print("Please enter valid input")
if(cheese=="Y"):
    bill+=1
    print(f"Your final bill is: ${bill} ")
else:
    
    print(f"Your final bill is: ${bill}")  