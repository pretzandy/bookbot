from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted
import sys

def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    num_sorted = get_sorted(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(num_sorted)
    print("============= END ===============")

def get_book_text(book):
    with open(book) as f:
     return f.read()


main()


