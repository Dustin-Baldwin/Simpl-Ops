# Event Lifecycle Diagram

```mermaid
stateDiagram-v2
    [*] --> Received
    Received --> Normalized
    Normalized --> Queued
    Queued --> Processing
    Processing --> Completed
    Processing --> Failed
    Failed --> Queued: retry if safe
    Completed --> Published
    Published --> [*]
```
