from KnowledgeBase import *

# these sentences use only words that were defined
sentence1 = "time is of the essence"
sentence2 = "she quickly ran to the store"
sentence3 = "that is a big old place"
sentence4 = "i see that person"
sentence5 = "it is good that i went to the store"

# these sentences use a mix of words, some are defined and some are not
sentence6 = "i accidentally bought old food from the store"
sentence7 = "she went for another item"
sentence8 = "i have to see the walrus"
sentence9 = "he knows the store is too brobdingnagian"
sentence10 = "you have quickly moved up the ladder"


print("Sentence 1:")
print(sentence1)
print(tagSentence(sentence1))
print(" ")

print("Sentence 2:")
print(sentence2)
print(tagSentence(sentence2))
print(" ")

print("Sentence 3:")
print(sentence3)
print(tagSentence(sentence3))
print(" ")

print("Sentence 4:")
print(sentence4)
print(tagSentence(sentence4))
print(" ")

print("Sentence 5:")
print(sentence5)
print(tagSentence(sentence5))
print(" ")

print("Sentence 6:")
print(sentence6)
print(tagSentence(sentence6))
print(" ")

print("Sentence 7:")
print(sentence7)
print(tagSentence(sentence7))
print(" ")

print("Sentence 8:")
print(sentence8)
print(tagSentence(sentence8))
print(" ")

print("Sentence 9:")
print(sentence9)
print(tagSentence(sentence9))
print(" ")

print("Sentence 10:")
print(sentence10)
print(tagSentence(sentence10))
print(" ")



#Getting sentence
words = raw_input("type a sentence:")
words = words.lower()
words = words.translate(None, '.;/\:?<>,"{}|+=_-)(*&^%$#@!')
print("Sentence 11:")
print (tagSentence(words))
print(" ")
