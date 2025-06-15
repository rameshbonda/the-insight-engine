# consistency.py

from sklearn.metrics.pairwise import cosine_similarity
from api_clients.tachyon_embedding import get_embedding
import numpy as np

# Example input: 3-5 representative comments per category
CATEGORY_EXAMPLES = {
    "Login Issues": [
        "I can't log in to my account.",
        "The login page keeps loading forever.",
        "Password reset isn't working."
    ],
    "Payment Failure": [
        "My card transaction failed at checkout.",
        "UPI payment was deducted but not confirmed.",
        "I couldn’t complete the payment."
    ],
    "Performance Issues": [
        "The app is very slow to respond.",
        "It takes too long to load dashboards.",
        "Sluggish performance on mobile."
    ]
}

# Compute average embeddings for each category
def compute_category_embedding(comments):
    embeddings = [get_embedding(comment) for comment in comments]
    avg_embedding = np.mean(embeddings, axis=0)
    return avg_embedding.tolist()

# Build the category embedding dictionary at runtime
CATEGORY_EMBEDDINGS = {
    category: compute_category_embedding(examples)
    for category, examples in CATEGORY_EXAMPLES.items()
}

# Compare comment embedding to category vectors and return best match
def check_similarity(comment_embedding):
    similarities = {
        category: cosine_similarity([comment_embedding], [embedding])[0][0]
        for category, embedding in CATEGORY_EMBEDDINGS.items()
    }
    best_category = max(similarities, key=similarities.get)
    best_score = similarities[best_category]
    return best_category, best_score
