import serial

# Open the serial port (update the port and baudrate based on your Arduino configuration)
ser = serial.Serial('COM3', 9600)

# Read data from Arduino
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').rstrip()
        print(f"Received from Arduino: {data}")
