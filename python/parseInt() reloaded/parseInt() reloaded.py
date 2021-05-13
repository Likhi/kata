# parseInt() reloaded
# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

# returns an array of the millions place, thousands place, and hundreds place of a string expressed in english words e.g. "eighty" for 80
def get_places(string):
    result = ['zero','zero','zero']
    
    if 'million' in string:
        result[0] = string.split('million')[0].strip()
        string = string.split('million')[-1].strip()
    
    if 'thousand' in string:
        result[1] = string.split('thousand')[0].strip()
        string = string.split('thousand')[-1].strip()
    
    result[2] = string.strip()
    
    return result
     
     
# returns a number that represents a 3-digit spelled number e.g. 'nine hundred thirty-two' as 932
def parse_small_int(string):
    
    string = string.replace('and ', '') # remove "and" if it's in there.
    
    result = 0
    
    ones = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, '':0, 'zero':0}
    teens = {'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19}
    tens = {'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
    
    if 'hundred' in string:
        result += 100 * ones[string[0:string.find('hundred')].strip()]
    
    not_ones = False
    for i in teens: # eleven
        if i in string:
            result += teens[i]
            not_ones = True
    for i in tens: # thirty-...
        if i in string:
            try:
                result += tens[i] + ones[string[string.find('-')+1:].strip()] # thirty-four
            except:
                result += tens[i] # thirty
            not_ones = True
    
    if not not_ones: # if the number is like 'one hundred four' or 'four'
        if result >= 100: # use the 'hundreds' to know where to split
            result += ones[string[string.find('hundred')+len('hundred')+1:].strip()]
        else:
            result += ones[string]
        
    return result
        
def parse_int(string):
    result = 0
    #print(string)
    places = get_places(string)
    #print(places)
    
    result += 1000000 * parse_small_int(places[0])
    result += 1000 * parse_small_int(places[1])
    result += 1 * parse_small_int(places[2])

    return result