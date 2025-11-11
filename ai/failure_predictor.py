import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import requests
import os
import json

# --- Slack Webhook ---
SLACK_WEBHOOK = "https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"  # replace

def send_slack(message):
    requests.post(SLACK_WEBHOOK, json={"text": message})

# --- Simulated Historical Build Data ---
data = {
    "build_time": [5, 8, 15, 20, 6, 7, 25, 30],
    "test_failures": [0, 1, 3, 5, 0, 0, 6, 4],
    "changes": [10, 50, 100, 200, 15, 20, 300, 250],
    "status": [1, 1, 0, 0, 1, 1, 0, 0]  # 1=success, 0=failure
}

df = pd.DataFrame(data)

X = df[["build_time", "test_failures", "changes"]]
y = df["status"]

model = RandomForestClassifier()
model.fit(X, y)

# --- Simulate Current Build Metrics ---
current_build = np.array([[12, 2, 120]])  # (time, failures, changes)
prediction = model.predict(current_build)[0]

if prediction == 0:
    msg = "⚠️ *AI Prediction:* This build has a high chance of failure. Check tests carefully."
    print(msg)
    send_slack(msg)
else:
    msg = "✅ *AI Prediction:* Build looks healthy."
    print(msg)
    send_slack(msg)
