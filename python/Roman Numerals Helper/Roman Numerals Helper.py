# Roman Numerals Helper
# https://www.codewars.com/kata/51b66044bce5799a7f000003

"""TODO: create a RomanNumerals helper object"""

class RomanNumerals:
    def to_roman(num):
        result = ''
        
        try:
            ones_d = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
            result += ones_d[int(str(num)[-1])]
        except: pass

        try:
            tens_d = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
            result = tens_d[int(str(num)[-2])] + result
        except: pass

        try:
            hun_d = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
            result = hun_d[int(str(num)[-3])] + result
        except: pass

        try:
            thou_d = {1: 'M', 2: 'MM', 3: 'MMM', 4: 'MMMM'}
            result = thou_d[int(str(num)[-4])] + result
        except: pass

        return result
    
    def from_roman(rnum):
        # https://www.tutorialspoint.com/roman-to-integer-in-python
        rd = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        i = 0
        num = 0
        while i < len(rnum):
            if i+1<len(rnum) and rnum[i:i+2] in rd:
                num+=rd[rnum[i:i+2]]
                i+=2
            else:
                num+=rd[rnum[i]]
                i+=1
        
        return num

'''
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
'''


print(RomanNumerals.to_roman(2004))
print(RomanNumerals.from_roman('M'))