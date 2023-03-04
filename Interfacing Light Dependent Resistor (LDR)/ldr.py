import pyfirmata, pyfirmata.util

from time import sleep

class LDR:

    def __init__(self):
        self.setup()
        self.run()

    def setup(self):
        self.port = 'COM3'
        self.board = pyfirmata.Arduino(self.port)
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()
        
        self.HIGH = True
        self.LOW = False

        self.ldr = self.board.get_pin('a:0:i')
        self.rpin = self.board.get_pin('d:6:o')
        self.gpin = self.board.get_pin('d:5:o')
        self.bpin = self.board.get_pin('d:3:o')

    def run(self):
        while True:
            x = self.ldr.read()
            print("The value of LDR Reading: " + str(x))
            
            if x == None:
                continue
            
            elif x <= 0.17:
                self.rpin.write(self.HIGH)
                self.bpin.write(self.HIGH)
                self.gpin.write(self.LOW)
                print("Output Color: Purple")
                sleep(.150)

            elif x > 0.17 and x <= 0.34:
                self.bpin.write(1)
                self.rpin.write(0)
                self.gpin.write(0)
                print("Output Color: Blue")
                sleep(.150)

            elif x > 0.34 and x <= 0.50:
                self.gpin.write(1)
                self.rpin.write(0)
                self.bpin.write(0)
                print("Output Color: Green")
                sleep(.150)

            elif x > 0.50 and x <= 0.67:
                self.rpin.write(1)
                self.gpin.write(1)
                self.bpin.write(0)
                print("Output Color: Yellow")
                sleep(.150)

            elif x > 0.67 and x <= 0.84:
                self.rpin.write(1)
                self.gpin.write(1)
                self.bpin.write(0)
                print("Output Color: Orange")
                sleep(.150)

            elif x > 0.84:
                self.rpin.write(1)
                self.gpin.write(0)
                self.bpin.write(0)
                print("Output Color: Red")
                sleep(.150)

def main():
    ldr_start = LDR()

if __name__ == '__main__':
    main()
