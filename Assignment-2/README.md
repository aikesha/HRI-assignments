# ROBT 414 Programming Assignment 2
### Note: This assignment is about a “Follow Me” application on a NAO robot using Python NaoQi.
The result in Youtube -> [here](https://youtu.be/YIftSNFQ2hc)
## Requirements:
* Ubuntu 16.04 (also you can use Win or Mac)
* Python 2.7.12
* Choregraph 2.6 

For installation you can use this [website](https://developer.softbankrobotics.com/nao-naoqi-2-1)

## Goal:
The task was aimed for smooth motion. Upon the start of the
application, the robot wave hello and say: “Hi, Aigerim! I want to come with you”.
Then, the robot raises one of its arms for the user to hold it. Robot’s wrist was used as a
steering wheel to change direction (i.e. to turn right or left), and robot’s shoulder to control
the robot’s speed (e.g. when its arm is up, the robot moves faster, when it is at 90-degree
angle, the robot moves slower; when it is dropped, the robot stops).

## How to start? 

* Create your workspace and connect to a robot by using this commands:
```Linux Terminal
export PYTHONPATH=${PYTHONPATH}:/path/to/python-sdk/lib/python2.7/site-packages
export QI_SDK_PREFIX=/path/to/python-sdk
```
* Import Naoqi into your Python
```
python
import naoqi
exit()
```
* Launch Choregraphe
```terminal
./choregraphe
```
* Run your Python Script
```python
python test-4.py
```
<img src="images/nao_robot.jpg"


## Good Luck!
