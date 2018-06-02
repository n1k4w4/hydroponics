import smbus

bus = smbus.SMBus(1)
addr = 0x23
lux = bus.read_i2c_block_data(addr,0x10)

print ("lux : " + str((lux[0]*256+lux[1])/1.2))
