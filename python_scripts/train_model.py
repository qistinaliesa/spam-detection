"""
train_model.py — Train a spam detector using scikit-learn
Run once: python train_model.py
This saves model.pkl and vectorizer.pkl to the current directory.
"""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import urllib.request
import os
import zipfile

# ─────────────────────────────────────────────
# 1. Download the SMS Spam Collection dataset
# ─────────────────────────────────────────────
DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
ZIP_PATH = "smsspamcollection.zip"
DATA_FILE = "SMSSpamCollection"

if not os.path.exists(DATA_FILE):
    print("📥 Downloading dataset...")
    urllib.request.urlretrieve(DATASET_URL, ZIP_PATH)
    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall(".")
    os.remove(ZIP_PATH)
    print("✅ Dataset downloaded.")
else:
    print("✅ Dataset already exists.")

# ─────────────────────────────────────────────
# 2. Load & explore the data
# ─────────────────────────────────────────────
df = pd.read_csv(DATA_FILE, sep="\t", header=None, names=["label", "message"])
print(f"\n📊 Dataset shape: {df.shape}")
print(df["label"].value_counts())

# ─────────────────────────────────────────────
# 3. Preprocess: encode labels
# ─────────────────────────────────────────────
df["label_enc"] = df["label"].map({"ham": 0, "spam": 1})

X = df["message"]
y = df["label_enc"]

# ─────────────────────────────────────────────
# 4. Split into train / test sets
# ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ─────────────────────────────────────────────
# 5. Vectorize text with TF-IDF
# ─────────────────────────────────────────────
vectorizer = TfidfVectorizer(
    stop_words="english",   # remove common English words
    max_features=5000,      # keep top 5000 terms
    ngram_range=(1, 2),     # use unigrams + bigrams
)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)

# ─────────────────────────────────────────────
# 6. Train Multinomial Naive Bayes classifier
# ─────────────────────────────────────────────
model = MultinomialNB(alpha=0.1)
model.fit(X_train_tfidf, y_train)

# ─────────────────────────────────────────────
# 7. Evaluate the model
# ─────────────────────────────────────────────
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n🎯 Accuracy: {accuracy * 100:.2f}%")
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))

# ─────────────────────────────────────────────
# 8. Save model and vectorizer
# ─────────────────────────────────────────────
joblib.dump(model,      "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("\n💾 Saved: model.pkl and vectorizer.pkl")
print("🚀 Ready to run app.py!")
