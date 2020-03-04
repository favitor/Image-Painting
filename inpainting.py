import cv2
import numpy as np
import sys
import argparse

FLAGS = None
IMG = 'image'
MSK = 'mask'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
        type=str,
        help='Path to the image.')

parser.add_argument('-m', '--mask',
        type=str,
        help='Path to the mask.')

FLAGS, unparsed = parser.parse_known_args()

#Or you can use de command below instead argparse
img = cv2.imread(FLAGS.image)
#img = cv2.imread('yourimage.jpg')
mask = cv2.imread(FLAGS.mask)
#mask = cv2.imread('yourmask.jpg', 0)

#cv2.INPAINT_NS
final_img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('Final Image', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
