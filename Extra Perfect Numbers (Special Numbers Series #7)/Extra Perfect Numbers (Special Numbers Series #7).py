# https://www.codewars.com/kata/5a662a02e626c54e87000123
# Extra Perfect Numbers (Special Numbers Series #7)

def extra_perfect(n):
    result = []
    for i in range(1,n+1):
        i_as_binary = bin(i)[2:] # '0b1001' sliced to '1001'
        if (int(i_as_binary[0]) + int(i_as_binary[-1])) == 2:
            result.append(i)
    return result