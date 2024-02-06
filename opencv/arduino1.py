import serial

ser = serial.Serial('COM3', 9600, timeout= .1)

# def writeserial(x):

#     ser.write(bytes(x.encode('utf-8')))

# num = input("Enter a number: ")
# val = writeserial(num)

ser.write('7'.encode('utf-8'))

ser.close()