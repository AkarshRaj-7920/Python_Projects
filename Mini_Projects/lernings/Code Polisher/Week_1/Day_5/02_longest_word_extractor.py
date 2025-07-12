# Longest Word Extractor

# Function
def largest_word_extractor(text: str) -> list[str]:
    '''
    Extracts the largest word of the given Sentence.

    Args:
        text(str) -> The input statement

    Returns:
        list[str] -> Sorted list of all the largest words of the given statement
    '''
    words = text.strip().split()
    max_length = max(len(word) for word in words)
    max_length_words = [word for word in words if max_length == len(word)]
    
    return sorted(max_length_words)

# Input
def main():
    while True:
        statement = input("• Enter a Statement: ")
        if not all(word.isalpha()for word in statement.strip().split()):
            print(" ○ Invalid Input. Please enter Alphabetical words only.")
        else:
            break

    result = largest_word_extractor(statement)
    print(f"• Longest Word: {result}")

if __name__ == "__main__":
    main()
    