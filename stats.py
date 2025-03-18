def sort_on(dict):
    return dict["num"]

def count_words(text):
  words = text.split()
  return len(words)

def count_chars(text):
  char_list = list(text)
  char_dict = {}
  for char in char_list:
    if char.lower() in char_dict:
      char_dict[char.lower()] += 1
    else:
      char_dict[char.lower()] = 1
  return char_dict

def sort_chars(char_dict):
  key_list = []
  for key in char_dict:
    keypair = {"char": key, "num": char_dict[key]}
    key_list.append(keypair)
  key_list.sort(reverse=True, key=sort_on)
  return key_list