import serial

class LightControl:

    def __init__(self,baudrate,port = '/dev/ttyUSB0'):
        try:
            self.ser = serial.Serial()
            self.ser.port = port
            self.ser.baudrate = baudrate
            self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
            self.ser.parity = serial.PARITY_NONE #set parity check: no parity
            self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits
            self.ser.timeout = 1            #non-block read
            self.ser.xonxoff = False     #disable software flow control
            self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
            self.ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
            self.ser.writeTimeout = 2     #timeout for write
        except serial.SerialException:
            print('Serial Fail')
            return False

    def connect(self):
        try:
            self.ser.open()
            return True
        except serial.SerialException:
            return False

    def power_on(self):
        cmd = '\xA9\x05\x00\x00\x1F\x01\xDB\x5C'
        self.ser.write(cmd)

    def power_off(self):
        cmd = '\xA9\x05\x00\x00\x1F\x00\xDC\x5C'
        self.ser.write(cmd)

    def set_intensity(self):
        cmd = '\xA9\x07\x00\x00\x09\x80\x80\x00\xF0\x5C'
        self.ser.write(cmd)

    def disconnet(self):
        self.ser.close()

    def forward(self,txmessage):
        self.ser.write(txmessage)
