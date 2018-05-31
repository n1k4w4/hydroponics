import urllib.request, json
import MyPyDHT

if __name__ == '__main__':
    url = "http://104.215.14.58:80/statuses/"
    method = "POST"
    humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 26)
    obj = {
            "temp" : str(temperature),
            "hum" : str(humidity),
            "wtemp" : 15,
            "lux" : 22,
            "EC" : 15,
            "CO2" : 23,
            }
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type" : "application/json"}

    request = urllib.request.Request(url, data=json_data, headers=headers, method=method)
    try :
        response = urllib.request.urlopen(request)
        response_body = response.read().decode("utf-8")
        print("Success")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
