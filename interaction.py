def prompt_new_category(comment):
    print(f"\n⚠️ Low confidence for: \"{comment}\"")
    user_input = input("Enter new category or press Enter to auto-assign: ").strip()
    return user_input if user_input else None
