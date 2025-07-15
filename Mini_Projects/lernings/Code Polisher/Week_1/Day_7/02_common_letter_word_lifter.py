# Problem 2
# Common Letter Word Filter

# Function
def common_leter_word_filter(text: str, target_word: str) -> list[str]:
    '''
    Extracts all the words which match the letter of the given Target word with the given Stentence.
    Args:
        text(str): The input Sentence
        target_word(str): The input Target word
    Returns:
        list[str]: List of all the words which have common letter with the Target word   
    '''
    target_set = set(target_word.lower())
    words = text.strip().split()

    filtered_words = [word for word in words if set(word.lower()) & target_set]
    
    return sorted(filtered_words)

# Input
def main():
    while True:
        statement = input("Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(" ○ Invalid Input. Please enter Alphabetical words.\n")

        else:
            while True:
                target = input("Enter Target word: ")
                if not target.isalpha():
                    print(" ○ Invalid Input. Please enter Alphabetical single word only.\n")
                    continue
                
                else:
                    break
            break

    result = common_leter_word_filter(statement, target)
    print(f"Common Words: {result}")

if __name__ == "__main__":
    main()
