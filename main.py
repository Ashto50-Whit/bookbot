
from stats import get_book_text
from stats import count_each_character
from stats import sort_char_count
import sys
if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    string = book.split()
    num_words = len(string)
    #print (f"{num_words} words found in the document.")
    char_count = count_each_character(book)
    #print(char_count)
    sorted_char_list = sort_char_count(char_count)
    print_report(book_path, num_words, sorted_char_list)

def print_report(book_path, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()


    