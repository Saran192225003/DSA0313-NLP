import nltk
from collections import defaultdict, Counter
import random

# Download necessary NLTK resources
nltk.download('brown')
nltk.download('universal_tagset')

class SimplePOSTagger:
    def __init__(self):
        self.transition_probs = defaultdict(Counter)
        self.emission_probs = defaultdict(Counter)
        self.tag_counts = Counter()
        self.vocab = set()
    
    def train(self, tagged_sentences):
        for sentence in tagged_sentences:
            previous_tag = "<START>"
            for word, tag in sentence:
                self.transition_probs[previous_tag][tag] += 1
                self.emission_probs[tag][word] += 1
                self.tag_counts[tag] += 1
                self.vocab.add(word)
                previous_tag = tag
            self.transition_probs[previous_tag]["<END>"] += 1
    
    def predict(self, sentence):
        best_tags = []
        previous_tag = "<START>"
        for word in sentence:
            if word not in self.vocab:
                word = "<UNK>"
            possible_tags = self.transition_probs[previous_tag].keys()
            best_tag = max(possible_tags, key=lambda tag: (self.transition_probs[previous_tag][tag] + 1) * (self.emission_probs[tag][word] + 1) / (self.tag_counts[tag] + len(self.vocab)))
            best_tags.append((word, best_tag))
            previous_tag = best_tag
        return best_tags

# Example usage:
# Using the Brown corpus from NLTK for training
from nltk.corpus import brown

tagged_sentences = brown.tagged_sents(tagset='universal')
tagged_sentences = [[(word.lower(), tag) for word, tag in sentence] for sentence in tagged_sentences]

# Train the POS tagger
tagger = SimplePOSTagger()
tagger.train(tagged_sentences)

# Predict the POS tags for a new sentence
sentence = "This is a simple example sentence.".lower().split()
predicted_tags = tagger.predict(sentence)
print(predicted_tags)
