# Decode the Morse code, advanced
# https://www.codewars.com/kata/54b72c16cd7f5154e9000457

# remove leading 0s from bit stream
def b_trim(bits):
    front = '0'
    for b in bits:
        if b == '0':
            bits = bits[1:]
        else:
            break
    
    #remove ending 0s
    while(bits[-1] == '0'):
        bits = bits[:-1]

    return bits
        
# find shortest segment of 1s and call that [1 time unit]
def xmt_freq(bits):
    run = 999999 # initial guess; impractically long so that any real frequency will be less
    current_run = 0
    if '0' not in bits:
        return bits.count('1')        
    else:
        for b in bits:
            if b == '1':
                current_run +=1
            else:
                if current_run > 0 and current_run <= run:
                    run = current_run
                current_run = 0
    
    # sometimes there's actually middle 0s and their runs are very short. this means the time base is from 0
    if run > bits.count('0'):
        run = bits.count('0')
    
    return run

def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = b_trim(bits)
    tu = xmt_freq(bits)
    return bits.replace('111'*tu, '-').replace('000'*tu, ' ').replace('1'*tu, '.').replace('0'*tu, '')

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    letters = morseCode.split(' ')

    for l in letters:
        if l == '':
            letters[letters.index(l)] = ' '
        else:
            letters[letters.index(l)] = MORSE_CODE[l]

    return ''.join(letters)
'''
'''
test = '1'
# test = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
d = decode_bits(test)
# print(d)

#decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')