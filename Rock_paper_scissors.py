# rock beats scissor
# paper beats rock
# scissor beats paper
import random
while True:
    computer = random.choice(['rock','paper','scissors'])
    player = input('enter your choice(rock,paper,scissors):').lower()
    if player == "quit":
        break
    if player != 'rock' and player != 'paper' and player != 'scissors':
        print('invalid choice')
    elif player == computer:
        print('its a tie')
    elif (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper') or (player == 'rock' and computer == 'scissors'):
        print('Player Wins')
    else:
        print('Computer Wins')
    print(f'computer choice was {computer}')

