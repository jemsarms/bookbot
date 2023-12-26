def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print(f"This is the letter occurances in the document \n\n {letter_count}")



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





main()