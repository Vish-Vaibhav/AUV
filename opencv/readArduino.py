import serial


def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().split()
        if data:
            print(data)
    


if __name__ == '__main__':

    readserial('COM3', 9600)
