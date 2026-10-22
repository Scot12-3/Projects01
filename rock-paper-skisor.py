import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)

print("--- ROCK, PAPER, SCISSORS ---")
player = input('Choose rock, paper, or scissors: ').lower().strip()

if player not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie! 👔")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print('You win! 🏆')
    else:
        print('Computer wins! 🤖')
