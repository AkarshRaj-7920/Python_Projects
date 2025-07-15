# Problem 1
# Palidrome Word Extractor

# Function
def palindrome_words_filter(text: str) -> list[str]:
    '''
    Extracts all the Palindrome words from the given Sentence.
    
    Args:
        text(str) -> The input Sentence

    Returns:
        list[str] -> List of all Palindrome words 
    '''
    words = text.strip().split()
    palindrome_words = [word for word in words if word.lower() == word.lower()[::-1]]
    
    return palindrome_words

# Input
def main():
    while True:
        statement = input("Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(" ○ Invalid Input. Please enter Alphabetical words.\n")
        else:
            break

    result = palindrome_words_filter(statement)
    print(f"• Plindrome Words: {result}")

if __name__ == "__main__":
    main()
