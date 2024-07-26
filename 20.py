from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InformationRetrievalSystem:
    def __init__(self, documents):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)
    
    def query(self, query_text):
        query_vec = self.vectorizer.transform([query_text])
        results = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        return results

# Example usage:
documents = [
    "The cat in the hat.",
    "The quick brown fox.",
    "A fast white rabbit."
]
irs = InformationRetrievalSystem(documents)
query = "quick fox"
results = irs.query(query)
for i, score in enumerate(results):
    print(f"Document {i+1}: {score}")
