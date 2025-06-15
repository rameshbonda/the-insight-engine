from api_clients.tachyon_chat import classify_comment
from api_clients.tachyon_embedding import get_embedding
from consistency import check_similarity
from interaction import prompt_new_category
from config import CATEGORY_THRESHOLD

def classify_with_consistency(comment):
    category = classify_comment(comment)
    embedding = get_embedding(comment)
    consistent_cat, similarity = check_similarity(embedding)

    final_cat = category
    if similarity < CATEGORY_THRESHOLD:
        user_cat = prompt_new_category(comment)
        final_cat = user_cat or consistent_cat
    return final_cat, similarity
