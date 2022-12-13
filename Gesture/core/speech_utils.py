'''
Author: linin00
Date: 2022-12-13 22:26:49
LastEditTime: 2022-12-13 22:49:24
LastEditors: linin00
Description: 
FilePath: /open/Gesture/core/speech_utils.py

'''
import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
from pynput.keyboard import Key, Listener
sys.path.append('./Gesture/core')
from mqtt_utils import Mqtt_async
import sys
sys.path.append('./Speech')
from Speech import record, getSpeak, attack, start


class Speech():
  def __init__(self, mqtt: Mqtt_async, prefix: str):
    self.mqtt = mqtt
    self.prefix = prefix
  def listen(self):
    start(self.mqtt, self.prefix)

if __name__ == '__main__':
  speech = Speech(None, None)
  speech.listen()
