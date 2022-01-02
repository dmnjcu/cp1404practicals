"""
CP1404/CP5632 Practical
Count word occurrences in a string
"""

text = input("Input a text: ")
list_word = text.split()
count_word = {}

max_length = 0
for word in list_word:
    if word not in count_word:
        max_length = len(word) if len(word) > max_length else max_length
        count_word[word] = 1
    else:
        count_word[word] += 1

for index, (word, count) in enumerate(count_word.items()):
    print("{:{}} : {}".format(word, max_length, count))