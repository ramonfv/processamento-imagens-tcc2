import cv2
import numpy as np


def blur(image, scale):
    ksize = (scale, scale) 
    return cv2.blur(image, ksize)