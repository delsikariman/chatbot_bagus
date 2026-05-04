import json
import re
from pathlib import Path


DATA_FILE = Path(__file__).with_name("data.json")
STOPWORDS = {
    "adalah",
    "agar",
    "akan",
    "antara",
    "apa",
    "apakah",
    "atau",
    "bagi",
    "bagaimana",
    "dalam",
    "dan",
    "dapat",
    "dengan",
    "di",
    "ini",
    "itu",
    "ke",
    "kenapa",
    "mengapa",
    "pada",
    "secara",
    "sebagai",
    "sejak",
    "terhadap",
    "tidak",
    "untuk",
    "yang",
}
SUGGESTED_QUESTIONS = [
    "Apa itu AI?",
    "Apa itu Machine Learning?",
    "Apa itu Deep Learning?",
    "Apa itu NLP?",
    "Apa itu Computer Vision?",
    "Contoh penerapan AI",
]
DEFAULT_RESPONSE = (
    "Maaf, saya belum menemukan jawaban yang sesuai.\n\n"
    "Coba tanyakan salah satu topik berikut:\n"
    + "\n".join(f"- {question}" for question in SUGGESTED_QUESTIONS)
)


def load_knowledge_base():
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def normalize_text(value):
    value = value.lower()
    value = re.sub(r"[^\w\s]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def get_important_words(value):
    return {
        word
        for word in normalize_text(value).split()
        if len(word) > 1 and word not in STOPWORDS
    }


def get_match_score(text, keyword):
    normalized_keyword = normalize_text(keyword)
    if not normalized_keyword:
        return 0

    if normalized_keyword == text:
        return 200 + len(normalized_keyword)

    if normalized_keyword in text:
        return 70 + len(normalized_keyword)

    text_words = get_important_words(text)
    keyword_words = get_important_words(normalized_keyword)

    if len(text_words) < 2 or not keyword_words:
        return 0

    same_words = text_words & keyword_words
    if len(same_words) < 2:
        return 0

    text_coverage = len(same_words) / len(text_words)
    keyword_coverage = len(same_words) / len(keyword_words)

    if text_coverage < 0.6 or keyword_coverage < 0.35:
        return 0

    return (text_coverage * 60) + (keyword_coverage * 40) + len(same_words)


def get_response(user_text):
    text = normalize_text(user_text)
    knowledge_base = load_knowledge_base()
    best_match = None

    for item in knowledge_base:
        keywords = item.get("keywords", []).copy()
        if item.get("question"):
            keywords.append(item["question"])

        exact_keywords = [normalize_text(keyword) for keyword in item.get("exact_keywords", [])]
        if text in exact_keywords:
            return item["response"]

        for keyword in keywords:
            score = get_match_score(text, keyword)
            if score:
                if best_match is None or score > best_match["score"]:
                    best_match = {
                        "score": score,
                        "response": item["response"],
                    }

    if best_match:
        return best_match["response"]

    return DEFAULT_RESPONSE
