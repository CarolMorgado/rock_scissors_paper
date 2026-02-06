import random

choices = ('r', 'p', 's')
choices_key = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

while True:
    computer = random.choice(choices)
    player = input('Rock, Paper, or Scissors?(r,p,s): ').lower()
    if player not in ('r', 'p', 's'):
        print('Invalid choice!')
        continue

    player_word = choices_key[player]
    computer_word = choices_key[computer]

    print(f'You chose {player_word}')
    print(f'Computer chose {computer_word}')

    if player == computer:
        print('Tie')
    elif (
        (player == 'r' and computer == 's') or
        (player == 'p' and computer == 's') or
            (player == 'p' and computer == 'r')):
        print('You win!')
    else:
        print('You lose!')

        continue_process = input('Continue?(y/n): ').lower()
        if continue_process not in ['y', 'n']:
            print('Invalid choice!')
            continue_process
        elif continue_process == 'n':
            break
