# Problem 2
# Word case Transformer

# Functions
def word_case_transformer(text: str) -> list[str]:
    '''
    Transforms all the words starting with vowels to UPPERCASE and words starting with consonants to lowercase from the given Sentence.
    Args:
        text(str): The Input sentence

    Returns:
        list[str]: List of the transformed sentence
    '''
    vowels = ("a", "e", "i", "o", "u")
    words = text.strip().split()
    filtered_words = [word.upper() if word.lower().startswith(vowels) else word.lower() for word in words]

    return filtered_words

# Input
def main():
    while True:
        statement = input("• Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(" ○ Invalid Input. Please enter Alphabetic words only.\n")
        else:
            break

    result = word_case_transformer(statement)
    print(f"• Transformed Sentence: {" ".join(result)}")

if __name__ == "__main__":
    main()
