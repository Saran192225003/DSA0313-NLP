from nltk.wsd import lesk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def disambiguate_word(word, sentence):
    # Tokenize the sentence to create context for the word
    context = word_tokenize(sentence)
    # Apply the Lesk algorithm to find the most suitable sense of the word
    sense = lesk(context, word)
    return sense

# Example usage:
sentence = "I went to the bank to deposit money."
word = "bank"
sense = disambiguate_word(word, sentence)
if sense:
    print("Sense:", sense)
    print("Definition:", sense.definition())
else:
    print("No sense found.")
