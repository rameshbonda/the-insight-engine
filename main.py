from io_utils import load_comments, write_output
from classifier import classify_with_consistency

def main(input_path):
    df = load_comments(input_path)
    results = []

    for comment in df['comment']:
        try:
            category, sim = classify_with_consistency(comment)
            results.append({
                "comment": comment,
                "category": category,
                "similarity_score": round(sim, 3)
            })
        except Exception as e:
            print(f"❌ Error processing comment: {comment} — {e}")

    write_output(results)

if __name__ == "__main__":
    main("data/input_sample.csv")