alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your Message:\n").lower()
shift=int(input("Type the shift number:\n"))
def ceaser(text,shift,dir):
    end_text=""
    if dir=="decode":
            shift*=-1
    for letter in text:
        pos=alphabet.index(letter)
        new_pos=pos+shift
        end_text+=alphabet[new_pos]
    print(f"The {dir}d text is {end_text}")
ceaser(text,shift,dir=direction)