from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    text = f.read()
  return text

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
  path = sys.argv[1]
  book = get_book_text(path)
  num_words = count_words(book)
  char_dict = count_chars(book)
  sorted_list = sort_chars(char_dict)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for dict in sorted_list:
    char = dict["char"]
    count = dict["num"]
    if dict["char"].isalpha():
      print(f"{char}: {count}")

if __name__ == '__main__':
  main()