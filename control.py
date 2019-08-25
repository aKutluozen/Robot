#!/usr/bin/env python3

# Import required modules
import tty
import sys
import termios
from robot import Robot

robot = Robot()

print('\nWelcome!\n - Please use WASD keys to move the robot, any other key to stop it, and ESC to stop the program.')

orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
char = 0
while char != chr(27): # ESC
    char = sys.stdin.read(1)[0]
    if char == 'w':
        robot.move('forward')
    elif char == 's':
        robot.move('backward')
    elif char == 'a':
        robot.move('left')
    elif char == 'd':
        robot.move('right')
    else:
        robot.stop()
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    

robot.clear()
print('done')


