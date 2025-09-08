"""Watches a log file (tail -f style) and forwards lines to alert engine"""
import time
import os
import requests

LOG_FILE = "../sample_logs/syslogs.log"
ALERT_ENGINE_URL = "http://localhost:9000/alert"


def follow(file):
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line.strip()


def main():
    print("Starting log collector — sending to", ALERT_ENGINE_URL)
    with open(LOG_FILE, "r") as f:
        loglines = follow(f)
        for line in loglines:
            payload = {"log": line}
            try:
                requests.post(ALERT_ENGINE_URL, json=payload, timeout=1)
            except Exception as e:
                # In production, buffer and retry
                print("Warning: failed to send to alert engine:", e)

if __name__ == "__main__":
    main()
