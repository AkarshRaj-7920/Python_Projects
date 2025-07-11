# Consonant Word Extractor

# Function
def extract_consonant_word(text: str) -> list[str]:
    '''
    Extract words starting with consonants from a sentence.

    Args:
        text (str) -> The input staement
    
    Returns:
        list(str) -> Sorted list of lowercase words starting with consonants.
    '''

    vowels = ("a" ,"e" ,"i" ,"o" ,"u")
    words = text.lower().strip().split()
    consonant_word = [word for word in words if not word.startswith(vowels)]
    
    return sorted(consonant_word)

# Input
def main():
    while True:
        statement = input("• Enter a Statement: ")
        if not statement.replace(" " ,"").isalpha():
            print(" ○ Invalid Input. Please enter alphabetic words only. \n")
        else:
            break

    result = extract_consonant_word(statement)
    print(f"• Consonant Words (A - Z): {result}")

if __name__ == "__main__":
    main()
