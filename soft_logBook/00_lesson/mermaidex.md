```mermaid
graph TD;
  A[Start] --> B{Is it OK?};
  B -->|Yes| C[Continue];
  B -->|No| D[Stop];
