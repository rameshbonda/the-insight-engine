from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = "TACHYON_API_KEY"

VECTOR_STORE_NAME = "client-comments-store"
CATEGORY_THRESHOLD = 0.8
PREDEFINED_CATEGORIES = [
    "Login Issues",
    "Payment Failure",
    "Performance Issues",
    "App Crash",
    "Feedback",
    "Feature Request",
    "Others"
]