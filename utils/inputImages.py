import cv2
import glob
import numpy as np
import os


class ImageLoader:
    def __init__(self, folderPath):
        self.imagePaths = glob.glob(os.path.join(folderPath, '*.jpg'))
        self.images = [cv2.imread(imagePath) for imagePath in self.imagePaths]
        self.currenteIndex = 0

    def getCurrentImage(self):
        return self.images[self.currenteIndex]
    
    def getNextImage(self):
        self.currenteIndex += 1
        if self.currenteIndex >= len(self.images):
            self.currenteIndex = 0
        return self.getCurrentImage()
    
    def getPreviosImage(self):
        self.currenteIndex -= 1
        if self.currenteIndex >= len(self.images):
            self.currenteIndex = 0
        return self.getCurrentImage()
    
    
def loadImages(folderPath):
    return ImageLoader(folderPath)


