import random

choices = ('r', 'p', 's')
choices_key = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

# play round \\ define the formula that takes how the games works


def play_round():
    while True:
        computer = random.choice(choices)
        player = input('Rock, Paper, or Scissors?(r,p,s): ').lower()
        if player not in choices:
            print('Invalid choice!')
        else:
            break  # get out of the loop

    player_word = choices_key[player]
    computer_word = choices_key[computer]

    print(f'You chose {player_word}')
    print(f'Computer chose {computer_word}')

    if player == computer:
        print('Tie')
        return 'tie'
    elif (
        (player == 'r' and computer == 's') or
        (player == 's' and computer == 'p') or
            (player == 'p' and computer == 'r')):
        print('You win!')
        return 'player'
    else:
        print('You lose!')
        return 'computer'

# Play best of three rounds: first 2 wins\\ define the formula that takes the points


def best_of_three():
    player_wins = 0
    computer_wins = 0
    tie = 0

    while player_wins < 2 and computer_wins < 2:
        winner = play_round()

        if winner == 'player':
            player_wins += 1
        elif winner == 'computer':
            computer_wins += 1

        print(f'Score - You: {player_wins}, Computer: {computer_wins}')

     # Declare overall winner
    if player_wins == 2:
        print("Congratulations! You win the match!")
    else:
        print("Computer wins the match!")


# The main game
while True:
    best_of_three()

    # Ask if plyer wants to continue
    continue_process = input('Continue?(y/n): ').lower()
    if continue_process not in ['y', 'n']:
        print('Invalid choice!')
    elif continue_process == 'n':
        print('Thank you for playing!')
        break
