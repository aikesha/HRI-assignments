from naoqi import ALProxy
import time
import math

textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)

# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

textSpeakProxy.say("Hi, Aigerim!")
textSpeakProxy.say("I want to come with you")

names.append("RShoulderPitch")
times.append([0.96])
keys.append([[-1.30725, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1.64, 2.36, 3, 3.68, 4.32])
keys.append([[-0.757473, [3, -0.56, 0], [3, 0.24, 0]], [-0.00872665, [3, -0.24, 0], [3, 0.213333, 0]], [-1.05592, [3, -0.213333, 0], [3, 0.226667, 0]], [-0.0279253, [3, -0.226667, 0], [3, 0.213333, 0]], [-1.028, [3, -0.213333, 0], [3, 0, 0]]])

try:
  motion = ALProxy("ALMotion", "127.0.0.1", 9559)
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err

shoulderName = "RShoulderPitch"
wristName = "RWristYaw"

useSen = 0
useSen1 = 0

while(1):
        
	x = motionProxy.getAngles(shoulderName, useSen)
        y = motionProxy.getAngles(wristName, useSen1)

	#print(x[0]) #right hand position in degrees
        #print(y[0]) #right hand position in degrees

        if x[0] <= (-0.6) :
             if y[0] < -0.7 :
                 motionProxy.moveTo(0.0, 0.0, 1.57) #radians +90 deg
                 motionProxy.move(3.0, 0.0, 0.0)
             elif y[0] > 0.7 :
                 motionProxy.moveTo(0.0, 0.0, -1.57) #radians -90 deg
                 motionProxy.move(3.0, 0.0, 0.0)
             else :
                 motionProxy.move(3.0, 0.0, 0.0)

        elif x[0] > (-0.6) and x[0] <= 0.8 :
             if y[0] < -0.7 :
                 motionProxy.moveTo(0.0, 0.0, 1.57) #radians +90 deg
                 motionProxy.move(0.5, 0.0, 0.0)
             elif y[0] > 0.7 :
                 motionProxy.moveTo(0.0, 0.0, -1.57) #radians -90 deg
                 motionProxy.move(0.5, 0.0, 0.0)
             else :
                 motionProxy.move(0.5, 0.0, 0.0)

        elif x[0] > 0.8:
             if y[0] < -0.7 :
                 motionProxy.moveTo(0.0, 0.0, 1.57) #radians +90 deg
                 motionProxy.move(0.0, 0.0, 0.0)
             elif y[0] > 0.7 :
                 motionProxy.moveTo(0.0, 0.0, -1.57) #radians -90 deg
                 motionProxy.move(0.0, 0.0, 0.0)
             else :
                 motionProxy.move(0.0, 0.0, 0.0)

  
        time.sleep(3)


