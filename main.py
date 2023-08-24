from machine import Pin, I2C
i2c = I2C(0, scl=Pin(13),sda=Pin(12 ),freq=100000)

def radio(frequency, volume, onlyVolume=False, mute=False): 
    freqB = round((frequency-87)*10) #Rounded because of the float variables "Noise".
    
    data = bytearray(8)
    if(mute):       data[0] = (0xC0-64)
    else:           data[0] =  0xC0
    data[1] = 0x05
    data[2] = ( freqB & 0b1111111100) >> 2
    if(onlyVolume): data[3] = ((freqB & 0b0000000011) << 6)
    else:           data[3] = ((freqB & 0b0000000011) << 6) + 0b10000
    data[4] = 0x02
    data[5] = 0x00
    data[6] = 0x08
    data[7] = (0x80 | volume)
    
    i2c.writeto(0x10, data)
  #radio(frequency= XX.X, volume= 0-15, onlyVolume=False/True, mute=False/True)
  #When only changing the volume, set onlyVolume parameter to True so it only changes the volume and doesn't retune
