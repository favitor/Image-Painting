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
bg = np.zeros((height, width, 3), np.uint8)

def draw_circle(x,y):
        cv2.circle(img, ( x, y), radius, (255, 255, 255), -1)
        cv2.circle(bg, ( x, y), radius, (255, 255, 255), -1)
        cv2.imshow('Eraser', img)

def handleMouseEvent(event, x, y, flags, param):
      global eraser , radius     
      if (event == cv2.EVENT_MOUSEMOVE):
              # update eraser position
            if eraser==True:
                  draw_circle(x, y)

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
mask = cv2.imwrite('mask.jpg', bg)
