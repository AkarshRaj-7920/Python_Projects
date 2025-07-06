# Vowel Count

''' My Code '''

'''
# Input
while True:
    statement = input("Enter a Sentence: ")
    if not statement:
        print(" ○ Invalid Input \n")
    else:
        break

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for letter in statement:
    if letter == "a":
        count_a+=1
    elif letter == "e":
        count_e+=1
    elif letter == "i":
        count_i+=1
    elif letter == "o":
        count_o+=1
    elif letter == "u":
        count_u+=1

dictionary_vowels = {"Vowels" : {" • a = ": count_a, " • e = ": count_e, " • i = ": count_i, " • o = ": count_o, " • u = ": count_u}, "Total" : count_a + count_e + count_i + count_o + count_u}
print(dictionary_vowels)
'''

''' Polished Code '''

from typing import Dict
def count_vowels(text: str) -> Dict[str, int]:
    """
    Count the occurences of each vowel (case-insensitive) in the input string.

    Args:
        text (str): Input string to analyze

    Returns:
        Dict[str, int]: A Dictionary with indivisual vowel counts and total vowel count.
    """

    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}

    for char in text.lower():
        if char in vowel_count:
            vowel_count[char] += 1
    
    total = sum(vowel_count.values())
    vowel_count['Total'] = total
    return vowel_count

def main():
    while True:
        statement = input("Enter a Statement: ").strip()
        if not statement:
            print(" ○ Invalid Input.\n   Please try again.\n")
        else:
            break

    result = count_vowels( text = statement)
    print("\nVowels Counts:")
    for vowel in "aeiou":
        print(f" • {vowel} = {result[vowel]}")
    print(f"\nTotal Vowels = {result['Total']}")

if __name__ == '__main__':
    main()
