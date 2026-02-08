import random

choices = ('r', 'p', 's')
choices_key = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

# Stats as a dictionary
stats = {
    'player1_wins': 0,
    'player2_wins': 0,
    'tie': 0,
    'matches_played': 0,
    'player1_match_wins': 0}

# play round \\ define the formula that takes how the games works


def play_round():
    while True:
        player1 = input('Player 1: Rock, Paper, or Scissors?(r,p,s): ').lower()
        player2 = input('Player 2: Rock, Paper, or Scissors?(r,p,s): ').lower()
        if player1 not in choices and player2 not in choices:
            print('Invalid choice!')
        else:
            break  # get out of the loop

    player1_word = choices_key[player1]
    player2_word = choices_key[player2]

    print(f'Player 1 chose {player1_word}')
    print(f'Player 2 chose {player2_word}')

    if player1 == player2:
        print('Tie')
        stats['tie'] += 1  # returns the value stored in the dictionary
        return 'tie'
    elif (
        (player1 == 'r' and player2 == 's') or
        (player1 == 's' and player2 == 'p') or
            (player1 == 'p' and player2 == 'r')):
        print('Player 1 wins!')
        # returns the value stored in the dictionary
        stats['player1_wins'] += 1
        return 'player1'
    else:
        print('Player 2 wins!')
        # returns the value stored in the dictionary
        stats['player2_wins'] += 1
        return 'player2'

# Play best of three rounds: first 2 wins\\ define the formula that takes the points


def best_of_three():
    player1_wins = 0
    player2_wins = 0
    global stats  # Variable is defined outside a function

    stats['matches_played'] += 1

    while player1_wins < 2 and player2_wins < 2:
        winner = play_round()

        if winner == 'player1':
            player1_wins += 1
        elif winner == 'player2':
            player2_wins += 1
        print(f'Score - Player 1: {player1_wins}, Player 2: {player2_wins}')

     # Declare overall winner

    if player1_wins == 2:
        print("Congratulations! Player 1 wins the match!")
        stats['player1_match_wins'] += 1
    else:
        print("Congratulations! Player 2 wins the match!")

# Overall Stats


def show_stats():
    print('FINAL GAME STATISTICS:')
    print(
        f"Total Rounds Played: {stats['player1_wins'] + stats['player2_wins'] + stats['tie']}")
    print(f'Player 1 wins: {stats['player1_wins']}')
    print(f'Player 2 wins: {stats['player2_wins']}')
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
