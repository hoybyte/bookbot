def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_frequencies = get_letter_count(text)
    generate_report(book_path, num_words, letter_frequencies)
    

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_count = {}
    book_text = text.lower()

    for letter in book_text:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    
    letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    return letter_count

def generate_report(book_path, num_words, letter_frequencies):
    print(f" --- Begin report for {book_path} ---")
    print(f"{num_words} words found in book")

    for letter in letter_frequencies:
        print(f"The {letter} character was found {letter_frequencies[letter]} times")

    print(f"--- End Report ---")
    
main()
