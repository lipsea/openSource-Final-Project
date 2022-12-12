'''
Author: linin00
Date: 2022-12-11 11:51:43
LastEditTime: 2022-12-12 15:21:03
LastEditors: linin00
Description: 
FilePath: /open/Gesture/core/mqtt_utils.py

'''

import paho.mqtt.client as mqtt
import json
import time
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))

class Mqtt:

    def __init__(self, host, post):
        self.host = host
        self.post = post
        self.mqttClient = mqtt.Client()
        self.mqttClient.on_connect = on_connect
        self.mqttClient.on_message = on_message
        self.__connect()

    def __connect(self):
        self.mqttClient.connect(self.host, self.post, 60)
        # self.mqttClient.loop_start()

    def PUB(self, topic, payload, qos=1):
        """发布信息"""
        self.mqttClient.publish(topic, payload, qos)

    def SUB(self, topic, qos=1):
        """订阅频道"""
        self.mqttClient.subscribe(topic, qos)
        self.mqttClient.loop_forever()
