import serial
import time

# Open the serial port (update the port and baudrate based on your Arduino configuration)
ser = serial.Serial('COM3', 9600)

# Write data to Arduino (include newline character)
ser.write("Hello from Python!\n".encode('utf-8'))

# Close the serial port
ser.close()

time.sleep(1)
