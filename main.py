#Step 4

import random
import hangman_art
import hangman_words

print(hangman_art.logo)
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 7.
lives = 6

#Testing code
print(f'Pssst, You have to guess a {chosen_word} letter word.')

#Create blanks
display = []
user_entered_letters = []
for _ in range(word_length):
    display += "_"

while lives >= 0:
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
#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        break
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if element_check == 0:
        print(hangman_art.stages[lives])
        print(f"You have guessed wrong letter {guess}, you loose a life - Guess again")
        lives -= 1
        
        print(f"you have {lives+1} left.")

if end_of_game == True:
    print("You Win")
else:
    print("You Lost")
