# Even Word Reverser

'''My Version'''
'''
word = input("Word: ")
word_lis = word.strip().split()

rever_list = []
for i in word_lis:
    if len(i)%2 != 0:
        rever_list.append(i)
    elif len(i)%2 == 0:
        a = i[::-1]
        rever_list.append(a)
    
print(" ".join(rever_list))
'''

'''Polished Version'''
def reverse_even_words(sentence):
    words = sentence.strip().split()
    processed = []

    for word in words:
        if len(word)%2 == 0:
            reverse_words = word[::-1]
            processed.append(reverse_words)
        else:
            processed.append(word)
    return " ".join(processed)

# Input
user_input = input("Enter a Sentence: ")
result = reverse_even_words(user_input)
print(result)
