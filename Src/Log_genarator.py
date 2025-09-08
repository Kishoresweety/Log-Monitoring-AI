"""Simple log generator: appends sample log lines to sample_logs/syslogs.log"""
import time
import random
from datetime import datetime

LOG_FILE = "../sample_logs/syslogs.log"

TEMPLATES = [
    "{ts} HOST1 kernel: [INFO] eth0 link up",
    "{ts} HOST2 sshd[1234]: Accepted password for user root from 10.0.0.{oct}",
    "{ts} HOST3 sudo: pam_unix(sudo:session): session opened for user root",
    "{ts} HOST1 app[444]: Failed login for user 'admin' - invalid password",
    "{ts} HOST2 kernel: [CRITICAL] possible exploit attempt ptrace detected for pid {pid}",
    "{ts} HOST4 audit: AVC avc: denied { read } for pid={pid} comm=\"malicious\" scontext=unconfined_u:unconfined_r:unconfined_t:s0 tcontext=system_u:object_r:etc_t:s0",
]


def random_line():
    ts = datetime.utcnow().isoformat() + "Z"
    return random.choice(TEMPLATES).format(ts=ts, oct=random.randint(2,254), pid=random.randint(1000,9999))


def main():
    print("Starting log generator — writing to:", LOG_FILE)
    with open(LOG_FILE, "a") as f:
        for _ in range(200):
            line = random_line()
            f.write(line + "\n")
            f.flush()
            time.sleep(random.uniform(0.01, 0.2))

if __name__ == "__main__":
    main()
