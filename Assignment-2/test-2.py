from naoqi import ALProxy
import time
import math


textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)


#10.1.198.45
handName = "LHand"

useSen = 0

# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LAnklePitch")
times.append([2.6])
keys.append([[0.0383972, [3, -0.88, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([2.6])
keys.append([[-0.0767945, [3, -0.88, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([2.6])
keys.append([[-0.380482, [3, -0.88, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([2.6])
keys.append([[0.0314159, [3, -0.88, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([2.6])
keys.append([[0.202458, [3, -0.88, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.96, 1.8])
keys.append([[-1.6057, [3, -0.333333, 0], [3, 0.28, 0]], [-1.6057, [3, -0.28, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.5])
keys.append([[-0.439823, [3, -0.88, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.5])
keys.append([[-0.10821, [3, -0.88, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.5])
keys.append([[0.0314159, [3, -0.88, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.5])
keys.append([[0.753982, [3, -0.88, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.5])
keys.append([[-1.52716, [3, -0.333333, 0], [3, 0, 0]]])

textSpeakProxy.say("Hello Aikesha!")

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "127.0.0.1", 9559)
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err


while(1):
        
	x = motionProxy.getAngles(handName, useSen)

	print(x[0]) #left hand position in degrees

        textSpeakProxy.say("Go forward!")
	motionProxy.moveTo(x[0], 0.0, 0.0)
        textSpeakProxy.say("Stop!")
        time.sleep(5)
        
        textSpeakProxy.say("Turn Right!")
        motionProxy.moveTo(0.0, 0.0, -1.57) #radians -45 deg
        textSpeakProxy.say("Turn Left!")
        motionProxy.moveTo(0.0, 0.0, 3.14) #radians +90 deg
  
        time.sleep(10)


