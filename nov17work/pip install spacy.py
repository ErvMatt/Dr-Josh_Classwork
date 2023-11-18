pip install spacy
def learn_from_sentence(sentence):
    # Convert the sentence to lowercase to ensure case-insensitivity
    sentence = sentence.lower()
    
    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty dictionary to store word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        # Remove punctuation if any (for simplicity, you may need a more sophisticated approach)
        word = word.strip('.,!?')

        # Update the word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Example usage:
sentence = "The cat and the dog played, and the cat purred."
result = learn_from_sentence(sentence)
print(result)
import utils
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)