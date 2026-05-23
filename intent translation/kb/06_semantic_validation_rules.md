# Semantic Validation Rules

Semantic validation checks whether the candidate JSON preserves the meaning of the original user intent.

## Semantic Validation Tasks

1. Check expected serviceType from the natural-language scenario.
2. Check whether QoS values are reasonable for the expected serviceType and scenario.
3. Check whether region and time preserve the user's request.
4. Check whether application semantics are correctly reflected by sliceType.

## Expected ServiceType by Scenario

### Expected URLLC
Use `URLLC` for:
- remote surgery operation
- robotic-arm control over 6G
- smart factory robot arms and AGVs
- sub-10ms control loops
- autonomous driving fleet / self-driving trucks
- cooperative awareness messages
- smart grid protection signals
- fault detection and isolation
- emergency drones and rescue robots
- real-time control commands
- mission-critical reliability

Wrong-service examples:
- Remote surgery expected `URLLC`, but got `mMTC` or `eMBB`.
- V2X highway expected `URLLC`, but got `eMBB`.
- Emergency drones expected `URLLC`, but got `mMTC`.

### Expected eMBB
Use `eMBB` for:
- 8K volumetric video
- holographic townhall
- AR headsets for immersive telepresence
- high-speed train cloud gaming and 4K video
- high-capacity airport hotspot
- HD video streaming
- large file downloads
- stadium 4K live streaming
- multi-angle replays
- campus online classes
- interactive labs
- AR-assisted teaching

Wrong-service examples:
- Stadium 4K event expected `eMBB`, but got `mMTC` or `URLLC`.
- High-speed train cloud gaming and 4K expected `eMBB`, but got `mMTC`.
- Airport hotspot expected `eMBB`, but got `URLLC`.

### Expected mMTC
Use `mMTC` for:
- urban smart parking ground sensors
- occasional occupancy upload
- smart agriculture soil moisture sensors
- climate stations
- city-wide smart metering
- tens of thousands of electricity meters
- periodic consumption reporting
- environmental sensors
- air quality, temperature, and humidity monitoring
- low-power logistics trackers
- infrequent location updates

Wrong-service examples:
- Environmental sensing expected `mMTC`, but got `eMBB`.
- Smart agriculture expected `mMTC`, but got `URLLC`.
- Logistics tracking expected `mMTC`, but got `eMBB`.

## QoS Semantic Rules

### URLLC QoS
Expected:
- latency: 1-10 ms
- throughput: 20-200 Mbps
- reliability: 99.90%-99.999%
- priority: 1

Flag:
- latency around 40 ms or 50 ms.
- reliability around 98%.
- throughput around 5 Mbps.

Example messages:
- `For this URLLC scenario, latency should be in the range 1–10 ms, but got about 40.0 ms.`
- `For this URLLC scenario, reliability should be in the range 99.90%–99.999%, but got about 98.000%.`
- `For this URLLC scenario, throughput should be in the range 20–200 Mbps, but got about 5.0 Mbps.`

### eMBB QoS
Expected:
- latency: 15-40 ms
- throughput: 100-2000 Mbps
- reliability: about 97%-99.7%
- priority: 2 or 3

Flag:
- throughput around 50 Mbps.
- latency around 80 ms.

Example messages:
- `For this eMBB scenario, throughput should be in the range 100–2000 Mbps, but got about 50.0 Mbps.`
- `For this eMBB scenario, latency should be in the range 15–40 ms, but got about 80.0 ms.`

### mMTC QoS
Expected:
- latency: 80-200 ms
- per-device throughput: 0.05-2.00 Mbps
- reliability: about 95%-99.3%
- priority: 3, 4, or 5

Flag:
- latency around 5 ms or 10 ms.
- throughput around 500 Mbps.

Example messages:
- `For this mMTC scenario, latency should be in the range 80–200 ms, but got about 10.0 ms.`
- `For this mMTC scenario, per-device throughput should be in the range 0.05–2.00 Mbps, but got about 500.00 Mbps.`

## Semantic Validation Should Not Over-Penalize

If serviceType, sliceType, and QoS values all match the scenario, output:
`No issue detected.`

Do not report a semantic issue solely because the candidate uses `<` in latency, e.g., `"<145ms"`.
Do not report a semantic issue solely because the region is a city outside China, e.g., Singapore, Tokyo, London, Dubai, Bangkok, Seoul.
