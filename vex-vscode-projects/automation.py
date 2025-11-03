from vex import *
from vex import Sonar
from vex import Brain
from vex import Light
from vex import Distance

#Initialize brain
brain=Brain()

#Initialize motors
motor1 = Motor(Ports.PORT1)
motor2 = Motor(Ports.PORT2)
motor3 = Motor(Ports.PORT3)

#Initialize sensors
sonar1=Sonar(brain.three_wire_port.d)
sonar2=Sonar(brain.three_wire_port.e)
button1=Bumper(brain.three_wire_port.f)
accel1=Accelerometer(brain.three_wire_port.h)
distance1 = Distance(brain.three_wire_port.d)

# Assign variable to distance value
proxToBall = distance1
def vex.Distance.object_distance()

# Movement
