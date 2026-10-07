import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# NLTK ka zaroori data (sirf pehli dafa download hota hai, internet chahiye)
for pkg in ("stopwords", "wordnet", "omw-1.4"):
    nltk.download(pkg, quiet=True)

# ---------------------------------------------------------------
# 1. FAQs (topic: online shopping store). Apni marzi ka topic rakhne
#    ke liye bas yahan questions aur answers badal dein.
# ---------------------------------------------------------------
FAQS = [
    {"question": "How can I place an order?",
     "answer": "Browse the products, add items to your cart and click Checkout. Enter your address and payment details to confirm the order."},
    {"question": "What payment methods do you accept?",
     "answer": "We accept credit/debit cards, bank transfer, mobile wallets and cash on delivery."},
    {"question": "How long does delivery take?",
     "answer": "Delivery usually takes 3 to 5 working days. Remote areas may take up to 7 days."},
    {"question": "How much is the shipping charge?",
     "answer": "Shipping is free on orders above 3000 PKR. For smaller orders, a flat fee of 200 PKR applies."},
    {"question": "How can I track my order?",
     "answer": "Go to My Orders in your account and click Track Order. You will also get a tracking link by email and SMS."},
    {"question": "Can I cancel my order?",
     "answer": "Yes, you can cancel your order before it is shipped from the My Orders page."},
    {"question": "What is your return policy?",
     "answer": "You can return most items within 7 days of delivery if they are unused and in their original packaging."},
    {"question": "How do I get a refund?",
     "answer": "Once we receive your returned item, the refund is processed within 5 to 7 working days to your original payment method."},
    {"question": "What should I do if I receive a damaged product?",
     "answer": "Please contact our support team within 48 hours with photos of the damaged item. We will replace it or refund you."},
    {"question": "How can I reset my password?",
     "answer": "Click Forgot Password on the login page, enter your email and follow the link we send you."},
    {"question": "How can I contact customer support?",
     "answer": "You can email us at support@shopeasy.com or call 0300-0000000, Monday to Saturday, 9 AM to 6 PM."},
    {"question": "Do you offer discounts or coupons?",
     "answer": "Yes! Subscribe to our newsletter to receive discount coupons and updates about seasonal sales."},
    {"question": "Do you deliver internationally?",
     "answer": "At the moment we deliver only within Pakistan. International shipping will be available soon."},
]

FALLBACK = ("Sorry, I could not understand that. Please try rephrasing your question "
            "or contact support@shopeasy.com.")

# ---------------------------------------------------------------
# 2. Preprocessing (NLTK): lowercase, tokenize, stopwords hatana, lemmatize
# ---------------------------------------------------------------
tokenizer = RegexpTokenizer(r"[a-z0-9]+")
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return " ".join(tokens)


# ---------------------------------------------------------------
# 3. TF-IDF + cosine similarity
# ---------------------------------------------------------------
cleaned_questions = [preprocess(f["question"]) for f in FAQS]
vectorizer = TfidfVectorizer()
faq_matrix = vectorizer.fit_transform(cleaned_questions)


def get_answer(user_input, threshold=0.25):
    """User ke sawal ka sab se milta julta FAQ dhoond kar uska answer wapas karta hai."""
    cleaned = preprocess(user_input)
    if not cleaned:
        return FALLBACK, 0.0
    user_vec = vectorizer.transform([cleaned])
    scores = cosine_similarity(user_vec, faq_matrix)[0]
    best = int(scores.argmax())
    if scores[best] < threshold:
        return FALLBACK, float(scores[best])
    return FAQS[best]["answer"], float(scores[best])


# Terminal mn test karne ke liye: python chatbot.py
if __name__ == "__main__":
    print("FAQ Chatbot (type 'quit' to exit)")
    while True:
        q = input("You: ").strip()
        if q.lower() in ("quit", "exit"):
            break
        answer, score = get_answer(q)
        print(f"Bot: {answer}  (match score: {score:.2f})")
