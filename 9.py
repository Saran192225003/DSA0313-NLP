import nltk
import re
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')

class RuleBasedPOSTagger:
    def __init__(self):
        self.patterns = [
            (r'.*ing$', 'VBG'),   # gerunds
            (r'.*ed$', 'VBD'),    # past tense verbs
            (r'.*es$', 'VBZ'),    # 3rd person singular present
            (r'.*ould$', 'MD'),   # modals
            (r'.*\'s$', 'POS'),   # possessive nouns
            (r'.*s$', 'NNS'),     # plural nouns
            (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),   # cardinal numbers
            (r'.*', 'NN')         # default to nouns
        ]
    
    def tag(self, sentence):
        words = word_tokenize(sentence)
        tags = []
        for word in words:
            for pattern, tag in self.patterns:
                if re.match(pattern, word):
                    tags.append((word, tag))
                    break
        return tags

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog and barked loudly."
tagger = RuleBasedPOSTagger()
tags = tagger.tag(sentence)
print(tags)
