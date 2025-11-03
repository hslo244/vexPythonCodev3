# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ajim                                                         #
# 	Created:      3/21/2024, 3:26:26 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
from vex import Sonar
from vex import Brain
from vex import Light

# Brain should be defined by default
brain=Brain()

#Initialize sensors
sonar1=Sonar(brain.three_wire_port.d)
sonar2=Sonar(brain.three_wire_port.e)
button1=Bumper(brain.three_wire_port.f)
accel1=Accelerometer(brain.three_wire_port.h)

#Initialize motors
motor1 = Motor(Ports.PORT1)
motor2 = Motor(Ports.PORT2)
motor3 = Motor(Ports.PORT3)

# Initialize controller
controller_1 = Controller(ControllerType.PRIMARY)

# Assign joystick values to variables
left_stick_y = controller_1.axis3.position()
right_stick_y = controller_1.axis2.position()

# Sonar and button value logic
sonarDist=sonar1.value()
if sonarDist < 1:
    motor1.set_velocity(0)
if button1.pressed == True:
    motor3.set_velocity(0)
if accel1.acceleration == True:
    motor1.set_velocity(30,RPM)
    motor2.set_velocity(30,RPM)

# Automated movement
    
# Set motor speeds based on joystick values
    motor1.set_velocity(left_stick_y, RPM)
    motor2.set_velocity(right_stick_y, RPM)