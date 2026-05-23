# Bridge from Intent Translation to Policy Generation

After a structured intent passes validation, it can be passed to the policy-generation layer.

## Intent-to-Optimization Mapping

### URLLC
Primary objective:
- minimize latency
- maximize reliability
- minimize packet loss
- guarantee high priority resource scheduling

Typical constraints:
- latency <= specified threshold
- reliability >= specified threshold
- packet loss <= target threshold if available
- priority = 1
- PRB allocation lower bound for safety-critical traffic

Typical decision variables:
- PRB allocation
- slice scheduling weight
- transmission power
- modulation and coding scheme
- admission control
- RAN slice priority

Suggested algorithms:
- PPO-Clip for dynamic high-dimensional scheduling
- MILP for small-scale bounded combinatorial cases
- heuristic fallback for fast safety-net rollback

### eMBB
Primary objective:
- maximize throughput
- guarantee sufficient broadband capacity
- control latency within acceptable range

Typical constraints:
- throughput >= target
- latency <= target
- PRB budget
- fairness among users

Typical decision variables:
- PRB allocation
- scheduling weight
- user grouping
- MCS level
- traffic steering

Suggested algorithms:
- Proportional Fair
- PPO/DDPG/TD3 for dynamic scheduling
- MILP/LP for small-scale deterministic allocation

### mMTC
Primary objective:
- support massive device connectivity
- reduce per-device resource usage
- maintain periodic reporting reliability
- minimize signaling congestion

Typical constraints:
- device access capacity
- per-device throughput
- latency tolerance
- energy or low-power preference if available

Typical decision variables:
- random access configuration
- grant scheduling period
- PRB allocation for IoT slice
- aggregation/grouping interval
- access barring parameters

Suggested algorithms:
- heuristic/group-based scheduling
- LP/MILP for resource partitioning
- lightweight RL if dynamics are strong

## Policy Generation Prompt Input

Recommended policy-generation input should contain:
```json
{
  "validatedIntent": {},
  "networkContext": {
    "totalPRBs": 52,
    "currentPRBUsage": "",
    "activeSlices": [],
    "slaStatus": {}
  }
}
```

## Acceptance Criteria

A policy can be accepted when:
- all QoS targets are satisfied;
- SLA satisfaction remains above target over consecutive decision cycles;
- canary deployment does not trigger anomaly alarms;
- rollback rate remains below the preset safety threshold.
