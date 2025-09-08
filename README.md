#SOC Entry-Level Project — Log Monitoring & AI Security Layer

This project covers the basics of log monitoring, alert detection, and anomaly detection with AI. A Mojo design stub is also included to highlight awareness of modern kernel-level threats (like Pegasus).


---

🎯 What This Project Shows

Real-time log monitoring

Rule-based detection for common issues (failed logins, exploit attempts, kernel alerts)

AI-based anomaly scoring for unusual patterns

Conceptual use of Mojo for future kernel-level defense


---

⚙️ How It Works

1. log_generator.py — creates log lines similar to real syslogs.


2. log_collector.py — tails the log file and sends data to the alert engine.


3. alert_engine.py — applies:

Rules (e.g., detect failed login, exploit attempt)

AI anomaly scores (from ai_detector.py)

Creates alerts with severity (INFO, MEDIUM, HIGH)



4. ai_detector.py — a small Python service that simulates anomaly detection. In production, this would be replaced or extended with a Mojo model.




---

🚀 How to Run

# Setup environment
python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run each service in a separate terminal
python src/ai_detector.py
python src/alert_engine.py
python src/log_generator.py
python src/log_collector.py

👉 The alert_engine.py console will show alerts with rules matched, anomaly scores, and severity.


---

🔒 Why This Matters

Shows basic SOC skills: log collection, detection, alerting, and triage.

Adds awareness of AI-assisted detection.

Demonstrates forward-thinking with Mojo design stub for kernel defense.



---

📘 Helpful Docs

PROCESS.md: overview of workflow and decisions

DEPLOY.md: step-by-step setup



---

📜 License

MIT License © 2025 Kishore

