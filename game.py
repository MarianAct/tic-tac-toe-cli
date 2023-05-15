import random
import re

players = {
    0: {
        'name': 'Player0',
        'turn': 0,
        'dice': 0,
        'symbol': ''
    },
    1: {
        'name': 'Player1',
        'turn': 0,
        'dice': 0,
        'symbol': ''
    }
}

print("[INFO]: Welcome to the X and O game!")

player_first = None
while player_first is None:
    input_value = str(input(f"[GAME]: Enter first player name: "))
    if len(input_value) <= 2:
        print('[INFO]: Value must contains more the 2 characters, please try again.')
    else:
        player_first = input_value
players[0]['name'] = player_first

player_second = None
while player_second is None:
    input_value = str(input(f"[GAME]: Enter second player name: "))
    if len(input_value) <= 2:
        print('[INFO]: Value must contains more the 2 characters, please try again.')
    else:
        player_second = input_value
players[1]['name'] = player_second

print(f"[INFO]: Hello {players[0]['name']} and {players[1]['name']}. Good Luck!")
print("[INFO]: Let's start dice to see how is starting first.")

while players[0]['dice'] == players[1]['dice']:
    players[0]['dice'] = random.choice(range(1, 7))
    players[1]['dice'] = random.choice(range(1, 7))
    print(f"[DICE]: {players[0]['name']} rolled {players[0]['dice']} and {players[1]['name']} rolled {players[1]['dice']}")
    if players[0]['dice'] == players[1]['dice']:
        print("[DICE]: The round is a draw, dice again.")

if players[0]['dice'] > players[1]['dice']:
    players[0]['turn'] = 1
    print(f"[DICE]: {players[0]['name']} is starting first!")
else:
    players[1]['turn'] = 1
    print(f"[DICE]: {players[1]['name']} is starting first!")

data = ['1', '2', '3', 
        '4', '5', '6', 
        '7', '8', '9']

def display(data):
    print("-------------------")
    print(f"| .{data[0]}. | .{data[1]}. | .{data[2]}. |")
    print(f"| .{data[3]}. | .{data[4]}. | .{data[5]}. |")
    print(f"| .{data[6]}. | .{data[7]}. | .{data[8]}. |")
    print("-------------------")

def isGameOver(data):

    winner = 'Nobody'
    over = False

    zone = {
        'orizontal': {
            0: [0, 1, 2], 
            1: [3, 4, 5], 
            2: [6, 7, 8]
        },
        'vertical': {
            0: [0, 3, 6],
            1: [1, 4, 7],
            2: [2, 5, 8]
        },
        'diagonal': {
            'LR': [0, 4, 8],
            'RL': [2, 4, 6]
        }
    }
    
    for i in zone.keys():
        for j in zone[i].keys():
            if data[zone[i][j][0]] == data[zone[i][j][1]] == data[zone[i][j][2]]:
                over = True
                symbol = data[zone[i][j][0]]
                player_id = getPlayerBySymbol(symbol)
                winner = players[player_id]['name']
                break
    
    if len(re.sub(r"\D", '', ''.join([i for i in data]))) == 0:
        over = True

    if over:
        display(data)
        if winner != 'Nobody':
            print(f'Congratulations! The winner is {winner}.')
        print("Game is over.")
    return over

def getPlayerBySymbol(symbol):
    for i in range(0, 2):
        if players[i]['symbol'] == symbol:
            return i

def whoseTurnIsIt():
    for i in range(0, 2):
        if players[i]['turn'] == 1:
            return i

while not isGameOver(data):

    player_id = whoseTurnIsIt()

    if players[player_id]['symbol'] == '':
        value = None
        while value is None:
            input_value = input(f"[GAME]: {players[player_id]['name']} is your turn, enter value (X or O): ")
            if input_value not in ['O', 'X']:
                print('[INFO]: Value must be O or X, please try again.')
            else:
                value = str(input_value)
        
        if value is not None:
            players[player_id]['symbol'] = value
            if value == 'X':
                players[int(not(player_id))]['symbol'] = 'O'
            else:
                players[int(not(player_id))]['symbol'] = 'X'
    else:
        value = players[player_id]['symbol']

    display(data)

    position = None
    while position is None:
        input_value = input(f"[GAME]: {players[player_id]['name']} is your turn, enter position: ")
        try:
            x = int(input_value)
            if x < 0 or x > 9:
                print(f"[INFO]: Position must be between 1 and 9, please try again.")
            else:
                if data[x - 1] in ['X', 'O']:
                    print('[INFO]: Position is already taken, please try again.')
                else:
                    position = x
        except ValueError:
            print(f"[INFO]: Position '{input_value}' is not a number, please try again.")

    if position is not None:
        data[position - 1] = value
        players[player_id]['turn'] = 0
        players[int(not(player_id))]['turn'] = 1