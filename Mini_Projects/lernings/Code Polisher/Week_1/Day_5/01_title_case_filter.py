# Title Case Filter

# Function
def title_word_extractor(text: str) -> list[str]:
    '''
    Extracts all the words of a setntece whose initial letter is Uppercase.

    Args:
        text(str) -> The input statement

    Returns:
        list[str] -> Sorted list of all title words extracted from the given sentence.
    '''

    words = text.strip().split()
    titlecase_words = [word for word in words if word.istitle()]
    
    return titlecase_words

# Input
def main():
    while True:
        statement = input("Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(f" ○ Invalid Input. Please enter Alphabetical words only.\n")
        else:
            break

    result = title_word_extractor(statement)
    print(f"Title Words: {result}")

if __name__ == "__main__":
    main()
