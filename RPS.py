import random
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = prev_play
    if guess == '':
        guess = "R"
    response = {'P': 'S', 'R': 'P', 'S': 'R'}
    last_three = set(opponent_history[-3:])

    if len(last_three) == 3:
        response = {'S': 'P', 'P': 'R', 'R': 'P'}
    elif len(last_three) == 2:
        response = {'P': 'S', 'R': 'P', 'S': 'R'}
    elif len(last_three) == 1:
        response = {'P': 'P', 'R': 'R', 'S': 'S'}


    return response[guess]
