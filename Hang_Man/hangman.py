import random
from words import words
from hangmanvisual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   
    
    lives = 7

#getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: '.upper())
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print('\nYou have already used that letter. Gues another letter.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Gues another letter.')
        else:
            print('\n That is not valid letter.')
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You are hanged! Try again', word)
    else:
        print('You survived!', word)
if __name__ == '__main__':
    hangman()