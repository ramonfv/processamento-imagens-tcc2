# import cv2
# # import numpy as np

# class ImageProcessor:
#     def __init__(self):
#         self.filters = {
#             'blur': self.blur,
#             'hsv' : self.hsv,
#         }

#     def apply(self, image, filter_name, scale, *args, **kwargs):
#         if filter_name not in self.filters:
#             raise ValueError(f'Filter "{filter_name}" is not defined.')
#         filter_func = self.filters[filter_name]
#         return filter_func(image, scale, *args, **kwargs)

#     def blur(self, image, scale):
#         ksize = (scale, scale) 
#         return cv2.blur(image, ksize)
    
#     def hsv(self, image, scale):
#         blurred_image = self.blur(image, scale)
#         hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
#         hsv_image[..., 0] = (hsv_image[..., 0] + scale) % 180  # Ajusta o canal H (matiz)
#         return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)


# import cv2
# import numpy as np
# from utils.inputImages import loadImages

# class ImageProcessor:
#     def __init__(self):
#         self.filters = {
#             'blur': self.blur,
#             'hsv': self.hsv,
            
#         }

#         self.scale = 1 
#         self.current_scale = self.scale

#         self.hmin = 0
#         self.smin = 0
#         self.vmin = 0
#         self.hmax = 255
#         self.smax = 255
#         self.vmax = 255

#         self.frame = None

#     def on_trackbar_changed_blur(self, value):
#         self.scale = value
#         self.current_scale = self.scale
#         filtered_frame = self.apply(self.frame, 'blur', self.scale)
#         cv2.imshow('Blur', filtered_frame)
#         self.update_hsv_filter(filtered_frame)

#     def on_trackbar_changed_hsv(self, value):
#         self.hmin = cv2.getTrackbarPos('H Min', 'HSV Filter')
#         self.smin = cv2.getTrackbarPos('S Min', 'HSV Filter')
#         self.vmin = cv2.getTrackbarPos('V Min', 'HSV Filter')
#         self.hmax = cv2.getTrackbarPos('H Max', 'HSV Filter')
#         self.smax = cv2.getTrackbarPos('S Max', 'HSV Filter')
#         self.vmax = cv2.getTrackbarPos('V Max', 'HSV Filter')
#         if self.frame is not None:
#             self.update_hsv_filter(self.frame)

#     def update_hsv_filter(self, image):
#         hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#         lower_range = np.array([self.hmin, self.smin, self.vmin])
#         upper_range = np.array([self.hmax, self.smax, self.vmax])
#         mask = cv2.inRange(hsv_image, lower_range, upper_range)
#         filtered_image = cv2.bitwise_and(image, image, mask=mask)
#         threshold_image = self.apply_otsu_threshold(filtered_image)
#         cv2.imshow('HSV Filter', filtered_image)
#         cv2.imshow('Mask', mask)


#     # def apply(self, image, filter_name, scale, *args, **kwargs):
#     #     if filter_name not in self.filters:
#     #         raise ValueError(f'Filter "{filter_name}" is not defined.')
#     #     filter_func = self.filters[filter_name]
#     #     return filter_func(image, scale, *args, **kwargs)
    

#     def apply(self, image, filter_name, scale, *args, **kwargs):
#         if filter_name not in self.filters:
#             raise ValueError(f'Filter "{filter_name}" is not defined.')
#         filter_func = self.filters[filter_name]
#         return filter_func(image, scale, *args, **kwargs)
    
#     def apply_otsu_threshold(self, image):
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         mask = np.uint8(threshold_image)
#         image_with_mask = cv2.bitwise_and(image, image, mask=mask)
#         return image_with_mask

#     def blur(self, image, scale):
#         if scale % 2 == 0:
#             scale += 1  # Certifica-se de que o tamanho da janela é ímpar
#         return cv2.GaussianBlur(image, (scale, scale), 0)

#     def hsv(self, image, scale):
#         blurred_image = self.blur(image, scale)
#         hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
#         hsv_image[..., 0] = (hsv_image[..., 0] + scale) % 180  # Ajusta o canal H (matiz)
#         return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    
#     def createBar(self, control, nameFilter, parameter, maxValue, update):
#         cv2.namedWindow(nameFilter, cv2.WINDOW_NORMAL)
#         cv2.createTrackbar(control, nameFilter, parameter, maxValue, update)


    
#     def remove_background_otsu(self, image):
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         mask = np.uint8(threshold_image)
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)
#         image_without_background = cv2.bitwise_and(image, image, mask=mask)
#         return image_without_background
    
    # def on_trackbar_changed_otsu(self, value):
    #     self.threshold_value = value
    #     filtered_frame = self.apply_otsu_threshold(self.frame, self.threshold_value)
    #     cv2.imshow('OTSU Filter', filtered_frame)

import cv2
import json
import numpy as np
from utils.inputImages import loadImages

class ImageProcessor:
    def __init__(self):
        self.filters = {
            'blur': self.blur,
            'hsv': self.hsv,
        }

        self.scale = 1
        self.current_scale = self.scale

        self.hmin = 0
        self.smin = 0
        self.vmin = 0
        self.hmax = 255
        self.smax = 255
        self.vmax = 255

        self.threshold_value = 0

        self.frame = None


    def save_parameters(self, file_path):
        params = {
            'scale': self.scale,
            'hmin': self.hmin,
            'smin': self.smin,
            'vmin': self.vmin,
            'hmax': self.hmax,
            'smax': self.smax,
            'vmax': self.vmax
        }

        with open(file_path, 'w') as f:
            json.dump(params, f)

    def load_parameters(self, file_path):
        with open(file_path, 'r') as f:
            params = json.load(f)
        
        self.scale = params['scale']
        self.hmin = params['hmin']
        self.smin = params['smin']
        self.vmin = params['vmin']
        self.hmax = params['hmax']
        self.smax = params['smax']
        self.vmax = params['vmax']

    def on_trackbar_changed_blur(self, value):
        self.scale = value
        self.current_scale = self.scale
        filtered_frame = self.apply(self.frame, 'blur', self.scale)
        cv2.imshow('Blur', filtered_frame)
        self.update_hsv_filter(filtered_frame)

    def on_trackbar_changed_hsv(self, value):
        self.hmin = cv2.getTrackbarPos('H Min', 'HSV Filter')
        self.smin = cv2.getTrackbarPos('S Min', 'HSV Filter')
        self.vmin = cv2.getTrackbarPos('V Min', 'HSV Filter')
        self.hmax = cv2.getTrackbarPos('H Max', 'HSV Filter')
        self.smax = cv2.getTrackbarPos('S Max', 'HSV Filter')
        self.vmax = cv2.getTrackbarPos('V Max', 'HSV Filter')
        if self.frame is not None:
            self.update_hsv_filter(self.frame)

    def on_trackbar_changed_otsu(self, value):
        self.threshold_value = value
        filtered_frame = self.apply_otsu_threshold(self.frame)
        cv2.imshow('OTSU Filter', filtered_frame)

    def update_hsv_filter(self, image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_range = np.array([self.hmin, self.smin, self.vmin])
        upper_range = np.array([self.hmax, self.smax, self.vmax])
        mask = cv2.inRange(hsv_image, lower_range, upper_range)
        filtered_hsv = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
        filtered_image = cv2.cvtColor(filtered_hsv, cv2.COLOR_HSV2BGR)
        threshold_image = self.apply_otsu_threshold(filtered_image)
        self.frame = filtered_image
        cv2.imshow('HSV Filter', filtered_image)
        cv2.imshow('Mask', mask)
        cv2.imshow('OTSU Filter', threshold_image)
        self.frame = filtered_image

    def apply(self, image, filter_name, scale, *args, **kwargs):
        if filter_name not in self.filters:
            raise ValueError(f'Filter "{filter_name}" is not defined.')
        filter_func = self.filters[filter_name]
        return filter_func(image, scale, *args, **kwargs)

    def apply_otsu_threshold(self, image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        gray_image = hsv_image[..., 2]  # Extrai o canal de valor (V)
        _, threshold_image = cv2.threshold(gray_image, self.threshold_value, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        mask = np.uint8(threshold_image)
        filtered_hsv = np.copy(hsv_image)
        filtered_hsv[..., 2] = np.where(mask == 255, filtered_hsv[..., 2], 0)  # Aplica a máscara no canal de valor (V)
        filtered_image = cv2.cvtColor(filtered_hsv, cv2.COLOR_HSV2BGR)
        return filtered_image

    def blur(self, image, scale):
        if scale % 2 == 0:
            scale += 1  # Certifica-se de que o tamanho da janela é ímpar
        return cv2.GaussianBlur(image, (scale, scale), 0)

    def hsv(self, image, scale):
        blurred_image = self.blur(image, scale)
        hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
        hsv_image[..., 0] = (hsv_image[..., 0] + scale) % 180  # Ajusta o canal H (matiz)
        return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)