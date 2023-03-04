import pyfirmata, pyfirmata.util

from time import sleep

class Potentiometer:

    def __init__(self, baudrate):
        self.baudrate = baudrate
        self.setup()
        self.run()

    def setup(self):
        self.port = 'COM6'
        self.board = pyfirmata.Arduino(self.port)
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()
        self.HIGH = True
        self.LOW = False

        self.green1 = self.board.get_pin('d:2:o')
        self.green2 = self.board.get_pin('d:4:o')
        self.yellow1 = self.board.get_pin('d:6:o')
        self.yellow2 = self.board.get_pin('d:8:o')
        self.red1 = self.board.get_pin('d:10:o')
        self.red2 = self.board.get_pin('d:12:o')
        self.button = self.board.get_pin('d:13:o')
        self.potentiometer = self.board.get_pin('a:0:i')
        
        self.digits =  [[0,0,1,1,0,0,0,0], # digit 1 
                        [0,1,1,0,1,1,0,1], # digit 2
                        [0,1,1,1,1,0,0,1], # digit 3
                        [0,0,1,1,0,0,1,1], # digit 4
                        [0,1,0,1,1,0,1,1], # digit 5
                        [0,1,0,1,1,1,1,1]] # digit 6
        
        self.DS1_pin = self.board.get_pin('d:3:o')
        self.STCP1_pin = self.board.get_pin('d:5:o')
        self.SHCP1_pin = self.board.get_pin('d:7:o')
        
    def display_digit(self, digit):
        self.STCP1_pin.write(self.LOW)
        self.selected_digit = self.digits[digit]
        
        for i in self.selected_digit:
            self.SHCP1_pin.write(self.LOW)
            
            if i == 0:
                self.DS1_pin.write(self.LOW)
            elif i == 1:
                self.DS1_pin.write(self.HIGH)
            
            self.SHCP1_pin.write(self.HIGH)
            
        self.STCP1_pin.write(self.HIGH)
            

    def run(self):
        while True:
            self.val = self.potentiometer.read()
            print("The value of Potentiometer Reading: " + str(self.val))
            
            if self.val is None:
                continue
            
            elif self.val < 0.166:
                self.green1.write(self.HIGH)
                self.button.write(self.LOW)
                
            elif 0.166 < self.val < 0.332:
                self.green1.write(self.HIGH)
                self.green2.write(self.HIGH)
                self.button.write(self.LOW)
                
            elif 0.332 < self.val < 0.498:
                self.green1.write(self.HIGH)
                self.green2.write(self.HIGH)
                self.yellow1.write(self.HIGH)
                self.button.write(self.LOW)
                
            elif 0.498 < self.val < 0.664:
                self.green1.write(self.HIGH)
                self.green2.write(self.HIGH)
                self.yellow1.write(self.HIGH)
                self.yellow2.write(self.HIGH)
                self.button.write(self.LOW)
                
            elif 0.664 < self.val < 0.83:
                self.green1.write(self.HIGH)
                self.green2.write(self.HIGH)
                self.yellow1.write(self.HIGH)
                self.yellow2.write(self.HIGH)
                self.red1.write(self.HIGH)
                self.button.write(self.HIGH)
                
            elif 0.83 < self.val < 0.996:
                self.green1.write(self.HIGH)
                self.green2.write(self.HIGH)
                self.yellow1.write(self.HIGH)
                self.yellow2.write(self.HIGH)
                self.red1.write(self.HIGH)
                self.red2.write(self.HIGH)
                self.button.write(self.HIGH)
                sleep(.5)
            

            if self.val < 0.996:
                self.red2.write(self.LOW)
                self.button.write(self.LOW)
                
            if self.val < 0.83:
                self.red2.write(self.LOW)
                self.red1.write(self.LOW)
                self.button.write(self.LOW)
                
            if self.val < 0.664:
                self.red2.write(self.LOW)
                self.red1.write(self.LOW)
                self.yellow2.write(self.LOW)
                
            if self.val < 0.498:
                self.red2.write(self.LOW)
                self.red1.write(self.LOW)
                self.yellow2.write(self.LOW)
                self.yellow1.write(self.LOW)
                
            if self.val < 0.332:
                self.red2.write(self.LOW)
                self.red1.write(self.LOW)
                self.yellow2.write(self.LOW)
                self.yellow1.write(self.LOW)
                self.green2.write(self.LOW)
                
            else:
                self.red2.write(self.LOW)
                self.red1.write(self.LOW)
                self.yellow2.write(self.LOW)
                self.yellow1.write(self.LOW)
                self.green2.write(self.LOW)
                self.green1.write(self.LOW)

def main():
    potentiometer_start = Potentiometer(115200)

if __name__ == '__main__':
    main()
