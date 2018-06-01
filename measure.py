import MyPyDHT

humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 26)
print("temperature=" + str(temperature) + "*C", "humidity=" + str(humidity) + "%")
