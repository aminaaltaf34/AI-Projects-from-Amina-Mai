# 🤖 FAQ Chatbot

A simple chatbot that answers frequently asked questions using Natural Language Processing. Built as part of the **CodeAlpha Artificial Intelligence Internship** (Task 2).

The chatbot uses the FAQs of an example online store (ShopEasy), but the topic can be changed easily by editing the FAQ list.

## Features
- Answers questions about orders, payments, shipping, returns and support
- Understands differently worded questions (e.g. "track my package" and "track my order")
- Shows a polite fallback message when the question is not understood
- Simple chat interface built with Streamlit
- Terminal mode for quick testing

## Technologies Used
- Python
- NLTK (tokenization, stopword removal, lemmatization)
- scikit-learn (TF-IDF vectorizer, cosine similarity)
- Streamlit (chat UI)

## How It Works
1. A list of FAQ questions and answers is stored in `chatbot.py`.
2. Text is preprocessed with NLTK: converted to lowercase, tokenized, stopwords removed and words lemmatized.
3. FAQ questions are converted into TF-IDF vectors.
4. The user's question is converted into a vector in the same way.
5. Cosine similarity finds the FAQ that matches the user's question best, and its answer is shown.
6. If the similarity score is below the threshold (0.25), a fallback message is shown.

## Project Structure
```
Chatbot/
├── app.py            # Streamlit chat interface
├── chatbot.py        # FAQ data, preprocessing and matching logic
├── requirements.txt  # Required libraries
└── README.md
```

## How to Run
1. Install Python 3.9 or higher.
2. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
3. Run the chat interface:
   ```
   streamlit run app.py
   ```
4. Or test in the terminal:
   ```
   python chatbot.py
   ```

An internet connection is needed the first time to download the NLTK data.

## Screenshots

**Chat Interface**

![Chat interface](screenshot1.png)

**Answering Questions**

![Answering questions](screenshot2.png)

**Fallback Response**

![Fallback response](screenshot3.png)

## Customization
To use a different topic, edit the `FAQS` list in `chatbot.py` with your own questions and answers.

## Author
Amina Mai
