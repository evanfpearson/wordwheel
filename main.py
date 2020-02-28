import sys

def valid(word, centre_letter, outer_letters):
  word = word.lower()
  word_length = len(word)
  all_valid_letters = [centre_letter] + outer_letters
  if not 3 < word_length <= len(all_valid_letters): 
    return False
  if centre_letter not in word:
    return False
  for letter in word:
    if letter not in all_valid_letters:
      return False
    all_valid_letters.remove(letter)
  return True

def main(letters):
  centre_letter = letters[0].lower()
  outer_letters = [char.lower() for char in letters[1:]]
  with open("dictionary.txt") as file:
    formatted_words = [word.strip().lower() for word in file.readlines()]
    valid_words = [word for word in formatted_words if valid(word, centre_letter, outer_letters)]
  print(valid_words)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Use one argument. A string containing all letters in the word wheel - beginning with the center letter.')
    exit()
  main(sys.argv[1])
