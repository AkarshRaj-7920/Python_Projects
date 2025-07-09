# Reverse Words in a Sentence

# Functions
def reverse_words_sentence(text: str) -> str:
    '''
    Reverses the order of the words in a sentence while preserving esch word.
    Args:
        text (str): The input sentence.

    Returns:
        str: The sentence with word order reversed.
    '''

    words = text.split()
    reversed_words = words[::-1]
    
    return " ".join(reversed_words)
    
# Input
def main():
    while True:
        statement = input("Enter a Statement: ").strip()
        if not statement:
            print(" ○ Invalid Input. Please enter values again...")
        else:
            break

    result = reverse_words_sentence(statement)
    print(f"Reversed Statement: {result}")
    
if __name__ == "__main__":
    main()