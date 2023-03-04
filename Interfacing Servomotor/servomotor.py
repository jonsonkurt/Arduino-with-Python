import pyfirmata

from time import sleep

class Servomotor:

    def __init__(self):
        self.setup()
        self.run()

    def setup(self):
        self.port = 'COM3'
        self.board = pyfirmata.Arduino(self.port)
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()

        self.servo = self.board.get_pin('d:9:s')
        
    def rotate_servo(self, angle):
        self.servo.write(angle)
        sleep(0.015)

    def run(self):
        while True:
            self.rotate_servo(180)
            sleep(1)
            self.rotate_servo(0)
            sleep(1)
        
def main():
    servomotor_start = Servomotor()

if __name__ == '__main__':
    main()
