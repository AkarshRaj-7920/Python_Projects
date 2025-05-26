# Problem 7
# Word Frequency

word = input("Type a sentence: ")
word_count = input("Word in sentence to count: ").lower().strip()

lis1 = word.lower().strip().split()

count  = 0
for i in lis1:
    if i == word_count:
        count += 1
    
print(f"Number of {word_count} in the sentence is {count}")