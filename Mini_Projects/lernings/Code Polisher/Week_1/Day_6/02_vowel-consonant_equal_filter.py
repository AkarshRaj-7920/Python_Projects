# Problem 2
# Equal Vowel-Consonant Word Filter

# Function
def equal_vowel_consonant_filter(text: str) -> list[str]:
    '''
    Filters and returns words with equal number of vowels and consonants.

    Args:
        text(str): Input sentence

    Returns:
        list[str]: Words where vowels == consonants
    '''
    vowels = ("a", "e", "i", "o", "u")
    words = text.strip().split()
    result = []

    for word in words:
        vowel_count = 0
        consonant_count = 0
        for char in word:
            if char.lower() in vowels:
                vowel_count += 1
            elif char.isalpha():
                consonant_count += 1

        if vowel_count == consonant_count:
            result.append(word)

    return result

# Input
def main ():
    while True:
        statement = input("• Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(" ○ Invlaid Input. Please enter Alphabetical words only.")
        else:
            break

    result = equal_vowel_consonant_filter(statement)
    print(f"• Equal Vowel-Consonant Words: {result}")

if __name__ == "__main__":
    main()
