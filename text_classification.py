from transformers import pipeline

# Load the pre-trained model and tokenizer
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define the input text
texts = [
    "The economy is improving, and the stock market is hitting new highs.",
    "The new movie was a thrilling adventure with stunning visuals.",
    "The football team lost the match due to poor defense and missed opportunities.",
    "The movie was so scary I couldn't stay to finish it.",
    "Loved the way they ended the movie.",
    "We won the FA cup.",
    "We didn't win any major trophy, but it was a season to remember.",
    "The traffic was terrible this morning, and I was late for work.",
    "I received a rejection letter from the job I applied for, and I'm feeling disappointed.",
    "The restaurant experience was awful - the food was cold, and the service was slow.",
    "My car broke down on the highway, and I had to wait for hours for a tow truck.",
    "I'm feeling stressed and overwhelmed with all the deadlines at work."
]


# Classify the text
results = classifier(texts)

# Print the results
for i, text in enumerate(texts):
    print(f"Text: {text}")
    print(f"Classification: {results[i]['label']}, Confidence: {results[i]['score']:.4f}")
    print()
