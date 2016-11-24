'''
Descending_Order(num):
Your task is to make a function that can take any non-negative integer as a
argument and return it with it's digits in descending order. Descending order
means that you take the highest digit and place the next highest digit
immediately after it.

diamond(n):
You need to return a string that displays a diamond shape on the screen using
asterisk ("*") characters. Please see provided test cases for exact output
format.

The shape that will be returned from print method resembles a diamond, where
the number provided as input represents the number of *’s printed on the middle
line. The line above and below will be centered and will have 2 less *’s than
the middle line. This reduction by 2 *’s for each line continues until a line
with a single * is printed at the top and bottom of the figure.

Return null/none if input is even number or negative (as it is not possible
to print diamond with even number or negative number).

Please see provided test case(s) for examples.

'''

def Descending_Order(num):
    n = list(str(num))
    n.sort()
    n.reverse()
    return int(''.join(n))

def diamond(n):
    # Make some diamonds!
    top = 'top\n'
    bot = 'bot\n'

    for i in range(n):
        top += ('*' * (i+1)) + '\n'
    return top+bot

#print(Descending_Order(0))
#print(Descending_Order(15))
#print(Descending_Order(123456789))
print(diamond(5))
