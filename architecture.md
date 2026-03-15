# SentinelAI Architecture

## System Flow

1. Log Ingestion Layer  
Collects logs from network devices, servers, authentication systems.

2. Anomaly Detection Engine  
Uses ML models like Isolation Forest or LSTM to detect abnormal patterns.

3. Reasoning Agent  
Uses LLM to analyze threat context and decide severity.

4. Memory Layer  
Vector database storing previous incidents for better decision-making.

5. Response Engine  
Executes actions:
- Block IP
- Isolate host
- Generate alerts

6. Dashboard  
Displays incident summaries and system status.
