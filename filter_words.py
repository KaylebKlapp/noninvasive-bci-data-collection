KEY_LETTER_1 = 'k'
KEY_LETTER_2 = 'v'
KEY_LETTER_3 = 'e'

# Read the content from "words_master.txt" and split it into words
with open("words_master.txt", "r") as words_master:
    words_master_contents = words_master.read()
    words = words_master_contents.split("\n")

# Create separate lists for words with and without keys
words_with_keys = []
words_without_keys = []

for word in words:
    if KEY_LETTER_1 in word or KEY_LETTER_2 in word or KEY_LETTER_3 in word:
        words_with_keys.append(word)
    else:
        words_without_keys.append(word)

# Write the filtered words to their respective files
with open("words_with_keys.txt", "w") as file:
    file.write("\n".join(words_with_keys))

with open("words_without_keys.txt", "w") as file:
    file.write("\n".join(words_without_keys))
