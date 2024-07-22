import nltk

# Download the necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tag_text(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    # Perform POS tagging
    pos_tags = nltk.pos_tag(words)
    return pos_tags

# Example usage:
text = "This is a simple example sentence for part-of-speech tagging using NLTK."
pos_tags = pos_tag_text(text)
print(pos_tags)
