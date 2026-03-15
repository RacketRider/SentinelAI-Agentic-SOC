import random
import time

print("SentinelAI Prototype Simulation Started...\n")

events = [
    "Normal Login",
    "Failed Login Attempt",
    "Multiple Failed Logins",
    "Suspicious IP Access",
    "Privilege Escalation Attempt",
    "Lateral Movement Detected"
]

while True:
    event = random.choice(events)
    print(f"Log Event Detected: {event}")

    if event in ["Multiple Failed Logins", "Suspicious IP Access", "Privilege Escalation Attempt", "Lateral Movement Detected"]:
        print("⚠ Threat Detected!")
        print("Reasoning Agent analysing context...")
        time.sleep(1)
        action = random.choice(["Blocking IP", "Isolating Host", "Alerting Admin"])
        print(f"Response Action Executed: {action}")
    
    print("-"*40)
    time.sleep(2)
