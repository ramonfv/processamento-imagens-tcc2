



# import cv2
# from utils.inputImages import loadImages
# from utils.processor import ImageProcessor
# import os
# base_path = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC"
# folderPath = os.path.join(base_path,"PlantDoc-Dataset-master\\train\\Tomato leaf bacterial spot")
# outputFolder =  os.path.join(base_path,"PlantDoc-Dataset-master")
# image_loader = loadImages(folderPath)
# image_processor = ImageProcessor()

# cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Blur', cv2.WINDOW_NORMAL)
# cv2.namedWindow('HSV Filter', cv2.WINDOW_NORMAL)


# cv2.createTrackbar('Blur', 'Blur', image_processor.scale, 50, image_processor.on_trackbar_changed_blur)
# cv2.createTrackbar('H Min', 'HSV Filter', image_processor.hmin, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('S Min', 'HSV Filter', image_processor.smin, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('V Min', 'HSV Filter', image_processor.vmin, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('H Max', 'HSV Filter', image_processor.hmax, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('S Max', 'HSV Filter', image_processor.smax, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('V Max', 'HSV Filter', image_processor.vmax, 255, image_processor.on_trackbar_changed_hsv)


# filtered_frame = None


# while True:
#     frame = image_loader.getCurrentImage()

#     if frame is not None:
#         cv2.imshow('Imagem Original', frame)

#         filtered_frame = image_processor.apply(frame, 'blur', image_processor.current_scale)
#         cv2.imshow('Blur', filtered_frame)

#         image_processor.update_hsv_filter(filtered_frame)

#     key = cv2.waitKey(1) & 0xFF

#     if key == ord('q'):
#         break
#     elif key == ord('n'):
#         frame = image_loader.getNextImage()
#     elif key == ord('p'):
#         frame = image_loader.getPreviosImage()


# cv2.destroyAllWindows()


# import cv2
# from utils.inputImages import loadImages
# from utils.processor import ImageProcessor
# import os

# base_path = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC"
# folderPath = os.path.join(base_path,"PlantDoc-Dataset-master\\train\\Tomato leaf")
# outputFolder =  os.path.join(base_path,"PlantDoc-Dataset-master")
# image_loader = loadImages(folderPath)
# image_processor = ImageProcessor()

# cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Blur', cv2.WINDOW_NORMAL)
# cv2.namedWindow('HSV Filter', cv2.WINDOW_NORMAL)


# cv2.createTrackbar('Blur', 'Blur', image_processor.scale, 50, image_processor.on_trackbar_changed_blur)
# cv2.createTrackbar('H Min', 'HSV Filter', image_processor.hmin, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('S Min', 'HSV Filter', image_processor.smin, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('V Min', 'HSV Filter', image_processor.vmin, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('H Max', 'HSV Filter', image_processor.hmax, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('S Max', 'HSV Filter', image_processor.smax, 255, image_processor.on_trackbar_changed_hsv)
# cv2.createTrackbar('V Max', 'HSV Filter', image_processor.vmax, 255, image_processor.on_trackbar_changed_hsv)


# filtered_frame = None
# while True:
#     frame = image_loader.getCurrentImage()

#     if frame is not None:
#         cv2.imshow('Imagem Original', frame)

#         filtered_frame = image_processor.apply(frame, 'blur', image_processor.current_scale)
#         cv2.imshow('Blur', filtered_frame)

#         image_processor.update_hsv_filter(filtered_frame)

#     key = cv2.waitKey(1) & 0xFF

#     if key == ord('q'):
#         break
#     elif key == ord('n'):
#         frame = image_loader.getNextImage()
#     elif key == ord('p'):
#         frame = image_loader.getPreviosImage()
#     elif key == ord('s'):
#         if filtered_frame is not None:
#             output_path = os.path.join(outputFolder, f"processed_image_blur.jpg")
#             cv2.imwrite(output_path, filtered_frame)
#             print(f"Saved image with blur filter to {output_path}")
 

# cv2.destroyAllWindows()



import cv2
import time
import glob
import os
from utils.inputImages import loadImages
from utils.processor import ImageProcessor

directories = [ 
                
                 "Tomato_Early_blight_leaf_verificado"]


# directories = [ "Tomato_Septoria_leaf_spot", "Tomato_mold_leaf_verificado", "Tomato_leaf_yellow_virus_verificado",
#                 "Tomato_leaf_mosaic_virus_verificado", "Tomato_leaf_late_blight_verificado", "Tomato_leaf_bacterial_spot_verificado",
#                 "Tomato_leaf_verificado", "Tomato_Early_blight_leaf_verificado"]

# directories = ["Tomato___Tomato_Yellow_Leaf_Curl_Virus",
#                "Tomato___Tomato_mosaic_virus", "Tomato___Target_Spot",
#                 "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Septoria_leaf_spot", "Tomato___Leaf_Mold",
#                 "Tomato___Late_blight", "Tomato___healthy", "Tomato___Early_blight",  "Tomato___Bacterial_spot"]


basePathOrigin = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC\\PlantDoc-Dataset-master\\PLantDoc"


outputFolder = [ 
                 "Tomato_Early_blight_leaf"
]

# outputFolder = [ "Tomato_Septoria_leaf_spot", "Tomato_mold_leaf", "Tomato_leaf_yellow_virus", "Tomato_leaf_mosaic_virus",
#                 "Tomato_leaf_late_blight", "Tomato_leaf_bacterial_spot", "Tomato_leaf", "Tomato_Early_blight_leaf"
# ]

# outputFolder = ["Tomato___Tomato_Yellow_Leaf_Curl_Virus",
#                 "Tomato___Tomato_mosaic_virus", "Tomato___Target_Spot",
#                 "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Septoria_leaf_spot", "Tomato___Leaf_Mold",
#                 "Tomato___Late_blight", "Tomato___healthy", "Tomato___Early_blight", "Tomato___Bacterial_spot"]

basePathOutput = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC\\PlantDoc-Dataset-master\\Processados"
parameters = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC\\PlantDoc-Dataset-master\\Processados\\parameters"

current_directory_index = 0
counter = 0

# folderPath = os.path.join(basePathOrigin, directories[current_directory_index])
# outputFolder = os.path.join(basePathOutput, outputFolder[current_directory_index])

# print(folderPath)
# print(outputFolder)

while current_directory_index < len(directories):
    folderPath = os.path.join(basePathOrigin, directories[current_directory_index])
    outputFolder = os.path.join(basePathOutput, outputFolder[current_directory_index])

    parameters = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC\\PlantDoc-Dataset-master\\Processados\\parameters"
    image_loader = loadImages(folderPath)
    image_processor = ImageProcessor()

    cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Blur', cv2.WINDOW_NORMAL)
    cv2.namedWindow('HSV Filter', cv2.WINDOW_NORMAL)
    cv2.namedWindow('OTSU Filter', cv2.WINDOW_NORMAL)

    cv2.createTrackbar('Blur', 'Blur', image_processor.scale, 50, image_processor.on_trackbar_changed_blur)
    cv2.createTrackbar('H Min', 'HSV Filter', image_processor.hmin, 255, image_processor.on_trackbar_changed_hsv)
    cv2.createTrackbar('S Min', 'HSV Filter', image_processor.smin, 255, image_processor.on_trackbar_changed_hsv)
    cv2.createTrackbar('V Min', 'HSV Filter', image_processor.vmin, 255, image_processor.on_trackbar_changed_hsv)
    cv2.createTrackbar('H Max', 'HSV Filter', image_processor.hmax, 255, image_processor.on_trackbar_changed_hsv)
    cv2.createTrackbar('S Max', 'HSV Filter', image_processor.smax, 255, image_processor.on_trackbar_changed_hsv)
    cv2.createTrackbar('V Max', 'HSV Filter', image_processor.vmax, 255, image_processor.on_trackbar_changed_hsv)

    image_extensions = ["*.jpg", "*.jpeg", "*.png"]
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(folderPath, extension)))

    lenDir = len(image_files)

    threshold_image = None
    filtered_frame = None
    start = False

    while True:
        frame = image_loader.getCurrentImage()

        if frame is not None:
            cv2.imshow('Imagem Original', frame)

            filtered_frame = image_processor.apply(frame, 'blur', image_processor.current_scale)
            cv2.imshow('Blur', filtered_frame)

            image_processor.update_hsv_filter(filtered_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif counter == lenDir:
            current_directory_index += 1
            counter = 0
            break
        elif key == ord('x'):
            params_path = os.path.join(parameters, "filter_params.json")
            image_processor.save_parameters(params_path)
        elif key == ord('l'):
            params_path = os.path.join(parameters, "filter_params.json")
            image_processor.load_parameters(params_path)
            filtered_frame = image_processor.apply(frame, 'blur', image_processor.current_scale)
            threshold_image = image_processor.apply_otsu_threshold(filtered_frame)
            start = True
        # elif key == ord('s'):
        if image_processor.frame is not None and start:
            threshold_image = image_processor.apply_otsu_threshold(image_processor.frame)
            output_path = os.path.join(outputFolder, f"image ({image_loader.currenteIndex}).jpg")
            cv2.imwrite(output_path, threshold_image)
            print(f"Imagem salva em: {output_path}")

            frame = image_loader.getNextImage()
            # time.sleep(1)
            counter += 1

    cv2.destroyAllWindows()