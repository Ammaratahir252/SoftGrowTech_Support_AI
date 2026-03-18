
from flask import Flask, render_template, request, jsonify, session
import numpy as np
import random, re, string, threading, webbrowser, uuid
from datetime import datetime

# NLP / ML
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Import knowledge base
from intents import INTENTS

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
app.secret_key = "softgrowtech-chatbot-2024"

# ── Download NLTK data ────────────────────────────────────────────
print("[..] Downloading NLTK data...")
nltk.download("punkt",        quiet=True)
nltk.download("punkt_tab",    quiet=True)
nltk.download("stopwords",    quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
print("[OK] NLTK ready")

# ── NLP Tools ────────────────────────────────────────────────────
stemmer   = PorterStemmer()
stop_words = set(stopwords.words("english")) - {
    "not", "no", "what", "how", "when", "where", "why", "which", "who"
}

# ── Build training data from intents ─────────────────────────────
all_patterns  = []   # raw text patterns
all_tags      = []   # corresponding intent tags
tag_responses = {}   # tag → list of responses

for intent in INTENTS:
    tag = intent["tag"]
    tag_responses[tag] = intent["responses"]
    for pattern in intent["patterns"]:
        all_patterns.append(pattern)
        all_tags.append(tag)

# ── TF-IDF Vectorizer ────────────────────────────────────────────
# Fit on all patterns so we can compare user input against them
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words=None,       # we handle stop words ourselves
    lowercase=True,
    analyzer="word",
)
if all_patterns:
    X_patterns = vectorizer.fit_transform(all_patterns)
print(f"[OK] Vectorizer fitted on {len(all_patterns)} patterns across {len(tag_responses)} intents")

# ── Text preprocessing ────────────────────────────────────────────
def preprocess(text: str) -> str:
    """Lowercase, remove punctuation, stem words, remove stopwords."""
    text  = text.lower().strip()
    text  = re.sub(r"[%s]" % re.escape(string.punctuation), " ", text)
    try:
        tokens = word_tokenize(text)
    except Exception:
        tokens = text.split()
    tokens = [stemmer.stem(t) for t in tokens if t not in stop_words and len(t) > 1]
    return " ".join(tokens)

# ── Intent recognition ────────────────────────────────────────────
CONFIDENCE_THRESHOLD = 0.15   # minimum cosine similarity to accept a match

def predict_intent(user_input: str) -> dict:
    """
    1. Preprocess user input
    2. Vectorize with same TF-IDF
    3. Compute cosine similarity against all training patterns
    4. Return best matching intent and confidence score
    """
    cleaned = preprocess(user_input)
    if not cleaned.strip():
        return {"tag": "fallback", "confidence": 0.0}

    try:
        user_vec = vectorizer.transform([cleaned])
        sims     = cosine_similarity(user_vec, X_patterns).flatten()
        best_idx = int(np.argmax(sims))
        best_sim = float(sims[best_idx])

        if best_sim < CONFIDENCE_THRESHOLD:
            return {"tag": "fallback", "confidence": best_sim}

        return {"tag": all_tags[best_idx], "confidence": best_sim}
    except Exception:
        return {"tag": "fallback", "confidence": 0.0}

def get_response(tag: str) -> str:
    """Pick a random response for the given intent tag."""
    responses = tag_responses.get(tag, tag_responses["fallback"])
    return random.choice(responses)

# ── Conversation context ───────────────────────────────────────────
# Store per-session conversation history
conversations = {}   # session_id → list of messages

def get_session_id():
    if "sid" not in session:
        session["sid"] = str(uuid.uuid4())
    return session["sid"]

def get_history(sid):
    return conversations.get(sid, [])

def add_message(sid, role, text, tag=None, confidence=None):
    if sid not in conversations:
        conversations[sid] = []
    conversations[sid].append({
        "role":       role,        # "user" or "bot"
        "text":       text,
        "tag":        tag,
        "confidence": round(confidence * 100, 1) if confidence else None,
        "time":       datetime.now().strftime("%H:%M"),
    })

# ── Quick reply suggestions ────────────────────────────────────────
QUICK_REPLIES = [
    "Track my order",
    "Return an item",
    "Payment options",
    "Shipping info",
    "Reset password",
    "Contact support",
    "Current discounts",
    "Warranty claim",
]

def get_suggestions(tag: str) -> list:
    """Return contextual follow-up suggestions based on current intent."""
    mapping = {
        "greeting":     ["Track my order", "Return an item", "Shipping info", "Contact support"],
        "order_status": ["Return an item", "Payment options", "Contact support", "Shipping info"],
        "returns":      ["Refund status", "Payment options", "Contact support", "Warranty claim"],
        "payment":      ["Track my order", "Current discounts", "Contact support", "Shipping info"],
        "shipping":     ["Track my order", "Return an item", "Payment options", "Contact support"],
        "account":      ["Contact support", "Track my order", "Payment options", "Current discounts"],
        "product":      ["Shipping info", "Payment options", "Current discounts", "Return an item"],
        "discount":     ["Track my order", "Payment options", "Shipping info", "Return an item"],
        "contact":      ["Track my order", "Return an item", "Reset password", "Shipping info"],
        "warranty":     ["Return an item", "Contact support", "Track my order", "Payment options"],
        "thanks":       ["Track my order", "Return an item", "Shipping info", "Current discounts"],
        "goodbye":      [],
        "fallback":     ["Track my order", "Return an item", "Contact support", "Shipping info"],
    }
    return mapping.get(tag, QUICK_REPLIES[:4])

# ── Routes ────────────────────────────────────────────────────────
@app.route("/")
def index():
    sid = get_session_id()
    return render_template("index.html",
                           quick_replies=QUICK_REPLIES[:6],
                           history=get_history(sid))

@app.route("/api/chat", methods=["POST"])
def api_chat():
    sid        = get_session_id()
    data       = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input or len(user_input) < 1:
        return jsonify({"error": "Empty message"}), 400

    # Detect intent
    result     = predict_intent(user_input)
    tag        = result["tag"]
    confidence = result["confidence"]
    response   = get_response(tag)
    suggestions= get_suggestions(tag)

    # Save to history
    add_message(sid, "user", user_input)
    add_message(sid, "bot",  response, tag=tag, confidence=confidence)

    return jsonify({
        "response":    response,
        "tag":         tag,
        "confidence":  round(confidence * 100, 1),
        "suggestions": suggestions,
        "time":        datetime.now().strftime("%H:%M"),
    })

@app.route("/api/history")
def api_history():
    sid = get_session_id()
    return jsonify(get_history(sid))

@app.route("/api/clear", methods=["POST"])
def api_clear():
    sid = get_session_id()
    conversations[sid] = []
    return jsonify({"ok": True})

@app.route("/api/intents")
def api_intents():
    """Return all intent tags and pattern counts for the dashboard."""
    return jsonify([
        {
            "tag":           i["tag"],
            "pattern_count": len(i["patterns"]),
            "response_count":len(i["responses"]),
        }
        for i in INTENTS if i["tag"] != "fallback"
    ])

# ── Launch ────────────────────────────────────────────────────────
def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    print("\n" + "="*52)
    print("="*52)
    print(f"  Intents loaded:  {len(INTENTS)}")
    print(f"  Training patterns: {len(all_patterns)}")
    print(f"  http://127.0.0.1:5000")
    print("="*52 + "\n")
    threading.Timer(1.2, open_browser).start()
    app.run(debug=False, port=5000, use_reloader=False)
