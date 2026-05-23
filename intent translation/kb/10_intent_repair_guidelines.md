# Intent Repair Guidelines

The repair agent should fix the candidate JSON according to validation results and domain knowledge.

## Repair Priorities

1. Preserve the user's original scenario meaning.
2. Fix missing required fields if the information appears in the user intent.
3. Fix output format errors without changing semantics.
4. Fix serviceType if it contradicts the user intent.
5. Fix sliceType prefix and scenario name to match serviceType.
6. Fix QoS values to fall within the expected service-level range.
7. Keep region and time faithful to the original user intent.

## Missing Field Repair

If `region` is missing:
- Extract the city or area from user intent.

If `time` is missing:
- Extract the date from user intent.

If `priority` is missing:
- URLLC safety-critical services → `"1"`.
- eMBB immersive broadband services → `"2"` or `"3"`.
- mMTC sensor/meter/tracker services → `"4"` or `"5"`.

## Format Repair

If throughput is numeric:
- Convert to string with `Mbps`.
- Example: `325.0` → `"325Mbps"`.

If reliability does not end with `%`:
- Add `%`.
- Example: `"99.910"` → `"99.910%"`.

If latency is numeric:
- Convert to string with `ms`.
- Example: `5` → `"<5ms"`.

## ServiceType Repair

Remote surgery, robotic control, V2X, smart grid protection, emergency drones:
- serviceType should be `URLLC`.

Holographic townhall, high-speed train cloud gaming, airport hotspot, stadium 4K, campus AR teaching:
- serviceType should be `eMBB`.

Smart parking, agriculture, smart metering, environmental sensing, logistics tracking:
- serviceType should be `mMTC`.

## SliceType Repair

Choose the closest sliceType:
- remote surgery → `URLLC-RemoteSurgery`
- smart factory robot arms / AGVs → `URLLC-IndustrialRobot`
- autonomous driving / highway trucks → `URLLC-V2XHighway`
- smart grid protection → `URLLC-SmartGridProtection`
- emergency drones / rescue robots → `URLLC-DroneEmergency`
- holographic townhall → `eMBB-HolographicTownhall`
- high-speed train → `eMBB-HighSpeedTrain`
- airport hotspot → `eMBB-AirportHotspot`
- stadium 4K event → `eMBB-Stadium4KEvent`
- campus broadband / AR teaching → `eMBB-CampusBroadband`
- smart parking → `mMTC-SmartParking`
- smart agriculture → `mMTC-Agriculture`
- smart metering → `mMTC-SmartMetering`
- environmental sensing → `mMTC-EnvironmentalSensing`
- logistics tracking → `mMTC-LogisticsTracking`

## QoS Repair

If URLLC latency is 40-50 ms:
- repair to a value in 1-10 ms.

If URLLC reliability is around 98%:
- repair to at least 99.90%.

If eMBB throughput is 50 Mbps:
- repair to at least 100 Mbps; for video/AR/8K, use several hundred Mbps or higher.

If eMBB latency is 80 ms:
- repair to 15-40 ms.

If mMTC latency is 5-10 ms:
- repair to 80-200 ms.

If mMTC throughput is 500 Mbps:
- repair to 0.05-2.00 Mbps.

## Repair Output Contract

Output repaired JSON only. Do not output Markdown.

Example repair:
Input issue:
- user intent: smart parking ground sensors
- candidate: serviceType `mMTC`, throughput `"500Mbps"`

Repaired output:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartParking",
  "latency": "<150ms",
  "throughput": "0.3Mbps",
  "region": "Dubai",
  "reliability": "97%",
  "priority": "4",
  "time": "2025-03-07"
}
```
