# Slice Type Taxonomy and Scenario Profiles

## URLLC-RemoteSurgery

- serviceType: `URLLC`
- Scenario: Remote robotic surgery in a hospital; surgeon controls robotic arms over the 6G network; extremely stable connection, very low latency, almost no packet loss.
- Keywords: remote surgery, hospital, surgeon, robotic arms, stable, very low latency, almost no packet loss
- Typical latency: <2ms to <5ms
- Typical throughput: 50-120Mbps
- Typical reliability: 99.95%-99.999%
- Typical priority: 1
- Consistency rule: `sliceType` must start with `URLLC-` and should semantically match the scenario.

## URLLC-IndustrialRobot

- serviceType: `URLLC`
- Scenario: Smart factory robot arms and AGVs; control loops require sub-10ms delay to avoid collisions and production errors.
- Keywords: smart factory, robot arms, AGVs, control loops, sub-10ms, collisions, production errors
- Typical latency: <2ms to <7ms
- Typical throughput: 40-120Mbps
- Typical reliability: 99.90%-99.999%
- Typical priority: 1
- Consistency rule: `sliceType` must start with `URLLC-` and should semantically match the scenario.

## URLLC-V2XHighway

- serviceType: `URLLC`
- Scenario: Autonomous driving test on expressway; fleet of self-driving trucks exchanges cooperative awareness messages.
- Keywords: autonomous driving, expressway, self-driving trucks, cooperative awareness messages, safety, millisecond-level latency
- Typical latency: <1ms to <10ms
- Typical throughput: 20-100Mbps
- Typical reliability: 99.90%-99.999%
- Typical priority: 1
- Consistency rule: `sliceType` must start with `URLLC-` and should semantically match the scenario.

## URLLC-SmartGridProtection

- serviceType: `URLLC`
- Scenario: Power-grid protection signals; fault detection and isolation messages require ultra-fast and reliable delivery.
- Keywords: power grid, protection signals, fault detection, isolation, ultra-fast, reliable delivery
- Typical latency: <1ms to <6ms
- Typical throughput: 20-60Mbps
- Typical reliability: 99.90%-99.999%
- Typical priority: 1
- Consistency rule: `sliceType` must start with `URLLC-` and should semantically match the scenario.

## URLLC-DroneEmergency

- serviceType: `URLLC`
- Scenario: Emergency response drill; swarm of drones and rescue robots exchange sensor data and control commands in real time.
- Keywords: emergency response, drones, rescue robots, sensor data, control commands, real time, mission-critical
- Typical latency: <1ms to <7ms
- Typical throughput: 40-120Mbps
- Typical reliability: 99.90%-99.999%
- Typical priority: 1
- Consistency rule: `sliceType` must start with `URLLC-` and should semantically match the scenario.

## eMBB-HolographicTownhall

- serviceType: `eMBB`
- Scenario: Global holographic townhall; 8K volumetric video broadcast to remote offices with AR headsets.
- Keywords: holographic townhall, 8K volumetric video, AR headsets, immersive telepresence
- Typical latency: <15ms to <40ms
- Typical throughput: 800-2000Mbps
- Typical reliability: 97%-99.5%
- Typical priority: 2
- Consistency rule: `sliceType` must start with `eMBB-` and should semantically match the scenario.

## eMBB-HighSpeedTrain

- serviceType: `eMBB`
- Scenario: High-speed train route; uninterrupted cloud gaming and 4K video for passengers.
- Keywords: high-speed train, cloud gaming, 4K video, passengers, uninterrupted
- Typical latency: <20ms to <40ms
- Typical throughput: 100-1200Mbps
- Typical reliability: 97%-99.5%
- Typical priority: 2 or 3
- Consistency rule: `sliceType` must start with `eMBB-` and should semantically match the scenario.

## eMBB-AirportHotspot

- serviceType: `eMBB`
- Scenario: Airport high-capacity 6G hotspot in departure halls; roaming users use HD video streaming and large file downloads.
- Keywords: airport, high-capacity hotspot, HD video streaming, large file downloads, roaming users
- Typical latency: <20ms to <40ms
- Typical throughput: 600-1500Mbps
- Typical reliability: 97%-99.7%
- Typical priority: 2 or 3
- Consistency rule: `sliceType` must start with `eMBB-` and should semantically match the scenario.

## eMBB-Stadium4KEvent

- serviceType: `eMBB`
- Scenario: Large sports event; 4K live streaming and multi-angle replays to spectators in a stadium.
- Keywords: sports event, stadium, 4K live streaming, multi-angle replays, spectators
- Typical latency: <20ms to <40ms
- Typical throughput: 600-1500Mbps
- Typical reliability: 97%-99.7%
- Typical priority: 2 or 3
- Consistency rule: `sliceType` must start with `eMBB-` and should semantically match the scenario.

## eMBB-CampusBroadband

- serviceType: `eMBB`
- Scenario: University campus 6G upgrade; online classes, interactive labs, and AR-assisted teaching.
- Keywords: university campus, online classes, interactive labs, AR-assisted teaching, students
- Typical latency: <20ms to <40ms
- Typical throughput: 300-1200Mbps
- Typical reliability: 97%-99.7%
- Typical priority: 2
- Consistency rule: `sliceType` must start with `eMBB-` and should semantically match the scenario.

## mMTC-SmartParking

- serviceType: `mMTC`
- Scenario: Urban smart parking; ground sensors occasionally upload occupancy information.
- Keywords: smart parking, ground sensors, occupancy information, occasional upload
- Typical latency: <80ms to <200ms
- Typical throughput: 0.05-2.00Mbps
- Typical reliability: 95%-99.3%
- Typical priority: 4 or 5
- Consistency rule: `sliceType` must start with `mMTC-` and should semantically match the scenario.

## mMTC-Agriculture

- serviceType: `mMTC`
- Scenario: Smart agriculture; soil moisture sensors and climate stations across large fields.
- Keywords: smart agriculture, soil moisture sensors, climate stations, large fields
- Typical latency: <80ms to <200ms
- Typical throughput: 0.05-2.00Mbps
- Typical reliability: 95%-99.3%
- Typical priority: 3, 4, or 5
- Consistency rule: `sliceType` must start with `mMTC-` and should semantically match the scenario.

## mMTC-SmartMetering

- serviceType: `mMTC`
- Scenario: City-wide smart metering; tens of thousands of electricity meters periodically report consumption data.
- Keywords: smart metering, electricity meters, tens of thousands, periodically reporting consumption
- Typical latency: <80ms to <200ms
- Typical throughput: 0.05-2.00Mbps
- Typical reliability: 95%-99.3%
- Typical priority: 4 or 5
- Consistency rule: `sliceType` must start with `mMTC-` and should semantically match the scenario.

## mMTC-EnvironmentalSensing

- serviceType: `mMTC`
- Scenario: Industrial park environmental sensors monitor air quality, temperature, and humidity.
- Keywords: environmental sensors, air quality, temperature, humidity, industrial park
- Typical latency: <80ms to <200ms
- Typical throughput: 0.05-2.00Mbps
- Typical reliability: 95%-99.3%
- Typical priority: 3, 4, or 5
- Consistency rule: `sliceType` must start with `mMTC-` and should semantically match the scenario.

## mMTC-LogisticsTracking

- serviceType: `mMTC`
- Scenario: Logistics company attaches low-power trackers to containers and pallets; infrequent location updates.
- Keywords: logistics, low-power trackers, containers, pallets, infrequent location updates
- Typical latency: <80ms to <200ms
- Typical throughput: 0.05-2.00Mbps
- Typical reliability: 95%-99.3%
- Typical priority: 4 or 5
- Consistency rule: `sliceType` must start with `mMTC-` and should semantically match the scenario.

# Inconsistent Slice Types

The following synthetic slice types are used as negative examples:
- `URLLC-InconsistentSlice`
- `eMBB-InconsistentSlice`
- `mMTC-InconsistentSlice`

When the prefix of sliceType conflicts with serviceType, report a consistency issue.

Examples:
- serviceType = `mMTC`, sliceType = `eMBB-InconsistentSlice`: inconsistent.
- serviceType = `URLLC`, sliceType = `mMTC-InconsistentSlice`: inconsistent.
- serviceType = `eMBB`, sliceType = `URLLC-InconsistentSlice`: inconsistent.
