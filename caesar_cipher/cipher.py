import re
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


def encrypt(plain_text, shift):
  ret = ''
  for char in plain_text:
    if re.search(r'\W', char):
      ret += char
    
    if char.isupper():
      ret += chr((ord(char) + shift-65) % 26 + 65)
      
    if char.islower():
      ret += chr((ord(char) + shift - 97) % 26 + 97)
      
    if char.isnumeric():
      ret += char
      
  return ret
    

def decrypt(text, shift):    
  return encrypt(text, -shift)

def count_words(text):
    words = text.split()

    word_count = [word for word in words if (word.lower()) in word_list or word in name_list]

    return len(word_count)


def is_it_english(string):
  recognized_word_count = count_words(string)
  potential_word_count = len(string.split())
  percentage = int(recognized_word_count / potential_word_count * 100)
  if percentage >= 50:
      return string
      
  if percentage < 50:
    return
  
def crack(text):
  for i in range(26):
    its_english_shifted_down = is_it_english(decrypt(text, i))
    its_english_shifted_up = is_it_english(decrypt(text, -i))
    
    if its_english_shifted_down:
      return its_english_shifted_down
    if its_english_shifted_up:
      return its_english_shifted_up
      
  return ''
  
  