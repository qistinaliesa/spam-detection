"""
app.py — Flask backend for the Spam Detector web app
Run: python app.py  (make sure you've run train_model.py first)
"""

from flask import Flask, request, jsonify, render_template
import joblib
import os
import re

app = Flask(__name__)

# ─────────────────────────────────────────────
# Load the trained model and vectorizer
# ─────────────────────────────────────────────
MODEL_PATH      = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError(
        "❌ model.pkl or vectorizer.pkl not found. "
        "Please run: python train_model.py"
    )

model      = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print("✅ Model and vectorizer loaded.")

# ─────────────────────────────────────────────
# Helper: preprocess input text
# ─────────────────────────────────────────────
def preprocess(text: str) -> str:
    text = text.lower()                         # lowercase
    text = re.sub(r"http\S+|www\S+", " url ", text)  # replace URLs
    text = re.sub(r"\d+", " num ", text)        # replace numbers
    text = re.sub(r"[^\w\s]", " ", text)        # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()    # collapse whitespace
    return text

# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main page."""
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    POST /predict
    Body (JSON): { "message": "Your text here" }
    Returns:     { "label": "spam"|"ham", "confidence": 0.0–1.0,
                   "spam_prob": float, "ham_prob": float }
    """
    data = request.get_json(force=True)
    raw_message = data.get("message", "").strip()

    if not raw_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    # Preprocess → vectorize → predict
    clean   = preprocess(raw_message)
    tfidf   = vectorizer.transform([clean])
    probs   = model.predict_proba(tfidf)[0]   # [ham_prob, spam_prob]
    pred    = model.predict(tfidf)[0]         # 0=ham, 1=spam

    label       = "spam" if pred == 1 else "ham"
    spam_prob   = float(probs[1])
    ham_prob    = float(probs[0])
    confidence  = max(spam_prob, ham_prob)

    return jsonify({
        "label":      label,
        "confidence": round(confidence * 100, 2),
        "spam_prob":  round(spam_prob * 100, 2),
        "ham_prob":   round(ham_prob * 100, 2),
    })


@app.route("/examples", methods=["GET"])
def examples():
    """Return a few sample messages for the UI demo."""
    samples = [
        {"text": "Congratulations! You've won a FREE iPhone. Click here to claim now!", "expected": "spam"},
        {"text": "Hey, are we still on for lunch tomorrow at noon?",                    "expected": "ham"},
        {"text": "URGENT: Your bank account has been suspended. Verify now at bit.ly/xyzbank", "expected": "spam"},
        {"text": "Don't forget to pick up milk on your way home.",                      "expected": "ham"},
        {"text": "You've been selected for a $1000 Walmart gift card! Call 1-800-SPAM.", "expected": "spam"},
        {"text": "I'll be 10 minutes late to the meeting, go ahead and start without me.", "expected": "ham"},
    ]
    return jsonify(samples)


# ─────────────────────────────────────────────
# Run
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=8000)
