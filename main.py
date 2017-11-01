from copy import deepcopy

def valid(Word, letters):
  
  """
  This function determines if a word can be constructed using the word wheel.
  
  The function which takes three inputs:
  -- A word
  -- A list of the letters on the outer word wheel, where letter one is the middle letter of the WW
  
  The function outputs:
  -- True if the word can be constructed using the word wheel
  -- False if it cannot.
  """
  word = Word.lower()
  if len(word) < 3 or len(word) > 9: return False
  if letters[0] in word:
    x = 0
    for letter in word:
      x+=1
      if letter in letters:
        letters.remove(letter)
        if x == len(word):
          return True
      else: return False
  else: return False

ml = input("Which letter is in the middle of the word wheel?")
while(len(ml) != 1 or not ml.isalpha()):
  ml = input("Which letter is in the middle of the word wheel? Please input a single letter!")
ml = ml.lower()

ol = [ml]
for _ in range(8):
  l = input("Please input the remaining letters, one by one:")
  while(len(l) != 1 or not l.isalpha()):
    l = input("Please input the remaining letters, one by one:")
  ol.append(l.lower())
print(ol)

validWords = []

with open("dictionary.txt", mode="rt", encoding="utf8") as dic:
  lst = dic.readlines()
  for EL in lst:
    if (valid(EL[:-1], deepcopy(ol))):
      print(EL)
      validWords.append(EL[:-1])

print(validWords)