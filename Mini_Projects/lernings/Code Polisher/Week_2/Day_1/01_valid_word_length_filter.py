# Problem 1
# Valid Word Length Filter

# Function
def word_length_filter(text: str, n: int) -> list[str]:
    '''
    Extracts all the words from the given sentence which are greater than or equal to the given word length.

    Args:
        text(str): The input sentence.
        n(int): The minimum character length to filter.

    Returns:
        list[str]: List of all the words whose length is greater than or equal to given Word length.
    '''
    words = text.strip().split()
    filtered_words = [word for word in words if len(word) >= n]

    return sorted(filtered_words)

# Input
def main():
    while True:
        statement = input("• Enter a Statement: ")
        if not all(word.isalpha() for word in statement.strip().split()):
            print(" ○ Invalid Input. Please enter Alphabetic words only.\n")
        else:
            while True:
                min_length = input("• Enter Character Length to filter: ")
                if not min_length.isdigit():
                    print(" ○ Invalid Input. Please enter an Integer Value.\n")
                    continue
                else:
                    break
            break

    result = word_length_filter(statement, int(min_length))
    if not result:
        print("## No words found with the specified minimum length.")
    else:
        print(f"• Result: {result}")

if __name__ == "__main__":
    main()
