import sys
from stats import get_word_count

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    contents = get_book_text(book_path)

    word_count = get_word_count(contents)
    character_count = get_character_count(contents)

    generate_report(book_path, word_count, character_count)


def get_character_count(book):
    char_counts = {}
    for character in book:
        character = character.lower()
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1

    return char_counts

def generate_report(book_path, word_count, character_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    sorted_dict = {key: value for key, value in sorted(character_count.items(), key=lambda item: item[1], reverse=True)}

    for character in sorted_dict:
        if character.isalpha():
            print(f"{character}: {character_count[character]}")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()