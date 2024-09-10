print("Welcome to treasure island.")
print("Your mission is to find the treasure")
direction=input("Left or Right? ")
pos=input("Swim or Wait? ")
door=input("Which door? red blue or yellow? ")
if(direction=="Left" and pos=="Wait"):
    
    if(door=="yellow"):
        print("You win!")
    else:
        print("Game over.")
else:
    print("Game over.")