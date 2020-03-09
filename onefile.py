#Author Vitor Araujo

#This is the one file version(not GUI version)

import cv2
import sys
import argparse
import numpy as np

FLAGS = None
IMG = 'image'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
        type=str,
        help='Path to the image.')

FLAGS, unparsed = parser.parse_known_args()

#Or you can use de command below instead argparse
#img = cv2.imread("base.jpg")
img = cv2.imread(FLAGS.image)
cv2.namedWindow('Eraser')
eraser = False 
radius = 5
height, width = img.shape[:2]
bg_mask = np.zeros((height, width, 3), np.uint8)

def draw_circle(x,y):
        cv2.circle(img, ( x, y), radius, (255, 255, 255), -1)
        cv2.circle(bg_mask, ( x, y), radius, (255, 255, 255), -1)
        cv2.imshow('Eraser', img)

def handleMouseEvent(event, x, y, flags, param):
      global eraser , radius     
      if (event == cv2.EVENT_MOUSEMOVE):
              # update eraser position
            if eraser==True:
                  draw_circle(x, y)
      elif (event==cv2.EVENT_MOUSEWHEEL):
              # change eraser size
              if flags > 0:
                radius +=   5
              else:
                if radius > 10:
                   radius -=   5
               

      elif event == cv2.EVENT_LBUTTONUP:
              # stop erasing
            eraser = False
      elif (event == cv2.EVENT_LBUTTONDOWN):
              # start erasing
            eraser = True
            draw_circle(x, y)

cv2.setMouseCallback('Eraser', handleMouseEvent)
cv2.imshow('Eraser', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
mask = cv2.imwrite('mask.jpg', bg_mask)

mask = cv2.imread('mask.jpg', 0)

#You use cv2.INPAINT_NS in the last argument
final_img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('Final Image', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
