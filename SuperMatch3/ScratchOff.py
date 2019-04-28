__author__ = "Gil Ortiz"
__version__ = "1.1"
__date_last_modification__ = "3/11/2019"
__python_version__ = "3"

# Program that generates scratch off tickets in batches
# The results will be automatically generated into text files (folder \Results\)
# Game model (Super Match 3 style)
#   game 1: N1 N2 N3 N4 N5
#   game 2: N1 N2 N3 N4 N5
#   game 3: N1 N2 N3 N4 N5

import random

# These are the numbers available for all games in every ticket
numbers = [1, 3, 5, 10, 100, 300, 30000]

# 1: 15 - this represents $1 dollar prize should be available every 15 tickets (common prize)
# 3000: 15000 - the prize of $3,000 dollars can be obtained every 15000 tickets printed (very rare prize)
winning_ratio = {1: 15, 3: 50, 5: 100, 10: 250, 100: 5000, 300: 10000, 3000: 15000}


#This function will generate non-winning tickets only
def CreateLosingTicket(numbers):
    ticket_result = []
    print('Generating LOSING tickets')
    n = 3
    result = []
    while (n > 0):
        while len(result) < 5:
            random.shuffle(numbers)
            tmp = numbers[0]  # use 1st number of the list of numbers that we just shuffled
            if result.count(tmp) < 2:
                result.append(tmp)

        random.shuffle(result)
        ticket_result.append(result.copy())
        result.clear()
        n -= 1

    print(ticket_result)
    print("--------------------------------------------")


def CreateWiningTicket(numbers, val):
    ticket_result = []
    print('Generating winning tickets of $' + str(val))
    usable_numbers = numbers.copy()
    usable_numbers.remove(val)
    n = 3
    result = []
    winning_game = random.randint(1,n) #decision which of the 3 games will be the winner
    while (n > 0):
        if n == winning_game: #this line/game should have the winning combination for the $ amount in val parameter
            random.shuffle(usable_numbers)
            result.append(usable_numbers[0])  # use 1st number of the list of numbers that we just shuffled
            random.shuffle(usable_numbers)
            result.append(usable_numbers[0])
            result.append(val)
            result.append(val)
            result.append(val)

            random.shuffle(result)
            #print(result)
            ticket_result.append(result.copy())
           # print(ticket_result)
            result.clear()
        else:
            while len(result) < 5:
                random.shuffle(numbers)
                tmp = numbers[0] #use 1st number of the list of numbers that we just shuffled
                if result.count(tmp) < 2:
                    result.append(tmp)

            random.shuffle(result)
            #print(result)
            ticket_result.append(result.copy())
            #print(ticket_result)
            result.clear()

        n -= 1
    print(ticket_result)
    print("--------------------------------------------")




# E.g.: 250 tickets request
# According to the winning ratio, I should expect:
# - 17 tickets with $1 prize
# - 5 tickets with $3 prize
# - 2 tickets with $5 prize
# - 1 ticket with $10 prize



print_ticket_qty = 0
valid_entry = False
while valid_entry is False:
    print_ticket_qty = input("\nEnter the number of tickets you want to generate in this batch (min. 10 tickets):")
    if (print_ticket_qty.isdigit()):
        if (int(print_ticket_qty) >= 10):
            print_ticket_qty = int(print_ticket_qty)
            valid_entry = True
        else:
            print("\nEach batch should contain a minimum of 10 tickets")
    else:
        print("\nThis is an invalid number!")





already_printed = 0
#Step 1 of 2: Loop through the winning ratio dictionary and call the function CreateWiningTickets as many times as necessary
for k,v in winning_ratio.items():
    quant = round(print_ticket_qty / v)
    if (quant > 0):
        for n in range(0,quant):
            CreateWiningTicket(numbers,k)
            already_printed += 1

#Step 2 of 2: We have just printed all winning tickets. Now we have to print the losing tickets.
for i in range(1, print_ticket_qty - already_printed):
    CreateLosingTicket(numbers)

