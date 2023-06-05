import cv2
import glob
import numpy as np
import os


class ImageLoader():
    def __init__(self, folderPath):
        self.folderPath = os.path.abspath(folderPath)
        self.imagePaths = self.getImagePaths()
        self.imageGenerator = self.getImageGenerator()
        self.currentPath = None
        self.curretFrame = None

    def getImagePaths(self):
        imagePaths = []
        imagePaths += glob.glob(os.path.join(self.folderPath, '*.jpg'))
        return imagePaths

    def getImageGenerator(self):
        for imagePath in self.imagePaths:
            image = cv2.imread(imagePath)
            yield image, imagePath

    def read(self):
        if self.currentPath is None:
            self.currentFrame, self.currentPath = next(self.imageGenerator)
            return self.currentFrame
        
    def nextImage(self):
        self.currentFrame, self.currentPath = next(self.imageGenerator)

    def prevImage(self):
        self.imageGenerator = self.getImageGenerator()
        for image, path in self.imageGenerator:
            if path == self.currentPath:
                break
            self.currentFrame, self.currentPath = image, path
         