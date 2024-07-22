import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('treebank')
nltk.download('treebank_tagged')

class TransformationBasedTagger:
    def __init__(self, initial_tagger):
        self.initial_tagger = initial_tagger
        self.rules = []

    def add_rule(self, condition, old_tag, new_tag):
        self.rules.append((condition, old_tag, new_tag))

    def apply_rules(self, tagged_sentence):
        new_tagged_sentence = []
        for word, tag in tagged_sentence:
            new_tag = tag
            for condition, old_tag, new_tag_rule in self.rules:
                if tag == old_tag and condition(word, tag):
                    new_tag = new_tag_rule
            new_tagged_sentence.append((word, new_tag))
        return new_tagged_sentence

    def tag(self, sentence):
        initial_tags = self.initial_tagger.tag(word_tokenize(sentence))
        return self.apply_rules(initial_tags)

# Example usage
def main():
    # Load training data
    train_data = nltk.corpus.treebank.tagged_sents()

    # Create initial tagger
    default_tagger = DefaultTagger('NN')
    unigram_tagger = UnigramTagger(train_data, backoff=default_tagger)
    bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)

    # Initialize transformation-based tagger with initial tagger
    tbt = TransformationBasedTagger(bigram_tagger)

    # Add transformation rules
    # Example rule: If a word ends with 'ed' and is tagged as NN, change it to VBD
    tbt.add_rule(lambda w, t: w.endswith('ed'), 'NN', 'VBD')

    # Tag a sentence
    sentence = "The quick brown fox jumps over the lazy dog and barked loudly."
    tagged_sentence = tbt.tag(sentence)
    print(tagged_sentence)

if __name__ == "__main__":
    main()
