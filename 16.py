import spacy

def perform_ner(text):
    # Load SpaCy's small English model
    nlp = spacy.load("en_core_web_sm")
    # Process the input text
    doc = nlp(text)
    # Iterate over the detected named entities
    for ent in doc.ents:
        print(ent.text, ent.label_)

# Example usage:
text = "Apple is looking at buying U.K. startup for $1 billion."
perform_ner(text)
