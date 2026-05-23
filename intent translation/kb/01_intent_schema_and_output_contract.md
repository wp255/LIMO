# Structured Network Intent Schema and Output Contract

## Core Task

Convert a user's natural-language service requirement into a structured network intent JSON for 6G RAN management and orchestration.

The JSON should be directly usable by the downstream policy-generation layer. It should express the service category, target network slice, QoS requirements, location, time, and priority.

## Required Fields

The following fields are required in the structured intent JSON:

```json
{
  "serviceType": "",
  "sliceType": "",
  "latency": "",
  "throughput": "",
  "region": "",
  "reliability": "",
  "priority": "",
  "time": ""
}
```

## Field Definitions

### serviceType
Allowed values:
- `URLLC`: ultra-reliable and low-latency communication.
- `eMBB`: enhanced mobile broadband.
- `mMTC`: massive machine-type communication.

### sliceType
The slice type must be consistent with serviceType:
- URLLC slice types should start with `URLLC-`.
- eMBB slice types should start with `eMBB-`.
- mMTC slice types should start with `mMTC-`.

### latency
Latency must be a string containing a numeric value and the unit `ms`.
Accepted examples:
- `"<2ms"`
- `"<10ms"`
- `"29ms"`
- `"<181ms"`

### throughput
Throughput must be a string containing a numeric value and the unit `Mbps`.
Accepted examples:
- `"70Mbps"`
- `"108Mbps"`
- `"650Mbps"`
- `"0.21Mbps"`

Do not output throughput as a bare number such as `325.0`.

### region
Region is the city or deployment area extracted from the user request.
Examples:
- `"Beijing"`
- `"Shanghai"`
- `"Xi'an"`
- `"Singapore"`
- `"Tokyo"`

### reliability
Reliability must be a string ending with `%`.
Accepted examples:
- `"99.976%"`
- `"98.76%"`
- `"96.88%"`

Do not output reliability as `"99.976"` or `99.976`.

### priority
Priority must be a string from `"1"` to `"5"`.
- `"1"`: highest priority; mission-critical, safety-critical, or real-time control.
- `"2"`: high priority; immersive, high-bandwidth, or interactive broadband.
- `"3"`: medium priority.
- `"4"`: low-to-medium priority; periodic sensing or monitoring.
- `"5"`: low priority; delay-tolerant massive IoT.

### time
Time should preserve the date or time expression from the user's request.
Preferred format:
- `"YYYY-MM-DD"`

Examples:
- `"2025-04-20"`
- `"2025-03-11"`
- `"2025-06-20"`

## Optional Fields

Optional fields may be added if useful:
- `application`: application name, e.g., `"remote surgery"`, `"4K live streaming"`.
- `userCount`: number of users or devices.
- `deviceType`: device type, e.g., `"robotic arms"`, `"sensors"`, `"AR headsets"`.
- `mobility`: mobility property, e.g., `"high-speed train"`, `"highway fleet"`.
- `trafficPattern`: e.g., `"periodic small-packet upload"`, `"8K video broadcast"`.
- `explanation`: short reason for the mapping.

## JSON Output Contract

When the task is intent translation:
- Output valid JSON only.
- Do not output Markdown.
- Do not output explanations outside the JSON.
- If a field is not explicitly stated but can be safely inferred from the scenario, infer it and mention the inference in `explanation`.
- Do not invent a region or date if not present in the user intent. If absent, set the field to `""` and mention it in `explanation`.

## Minimal Valid Example

```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<2ms",
  "throughput": "108Mbps",
  "region": "Beijing",
  "reliability": "99.976%",
  "priority": "1",
  "time": "2025-04-20",
  "application": "remote surgery",
  "explanation": "The intent describes robotic-arm remote surgery with extremely stable connection, very low latency, and almost no packet loss. It is mapped to URLLC."
}
```
