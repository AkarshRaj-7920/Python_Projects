# Task 09: Word analyzer tool

ent_sen = input("Type a sentence: ")

# Spaces count
print("Did you left what was asked to do:", ent_sen.isspace())

# Length of character
length_ = len(ent_sen)
print("Length:", length_)

# Counting words
word_count = len(ent_sen.split())
print("Number of Words:", word_count)

# Vowels count
vowels = "aeiou"
count = ""
for i in ent_sen:
    if i in vowels:
        count += i
print("Number of Vowels:", len(count))

# Digits count
digits = ""
for k in ent_sen:
    if k.isdigit():
        digits += k
print ("Number of digits used:", len(digits))

# Letters count
letters = ""
for g in ent_sen:
    if g.isalpha():
        letters += g
print("Number of letters used:",len(letters))

# Reversed string
print("Your sentence in reversed form:\n\t", ent_sen[::-1])

# Summary in f-string
print("---Overall summary of your written sentence---\n")
print(f"""You wrote a sentence whose length is {length_}, 
Number of words used to form this sentence is {word_count},
Number of Vowels used in this sentence is {len(count)}, Digits used is {len(digits)},
Letter used is {len(letters)} and at last reverse of your sentence is 
            {ent_sen[::-1]}""")
