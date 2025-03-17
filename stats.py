#counts the number of words in the book
def count_words(book_text):
    words = book_text.split()
    return len(words)


#counts number of time each character appears in the book (count all as lowercase)
def count_characters(book_text):
    characters = {}
    for character in book_text:
        character = character.lower()
        if character.isalpha() == True:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters


# takes the dictionary of characters and their counts and returns a sorted list of dictionaries
def sort_characters(characters):
    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

    return sorted_characters