# Unique Letter Word Finder

# Function
def unique_words_extractor(text: str) -> list[str]:
    '''
    Extracts unique words from the given statements whose letters are'nt repeated.

    Args:
        text (str) -> The input Sentence

    Returns:
        list[str] -> Sorted list of Unique words in the Statement
    '''
    words = text.strip().split()
    unique_words = [word for word in words if len(word) == len(set(word))]

    return sorted(unique_words)

# input
def main():
    while True:
        statement = input("• Enter a Sentence: ")
        if not all(word.isalpha() for word in statement.split()):
            print(" ○ Invalid Input. Please enter alphabetical words only.\n")
        else:
            break

    result = unique_words_extractor(statement)
    print(f"• Unique words: {result}")
    
if __name__ == "__main__":
    main()
    