# Vowel Word Filter

# Functions
def vowel_word_filter(text: str) -> list[str]:
    '''
    Filters and returns all words from a sentence starting with a vowel.

    Args:
        text (str): The input sentence
    
    Returns:
        list[str]: Alphabetically sorted list of lowercase words starting with vowels.
    '''

    vowels = ("a", "e", "i", "o", "u")
    words = text.lower().strip().split()
    vowel_words = [word for word in words if word.startswith(vowels)]

    return sorted(vowel_words)

# Input
def main():
    while True:
        statement = input("• Enter a Sentence: ")
        if not statement.replace(" ", "").isalpha():
            print(" ○ Invalid Input. Please enter alphabetic words only. \n")
        else:
            break

    result = vowel_word_filter(statement)
    print(f"• Words starting with Vowels (sorted): {result}")

if __name__ == "__main__":
    main()
