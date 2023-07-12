import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return (0, user, computer)
    
    if is_win(user,computer):
        return (-1, user, computer)
    return (-1, user, computer)


def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print('It is a tie. You and the computer have both chose {}. \n'. format(user))
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
        else: 
            computer_wins += 1
            print('You chose {} and the computer choe {} You lost! :(\n'.format(user,computer))
        if player_wins > computer_wins:
            print('You have won the best of {} games!'.format(n))
        else: 
            print('Unfortunately, the computer has won the best of {} games.'.format(n))
            


if __name__ == '__main__':
    play_best_of(10)
    
#This idiom allows a Python file to be used both as a module and automatically executes certain code when run directly.
    
#This snippet defines the play_best_of function and then calls play_best_of(10) in the if __name__ == '__main__': block to play 10 rounds. This code will start 10 rounds game when run directly, but will not work when imported by another module.