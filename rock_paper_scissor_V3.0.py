import random

choices = ('r', 'p', 's')
choices_key = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

# Stats as a dictionary
stats = {
    'player_wins': 0,
    'computer_wins': 0,
    'tie': 0,
    'matches_played': 0,
    'player_match_wins': 0}

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
        stats['tie'] += 1  # returns the value stored in the dictionary
        return 'tie'
    elif (
        (player == 'r' and computer == 's') or
        (player == 's' and computer == 'p') or
            (player == 'p' and computer == 'r')):
        print('You win!')
        stats['player_wins'] += 1  # returns the value stored in the dictionary
        return 'player'
    else:
        print('You lose!')
        # returns the value stored in the dictionary
        stats['computer_wins'] += 1
        return 'computer'

# Play best of three rounds: first 2 wins\\ define the formula that takes the points


def best_of_three():
    player_wins = 0
    computer_wins = 0
    global stats  # Variable is defined outside a function

    stats['matches_played'] += 1

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
        stats['player_match_wins'] += 1
    else:
        print("Computer wins the match!")

# Overall Stats


def show_stats():
    print('FINAL GAME STATISTICS:')
    print(
        f"Total Rounds Played: {stats['player_wins'] + stats['computer_wins'] + stats['tie']}")
    print(f'Player wins: {stats['player_wins']}')
    print(f'Computer wins: {stats['computer_wins']}')
    print(f'Ties: {stats['tie']}')
    print(f'Matches played: {stats['matches_played']}')


# The main game
while True:
    best_of_three()

    # Ask if plyer wants to continue
    continue_process = input('Continue?(y/n): ').lower()
    if continue_process not in ['y', 'n']:
        print('Invalid choice!')
    elif continue_process == 'n':
        show_stats()
        print('Thank you for playing!')
        break
