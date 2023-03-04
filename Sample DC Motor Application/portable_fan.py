import pyfirmata

from time import sleep

class DCMotor:

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

        # Pin configuration of DC Motor
        self.motor = self.board.get_pin('d:10:o')
        self.motor_pwm = self.board.get_pin('d:9:p')

        # Pin configuration of Button
        self.prev_button_state = 0
        self.button = self.board.get_pin('d:13:i')
        
        # Pin configuration of One Digit 7-Segment Display
        self.DS1_pin = self.board.get_pin('d:4:o')
        self.STCP1_pin = self.board.get_pin('d:3:o')
        self.SHCP1_pin = self.board.get_pin('d:2:o')
        self.digits =  [[0,1,1,1,1,1,1,0], # Digit 0
                        [0,0,0,0,1,1,0,0], # Digit 1 
                        [1,0,1,1,0,1,1,0], # Digit 2
                        [1,0,0,1,1,1,1,0], # Digit 3
                        [1,1,0,0,1,1,0,0], # Digit 4
                        [1,1,0,1,1,0,1,0], # Digit 5
                        [1,1,1,1,1,0,1,0]] # Digit 6

    def display_digit(self, digit):
        self.STCP1_pin.write(self.LOW)
        self.selected_digit = self.digits[digit]
        
        for i in self.selected_digit:
            self.SHCP1_pin.write(self.LOW)

            if i == 0:
                self.DS1_pin.write(self.LOW)
            if i == 1:
                self.DS1_pin.write(self.HIGH)
            
            self.SHCP1_pin.write(self.HIGH)
         
        self.STCP1_pin.write(self.HIGH)

    def rotate_motor(self, state, speed):
        self.motor.write(state) # To turn on or off the motor
        self.motor_pwm.write(speed) # To adjust the motor speed
        
    def run(self):
        count = 0
        
        while True:
            self.prev_button_state = self.button.read()

            if self.prev_button_state == None:
                self.display_digit(0)
                continue

            if self.prev_button_state == True:
                count += 1
                sleep(0.05)

                if count == 1:
                    self.rotate_motor(1,0.25)
                    self.display_digit(1)
                    sleep(1)
                elif count == 2:
                    self.rotate_motor(1,0.75)
                    self.display_digit(2)
                    sleep(1)
                elif count == 3:
                    self.rotate_motor(1,1)
                    self.display_digit(3)
                    sleep(1)
                elif count == 4:
                    self.rotate_motor(0,0)
                    self.display_digit(0)
                    count = 0
                    break

def main():
    dcmotor_start = DCMotor()

if __name__ == '__main__':
    main()
