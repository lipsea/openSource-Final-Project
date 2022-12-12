'''
Author: linin00
Date: 2022-12-07 18:45:02
LastEditTime: 2022-12-12 15:33:07
LastEditors: linin00
Description: 
FilePath: /open/Gesture/core/mediapipe_utils.py

'''

import cv2
import mediapipe as mp
import numpy as np
import sys
sys.path.append('./Gesture/core/type')
from Gesture import Gesture

# 手部识别
class HandDetector():
  def __init__(self,
              mode=False,
              maxHands=1,
              minDetectionConfidence=0.5,
              minTrackingConfidence=0.5): # 默认识别一只手
    self.__mpHands = mp.solutions.hands
    self.__hands = self.__mpHands.Hands(
      static_image_mode=mode,
      max_num_hands=maxHands,
      min_detection_confidence=minDetectionConfidence,
      min_tracking_confidence=minTrackingConfidence
    )
    self.__mpDraw = mp.solutions.drawing_utils

  def findHands(self, img, draw = True): # 识别手部关键点，默认在传入的图片上画出来
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    self.__results = self.__hands.process(imRGB)
    if draw and self.__results.multi_hand_landmarks :
      for handsLms in self.__results.multi_hand_landmarks :
        self.__mpDraw.draw_landmarks(img, handsLms, self.__mpHands.HAND_CONNECTIONS)

  def trackLandmark(self, img, index, draw = True): # 跟踪某一个关键点坐标，默认在传入的图片上画出来，返回值是关键点的像素坐标
    res = []
    if self.__results.multi_hand_landmarks :
      for handsLms in self.__results.multi_hand_landmarks :
        for id, lm in enumerate(handsLms.landmark) :
          h, w, c = img.shape
          cx, cy = int (lm.x * w), int(lm.y * h)
          if (id == index) :
            if draw :
              cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
            res.append([cx, cy])
    return res

  def trackLandmarks(self, img, draw = True): # 跟踪所有坐标，默认在传入的图片上画出来，返回值是关键点的像素坐标
    res = []
    if self.__results.multi_hand_landmarks :
      for handsLms in self.__results.multi_hand_landmarks :
        for id, lm in enumerate(handsLms.landmark) :
          h, w, c = img.shape
          cx, cy = int (lm.x * w), int(lm.y * h)
          res.append([cx, cy])
          if draw :
            cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
    return res
  def _getLandmarks(self): # 返回识别的结果
    return self.__results.multi_hand_landmarks

# 躯体识别
class BodyDetector():
  def __init__(self):
    print('hello world')

class BodyController():
  def __init__(self):
    print('hello world')
  def process(self, img):
    print('hello world')

if __name__ == '__main__':
  import sys
  sys.path.append('Gesture Recognition and Control/utils')
  from cv2_utils import Camera, waitKey, showImage
  camera = Camera()
  fps = FPS()
  while True:
    img = camera.read()
    hand = HandDetector()
    hand.findHands(img)
    fps.printFps(img)
    showImage(img)
    if waitKey(1, 'q'):
      break