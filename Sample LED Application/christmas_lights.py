import pyfirmata, pyfirmata.util
import random

from time import sleep

class ChristmasLights:

    def __init__(self, baudrate):
        self.baudrate = baudrate
        self.setup()
        self.run()
        self.exit()

    def setup(self):
        self.port = 'COM3'
        self.board = pyfirmata.Arduino(self.port)
        self.HIGH = True
        self.LOW = False
        self.prev_button_state = 0
        
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()
        
        self.combination = [self.HIGH, self.LOW, self.HIGH, self.LOW, self.HIGH, self.LOW]
        
    def combination1(self):
        self.red.write(self.HIGH)
        self.green.write(self.LOW)
        self.blue.write(self.HIGH)
        self.yellow.write(self.LOW)
        sleep(0.5)
        
        self.red.write(self.HIGH)
        self.green.write(self.HIGH)
        self.blue.write(self.LOW)
        self.yellow.write(self.HIGH)
        sleep(0.5)
        
        self.red.write(self.LOW)
        self.green.write(self.HIGH)
        self.blue.write(self.LOW)
        self.yellow.write(self.HIGH)
        sleep(0.5)
        
        self.red.write(self.HIGH)
        self.green.write(self.LOW)
        self.blue.write(self.LOW)
        self.yellow.write(self.LOW)
        sleep(0.5)
        
        self.red.write(self.LOW)
        self.green.write(self.LOW)
        self.blue.write(self.LOW)
        self.yellow.write(self.LOW)
        sleep(0.5)
        
    def combination2(self):
        self.red.write(random.choice(self.combination))
        self.green.write(random.choice(self.combination))
        self.blue.write(random.choice(self.combination))
        self.yellow.write(random.choice(self.combination))
        sleep(0.5)
        
        self.red.write(random.choice(self.combination))
        self.green.write(random.choice(self.combination))
        self.blue.write(random.choice(self.combination))
        self.yellow.write(random.choice(self.combination))
        sleep(0.5)
        
        self.red.write(random.choice(self.combination))
        self.green.write(random.choice(self.combination))
        self.blue.write(random.choice(self.combination))
        self.yellow.write(random.choice(self.combination))
        sleep(0.5)
        
        self.red.write(random.choice(self.combination))
        self.green.write(random.choice(self.combination))
        self.blue.write(random.choice(self.combination))
        self.yellow.write(random.choice(self.combination))
        sleep(0.5)
        
        self.red.write(self.LOW)
        self.green.write(self.LOW)
        self.blue.write(self.LOW)
        self.yellow.write(self.LOW)
        sleep(0.5)
    
    def run(self):
        self.blue = self.board.get_pin('d:11:o')
        self.green = self.board.get_pin('d:12:o')
        self.red = self.board.get_pin('d:13:o')
        self.yellow = self.board.get_pin('d:10:o')
        self.pushbutton = self.board.get_pin('d:8:i')
        self.buzzer = self.board.get_pin('d:9:o')
        
        self.count = 0
        self.count2 = 0

        while True:
            self.prev_button_state = self.pushbutton.read()
            
            if self.prev_button_state == self.HIGH:
                self.count += 1
                
                if self.count2 <= 8:
                    self.count2 += 1
                    
                    if self.count == 1:
                        while self.count == 1:
                            self.combination1()
                            self.prev_button_state = self.pushbutton.read()
                            if self.prev_button_state == True:
                                print('Combination 1 Ended')
                                self.buzzer.write(self.HIGH)
                                sleep(0.05)
                                self.buzzer.write(self.LOW)
                                break
                        
                    elif self.count == 2:
                        while self.count == 2:
                            self.combination2()
                            self.prev_button_state = self.pushbutton.read()
                            if self.prev_button_state == True:
                                print('Combination 2 Ended')
                                self.buzzer.write(self.HIGH)
                                sleep(0.05)
                                self.buzzer.write(self.LOW)
                                break
                        
                    elif self.count > 2:
                        self.count = 0
                else:
                    break
            else:
                print('Program is Running')

    def exit(self):
        self.red.write(self.LOW)
        self.green.write(self.LOW)
        self.blue.write(self.LOW)
        self.yellow.write(self.LOW)
        self.board.exit()

def main():
    obj_pushbutton = ChristmasLights(115200)

if __name__ == '__main__':
    main()