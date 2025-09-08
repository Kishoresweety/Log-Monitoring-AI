"""Alert engine: receives log lines, applies rule-based detection, calls AI scorer, and prints/stores alerts."""
from fastapi import FastAPI, Request
from pydantic import BaseModel
import re
import uvicorn
from datetime import datetime
import requests

# AI scorer endpoint (local wrapper)
AI_SCORER_URL = "http://localhost:9100/score"

app = FastAPI()

class LogLine(BaseModel):
    log: str

# simple rules
RULES = [
    (re.compile(r"Failed login"), "FAILED_LOGIN"),
    (re.compile(r"possible exploit|ptrace|AVC avc: denied|malicious"), "EXPLOIT_ATTEMPT"),
    (re.compile(r"Accepted password"), "SUCCESSFUL_AUTH"),
]

ALERT_STORE = []

@app.post("/alert")
async def receive_log(payload: LogLine):
    line = payload.log
    matched = []
    for rx, name in RULES:
        if rx.search(line):
            matched.append(name)

    # Call AI scorer for anomaly probability
    try:
        r = requests.post(AI_SCORER_URL, json={"log": line}, timeout=1)
        score = r.json().get("score", 0.0)
    except Exception:
        score = 0.0

    # Build alert if rules matched or score high
    alert = None
    severity = "INFO"
    if matched or score > 0.6:
        severity = "HIGH" if score > 0.8 or "EXPLOIT_ATTEMPT" in matched else "MEDIUM"
        alert = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "log": line,
            "matched_rules": matched,
            "ai_score": score,
            "severity": severity,
        }
        ALERT_STORE.append(alert)
        # In production: push to SIEM, pager, or ticketing
        print("ALERT:", alert)
    else:
        # For debugging
        print("OK:", line[:120])

    return {"status": "received", "alert": alert}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
