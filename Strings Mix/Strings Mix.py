# Strings Mix
# https://www.codewars.com/kata/5629db57620258aa9d000014

def mix(s1, s2):
    lowers = 'abcdefghijklmnopqrstuvwxyz' # lowercase letters
    
    d1={} # dictionary for occurrences of letters in s1
    for ch in s1:
        if ch in lowers:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] += 1
    
    d2={} # dictionary for occurrences of letters in s2
    for ch in s2:
        if ch in lowers:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] += 1
    
    diff_dict = {} # entries are tuples {letter: (occurrences, <s1 more, s2 more, or =>)} e.g. {'a': (4, '1')}
    for key in d1:
        if key not in d2: # the letter only occurs in s1
            if d1[key] > 1: # if this key has a value greater than 1, add it to the comparison dictionary
                diff_dict[key] = (d1[key],'1') # the key appears most d1[key] times in s1
        else: #s1 and s2 have the same letter
            if (d1[key] > d2[key]) and d1[key] > 1: # if s1 has the most of this letter with occcurences > 1
                diff_dict[key] = (d1[key],'1')
            elif (d2[key] > d1[key]) and d2[key] > 1: # if s2 has the most of this letter with occurrences > 1
                diff_dict[key] = (d2[key],'2')
            elif (d1[key] == d2[key]) and d1[key] > 1: #if s1 and s2 have the same amount of a letter and it happens more than once
                diff_dict[key] = (d1[key],'=') 
    for key in d2: # s2 might have other letters not in s1
        if (key not in diff_dict) and d2[key] > 1: # if the letter isn't already in our comparison dictionary and occurs more than once...
            diff_dict[key] = (d2[key],'2') # then note that s2 has this letter
    
    diff_dict_sorted = sorted(diff_dict.items(), key = lambda x: x[0]) # abc order
    #print(diff_dict_sorted)
    
    diff_dict_sorted = sorted(diff_dict_sorted, key = lambda x: x[1][1]) # sort by '1', '2', then '='
    #print(diff_dict_sorted)

    diff_dict_sorted = sorted(diff_dict_sorted, key = lambda x: x[1][0], reverse = True) # sort by occurences
    #print(diff_dict_sorted)
    
    result = ''
    for item in diff_dict_sorted:
        result += item[1][1] + ':' + item[0]*item[1][0] + '/'
    return result[0:-1]