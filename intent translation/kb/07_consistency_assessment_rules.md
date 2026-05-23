# Consistency Assessment Rules

Consistency assessment checks cross-field logical contradictions inside the structured JSON.

## Primary Consistency Checks

### serviceType and sliceType Prefix Consistency

The prefix of sliceType must match serviceType:
- serviceType `URLLC` → sliceType should start with `URLLC-`.
- serviceType `eMBB` → sliceType should start with `eMBB-`.
- serviceType `mMTC` → sliceType should start with `mMTC-`.

Examples:
- serviceType `mMTC` + sliceType `URLLC-RemoteSurgery`: inconsistent.
- serviceType `eMBB` + sliceType `mMTC-EnvironmentalSensing`: inconsistent.
- serviceType `URLLC` + sliceType `eMBB-Stadium4KEvent`: inconsistent.

Recommended message:
`sliceType '<sliceType>' is not consistent with serviceType '<serviceType>'.`

### serviceType and Latency Consistency

URLLC:
- Latency around 40-50 ms is too high for URLLC.
- Message: `serviceType 'URLLC' but latency around 40.0 ms is too high for URLLC.`

mMTC:
- Latency around 5-10 ms is much lower than the typical mMTC latency range.
- Message: `serviceType 'mMTC' but latency around 10.0 ms is much lower than the typical 80–200 ms range.`

eMBB:
- eMBB normally uses 15-40 ms in this dataset.
- Very high eMBB latency should be handled mainly in semantic validation unless it also creates a logical contradiction.

### serviceType and Throughput Consistency

mMTC:
- Throughput around 500 Mbps is too high for massive low-rate devices.
- Message: `serviceType 'mMTC' but throughput about 500.00 Mbps is too high for massive low-rate devices.`

eMBB:
- Very low throughput, e.g., 50 Mbps, is usually a semantic QoS issue for eMBB.
- It does not always need a consistency message unless cross-field contradiction is obvious.

URLLC:
- Throughput around 5 Mbps may be semantically too low for URLLC in this dataset, but not always a cross-field contradiction.

## Combined Consistency Messages

When multiple contradictions exist, concatenate them in one message.

Example:
`sliceType 'eMBB-HighSpeedTrain' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 24.0 ms is much lower than the typical 80–200 ms range. serviceType 'mMTC' but throughput about 545.00 Mbps is too high for massive low-rate devices.`

## When No Consistency Issue Exists

If serviceType, sliceType prefix, latency, and throughput are mutually compatible, output:
`No issue detected.`

Do not repeat semantic issues as consistency issues unless they indicate an internal contradiction.
For example:
- eMBB throughput 50 Mbps is a semantic QoS range issue but may not require consistency issue.
- URLLC throughput 5 Mbps is a semantic issue but may not require consistency issue.
