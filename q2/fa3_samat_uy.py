# FA3 - Science Lab Inventory System
# Name: Amber Gail C. Uy
# Section: 9-Samat


from abc import ABC, abstractmethod


# Abstract Base Class
class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


# Child class for pH sensors
class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")


# Child class for temperature sensors
class TempSensor(Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")


# Create one object for each sensor type
ph_sensor = PHSensor()
temp_sensor = TempSensor()


# Display sensor readings
print("--- Lab Inventory System ---")
ph_sensor.get_reading()
temp_sensor.get_reading()
