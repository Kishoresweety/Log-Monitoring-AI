1. Create a Python 3.11+ virtualenv.
2. pip install -r requirements.txt
3. In separate terminals run:
   - python src/ai_detector.py    # runs on port 9100
   - python src/alert_engine.py   # runs on port 9000
   - python src/log_generator.py  # generates sample lines
   - python src/log_collector.py  # tails sample_logs/syslogs.log and posts to alert engine

Explanation: log_generator writes to sample_logs; log_collector tails and posts each
line to alert_engine; alert_engine runs rules and queries AI scorer at /score.

Demo tips: Show sample alerts in alert_engine console; show stored alerts in memory
(ALERT_STORE) and explain how you'd forward to PagerDuty/Slack/SIEM.
