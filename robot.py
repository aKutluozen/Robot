# Ali Kutluozen - 7/18/19
class Robot:
    '''
    Robot class:
    Sets up GPIO pins and motors.
    Defines basic functionality
    '''

    import Jetson.GPIO as io
    import time

    def __init__(self):
        self.right_motor = [35, 33, 37] # yellow, orange, red
        self.left_motor = [19, 21, 23] # gray, purple, green
        self.motors = list(self.right_motor + self.left_motor)

        self.directions = {
            'forward': [1, 1, 0, 1, 1, 1],
            'backward': [1, 1, 1, 1, 1, 0],
            'left': [1, 1, 0, 1, 1, 0],
            'right': [1, 1, 1, 1, 1, 1]
        }

        self.io.setmode(self.io.BOARD)
        self.io.setup(self.motors, self.io.OUT)

    def move(self, direction, duration=0):
        '''
        Transfer the movement to motors

        :param str direction: Direction of movement
        :param int duration: Duration of movement
        '''
        self.io.output(self.motors, self.directions[direction])
        self.time.sleep(duration)

    def stop(self):
        self.io.output(self.motors, [0, 0, 0, 0, 0, 0])

    def clear(self):
        self.io.cleanup()
