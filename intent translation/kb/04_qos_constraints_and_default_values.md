# QoS Constraints and Default Values

## General Numeric Rules

- latency must be positive and expressed in ms.
- throughput must be positive and expressed in Mbps.
- reliability must be in the range `(0, 100]` and expressed as a percentage string.
- priority must be one of `"1"`, `"2"`, `"3"`, `"4"`, `"5"`.

## General Service-Level Ranges

| serviceType | latency range | throughput range | reliability range | typical priority |
|---|---:|---:|---:|---|
| URLLC | 1-10 ms | 20-200 Mbps | 99.90%-99.999% | 1 |
| eMBB | 15-40 ms | 100-2000 Mbps | 97%-99.7% | 2-3 |
| mMTC | 80-200 ms | 0.05-2.00 Mbps per device | 95%-99.3% | 3-5 |

## URLLC Defaults

Use URLLC when low latency and high reliability dominate.

Safe defaults when the user does not specify exact values:
```json
{
  "latency": "<10ms",
  "throughput": "50Mbps",
  "reliability": "99.90%",
  "priority": "1"
}
```

Stricter defaults:
- Remote surgery: `"<2ms"`, `"100Mbps"`, `"99.999%"`, priority `"1"`.
- V2X safety: `"<5ms"`, `"50Mbps"`, `"99.95%"`, priority `"1"`.
- Smart grid protection: `"<5ms"`, `"30Mbps"`, `"99.95%"`, priority `"1"`.
- Industrial robot control: `"<5ms"`, `"60Mbps"`, `"99.95%"`, priority `"1"`.
- Emergency drones: `"<5ms"`, `"80Mbps"`, `"99.95%"`, priority `"1"`.

Invalid or suspicious URLLC values:
- latency around 40-50 ms is too high for URLLC.
- reliability around 98% is too low for URLLC.
- throughput around 5 Mbps is lower than the expected URLLC scenario range in this dataset.

## eMBB Defaults

Use eMBB when high throughput, video, immersive broadband, or large downloads dominate.

Safe defaults:
```json
{
  "latency": "<30ms",
  "throughput": "500Mbps",
  "reliability": "98.5%",
  "priority": "2"
}
```

Stricter defaults:
- Holographic 8K volumetric video: `"<20ms"`, `"1500Mbps"`, `"99%"`, priority `"2"`.
- Stadium 4K event: `"<30ms"`, `"1000Mbps"`, `"98.5%"`, priority `"2"` or `"3"`.
- Airport hotspot: `"<30ms"`, `"800Mbps"`, `"98.5%"`, priority `"2"` or `"3"`.
- High-speed train cloud gaming and 4K: `"<30ms"`, `"800Mbps"`, `"98.5%"`, priority `"2"` or `"3"`.
- Campus AR-assisted teaching: `"<30ms"`, `"500Mbps"`, `"98.5%"`, priority `"2"`.

Invalid or suspicious eMBB values:
- throughput around 50 Mbps is too low for eMBB broadband scenarios.
- latency around 80 ms is too high for the eMBB scenarios in this dataset.
- eMBB with extremely low throughput should be flagged in semantic validation.

## mMTC Defaults

Use mMTC when massive sensors, meters, or low-power trackers dominate.

Safe defaults:
```json
{
  "latency": "<150ms",
  "throughput": "0.5Mbps",
  "reliability": "97%",
  "priority": "4"
}
```

Scenario-specific defaults:
- Smart parking: `"<150ms"`, `"0.3Mbps"`, `"97%"`, priority `"4"`.
- Smart agriculture: `"<150ms"`, `"0.5Mbps"`, `"97%"`, priority `"4"` or `"5"`.
- Smart metering: `"<150ms"`, `"0.3Mbps"`, `"97%"`, priority `"5"`.
- Environmental sensing: `"<150ms"`, `"0.3Mbps"`, `"97%"`, priority `"4"`.
- Logistics tracking: `"<150ms"`, `"0.3Mbps"`, `"97%"`, priority `"5"`.

Invalid or suspicious mMTC values:
- latency around 5-10 ms is much lower than the typical mMTC latency range and should be flagged.
- throughput around 500 Mbps is too high for massive low-rate devices.
- mMTC should not be used for broadband video or AR/VR scenarios.

## Boundary and Repair Notes

When a generated value violates the expected range:
- Do not change serviceType blindly.
- First check whether the natural-language scenario implies a different serviceType.
- If serviceType is correct but QoS values are wrong, repair QoS values to scenario-compatible ranges.
- If sliceType prefix conflicts with serviceType, repair sliceType to match serviceType and scenario.
