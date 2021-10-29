import serial

serialcomm = serial.Serial('COM3', baudrate = 9600, timeout = 1)

while True:
    serialcomm.write('f'.encode())