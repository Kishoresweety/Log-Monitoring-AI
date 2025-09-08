1) Problem statement
   - Detect suspicious activity in host logs (failed logins, ptrace/syscall anomalies, AVC denials)
   - Provide explainable alerts (which rule matched + anomaly score)
   - Add an AI layer (Mojo design) for kernel-level exploit detection and anomaly scoring

2) Architecture
   - Log generator -> Log file
   - Log collector (tailing) -> Alert Engine (FastAPI)
   - Alert Engine applies rules and calls AI scorer (python or Mojo service)
   - Alerts stored locally and printed; in production would push to SIEM

3) Why this setup
   - Demonstrates understanding of: log ingestion, detection engineering, alert triage,
     model-assisted scoring, and security considerations for kernel-level threats.

4) How to demo without a laptop
   - Host the repository on GitHub (this repo)
   - In an interview, walk through `docs/PROCESS.md`, open `src/alert_engine.py`, explain
     rule priorities, show sample alerts from `sample_logs/syslogs.log` and explain AI
     model design (ai_model.mojo).
   - Optionally run code in cloud IDE (GitHub Codespaces) — explain costs & steps in DEPLOY.md

5) Threat model & limitations
   - The AI model should never be the sole authority on a signal; combine with rules.
   - Kernel-level defense requires kernel hooks and secure telemetry; this project
     simulates detection via logs and signatures.

6) Ethical considerations
   - The project is defensive only; do not include or publish real exploit payloads.
