__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "4/28/2019"
__python_version__ = "3"

# This application generates scratch off tickets in batches (Double Dollars NY Lottery style)
# Results are currently being printed on-screen but the output can be easily tweaked to a TXT file output instead
# Game model (Double Dollars style - if "your_number" is greater than "their_number", you win the "PRIZE")
#   game 1: your_number  their_number  PRIZE
#   game 2: your_number  their_number  PRIZE
#   game 3: your_number  their_number  PRIZE
#   game 4: your_number  their_number  PRIZE
#   game 5: your_number  their_number  PRIZE

import random

# 1: 15 - this represents $1 dollar prize should be available every 15 tickets (common prize)
# 3000: 15000 - the prize of $3,000 dollars can be obtained every 15000 tickets printed (very rare prize)
winning_ratio = {'${:1,.2f}'.format(1): 15,
                 '${:1,.2f}'.format(3): 50,
                 '${:1,.2f}'.format(5): 100,
                 '${:1,.2f}'.format(10): 250,
                 '${:1,.2f}'.format(100): 5000,
                 '${:1,.2f}'.format(300): 10000,
                 '${:1,.2f}'.format(3000): 15000}


def create_loser_game():
    counter = 1
    print("\nGenerating loser ticket...")
    while counter < 6:
        your_number = random.randint(1, 30)
        their_number = random.randint(your_number + 1, 31)
        prize = random.choice(list(winning_ratio.keys()))
        print(f"game {counter} : {your_number} {their_number} {prize}")
        counter += 1

def create_winner_game(prize):
    print("\nGenerating winner ticket...")
    winner_line = random.randint(1, 6)
    counter = 1
    while counter < 6:
        if counter == winner_line:
            their_number = random.randint(1, 30)
            your_number = random.randint(their_number + 1, 31)  # my number is greater than the computer's, so I'll win here
            print(f"game {counter} : {your_number} {their_number} {prize}")
        else:
            your_number = random.randint(1, 30)
            their_number = random.randint(your_number + 1, 31)
            print(f"game {counter} : {your_number} {their_number} {random.choice(list(winning_ratio.keys()))}")
        counter += 1


# Ask how many scratch offs will be printed in the batch
print_ticket_qty = 0
valid_entry = False
while valid_entry is False:
    print_ticket_qty = input("\nEnter the number of tickets you want to generate in this batch (min. 10 tickets):")
    if print_ticket_qty.isdigit():
        if int(print_ticket_qty) >= 10:
            print_ticket_qty = int(print_ticket_qty)
            valid_entry = True
        else:
            print("\nEach batch should contain a minimum of 10 tickets")
    else:
        print("\nThis is an invalid number!")


already_printed = 0
# Step 1/2:Loop through the winning ratio dictionary and call the function create_winner_game as many times as necessary
for prize, frequency in winning_ratio.items():
    quant = round(print_ticket_qty / frequency)
    if quant > 0:
        for n in range(0, quant):
            create_winner_game(prize)
            already_printed += 1

# Step 2/2:We have just printed all winning tickets. Now we have to print the losing tickets.
for i in range(1, print_ticket_qty - already_printed):
    create_loser_game()

