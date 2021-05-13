# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3 
# Backspaces in string

def clean_string(s):
    result = ''
    for char in s:
        result = result + char
        if char == '#':
            result = result[0:-2]
    return result