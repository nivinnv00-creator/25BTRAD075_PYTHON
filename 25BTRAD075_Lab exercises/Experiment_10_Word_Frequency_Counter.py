# LAB EXERCISE 10: Frequency Counter Using Dictionaries

sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency:", freq)
