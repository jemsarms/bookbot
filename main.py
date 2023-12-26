def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)

    print(f"\n\n--- Report of {book_path} ---\n\n")
    print(f"{num_words} words found in the document\n\n")
    display_letter_report(letter_count)
    print(f"\n\n--- End of {book_path} report---\n\n")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letter_count(texts):
    alphabet_dict = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    for word in texts.split():
        for character in word:
            if character.isalpha():
                character = character.lower()
                alphabet_dict[character] += 1

    return alphabet_dict

def display_letter_report(letter_dict):
    keys_list = list(letter_dict.keys())
    values_list = list(letter_dict.values())


    for letter, count in zip(keys_list, values_list):
        print(f"The letter '{letter}' was found {count} times")
    





main()