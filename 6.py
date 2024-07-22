import random
from collections import defaultdict, Counter

class BigramModel:
    def __init__(self):
        self.bigram_counts = defaultdict(Counter)
        self.start_words = []

    def train(self, text):
        words = text.split()
        self.start_words.append(words[0])
        for i in range(len(words) - 1):
            self.bigram_counts[words[i]][words[i+1]] += 1
            if words[i][-1] in '.!?':  # Consider sentences ending in punctuation
                self.start_words.append(words[i+1])

    def generate(self, length=10):
        current_word = random.choice(self.start_words)
        result = [current_word]
        
        for _ in range(length - 1):
            current_word = random.choices(
                list(self.bigram_counts[current_word].keys()),
                list(self.bigram_counts[current_word].values())
            )[0]
            result.append(current_word)
        
        return ' '.join(result)

# Example usage:
text = """This is a simple example. This example is simple. Simple and short example for bigram model."""

bigram_model = BigramModel()
bigram_model.train(text)
generated_text = bigram_model.generate(10)
print(generated_text)
