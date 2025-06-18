# engine/classifier.py

from clients.llm_client import classify_comment_with_llm
from clients.tachyon_vector import vector_search
from utils.prompter import prompt_for_category
from config.settings import SIMILARITY_THRESHOLD

def classify_comment(comment: str) -> dict:
    # Step 1: Get LLM-based category suggestion
    llm_result = classify_comment_with_llm(comment)
    llm_category = llm_result.get("category", "")
    confidence = llm_result.get("confidence", 0)

    # Step 2: Consistency check with vector store
    similar_results = vector_search(comment)

    if similar_results:
        top_result = similar_results[0]
        score = top_result.get("score", 0)
        matched_category = top_result.get("metadata", {}).get("category", "")

        # If similarity score is high, use this category
        if score >= SIMILARITY_THRESHOLD:
            return {
                "comment": comment,
                "category": matched_category,
                "source": "vector_search",
                "score": round(score, 3)
            }

    # Step 3: If LLM result available and confidence good, use it
    if confidence >= 0.8 and llm_category:
        return {
            "comment": comment,
            "category": llm_category,
            "source": "llm",
            "score": round(confidence, 3)
        }

    # Step 4: Prompt user to assign a category manually
    final_category = prompt_for_category(comment, llm_category)
    return {
        "comment": comment,
        "category": final_category,
        "source": "user_prompt",
        "score": None
    }
