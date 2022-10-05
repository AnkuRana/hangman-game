import random
from hangman_words import word_list
from hangman_art import logo ,stages
print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, You have to guess a {chosen_word} letter word.')

#Create blanks
display = []
user_entered_letters = []
for _ in range(word_length):
    display += "_"

while lives > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in user_entered_letters:
        print("You have already entered the letter before, guess different")
    user_entered_letters.append(guess)
   
    element_check = 0
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            element_check = 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        break
#print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if element_check == 0:
        print(f"You have guessed wrong letter {guess}, you loose a life - Guess again")
        lives -= 1
        print(f"you have {lives} left.")
    print(stages[lives])

if end_of_game == True:
    print("You Win")
else:
    print("You Lost")
