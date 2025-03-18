import sys
from stats import count_words, count_characters, sort_characters

#path to the book
try:
    path_to_books = sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


#reads the text of the book
def get_book_text():
    
    with open(path_to_books) as f:
        file_contents = f.read()
    return file_contents


#Creates report
def reporter(word_count, sorted_characters, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_books}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for character in character_count:
        print(f"{character}: {character_count[character]}")
    
    print("============= END ===============")
    return



def main():
    book_text = get_book_text()
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_characters(character_count)
    reporter(word_count, sorted_characters, character_count)


main()