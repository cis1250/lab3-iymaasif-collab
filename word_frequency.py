import re
import string

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Clean sentence (remove punctuation + lowercase)
cleaned = user_sentence.translate(str.maketrans("", "", string.punctuation)).lower()

# Split into words
words_list = cleaned.split()

# Create parallel lists for words and their frequencies
words = []
frequencies = []

for word in words_list:
    if word in words:
        index = words.index(word)
        frequencies[index] += 1
    else:
        words.append(word)
        frequencies.append(1)

# Print results
print("\nWord frequencies:")
for i in range(len(words)):
    print(f"{words[i]}: {frequencies[i]}")
