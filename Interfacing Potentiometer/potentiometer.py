import pyfirmata

from time import sleep

class Potentiometer:

    def __init__(self):
        self.setup()
        self.run()

    def setup(self):
        self.port = 'COM6'
        self.board = pyfirmata.Arduino(self.port)
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()

        self.HIGH = True
        self.LOW = False

        self.pot = self.board.get_pin('a:2:i')
        self.red = self.board.get_pin('d:11:o')
        self.green = self.board.get_pin('d:10:o')
        self.blue = self.board.get_pin('d:9:o')

    def run(self):
        while True:
            self.pot_val = self.pot.read()
            print("The value of Potentiometer Reading: " + str(self.pot_val))
            
            if self.pot_val is None:
                continue

            elif self.pot_val >= 0 and self.pot_val < 0.320:
                self.red.write(self.HIGH)
                sleep(1)
                self.red.write(self.LOW)

            elif self.pot_val >= 0.320 and self.pot_val < 0.900:
                self.green.write(self.HIGH)
                sleep(1)
                self.green.write(self.LOW)

            elif self.pot_val >= 0.900 and self.pot_val <= 1:
                self.blue.write(self.HIGH)
                sleep(1)
                self.blue.write(self.LOW)

            sleep(1)
def main():
    potentiometer_start = Potentiometer()

if __name__ == '__main__':
    main()
