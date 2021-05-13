# Most frequently used words in a text
# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import re

def top_3_words(text):
    set = ' abcdefghijklmnopqrstuvwxyz\''
    print('Test input is:\n<',text,'>\n')
    #print(list(filter(lambda ch: ch in set, text.lower())))    
    #text = ''.join(list(filter(lambda ch: ch in set, text.lower()))) # remake input text, removing chars not in set
    #print(text)
    
    #          !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    
    rp = re.compile('[ !"#$%&\\()*+,-./:;<=>?@[\\]^_`{|}~]')
    text = text.lower()
    
    words = re.split(rp, text) # analyze only lowercase
    print(words)
       
    d = {}
    for w in words:
        #if w != '': # and w[0] != '\'': #omit empty strings, omit non-words
        if (re.match('.*\w+',w)):
            if w in d:
                d[w] +=1
            else:
                d[w] = 1

    print(d)
    # return 3 most-occuring word
    return [c[0] for c in sorted(d.items(), key = lambda x: x[1], reverse = True)[:3]]