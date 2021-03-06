'''
There is a secret string which is unknown to you. Given a collection of random
triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter
occurs somewhere before the next in the given string. "whi" is a triplet for the
string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the
secret string.

You can assume nothing about the triplets given to you other than that they are
valid triplets and that they contain sufficient information to deduce the
original string. In particular, this means that the secret string will never
contain letters that do not occur in one of the triplets given to you.
'''

def recoverSecret(triplets):
  'triplets is a list of triplets from the secrent string. Return the string.'
  w = []
  for triplet in triplets:
      for index,letter in enumerate(triplet):
          if letter not in w:
              w.append(letter)
          else:
              # check if rule is being followed
              for i in range(index+1:3):
                  if triplet[i] in w: # if triplet letter available in w
                    if w.index(triplet[i]) > w.index(letter):
                        pass # rule followed
                    else:
                        # move letter immediately before

          print(''.join(w)) # show the evolution of my algorithm process




secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
print(recoverSecret(triplets))
