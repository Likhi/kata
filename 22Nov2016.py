'''
remove_char(s):
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter. 

snail(array):

'''

def remove_char(s):
  if len(s) < 2:
    return ''
  else:
    return s[1:-1]

def snail(array):
  twist = []
  n = len(array)
  
  if array != [[]]: # if the array is not empty...
    for i in range(0,round(n/2)):
      # Add top edge
      twist += array[i][i:n-i-1]
      
      # Add right edge
      for j in range(i,n-i-1):
        twist.append(array[j][n-1-i])
      
      # Add bottom row
      bot_row_forward = array[n-i-1][(i+1):(n-i)]
      bot_row_forward.reverse() #bot_row_backward! ahaaaa...
      twist += bot_row_forward
      
      # Add left edge
      left_edge_forward = []
      for j in range(i+1,n-i):
        left_edge_forward.append(array[j][i])
      left_edge_forward.reverse() #left_edge_backward!
      twist += left_edge_forward
    
    if n%2 > 0: # for an 5x5 or 7x7 or other odd x odd matrix, manually add center value
      twist.append(array[int((n-1)/2)][int((n-1)/2)])
    
    return twist
  
  else: # the array is empty!
      return [] # this is the expected response for a 0x0 empty array, i.e. array = [[]]
  
      
print(remove_char('hello')) # 'ell'
print(remove_char('sos'))   # 'o'
print(remove_char('ho'))    # ''
print(remove_char(''))      # ''
print(remove_char('o'))     # ''

array = [[1,2,3],[4,5,6],[7,8,9]]
#array = [list(range(1,7)),list(range(7,13)),list(range(13,19)),list(range(19,25)),list(range(25,31)),list(range(31,37))]
#array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(array)
#array = [[]]
#array = [[1]]
print(snail(array))