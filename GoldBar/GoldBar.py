__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "5/15/2019"
__python_version__ = "3"
__notes__ = "PEP8 compliant, print out is on-screen only"

import random

# This application generates scratch off tickets in batches (Gold Bar style)
# Game model (Gold Bar) - a winning game consists in one of the options below:
#   1) 3 symbols in the same game: win the prize available for this game
#   2) 5x symbol in the game: your prize will be multiplied by 5
#   3) 7 symbol in the game: your prize will be multiplied by 10
winning_ratio = {'${:1,.2f}'.format(10): 15,  # every 15 printed GoldBar tickets, one will have the $10 prize
                 '${:1,.2f}'.format(20): 50,
                 '${:1,.2f}'.format(50): 100,
                 '${:1,.2f}'.format(100): 250,
                 '${:1,.2f}'.format(500): 400,  # every 400 printed GoldBar tickets, one will have the $500 prize
                 '${:1,.2f}'.format(5000): 700,
                 '5x-10': 60,
                 '5x-20': 120,
                 '5x-50': 240,
                 '7-10': 65,
                 '7-20': 130,
                 '7-50': 250,  # every 250 printed tickets, one will have the "7" in the game and the prize will be $250
                 'JACKPOT': 10000}

# list of icons that are normally printed as a picture, but here we only have the representation of each picture
items = ('bills', 'moon', 'bank', 'rainbow', 'lightening', 'bag', 'vault', 'strawberry', 'lemon', 'cherry')

# List of prizes
prizes = [elem for elem in winning_ratio.keys() if '$' in elem]
prizes.append('JACKPOT')


def create_loser_game(game_number):
    item1 = random.choice(items)
    item2 = random.choice(items)
    item3 = random.choice(items)
    if item1 == item2 == item3:
        # print(f'Trying again...{item1}-{item2}-{item3}')
        create_loser_game(game_number)
    else:
        print(f'Game {game_number}: {item1} - {item2} - {item3}: {random.choice(prizes)}')


def create_loser_ticket(): # Each ticket always contains 12 games
    counter = 1
    print('\nGenerating loser ticket...')
    while counter < 13:
        create_loser_game(counter)
        counter += 1


def create_winner_ticket(prz):
    counter = 1
    winner_position = random.randint(1, 12)  # select which random game will have the prize
    print('\nGenerating winner ticket... ')
    while counter < 13:
        if counter == winner_position:
            create_winner_game(counter, prz)
        else:
            create_loser_game(counter)
        counter += 1


def create_winner_game(game_number, prz):
    # the prize (prz) will indicate which mode this winner game operates
    if '-' in prz:
        if '5x' in prz:
            mode = 5
            prz = '${:1,.2f}'.format(int(prz.split('-')[1]))
        else:
            mode = 7
            prz = '${:1,.2f}'.format(int(prz.split('-')[1]))
    else:
        if 'JACKPOT' in prz:
            mode = 9
        else:
            mode = 1

    # mode 1 - regular
    # mode 5 - 5x
    # mode 7 - 7
    # mode 9 - JACKPOT

    val = random.choice(items)
    result = []
    if mode == 1 or mode == 9:
        result = [val, val, val]
    elif mode == 5:
        result.append(random.choice(items))
        result.append(random.choice(items))
        result.append('5x')
        random.shuffle(result)
    elif mode == 7:
        result.append(random.choice(items))
        result.append(random.choice(items))
        result.append('7')
        random.shuffle(result)
    elif mode == 9:
        result.append(random.choice(items))
        result.append(random.choice(items))
        result.append('JACKPOT')
        random.shuffle(result)

    print(f'Game {game_number}: {result[0]} - {result[1]} - {result[2]}: {prz}')


# Ask how many scratch offs will be printed in the batch
print_ticket_qty = 0
valid_entry = False
while valid_entry is False:
    print_ticket_qty = input("\nEnter the number of tickets you want to generate in this batch (min. 15 tickets):")
    if print_ticket_qty.isdigit():
        if int(print_ticket_qty) >= 15:
            print_ticket_qty = int(print_ticket_qty)
            valid_entry = True
        else:
            print("\nEach batch should contain a minimum of 15 tickets")
    else:
        print("\nThis is an invalid number!")


already_printed = 0
# Step 1/2:Loop through the winning ratio dictionaries and call function create_winner_ticket as many times as necessary
for prize, frequency in winning_ratio.items():
    quant = round(print_ticket_qty / frequency)
    if quant > 0:
        for n in range(0, quant):
            create_winner_ticket(prize)
            already_printed += 1

# Step 2/2:We have just printed all "winning tickets". Printing "losing tickets".
for i in range(1, print_ticket_qty - already_printed):
    create_loser_ticket()
