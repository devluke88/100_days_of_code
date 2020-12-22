import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# New, combined function called caesar().
def ceasar(text, shift, direction):
    new_text = ""
    shift = shift % 25
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            new_text += letter
        else:
            new_letter_index = alphabet.index(letter) + shift
            new_text += alphabet[new_letter_index]
    print (f"The {direction}d text is {new_text}")

# Continue game function
def continue_function():
    while True:
        continue_question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if continue_question == "yes":
            return continue_game == True
        elif continue_question == "no":
            print("Goodbye")
            return continue_game == False

# Prints the logo from art.py when the program starts.
print(art.logo)

continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Call a ceasar function
    ceasar(text, shift, direction)
    # Continue game?
    continue_game = continue_function()