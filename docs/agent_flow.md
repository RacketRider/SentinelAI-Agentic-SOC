# SentinelAI Agent Workflow

SentinelAI follows a multi-agent architecture where each agent performs a specialized task.

## Agents

### Log Analysis Agent
- Parses incoming system and network logs
- Identifies suspicious patterns

### Threat Intelligence Agent
- Matches events with known attack signatures
- Provides contextual risk scoring

### Reasoning Agent
- Uses LLM reasoning to determine threat severity
- Plans mitigation strategy

### Memory Agent
- Stores previous incident embeddings
- Improves future decision confidence

### Execution Agent
- Executes automated responses
  - Block malicious IP
  - Disable compromised account
  - Isolate affected endpoint

### Reporting Agent
- Generates incident summary
- Updates monitoring dashboard
