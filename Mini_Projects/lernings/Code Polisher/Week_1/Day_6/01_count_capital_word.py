# Problem 1
# Count Capital Words

# Function
def count_capital_words(text:str) -> list[str]:
    '''
    Extracts all words that are fully UPPERCASE from the given sentence

    Args:
        text(str): The input sentence

    Returns:
        list[str]: List of all UPPERCASE words 
    '''
    words = text.strip().split()
    capital_words = [word for word in words if word.isupper()]

    return capital_words

# Input
def main():
    while True:
        statement = input("Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(" ○ Invalid Input. Please enter Alphabetic words.\n")
        else:
            break

    result = count_capital_words(statement)
    print(f"All Capital Words: {result}")

if __name__ == "__main__":
    main()
