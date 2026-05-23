# Service Type Mapping Rules

## URLLC: Ultra-Reliable Low-Latency Communication

Map the intent to `URLLC` when the service is safety-critical, mission-critical, real-time control oriented, or explicitly requires ultra-low latency and high reliability.

Typical semantic indicators:
- extremely stable connection
- very low latency
- ultra-low latency
- millisecond-level latency
- almost no packet loss
- mission-critical reliability
- fault detection and isolation
- control robotic arms
- avoid collisions
- cooperative awareness messages
- real-time control commands
- safety-critical delivery

Typical scenarios:
- remote surgery
- smart factory robot arms and AGVs
- autonomous driving / V2X highway
- smart grid protection
- emergency response drones and rescue robots

Default priority:
- Usually `"1"`.

General QoS profile:
- latency: 1-10 ms
- throughput: 20-200 Mbps
- reliability: 99.90%-99.999%

## eMBB: Enhanced Mobile Broadband

Map the intent to `eMBB` when the service primarily requires high throughput, high capacity, large bandwidth, video streaming, immersive content, or broadband access for many users.

Typical semantic indicators:
- 4K/8K video
- volumetric video
- holographic townhall
- AR headsets
- HD video streaming
- large file downloads
- mobile broadband hotspot
- cloud gaming
- multi-angle replays
- online classes
- AR-assisted teaching

Important disambiguation:
- The word "massive" does not always imply mMTC. For example, "massive online classes" with AR-assisted teaching is an eMBB broadband service, not mMTC.

Typical scenarios:
- holographic townhall with 8K volumetric video
- high-speed train passenger cloud gaming and 4K video
- airport high-capacity hotspot
- stadium 4K event streaming
- campus broadband and AR-assisted teaching

Default priority:
- Usually `"2"` or `"3"`.

General QoS profile:
- latency: 15-40 ms
- throughput: 100-2000 Mbps
- reliability: about 97%-99.7%

## mMTC: Massive Machine-Type Communication

Map the intent to `mMTC` when the service primarily involves massive low-power devices, sensors, meters, trackers, or periodic small-packet reporting.

Typical semantic indicators:
- thousands of sensors
- tens of thousands of electricity meters
- low-power trackers
- infrequent location updates
- periodically reporting consumption data
- occasional occupancy upload
- environmental monitoring
- soil moisture sensors
- climate stations
- small monitoring packets

Typical scenarios:
- smart parking ground sensors
- smart agriculture sensors
- smart metering
- environmental sensing
- logistics tracking

Default priority:
- Usually `"3"`, `"4"`, or `"5"`.

General QoS profile:
- latency: 80-200 ms
- per-device throughput: 0.05-2.00 Mbps
- reliability: about 95%-99.3%

## Common Misclassification Patterns

### URLLC misclassified as eMBB or mMTC
If the intent mentions safety, robotic control, emergency drones, V2X, smart grid protection, or remote surgery, the expected serviceType is `URLLC`.

### eMBB misclassified as URLLC or mMTC
If the intent mentions 4K/8K video, AR/VR, high-capacity hotspots, cloud gaming, large file downloads, or stadium/campus broadband, the expected serviceType is `eMBB`.

### mMTC misclassified as URLLC or eMBB
If the intent mentions sensors, smart meters, low-power trackers, periodic small-packet upload, or massive IoT deployment, the expected serviceType is `mMTC`.
