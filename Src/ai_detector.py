"""AI detector service: lightweight Flask app that returns anomaly score for a log line.
In production this would call a Mojo model; here we use a simple sklearn-based vectorizer,
or a placeholder for Mojo runtime call."""
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
import threading

app = Flask(__name__)

# Small offline model for demo (trained on very small sample)
SAMPLE = [
    "kernel link up",
    "Accepted password for user",
    "session opened for user root",
    "Failed login for user admin invalid password",
    "possible exploit attempt ptrace detected",
    "AVC avc: denied",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(SAMPLE)
clf = IsolationForest(contamination=0.2, random_state=42)
clf.fit(X.toarray())

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json() or {}
    log = data.get('log', '')
    v = vectorizer.transform([log]).toarray()
    s = clf.decision_function(v)[0]  # higher = more normal
    # Convert to anomaly probability (0..1) where 1 => most anomalous
    prob_anom = max(0.0, min(1.0, (0.5 - s)))
    return jsonify({"score": round(prob_anom, 3)})

if __name__ == '__main__':
    # Run on port 9100
    app.run(host='0.0.0.0', port=9100)
