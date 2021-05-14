# Array plus array
# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151

def array_plus_array(arr1,arr2):
    return sum(list(map(lambda x,y: x+y, arr1, arr2)))

a,b = [100, 200, 300], [400, 500, 600]
print(array_plus_array(a,b))