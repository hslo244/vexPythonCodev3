# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ajim                                                         #
# 	Created:      1/30/2024, 3:20:16 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
from vex import Motor, DirectionType
from vex import Controller
from vex import ControllerType
from vex import Brain

# Brain should be defined by default
brain=Brain()

# Initialize motors
motor1 = Motor(Ports.PORT1)
motor2 = Motor(Ports.PORT2)
motor3 = Motor(Ports.PORT3)

# Define velocity for the buttons
veloButton1 = 100
veloButton2 = -50

# Initialize controllers
controller_1 = Controller(ControllerType.PRIMARY)

while True:
    # Read the joystick and button values
    left_stick_y = controller_1.axis3.position()
    right_stick_y = controller_1.axis2.position()
    up_button_pressed = controller_1.buttonUp.pressing()
    down_button_pressed = controller_1.buttonDown.pressing()
    buttonL1_pressed = controller_1.buttonL1.pressing()
    val1 = 1
    stick_status= False
    up_button_status = False

# Set motor speeds based on joystick values
    motor1.set_velocity(left_stick_y, RPM)
    motor2.set_velocity(right_stick_y, RPM)

    # Adjust motor speed based on button presses
    if left_stick_y > val1:
        stick_status = True
    if up_button_pressed == val1:
        up_button_status = True
    if stick_status == True and up_button_status == True:
        motor3.set_velocity(left_stick_y, RPM)
        

# idk if the buttons work lol    
    if up_button_pressed:
        brain.screen.print("Up button works!")

    # Spin motors
    motor1.spin(FORWARD)
    motor2.spin(FORWARD)
    motor3.spin(FORWARD)