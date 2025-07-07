# Clean Word Extractor

# Funcion
def clean_word_extractor(text: str) -> list[str]:
    '''
    Extracts words that contains only alphabetic characters from a fiven text, converts them to lower case and returns them in sorted order.
    Args:
        text (str): The Input sentence.

    Returns:
        list [str]: A list of clean, lowercase, sorted words.
    '''

    words = text.lower().split()
    clean_words = [word for word in words if word.isalpha()]

    return sorted(clean_words, reverse= True)

# Input Function
def main():
    while True:
        statement = input("Enter a Statement: ").strip()
        if not statement:
            print(" • Invalid Input. Please Try again. \n")
        else:
            break
        
    result = clean_word_extractor(text = statement) 
    print(f"\n ○ Input: {statement} \n ○ Output: {result}")

if __name__ == "__main__":
    main()
