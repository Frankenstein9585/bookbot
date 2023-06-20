def count_words(text):
    """Returns the number of words in a text file"""
    words = text.split()
    return len(words)


def count_letters(text) -> dict:
    """Returns the number of each character"""
    letter_dict = dict()
    text = text.lower()

    for _ in text:
        if _ in letter_dict:
            letter_dict[_] += 1
        else:
            letter_dict[_] = 1

    return letter_dict


def print_report(text) -> None:
    """Prints a report of the number of characters"""
    print('--- Begin report of books/frankenstein.txt ---')
    print()
    print('{} words found in the document'.format(count_words(text)))
    letter_dict = count_letters(text)   
    sorted_letter_dict = dict(sorted(letter_dict.items(), key=lambda k: k[1], reverse=True))
    for character, count in sorted_letter_dict.items():
        if character.isalpha():
            print("The character '{}' was found {} times".format(character, count))


with open("books//frankenstein.txt") as f:
    file_contents = f.read()
# print(count_words(file_contents))
# print(count_letters(file_contents))
print_report(file_contents)
