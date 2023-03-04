import pyfirmata, pyfirmata.util

from time import sleep

class Thermistor:

    def __init__(self, baudrate):
        self.baudrate = baudrate
        self.setup()
        self.run()

    def setup(self):
        self.port = 'COM3'
        self.board = pyfirmata.Arduino(self.port)
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()
        
        self.HIGH = True
        self.LOW = False

        self.thermis = self.board.get_pin('a:4:i')
        self.buzzer = self.board.get_pin('d:3:o')

    def run(self):
        while True:
            x = self.thermis.read()
            print("The value of Thermistor Reading: " + str(x))

            if x == None:
                continue
            
            elif x > 0.050:
                self.buzzer.write(self.HIGH)
                sleep(0.5)
                
            else:
                self.buzzer.write(self.LOW)

def main():
    thermi_start = Thermistor(115200)

if __name__ == '__main__':
    main()
