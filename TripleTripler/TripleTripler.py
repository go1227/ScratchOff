__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "9/29/2019"
__python_version__ = "3"

import random

# Prize Level:
#  Single Prize (prize remains the same) - most common occurrence
#  Triple Prize (win 3x the Prize)
#  Triple Tripler (win 9x the Prize)

prize_level = ("1x", "3x", "9x")
usable_dollar_values = (1, 2, 3, 5, 6, 10, 20, 30, 50, 60, 100, 300, 600, 1800)

game_number = 900000  # this could work as a serial number

winning_combos = {
    # frequency-triplefactor: $dolllarvalue
    "15-1x": 2,  # $2 x1 = $3 (with the frequency of every 15 non-winning tickets)
    "15-3x": 2,  # $2 x3 = $6
    "15-9x": 2,  # $2 x9 = $18
    "20-1x": 3, "20-3x": 3, "20-9x": 3,
    "30-1x": 5, "40-3x": 5, "90-9x": 5,
    "40-1x": 6, "50-3x": 6, "60-9x": 6,
    "50-1x": 10, "60-3x": 10, "70-9x": 10,
    "51-1x": 20, "61-3x": 20, "71-9x": 20,
    "52-1x": 30, "62-3x": 30, "72-9x": 30,
    "63-1x": 50, "63-3x": 50, "83-9x": 50,
    "76-1x": 60, "86-3x": 60, "106-9x": 60,
    "200-1x": 100, "250-3x": 100, "400-9x": 100,
    "5000-1x": 300, "7500-3x": 300, "10000-9x": 300,
    "250000-1x": 600, "500001-3x": 600, "750000-9x": 600,
    "500000-1x": 1800, "500000-3x": 1800, "1000000-9x": 1800
}


def winning_ticket(dollar, frequency):
    # Extract triple factor from 'frequency'
    triple_factor = frequency.split('-')[1]
    winner_line = random.randint(1, 5)
    count = 1
    while count <= 5:
        if count == winner_line:
            col1 = random.choice(usable_dollar_values)
            if col1 != dollar:
                tmp = [dollar, dollar, col1]
                random.shuffle(tmp)
                print(f"GAME {game_number} - {'${:1,.2f}'.format(tmp[0])} | {'${:1,.2f}'.format(tmp[1])} | {'${:1,.2f}'.format(tmp[2])} ({triple_factor})")
                count += 1
        else:
            col1 = random.choice(usable_dollar_values)
            col2 = random.choice(usable_dollar_values)
            col3 = random.choice(usable_dollar_values)
            if col1 != col2 != col3:
                col1 = '${:1,.2f}'.format(col1)
                col2 = '${:1,.2f}'.format(col3)
                col3 = '${:1,.2f}'.format(col3)
                print(f"GAME {game_number} - {col1} | {col2} | {col3} ({random.choice(prize_level)})")
                count += 1


def losing_ticket():
    count = 5
    while count > 0:
        col1 = random.choice(usable_dollar_values)
        col2 = random.choice(usable_dollar_values)
        col3 = random.choice(usable_dollar_values)
        if col1 != col2 != col3:
            col1 = '${:1,.2f}'.format(col1)
            col2 = '${:1,.2f}'.format(col3)
            col3 = '${:1,.2f}'.format(col3)
            print(f"GAME {game_number} - {col1} | {col2} | {col3} ({random.choice(prize_level)})")
            count -= 1


# Main Program Execution:

ticket_amt = 1000  # number of scratch off tickets to be printed per program execution
# This FOR loop will print the Winning Tickets only
for frequency, dollar_amount in winning_combos.items():
    quant = round(ticket_amt / int(frequency.split('-')[0]))
    # print(f"{dollar_amount} / {frequency}: {quant} times")

    while quant > 0:
        print(f"\nCalling winning function for ${dollar_amount} / frequency:{frequency}")
        game_number += 1
        winning_ticket(dollar_amount, frequency)
        ticket_amt -= 1
        quant -= 1

# Print Losing Tickets
while ticket_amt > 0:
    print("\nCalling losing function")
    game_number += 1
    losing_ticket()
    ticket_amt -= 1
