#21BCT0345
#Rakeem Shaikh
import random
import time

def generate_sensor_data():
    """
    Simulate various IoT sensor data including air quality, light intensity, 
    CO2 levels, noise levels, motion, GPS, and battery level.It returns a dictionary with 
    simulated sensor data for different parameters.
    """
    return {
        'air_quality_pm25': random.uniform(0.0, 500.0),  # the air quality data
        'air_quality_pm10': random.uniform(0.0, 500.0), 
        'light_intensity': random.uniform(0.0, 1000.0),  # Light intensity 
        'pressure': random.uniform(950.0, 1050.0),       # Atmospheric pressure 
        'co2_levels': random.uniform(300.0, 5000.0),     # CO2 levels 
        'noise_levels': random.uniform(30.0, 100.0),     # Noise levels 
        'motion_detected': random.choice([True, False]), # Motion detection 
        'gps_coordinates': (random.uniform(-90, 90), random.uniform(-180, 180)), # Latitude, Longitude
        'battery_level': random.uniform(0.0, 100.0)      # Battery level 
    }

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        print(data)
        time.sleep(5)  # Simulate periodic data generation with a time delay of 5 sec
