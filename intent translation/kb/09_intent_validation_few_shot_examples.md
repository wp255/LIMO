# Intent Validation Few-Shot Examples

These examples include missing fields, format errors, semantic mismatches, QoS range violations, and serviceType-sliceType inconsistencies.

## Validation Example 1

User intent:
A remote surgery operation is scheduled in a hospital in Beijing on 2025-04-20. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<2ms",
  "throughput": "108Mbps",
  "region": "Beijing",
  "reliability": "99.976%",
  "time": "2025-04-20"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'priority'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 2

User intent:
On 2025-03-11, a global holographic townhall in Tianjin will broadcast 8K volumetric video to remote offices, with participants wearing AR headsets for immersive telepresence.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HolographicTownhall",
  "latency": "<80ms",
  "throughput": "881Mbps",
  "region": "Tianjin",
  "reliability": "97.61%",
  "priority": "2",
  "time": "2025-03-11"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this eMBB scenario, latency should be in the range 15–40 ms, but got about 80.0 ms."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 3

User intent:
A high-speed train passing through Tianjin on 2025-01-29 should support uninterrupted cloud gaming and 4K video for passengers along the route.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HighSpeedTrain",
  "latency": "<27ms",
  "throughput": "50Mbps",
  "region": "Tianjin",
  "reliability": "97.52%",
  "priority": "2",
  "time": "2025-01-29"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this eMBB scenario, throughput should be in the range 100–2000 Mbps, but got about 50.0 Mbps."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 4

User intent:
A smart factory in Nanjing will coordinate robot arms and AGVs on 2025-03-10. Control loops require sub-10ms delay and virtually no packet loss to avoid collisions and production errors.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-IndustrialRobot",
  "latency": "<3ms",
  "throughput": "5Mbps",
  "region": "Nanjing",
  "reliability": "99.910",
  "priority": "1",
  "time": "2025-03-10"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '99.910'."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, throughput should be in the range 20–200 Mbps, but got about 5.0 Mbps."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 5

User intent:
An urban smart parking system in Dubai will deploy ground sensors from 2025-03-07, with devices occasionally uploading occupancy information.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartParking",
  "latency": "<158ms",
  "throughput": "500Mbps",
  "region": "Dubai",
  "reliability": "98.76%",
  "priority": "4",
  "time": "2025-03-07"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, per-device throughput should be in the range 0.05–2.00 Mbps, but got about 500.00 Mbps."
  },
  "consistency_check": {
    "message": "serviceType 'mMTC' but throughput about 500.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 6

User intent:
Starting from 2025-03-23, protection signals in the power grid of Singapore will be carried over the 6G network. Fault detection and isolation messages require ultra-fast and reliable delivery.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-SmartGridProtection",
  "latency": "<50ms",
  "throughput": "32Mbps",
  "region": "Singapore",
  "reliability": "98%",
  "priority": "1",
  "time": "2025-03-23"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, latency should be in the range 1–10 ms, but got about 50.0 ms. For this URLLC scenario, reliability should be in the range 99.90%–99.999%, but got about 98.000%."
  },
  "consistency_check": {
    "message": "serviceType 'URLLC' but latency around 50.0 ms is too high for URLLC."
  }
}
```

## Validation Example 7

User intent:
An industrial park in Nanjing plans dense deployment of environmental sensors on 2025-05-23 to monitor air quality, temperature and humidity.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "eMBB-InconsistentSlice",
  "latency": "<111ms",
  "throughput": "0.63Mbps",
  "region": "Nanjing",
  "reliability": "98.19%",
  "priority": "5",
  "time": "2025-05-23"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-InconsistentSlice' is not consistent with serviceType 'mMTC'."
  }
}
```

## Validation Example 8

User intent:
A smart factory in Bangkok will coordinate robot arms and AGVs on 2025-05-09. Control loops require sub-10ms delay and virtually no packet loss to avoid collisions and production errors.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-IndustrialRobot",
  "latency": "<7ms",
  "throughput": "5Mbps",
  "region": "Bangkok",
  "reliability": "99.909%",
  "priority": "1",
  "time": "2025-05-09"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, throughput should be in the range 20–200 Mbps, but got about 5.0 Mbps."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 9

User intent:
An international airport in Chengdu plans to deploy high-capacity 6G hotspots in departure halls on 2025-05-15, serving roaming users with HD video streaming and large file downloads.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-AirportHotspot",
  "latency": "<36ms",
  "throughput": "859Mbps",
  "region": "Chengdu",
  "reliability": "99.68",
  "priority": "3",
  "time": "2025-05-15"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '99.68'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 10

User intent:
A large sports event in Beijing on 2025-02-08 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<32ms",
  "throughput": "1408Mbps",
  "region": "Beijing",
  "reliability": "99.60",
  "priority": "3",
  "time": "2025-02-08"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '99.60'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 11

User intent:
A smart agriculture project near Beijing from 2025-04-08 will connect soil moisture sensors and climate stations across large fields.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-Agriculture",
  "latency": "<10ms",
  "throughput": "0.27Mbps",
  "region": "Beijing",
  "reliability": "95.72%",
  "priority": "3",
  "time": "2025-04-08"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, latency should be in the range 80–200 ms, but got about 10.0 ms."
  },
  "consistency_check": {
    "message": "serviceType 'mMTC' but latency around 10.0 ms is much lower than the typical 80–200 ms range."
  }
}
```

## Validation Example 12

User intent:
On 2025-01-11, an autonomous driving test on the expressway near Tokyo will involve a fleet of self-driving trucks exchanging cooperative awareness messages. The service must guarantee millisecond-level latency and extremely high reliability for safety.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "URLLC-V2XHighway",
  "latency": "1ms",
  "throughput": "79Mbps",
  "region": "Tokyo",
  "reliability": "99.921%",
  "priority": "1",
  "time": "2025-01-11"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'URLLC' for this intent, but got 'eMBB'."
  },
  "consistency_check": {
    "message": "sliceType 'URLLC-V2XHighway' is not consistent with serviceType 'eMBB'."
  }
}
```

## Validation Example 13

User intent:
A high-speed train passing through Tokyo on 2025-02-01 should support uninterrupted cloud gaming and 4K video for passengers along the route.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "eMBB-HighSpeedTrain",
  "latency": "<24ms",
  "throughput": "545Mbps",
  "region": "Tokyo",
  "reliability": "97.16%",
  "priority": "3"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'time'."
  },
  "semantic_check": {
    "message": "Expected serviceType 'eMBB' for this intent, but got 'mMTC'."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-HighSpeedTrain' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 24.0 ms is much lower than the typical 80–200 ms range. serviceType 'mMTC' but throughput about 545.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 14

User intent:
An industrial park in Shenzhen plans dense deployment of environmental sensors on 2025-01-13 to monitor air quality, temperature and humidity.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<101ms",
  "throughput": "0.41Mbps",
  "region": "Shenzhen",
  "reliability": "95.89%",
  "priority": "4"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'time'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 15

User intent:
An industrial park in Wuhan plans dense deployment of environmental sensors on 2025-01-07 to monitor air quality, temperature and humidity.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<125ms",
  "throughput": "0.67Mbps",
  "region": "Wuhan",
  "reliability": "97.50%",
  "priority": "4",
  "time": "2025-01-07"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'mMTC' for this intent, but got 'eMBB'."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-EnvironmentalSensing' is not consistent with serviceType 'eMBB'."
  }
}
```

## Validation Example 16

User intent:
A remote surgery operation is scheduled in a hospital in Guangzhou on 2025-04-27. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<40ms",
  "throughput": "107Mbps",
  "region": "Guangzhou",
  "reliability": "99.970%",
  "priority": "1",
  "time": "2025-04-27"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, latency should be in the range 1–10 ms, but got about 40.0 ms."
  },
  "consistency_check": {
    "message": "serviceType 'URLLC' but latency around 40.0 ms is too high for URLLC."
  }
}
```

## Validation Example 17

User intent:
A university campus in Beijing will upgrade to 6G on 2025-05-25 to support massive online classes, interactive labs and AR-assisted teaching for students.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-CampusBroadband",
  "latency": "<23ms",
  "throughput": 325.0,
  "region": "Beijing",
  "reliability": "98.09%",
  "priority": "2",
  "time": "2025-05-25"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '325.0'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 18

User intent:
A university campus in Shanghai will upgrade to 6G on 2025-04-07 to support massive online classes, interactive labs and AR-assisted teaching for students.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-CampusBroadband",
  "latency": "<38ms",
  "throughput": "657Mbps",
  "region": "Shanghai",
  "reliability": "98.25",
  "priority": "2",
  "time": "2025-04-07"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '98.25'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 19

User intent:
During an emergency response drill in London on 2025-01-04, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<4ms",
  "throughput": "43Mbps",
  "reliability": "99.907%",
  "priority": "1",
  "time": "2025-01-04"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'region'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 20

User intent:
A large sports event in Bangkok on 2025-02-20 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<28ms",
  "throughput": "1345Mbps",
  "region": "Bangkok",
  "reliability": "97.12%",
  "priority": "2",
  "time": "2025-02-20"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'eMBB' for this intent, but got 'mMTC'."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-Stadium4KEvent' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 28.0 ms is much lower than the typical 80–200 ms range. serviceType 'mMTC' but throughput about 1345.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 21

User intent:
An international airport in Xi'an plans to deploy high-capacity 6G hotspots in departure halls on 2025-03-12, serving roaming users with HD video streaming and large file downloads.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-AirportHotspot",
  "latency": "<28ms",
  "throughput": "875Mbps",
  "region": "Xi'an",
  "reliability": "98.90",
  "priority": "3",
  "time": "2025-03-12"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '98.90'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 22

User intent:
During an emergency response drill in Seoul on 2025-01-31, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<50ms",
  "throughput": "48Mbps",
  "region": "Seoul",
  "reliability": "98",
  "priority": "1",
  "time": "2025-01-31"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '98'."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, latency should be in the range 1–10 ms, but got about 50.0 ms. For this URLLC scenario, reliability should be in the range 99.90%–99.999%, but got about 98.000%."
  },
  "consistency_check": {
    "message": "serviceType 'URLLC' but latency around 50.0 ms is too high for URLLC."
  }
}
```

## Validation Example 23

User intent:
A logistics company in Guangzhou will attach low-power trackers to thousands of containers and pallets from 2025-02-08, sending infrequent location updates.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-LogisticsTracking",
  "latency": "<175ms",
  "throughput": "500Mbps",
  "region": "Guangzhou",
  "reliability": "98.53%",
  "time": "2025-02-08"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'priority'."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, per-device throughput should be in the range 0.05–2.00 Mbps, but got about 500.00 Mbps."
  },
  "consistency_check": {
    "message": "serviceType 'mMTC' but throughput about 500.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 24

User intent:
A remote surgery operation is scheduled in a hospital in Shanghai on 2025-03-20. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<3ms",
  "throughput": "69Mbps",
  "region": "Shanghai",
  "reliability": "99.985%",
  "priority": "1",
  "time": "2025-03-20"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'URLLC' for this intent, but got 'mMTC'."
  },
  "consistency_check": {
    "message": "sliceType 'URLLC-RemoteSurgery' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 3.0 ms is much lower than the typical 80–200 ms range. serviceType 'mMTC' but throughput about 69.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 25

User intent:
On 2025-02-04, an autonomous driving test on the expressway near Tianjin will involve a fleet of self-driving trucks exchanging cooperative awareness messages. The service must guarantee millisecond-level latency and extremely high reliability for safety.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-V2XHighway",
  "latency": "<8ms",
  "throughput": "5Mbps",
  "region": "Tianjin",
  "reliability": "99.936",
  "priority": "1",
  "time": "2025-02-04"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '99.936'."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, throughput should be in the range 20–200 Mbps, but got about 5.0 Mbps."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 26

User intent:
During an emergency response drill in Shanghai on 2025-05-11, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "mMTC-InconsistentSlice",
  "latency": "<4ms",
  "throughput": "92Mbps",
  "region": "Shanghai",
  "reliability": "99.971",
  "priority": "1",
  "time": "2025-05-11"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '99.971'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-InconsistentSlice' is not consistent with serviceType 'URLLC'."
  }
}
```

## Validation Example 27

User intent:
A smart agriculture project near Beijing from 2025-02-10 will connect soil moisture sensors and climate stations across large fields.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-InconsistentSlice",
  "latency": "<149ms",
  "throughput": "0.35Mbps",
  "region": "Beijing",
  "reliability": "98.52%",
  "priority": "5",
  "time": "2025-02-10"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'mMTC' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "serviceType 'URLLC' but latency around 149.0 ms is too high for URLLC."
  }
}
```

## Validation Example 28

User intent:
A university campus in Wuhan will upgrade to 6G on 2025-01-27 to support massive online classes, interactive labs and AR-assisted teaching for students.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "mMTC-InconsistentSlice",
  "latency": "<80ms",
  "throughput": "1080Mbps",
  "region": "Wuhan",
  "reliability": "98.34%",
  "priority": "2",
  "time": "2025-01-27"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this eMBB scenario, latency should be in the range 15–40 ms, but got about 80.0 ms."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-InconsistentSlice' is not consistent with serviceType 'eMBB'."
  }
}
```

## Validation Example 29

User intent:
A logistics company in Shenzhen will attach low-power trackers to thousands of containers and pallets from 2025-03-03, sending infrequent location updates.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "eMBB-InconsistentSlice",
  "latency": "<10ms",
  "throughput": "0.42Mbps",
  "region": "Shenzhen",
  "reliability": "95.12%",
  "priority": "5",
  "time": "2025-03-03"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, latency should be in the range 80–200 ms, but got about 10.0 ms."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-InconsistentSlice' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 10.0 ms is much lower than the typical 80–200 ms range."
  }
}
```

## Validation Example 30

User intent:
A remote surgery operation is scheduled in a hospital in Guangzhou on 2025-04-27. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "mMTC-InconsistentSlice",
  "latency": "<2ms",
  "throughput": "68Mbps",
  "region": "Guangzhou",
  "reliability": "99.952%",
  "priority": "1",
  "time": "2025-04-27"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-InconsistentSlice' is not consistent with serviceType 'URLLC'."
  }
}
```

## Validation Example 31

User intent:
A remote surgery operation is scheduled in a hospital in Dubai on 2025-04-18. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<5ms",
  "throughput": 55.0,
  "region": "Dubai",
  "reliability": "99.964%",
  "priority": "1",
  "time": "2025-04-18"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '55.0'."
  },
  "semantic_check": {
    "message": "Expected serviceType 'URLLC' for this intent, but got 'mMTC'."
  },
  "consistency_check": {
    "message": "sliceType 'URLLC-RemoteSurgery' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 5.0 ms is much lower than the typical 80–200 ms range. serviceType 'mMTC' but throughput about 55.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 32

User intent:
During an emergency response drill in London on 2025-01-16, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<3ms",
  "throughput": "47Mbps",
  "region": "London",
  "reliability": "99.908%",
  "priority": "1",
  "time": "2025-01-16"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'URLLC' for this intent, but got 'mMTC'."
  },
  "consistency_check": {
    "message": "sliceType 'URLLC-DroneEmergency' is not consistent with serviceType 'mMTC'. serviceType 'mMTC' but latency around 3.0 ms is much lower than the typical 80–200 ms range. serviceType 'mMTC' but throughput about 47.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 33

User intent:
An international airport in Hangzhou plans to deploy high-capacity 6G hotspots in departure halls on 2025-03-28, serving roaming users with HD video streaming and large file downloads.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "mMTC-InconsistentSlice",
  "latency": "29ms",
  "throughput": "1344Mbps",
  "region": "Hangzhou",
  "reliability": "98.64%",
  "priority": "3",
  "time": "2025-03-28"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-InconsistentSlice' is not consistent with serviceType 'eMBB'."
  }
}
```

## Validation Example 34

User intent:
On 2025-03-06, a global holographic townhall in Beijing will broadcast 8K volumetric video to remote offices, with participants wearing AR headsets for immersive telepresence.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HolographicTownhall",
  "latency": "<31ms",
  "throughput": 1460.0,
  "region": "Beijing",
  "reliability": "98.39%",
  "priority": "3",
  "time": "2025-03-06"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '1460.0'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 35

User intent:
During an emergency response drill in Guangzhou on 2025-03-05, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<40ms",
  "throughput": "5Mbps",
  "region": "Guangzhou",
  "reliability": "99.936%",
  "priority": "1",
  "time": "2025-03-05"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, latency should be in the range 1–10 ms, but got about 40.0 ms. For this URLLC scenario, throughput should be in the range 20–200 Mbps, but got about 5.0 Mbps."
  },
  "consistency_check": {
    "message": "serviceType 'URLLC' but latency around 40.0 ms is too high for URLLC."
  }
}
```

## Validation Example 36

User intent:
A logistics company in Shanghai will attach low-power trackers to thousands of containers and pallets from 2025-01-21, sending infrequent location updates.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "mMTC-LogisticsTracking",
  "latency": "<148ms",
  "throughput": "0.31Mbps",
  "region": "Shanghai",
  "reliability": "98.84%",
  "time": "2025-01-21"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'priority'."
  },
  "semantic_check": {
    "message": "Expected serviceType 'mMTC' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-LogisticsTracking' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 148.0 ms is too high for URLLC."
  }
}
```

## Validation Example 37

User intent:
An industrial park in Bangkok plans dense deployment of environmental sensors on 2025-04-10 to monitor air quality, temperature and humidity.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<85ms",
  "throughput": 0.62,
  "region": "Bangkok",
  "reliability": "95.41%",
  "priority": "3",
  "time": "2025-04-10"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '0.62'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 38

User intent:
A large sports event in Seoul on 2025-03-26 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<32ms",
  "throughput": "629Mbps",
  "region": "Seoul",
  "reliability": "99.58%",
  "priority": "2",
  "time": "2025-03-26"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'eMBB' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-Stadium4KEvent' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 32.0 ms is too high for URLLC."
  }
}
```

## Validation Example 39

User intent:
A smart agriculture project near London from 2025-04-28 will connect soil moisture sensors and climate stations across large fields.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "mMTC-Agriculture",
  "latency": "<198ms",
  "throughput": "0.36Mbps",
  "region": "London",
  "reliability": "98.64%",
  "priority": "4",
  "time": "2025-04-28"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'mMTC' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-Agriculture' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 198.0 ms is too high for URLLC."
  }
}
```

## Validation Example 40

User intent:
An industrial park in Singapore plans dense deployment of environmental sensors on 2025-02-16 to monitor air quality, temperature and humidity.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<98ms",
  "throughput": "500Mbps",
  "region": "Singapore",
  "reliability": "98.31",
  "priority": "4",
  "time": "2025-02-16"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '98.31'."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, per-device throughput should be in the range 0.05–2.00 Mbps, but got about 500.00 Mbps."
  },
  "consistency_check": {
    "message": "serviceType 'mMTC' but throughput about 500.00 Mbps is too high for massive low-rate devices."
  }
}
```

## Validation Example 41

User intent:
An international airport in Tokyo plans to deploy high-capacity 6G hotspots in departure halls on 2025-04-10, serving roaming users with HD video streaming and large file downloads.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-AirportHotspot",
  "latency": "<21ms",
  "throughput": 1382.0,
  "region": "Tokyo",
  "reliability": "97.47%",
  "priority": "3",
  "time": "2025-04-10"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '1382.0'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 42

User intent:
On 2025-05-20, a global holographic townhall in Suzhou will broadcast 8K volumetric video to remote offices, with participants wearing AR headsets for immersive telepresence.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HolographicTownhall",
  "latency": "<29ms",
  "throughput": "50Mbps",
  "region": "Suzhou",
  "reliability": "97.70%",
  "time": "2025-05-20"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'priority'."
  },
  "semantic_check": {
    "message": "For this eMBB scenario, throughput should be in the range 100–2000 Mbps, but got about 50.0 Mbps."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 43

User intent:
Starting on 2025-02-22, a city-wide smart metering rollout in Hangzhou will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<5ms",
  "throughput": 0.29,
  "region": "Hangzhou",
  "reliability": "96.66%",
  "priority": "4",
  "time": "2025-02-22"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '0.29'."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, latency should be in the range 80–200 ms, but got about 5.0 ms."
  },
  "consistency_check": {
    "message": "serviceType 'mMTC' but latency around 5.0 ms is much lower than the typical 80–200 ms range."
  }
}
```

## Validation Example 44

User intent:
On 2025-02-19, a global holographic townhall in Shanghai will broadcast 8K volumetric video to remote offices, with participants wearing AR headsets for immersive telepresence.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HolographicTownhall",
  "latency": "<25ms",
  "throughput": "1169Mbps",
  "region": "Shanghai",
  "reliability": "98.79",
  "priority": "3",
  "time": "2025-02-19"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '98.79'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 45

User intent:
A large sports event in Tianjin on 2025-01-10 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<33ms",
  "throughput": "938Mbps",
  "region": "Tianjin",
  "reliability": "98.69",
  "priority": "2",
  "time": "2025-01-10"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '98.69'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 46

User intent:
An urban smart parking system in Chengdu will deploy ground sensors from 2025-05-19, with devices occasionally uploading occupancy information.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartParking",
  "latency": "<98ms",
  "throughput": "0.08Mbps",
  "region": "Chengdu",
  "reliability": "99.19",
  "priority": "4",
  "time": "2025-05-19"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '99.19'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 47

User intent:
A smart factory in Seoul will coordinate robot arms and AGVs on 2025-03-29. Control loops require sub-10ms delay and virtually no packet loss to avoid collisions and production errors.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "eMBB-InconsistentSlice",
  "latency": "<5ms",
  "throughput": "76Mbps",
  "region": "Seoul",
  "reliability": "99.965%",
  "time": "2025-03-29"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'priority'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-InconsistentSlice' is not consistent with serviceType 'URLLC'."
  }
}
```

## Validation Example 48

User intent:
Starting on 2025-04-12, a city-wide smart metering rollout in Nanjing will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<159ms",
  "throughput": "0.12Mbps",
  "region": "Nanjing",
  "reliability": "96.50%",
  "priority": "4",
  "time": "2025-04-12"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'mMTC' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'mMTC-SmartMetering' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 159.0 ms is too high for URLLC."
  }
}
```

## Validation Example 49

User intent:
Starting on 2025-04-17, a city-wide smart metering rollout in Wuhan will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<195ms",
  "throughput": "0.33Mbps",
  "region": "Wuhan",
  "reliability": "96.74",
  "priority": "4",
  "time": "2025-04-17"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'reliability' should be a string ending with '%', but got '96.74'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 50

User intent:
A high-speed train passing through Tianjin on 2025-01-31 should support uninterrupted cloud gaming and 4K video for passengers along the route.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "eMBB-HighSpeedTrain",
  "latency": "<34ms",
  "throughput": "837Mbps",
  "region": "Tianjin",
  "reliability": "97.96%",
  "priority": "2"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'time'."
  },
  "semantic_check": {
    "message": "Expected serviceType 'eMBB' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-HighSpeedTrain' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 34.0 ms is too high for URLLC."
  }
}
```

## Validation Example 51

User intent:
A remote surgery operation is scheduled in a hospital in Hangzhou on 2025-04-07. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<40ms",
  "throughput": "61Mbps",
  "region": "Hangzhou",
  "reliability": "98%",
  "priority": "1",
  "time": "2025-04-07"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this URLLC scenario, latency should be in the range 1–10 ms, but got about 40.0 ms. For this URLLC scenario, reliability should be in the range 99.90%–99.999%, but got about 98.000%."
  },
  "consistency_check": {
    "message": "serviceType 'URLLC' but latency around 40.0 ms is too high for URLLC."
  }
}
```

## Validation Example 52

User intent:
On 2025-02-10, an autonomous driving test on the expressway near Nanjing will involve a fleet of self-driving trucks exchanging cooperative awareness messages. The service must guarantee millisecond-level latency and extremely high reliability for safety.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-V2XHighway",
  "latency": "<4ms",
  "throughput": 48.0,
  "region": "Nanjing",
  "reliability": "99.928%",
  "priority": "1",
  "time": "2025-02-10"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '48.0'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 53

User intent:
A smart factory in Dubai will coordinate robot arms and AGVs on 2025-04-26. Control loops require sub-10ms delay and virtually no packet loss to avoid collisions and production errors.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "eMBB-InconsistentSlice",
  "latency": "<7ms",
  "throughput": "38Mbps",
  "region": "Dubai",
  "reliability": "99.958%",
  "priority": "1",
  "time": "2025-04-26"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-InconsistentSlice' is not consistent with serviceType 'URLLC'."
  }
}
```

## Validation Example 54

User intent:
On 2025-04-16, a global holographic townhall in Singapore will broadcast 8K volumetric video to remote offices, with participants wearing AR headsets for immersive telepresence.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "URLLC-InconsistentSlice",
  "latency": "<33ms",
  "throughput": "50Mbps",
  "region": "Singapore",
  "reliability": "98.60%",
  "priority": "2",
  "time": "2025-04-16"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "For this eMBB scenario, throughput should be in the range 100–2000 Mbps, but got about 50.0 Mbps."
  },
  "consistency_check": {
    "message": "sliceType 'URLLC-InconsistentSlice' is not consistent with serviceType 'eMBB'."
  }
}
```

## Validation Example 55

User intent:
A large sports event in Tianjin on 2025-04-01 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<80ms",
  "throughput": "1418Mbps",
  "region": "Tianjin",
  "reliability": "98.65%",
  "priority": "3"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'time'."
  },
  "semantic_check": {
    "message": "For this eMBB scenario, latency should be in the range 15–40 ms, but got about 80.0 ms."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 56

User intent:
A university campus in Guangzhou will upgrade to 6G on 2025-01-26 to support massive online classes, interactive labs and AR-assisted teaching for students.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "eMBB-CampusBroadband",
  "latency": "<22ms",
  "throughput": "900Mbps",
  "region": "Guangzhou",
  "reliability": "97.99%",
  "priority": "3"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Missing required field 'time'."
  },
  "semantic_check": {
    "message": "Expected serviceType 'eMBB' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-CampusBroadband' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 22.0 ms is too high for URLLC."
  }
}
```

## Validation Example 57

User intent:
A high-speed train passing through Seoul on 2025-03-01 should support uninterrupted cloud gaming and 4K video for passengers along the route.

Candidate JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HighSpeedTrain",
  "latency": "<26ms",
  "throughput": 1249.0,
  "region": "Seoul",
  "reliability": "99.36%",
  "priority": "2",
  "time": "2025-03-01"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '1249.0'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 58

User intent:
Starting from 2025-05-25, protection signals in the power grid of Tokyo will be carried over the 6G network. Fault detection and isolation messages require ultra-fast and reliable delivery.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-SmartGridProtection",
  "latency": "<5ms",
  "throughput": 32.0,
  "region": "Tokyo",
  "reliability": "99.989%",
  "priority": "1",
  "time": "2025-05-25"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '32.0'."
  },
  "semantic_check": {
    "message": "No issue detected."
  },
  "consistency_check": {
    "message": "No issue detected."
  }
}
```

## Validation Example 59

User intent:
Starting on 2025-02-03, a city-wide smart metering rollout in Beijing will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Candidate JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<5ms",
  "throughput": 0.38,
  "region": "Beijing",
  "reliability": "95.97%",
  "priority": "3",
  "time": "2025-02-03"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "Field 'throughput' should be a string with 'Mbps', but got '0.38'."
  },
  "semantic_check": {
    "message": "For this mMTC scenario, latency should be in the range 80–200 ms, but got about 5.0 ms."
  },
  "consistency_check": {
    "message": "serviceType 'mMTC' but latency around 5.0 ms is much lower than the typical 80–200 ms range."
  }
}
```

## Validation Example 60

User intent:
A large sports event in Bangkok on 2025-02-09 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Candidate JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "22ms",
  "throughput": "750Mbps",
  "region": "Bangkok",
  "reliability": "98.92%",
  "priority": "2",
  "time": "2025-02-09"
}
```

Expected evaluation:
```json
{
  "format_check": {
    "message": "No issue detected."
  },
  "semantic_check": {
    "message": "Expected serviceType 'eMBB' for this intent, but got 'URLLC'."
  },
  "consistency_check": {
    "message": "sliceType 'eMBB-Stadium4KEvent' is not consistent with serviceType 'URLLC'. serviceType 'URLLC' but latency around 22.0 ms is too high for URLLC."
  }
}
```
