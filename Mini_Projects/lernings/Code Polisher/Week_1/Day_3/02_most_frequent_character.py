# Most Frequent Character

# Functions
def max_repeat_char_count(word: str) -> list[str]:
    '''
    Counts each and every letter of a words and returns the letter(s) which is repeated the most.

    Args:
        word (str): The input word
    
    Returns:
        list[str]: Sorted list of lowercase letters which is repeated the most in the given word
    '''

    freq = {}

    for char in word.lower():
        freq[char] = freq.get(char, 0) + 1

    each_letter_count = max(freq.values())
    most_repeated_letters = [letter for letter in freq if freq[letter] == each_letter_count]

    return sorted(most_repeated_letters)

# Input
def main():
    while True:
        user_input = input("Enter a Word: ")
        if not user_input.isalpha():
            print("• Invalid Input. Please enter Alphabetical Word only. \n")
        else:
            break

    result = max_repeat_char_count(user_input)
    print(f"• Most repeated letters: {result}")

if __name__ == "__main__":
    main()
