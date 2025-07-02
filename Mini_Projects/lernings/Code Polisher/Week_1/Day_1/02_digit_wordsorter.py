# Digit Word Sorter

'''My Version'''
'''
# Function
def digitwordsorter(sentence):
    words = sentence.strip().split()
    digits = []

    for word in words:
        if word.isdigit():
            digit = int(word)
            digits.append(digit)
    digits.sort()

    ascending_numbers = []
    for numbers in digits:
        number = str(numbers)
        ascending_numbers.append(number)

    return " ".join(ascending_numbers)
'''


'''Posiled Version'''
def digitwordsorter(sentence):
    digits = sorted(int(word) for word in sentence.split() if word.isdigit())
    return " ".join(map(str, digits))

# Input
statement = input("Enter a Sentence: ")
print(digitwordsorter(sentence = statement))
