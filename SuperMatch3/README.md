# SuperMatch3
Scratch Off ticket generator

This program is currently set hardcoded the number of tickets to be printed (n=250), but you can change that to whichever amount of tickets you wish to generate.


Expected output for a winning ticket:

Generating winning tickets of $1
[[100, 300, 1, 1, 10], [100, 1, 1, 10, 1], [5, 10, 100, 100, 5]]

In the real world, the scratch off ticket would have 3 games as such:
- Game 1: $100  $300  $1   $1   $10
- Game 2: $100  $1    $1   $10  $1   ----> This is the winner game in this ticket
- Game 3: $5    $10   $100 $100 $5


------------------------------------------------------------


Expected output for a losing ticket:

Generating LOSING tickets
[[30000, 1, 3, 10, 1], [10, 300, 30000, 3, 30000], [100, 10, 30000, 30000, 3]]

In the real world, the scratch off ticket would have 3 games as such:
- Game 1: $3,000  $1    $3      $10    $1
- Game 2: $10     $300  $3,000  $3     $3,000 
- Game 3: $100    $10   $3,000  $3,000 $3
