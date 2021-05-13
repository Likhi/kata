'''
Given a random number, you have to return the digits of this number within an
array in reverse order.
'''

def digitize(n):
    return list(reversed([int(x) for x in str(n)]))




print(digitize(123))
