# Odd - Even Word Sorter

''' Functions '''
def sort_words_by_length_parity(words: list[str]) -> str:
    '''Sorts even-length words in descending and odd-length words in ascending order'''
    odd_words = sorted([words for word in words if len(word)%2 != 0])
    even_words = sorted([words for word in words if len(word)%2 == 0], reverse = True)

    # Format Results
    output = (f"Odd Words (Ascending): {odd_words} \nEven Words (Descending): {even_words}")

    return output

''' Input '''
while True:
    sentence = input("Enter a Sentence: ").strip()
    if not sentence:
        print("No Input provided. Please Enter a sentence.")
    else:
        word_list = sentence.split()
        break