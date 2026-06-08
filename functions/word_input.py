def word_input(words: list, word_input: str = '') -> str:
    while len(word_input) != 5 or not word_input.isalpha() or word_input.lower() not in words:
        word_input = input("Enter a 5-letter word: ")
    return word_input.lower()