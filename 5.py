from nltk.stem import PorterStemmer
def perform_stemming(words):
    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return stemmed_words
words_to_stem = ["organization", "banking", "systemized", "stocks"]
stemmed_words = perform_stemming(words_to_stem)
print("Original Words:", words_to_stem)
print("Stemmed Words:", stemmed_words)
