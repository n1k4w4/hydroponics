import urllib.request, json
import MyPyDHT
import smbus
import getpass
import hashlib

if __name__ == '__main__':
    url = "http://104.215.14.58:80/statuses/"
    method = "POST"
    humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 26)
    bus = smbus.SMBus(1)
    addr = 0x23
    lux = bus.read_i2c_block_data(addr,0x10)
    obj = {
            "temp" : temperature,
            "hum" : humidity,
            "wtemp" : 15,
            "lux" : (lux[0]*256+lux[1])/1.2,
            "EC" : 15,
            "CO2" : 23,
            }
    p = getpass.getpass(prompt='Password : ')
    h = hashlib.sha256(p.encode()).hexdigest()
    print(h)
    data = {
            "username" : "dai",
            "password" : h,
            "statuses" : obj
            }
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type" : "application/json"}

    request = urllib.request.Request(url, data=json_data, headers=headers, method=method)
    try :
        response = urllib.request.urlopen(request)
        response_body = response.read().decode("utf-8")
        print("Success")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
