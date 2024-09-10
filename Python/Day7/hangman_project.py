import random
word_list=["ardvark","baboon","camel"]
choosen_word=random.choice(word_list)
print(f"Passt, the solution is {choosen_word}.")
display=[]
word_length=len(choosen_word)
lives=6
for _ in range(word_length):
    display+="_"
print(display)
eog=False
while not eog:
    guess=input("Guess a letter: ").lower()

    for position in range(word_length):
        letter=choosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter:{guess}")
        if letter==guess:
            display[position]=letter
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            eog=True
            print("You loose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        eog=True
        print("You win")