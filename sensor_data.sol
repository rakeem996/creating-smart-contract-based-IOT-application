// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SensorData {
    struct Data {
        uint256 air_quality_pm25;
        uint256 air_quality_pm10;
        uint256 light_intensity;
        uint256 pressure;
        uint256 co2_levels;
        uint256 noise_levels;
        bool motion_detected;
        uint256 latitude;
        uint256 longitude;
        uint256 battery_level;
        uint256 timestamp;
    }

    Data[] public dataEntries;

    function storeData(
        uint256 _air_quality_pm25,
        uint256 _air_quality_pm10,
        uint256 _light_intensity,
        uint256 _pressure,
        uint256 _co2_levels,
        uint256 _noise_levels,
        bool _motion_detected,
        uint256 _latitude,
        uint256 _longitude,
        uint256 _battery_level
    ) public {
        dataEntries.push(Data({
            air_quality_pm25: _air_quality_pm25,
            air_quality_pm10: _air_quality_pm10,
            light_intensity: _light_intensity,
            pressure: _pressure,
            co2_levels: _co2_levels,
            noise_levels: _noise_levels,
            motion_detected: _motion_detected,
            latitude: _latitude,
            longitude: _longitude,
            battery_level: _battery_level,
            timestamp: block.timestamp
        }));
    }

    function getData(uint256 index) public view returns (
        uint256, uint256, uint256, uint256, uint256, uint256, bool, uint256, uint256, uint256, uint256
    ) {
        Data memory data = dataEntries[index];
        return (
            data.air_quality_pm25, data.air_quality_pm10, data.light_intensity,
            data.pressure, data.co2_levels, data.noise_levels, data.motion_detected,
            data.latitude, data.longitude, data.battery_level, data.timestamp
        );
    }
}
