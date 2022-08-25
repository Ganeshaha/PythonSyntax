def print_upper_words_only_letter(word_list, letter):
    """for a list of words, prints out each word on a separate line, 
    but in all uppercase, only those that begin with a specified letter"""
    for word in word_list:
        if word[0] == letter.upper() or word[0] == letter.lower():
            print(word.upper())

print_upper_words_only_letter(["yeet", "beet", "echo"], "e")