'''
Author: linin00
Date: 2022-12-12 14:00:32
LastEditTime: 2022-12-12 15:22:36
LastEditors: linin00
Description: 
FilePath: /open/Gesture/test/mqtt_pub.py

'''
import sys
sys.path.append('Gesture/core')
from mqtt_utils import Mqtt

if __name__ == '__main__':
  mqtt = Mqtt('dev.linin.xyz', 8302)
  mqtt.PUB('LJ', 'testing')