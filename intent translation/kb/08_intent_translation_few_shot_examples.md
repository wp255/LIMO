# Intent Translation Few-Shot Examples

These examples are positive examples. They should be used to guide natural-language-to-JSON translation.

## Example 1

Natural language intent:
During an emergency response drill in Xi'an on 2025-04-19, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<5ms",
  "throughput": "117Mbps",
  "region": "Xi'an",
  "reliability": "99.946%",
  "priority": "1",
  "time": "2025-04-19"
}
```

## Example 2

Natural language intent:
During an emergency response drill in Seoul on 2025-01-22, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<1ms",
  "throughput": "103Mbps",
  "region": "Seoul",
  "reliability": "99.911%",
  "priority": "1",
  "time": "2025-01-22"
}
```

## Example 3

Natural language intent:
During an emergency response drill in Seoul on 2025-01-14, a swarm of drones and rescue robots will exchange sensor data and control commands in real time. The network must support ultra-low latency and mission-critical reliability.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-DroneEmergency",
  "latency": "<7ms",
  "throughput": "89Mbps",
  "region": "Seoul",
  "reliability": "99.969%",
  "priority": "1",
  "time": "2025-01-14"
}
```

## Example 4

Natural language intent:
A smart factory in Tokyo will coordinate robot arms and AGVs on 2025-01-21. Control loops require sub-10ms delay and virtually no packet loss to avoid collisions and production errors.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-IndustrialRobot",
  "latency": "<6ms",
  "throughput": "75Mbps",
  "region": "Tokyo",
  "reliability": "99.908%",
  "priority": "1",
  "time": "2025-01-21"
}
```

## Example 5

Natural language intent:
A smart factory in Suzhou will coordinate robot arms and AGVs on 2025-02-19. Control loops require sub-10ms delay and virtually no packet loss to avoid collisions and production errors.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-IndustrialRobot",
  "latency": "<2ms",
  "throughput": "61Mbps",
  "region": "Suzhou",
  "reliability": "99.990%",
  "priority": "1",
  "time": "2025-02-19"
}
```

## Example 6

Natural language intent:
A remote surgery operation is scheduled in a hospital in Chengdu on 2025-05-06. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<4ms",
  "throughput": "71Mbps",
  "region": "Chengdu",
  "reliability": "99.981%",
  "priority": "1",
  "time": "2025-05-06"
}
```

## Example 7

Natural language intent:
A remote surgery operation is scheduled in a hospital in Tianjin on 2025-01-16. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<3ms",
  "throughput": "51Mbps",
  "region": "Tianjin",
  "reliability": "99.996%",
  "priority": "1",
  "time": "2025-01-16"
}
```

## Example 8

Natural language intent:
A remote surgery operation is scheduled in a hospital in Chengdu on 2025-04-16. The surgeon will control robotic arms over the 6G network, and the connection must be extremely stable with very low latency and almost no packet loss.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-RemoteSurgery",
  "latency": "<2ms",
  "throughput": "111Mbps",
  "region": "Chengdu",
  "reliability": "99.991%",
  "priority": "1",
  "time": "2025-04-16"
}
```

## Example 9

Natural language intent:
Starting from 2025-02-18, protection signals in the power grid of Tianjin will be carried over the 6G network. Fault detection and isolation messages require ultra-fast and reliable delivery.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-SmartGridProtection",
  "latency": "<2ms",
  "throughput": "39Mbps",
  "region": "Tianjin",
  "reliability": "99.936%",
  "priority": "1",
  "time": "2025-02-18"
}
```

## Example 10

Natural language intent:
Starting from 2025-04-23, protection signals in the power grid of Singapore will be carried over the 6G network. Fault detection and isolation messages require ultra-fast and reliable delivery.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-SmartGridProtection",
  "latency": "<3ms",
  "throughput": "33Mbps",
  "region": "Singapore",
  "reliability": "99.994%",
  "priority": "1",
  "time": "2025-04-23"
}
```

## Example 11

Natural language intent:
Starting from 2025-01-01, protection signals in the power grid of Tianjin will be carried over the 6G network. Fault detection and isolation messages require ultra-fast and reliable delivery.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-SmartGridProtection",
  "latency": "<6ms",
  "throughput": "30Mbps",
  "region": "Tianjin",
  "reliability": "99.992%",
  "priority": "1",
  "time": "2025-01-01"
}
```

## Example 12

Natural language intent:
On 2025-04-01, an autonomous driving test on the expressway near Nanjing will involve a fleet of self-driving trucks exchanging cooperative awareness messages. The service must guarantee millisecond-level latency and extremely high reliability for safety.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-V2XHighway",
  "latency": "<3ms",
  "throughput": "25Mbps",
  "region": "Nanjing",
  "reliability": "99.957%",
  "priority": "1",
  "time": "2025-04-01"
}
```

## Example 13

Natural language intent:
On 2025-01-13, an autonomous driving test on the expressway near Guangzhou will involve a fleet of self-driving trucks exchanging cooperative awareness messages. The service must guarantee millisecond-level latency and extremely high reliability for safety.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-V2XHighway",
  "latency": "<3ms",
  "throughput": "70Mbps",
  "region": "Guangzhou",
  "reliability": "99.979%",
  "priority": "1",
  "time": "2025-01-13"
}
```

## Example 14

Natural language intent:
On 2025-05-23, an autonomous driving test on the expressway near Hangzhou will involve a fleet of self-driving trucks exchanging cooperative awareness messages. The service must guarantee millisecond-level latency and extremely high reliability for safety.

Target JSON:
```json
{
  "serviceType": "URLLC",
  "sliceType": "URLLC-V2XHighway",
  "latency": "<6ms",
  "throughput": "78Mbps",
  "region": "Hangzhou",
  "reliability": "99.944%",
  "priority": "1",
  "time": "2025-05-23"
}
```

## Example 15

Natural language intent:
An international airport in Shenzhen plans to deploy high-capacity 6G hotspots in departure halls on 2025-01-29, serving roaming users with HD video streaming and large file downloads.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-AirportHotspot",
  "latency": "<21ms",
  "throughput": "650Mbps",
  "region": "Shenzhen",
  "reliability": "99.68%",
  "priority": "3",
  "time": "2025-01-29"
}
```

## Example 16

Natural language intent:
An international airport in Tokyo plans to deploy high-capacity 6G hotspots in departure halls on 2025-02-17, serving roaming users with HD video streaming and large file downloads.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-AirportHotspot",
  "latency": "<40ms",
  "throughput": "1257Mbps",
  "region": "Tokyo",
  "reliability": "98.82%",
  "priority": "2",
  "time": "2025-02-17"
}
```

## Example 17

Natural language intent:
An international airport in Xi'an plans to deploy high-capacity 6G hotspots in departure halls on 2025-03-24, serving roaming users with HD video streaming and large file downloads.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-AirportHotspot",
  "latency": "<33ms",
  "throughput": "1260Mbps",
  "region": "Xi'an",
  "reliability": "97.50%",
  "priority": "2",
  "time": "2025-03-24"
}
```

## Example 18

Natural language intent:
A university campus in Suzhou will upgrade to 6G on 2025-02-18 to support massive online classes, interactive labs and AR-assisted teaching for students.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-CampusBroadband",
  "latency": "<27ms",
  "throughput": "918Mbps",
  "region": "Suzhou",
  "reliability": "99.42%",
  "priority": "2",
  "time": "2025-02-18"
}
```

## Example 19

Natural language intent:
A university campus in Singapore will upgrade to 6G on 2025-01-12 to support massive online classes, interactive labs and AR-assisted teaching for students.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-CampusBroadband",
  "latency": "<23ms",
  "throughput": "1189Mbps",
  "region": "Singapore",
  "reliability": "97.85%",
  "priority": "2",
  "time": "2025-01-12"
}
```

## Example 20

Natural language intent:
A high-speed train passing through Wuhan on 2025-04-21 should support uninterrupted cloud gaming and 4K video for passengers along the route.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HighSpeedTrain",
  "latency": "<24ms",
  "throughput": "816Mbps",
  "region": "Wuhan",
  "reliability": "98.76%",
  "priority": "2",
  "time": "2025-04-21"
}
```

## Example 21

Natural language intent:
On 2025-03-25, a global holographic townhall in Dubai will broadcast 8K volumetric video to remote offices, with participants wearing AR headsets for immersive telepresence.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-HolographicTownhall",
  "latency": "<20ms",
  "throughput": "1741Mbps",
  "region": "Dubai",
  "reliability": "98.98%",
  "priority": "2",
  "time": "2025-03-25"
}
```

## Example 22

Natural language intent:
A large sports event in Guangzhou on 2025-04-16 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<32ms",
  "throughput": "836Mbps",
  "region": "Guangzhou",
  "reliability": "99.14%",
  "priority": "3",
  "time": "2025-04-16"
}
```

## Example 23

Natural language intent:
A large sports event in Hangzhou on 2025-02-06 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<33ms",
  "throughput": "1316Mbps",
  "region": "Hangzhou",
  "reliability": "97.34%",
  "priority": "2",
  "time": "2025-02-06"
}
```

## Example 24

Natural language intent:
A large sports event in Nanjing on 2025-02-23 evening will provide 4K live streaming and multi-angle replays to spectators in the stadium on their mobile devices.

Target JSON:
```json
{
  "serviceType": "eMBB",
  "sliceType": "eMBB-Stadium4KEvent",
  "latency": "<26ms",
  "throughput": "1000Mbps",
  "region": "Nanjing",
  "reliability": "97.52%",
  "priority": "2",
  "time": "2025-02-23"
}
```

## Example 25

Natural language intent:
A smart agriculture project near Suzhou from 2025-01-05 will connect soil moisture sensors and climate stations across large fields.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-Agriculture",
  "latency": "<102ms",
  "throughput": "0.72Mbps",
  "region": "Suzhou",
  "reliability": "98.54%",
  "priority": "3",
  "time": "2025-01-05"
}
```

## Example 26

Natural language intent:
A smart agriculture project near Shenzhen from 2025-02-16 will connect soil moisture sensors and climate stations across large fields.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-Agriculture",
  "latency": "<190ms",
  "throughput": "0.68Mbps",
  "region": "Shenzhen",
  "reliability": "99.01%",
  "priority": "4",
  "time": "2025-02-16"
}
```

## Example 27

Natural language intent:
A smart agriculture project near Nanjing from 2025-03-26 will connect soil moisture sensors and climate stations across large fields.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-Agriculture",
  "latency": "<105ms",
  "throughput": "0.50Mbps",
  "region": "Nanjing",
  "reliability": "97.40%",
  "priority": "5",
  "time": "2025-03-26"
}
```

## Example 28

Natural language intent:
An industrial park in Singapore plans dense deployment of environmental sensors on 2025-05-22 to monitor air quality, temperature and humidity.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<112ms",
  "throughput": "0.13Mbps",
  "region": "Singapore",
  "reliability": "97.67%",
  "priority": "3",
  "time": "2025-05-22"
}
```

## Example 29

Natural language intent:
An industrial park in Seoul plans dense deployment of environmental sensors on 2025-03-09 to monitor air quality, temperature and humidity.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<145ms",
  "throughput": "0.84Mbps",
  "region": "Seoul",
  "reliability": "95.87%",
  "priority": "4",
  "time": "2025-03-09"
}
```

## Example 30

Natural language intent:
An industrial park in Guangzhou plans dense deployment of environmental sensors on 2025-05-19 to monitor air quality, temperature and humidity.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-EnvironmentalSensing",
  "latency": "<163ms",
  "throughput": "0.38Mbps",
  "region": "Guangzhou",
  "reliability": "95.54%",
  "priority": "5",
  "time": "2025-05-19"
}
```

## Example 31

Natural language intent:
Starting on 2025-04-06, a city-wide smart metering rollout in Singapore will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<181ms",
  "throughput": "0.21Mbps",
  "region": "Singapore",
  "reliability": "96.88%",
  "priority": "5",
  "time": "2025-04-06"
}
```

## Example 32

Natural language intent:
Starting on 2025-02-11, a city-wide smart metering rollout in Tokyo will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<191ms",
  "throughput": "0.36Mbps",
  "region": "Tokyo",
  "reliability": "97.55%",
  "priority": "3",
  "time": "2025-02-11"
}
```

## Example 33

Natural language intent:
Starting on 2025-03-28, a city-wide smart metering rollout in Chengdu will connect tens of thousands of electricity meters, each periodically reporting consumption data.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartMetering",
  "latency": "<135ms",
  "throughput": "0.33Mbps",
  "region": "Chengdu",
  "reliability": "98.03%",
  "priority": "3",
  "time": "2025-03-28"
}
```

## Example 34

Natural language intent:
An urban smart parking system in Beijing will deploy ground sensors from 2025-04-27, with devices occasionally uploading occupancy information.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartParking",
  "latency": "<144ms",
  "throughput": "0.24Mbps",
  "region": "Beijing",
  "reliability": "97.60%",
  "priority": "5",
  "time": "2025-04-27"
}
```

## Example 35

Natural language intent:
An urban smart parking system in Guangzhou will deploy ground sensors from 2025-01-14, with devices occasionally uploading occupancy information.

Target JSON:
```json
{
  "serviceType": "mMTC",
  "sliceType": "mMTC-SmartParking",
  "latency": "<89ms",
  "throughput": "0.18Mbps",
  "region": "Guangzhou",
  "reliability": "97.26%",
  "priority": "3",
  "time": "2025-01-14"
}
```
