'''
Source:
https://www.codewars.com/kata/counting-change-combinations/train/python

Hint:
https://andrew.neitsch.ca/publications/m496pres1.nb.pdf
http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/

Write a function that counts how many different ways you can make change for an
amount of money, given an array of coin denominations. For example, there are 3
ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite ammount of coins.

Your function should take an amount to change and an array of unique
denominations for the coins:

count_change(4, [1,2]) # => 3
count_change(10, [5,2,3]) # => 4
count_change(11, [5,7]) # => 0
'''
def count_change(money, coins):
    combos = 0
    for c in coins:
        if (money - c) == 0:
            return 1
        count_change(money-c,coins)


''.join(list)

count_change(4, [1,2]) # => 3
count_change(10, [5,2,3]) # => 4
count_change(11, [5,7]) # => 0
