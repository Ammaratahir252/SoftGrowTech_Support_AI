# SupportAI — AI Chatbot for Customer Support

**SoftGrowTech — AI Internship Final Project | Project 2**

---

## Project Requirements Covered
- [x] AI chatbot that answers user questions
- [x] Provides automated responses
- [x] Processes user input using NLP
- [x] Responds with relevant information

---

## Features
- NLP-powered intent recognition (TF-IDF + Cosine Similarity)
- 12 customer support intents (orders, returns, payments, shipping, etc.)
- Contextual quick reply suggestions after each response
- Real-time confidence scoring displayed in the UI
- Session analytics (messages, intents hit, avg confidence)
- Typing indicator for natural feel
- Topic shortcuts in the left panel
- Clear chat functionality

---

## Project Structure
```
chatbot_app/
├── app.py           # Flask backend + NLP engine
├── intents.py       # Knowledge base (patterns + responses)
├── requirements.txt
├── README.md
└── templates/
    └── index.html   # Chat interface
```

---

## Setup & Run
```bash
pip install -r requirements.txt
python app.py
```
Browser opens automatically at `http://127.0.0.1:5000`

---

## How It Works
```
User types message
      ↓
Text preprocessing (lowercase, stem, remove stopwords)
      ↓
TF-IDF vectorization
      ↓
Cosine similarity against all training patterns
      ↓
Best matching intent selected (if confidence > 15%)
      ↓
Random response selected from matched intent
      ↓
Contextual follow-up suggestions shown
```

## Supported Intents
| Intent | Description |
|--------|-------------|
| greeting | Hello, hi, hey |
| goodbye | Bye, see you, done |
| thanks | Thank you, appreciate it |
| order_status | Track order, delivery status |
| returns | Return policy, refund, exchange |
| payment | Payment methods, billing issues |
| shipping | Delivery time, shipping cost |
| account | Password reset, login issues |
| product | Product info, availability |
| discount | Promo codes, offers, coupons |
| contact | Speak to human, escalate |
| warranty | Warranty claim, defective product |
