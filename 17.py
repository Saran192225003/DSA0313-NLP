import nltk
from nltk.corpus import wordnet

def explore_word(word):
    # Ensure the WordNet corpus is downloaded
    nltk.download('wordnet')
    # Retrieve the synsets for the given word
    synsets = wordnet.synsets(word)
    # Iterate over each synset
    for synset in synsets:
        print("Synset:", synset)
        print("Definition:", synset.definition())
        print("Examples:", synset.examples())
        print("Lemmas:", [lemma.name() for lemma in synset.lemmas()])
        print()

# Example usage:
explore_word("dog")
