# import cv2
# import numpy as np

# # Função de callback para a trackbar
# def on_threshold_change(x):
#     global imagem_redimensionada, imagem_entrada
    
#     # Aplica a limiarização de Otsu com o valor da trackbar
#     _, imagem_limiarizada = cv2.threshold(imagem_cinza, x, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
#     # Encontra os contornos na imagem limiarizada
#     contornos, _ = cv2.findContours(imagem_limiarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Cria uma máscara em branco do mesmo tamanho da imagem
#     mascara = np.zeros_like(imagem_cinza)
    
#     # Desenha os contornos na máscara
#     cv2.drawContours(mascara, contornos, -1, 255, thickness=cv2.FILLED)
    
#     # Filtra a imagem original usando a máscara
#     imagem_sem_fundo = cv2.bitwise_and(imagem_entrada, imagem_entrada, mask=mascara)
    
#     # Exibe a imagem sem o fundo
#     cv2.imshow('Imagem sem Fundo', imagem_sem_fundo)

# # Carrega a imagem
# imagem = cv2.imread("C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC\\PlantDoc-Dataset-master\\processed_image_hsv.jpg")

# # Redimensiona a imagem de entrada
# largura_desejada = 800
# altura_desejada = 600
# imagem_entrada = cv2.resize(imagem, (largura_desejada, altura_desejada))

# # Converte a imagem de entrada para tons de cinza
# imagem_cinza = cv2.cvtColor(imagem_entrada, cv2.COLOR_BGR2GRAY)

# # Cria a janela para a trackbar
# cv2.namedWindow('Imagem sem Fundo')

# # Cria a trackbar que permite variar a sensibilidade
# cv2.createTrackbar('Sensibilidade', 'Imagem sem Fundo', 100, 255, on_threshold_change)

# # Inicializa a chamada de função para exibir a imagem sem o fundo
# on_threshold_change(100)

# # Aguarda o pressionamento de uma tecla e fecha a janela
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from utils.inputImages import loadImages
from utils.processor import ImageProcessor
import os

base_path = "C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar_TCC"
folderPath = os.path.join(base_path,"PlantDoc-Dataset-master\\train\\Tomato leaf")
outputFolder =  os.path.join(base_path,"PlantDoc-Dataset-master")
image_loader = loadImages(folderPath)
image_processor = ImageProcessor()


cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blur', cv2.WINDOW_NORMAL)
cv2.namedWindow('HSV Filter', cv2.WINDOW_NORMAL)
cv2.namedWindow('Watershed Segmentation', cv2.WINDOW_NORMAL)

cv2.createTrackbar('Blur', 'Blur', image_processor.scale, 50, image_processor.on_trackbar_changed_blur)
cv2.createTrackbar('H Min', 'HSV Filter', image_processor.hmin, 255, image_processor.on_trackbar_changed_hsv)
cv2.createTrackbar('S Min', 'HSV Filter', image_processor.smin, 255, image_processor.on_trackbar_changed_hsv)
cv2.createTrackbar('V Min', 'HSV Filter', image_processor.vmin, 255, image_processor.on_trackbar_changed_hsv)
cv2.createTrackbar('H Max', 'HSV Filter', image_processor.hmax, 255, image_processor.on_trackbar_changed_hsv)
cv2.createTrackbar('S Max', 'HSV Filter', image_processor.smax, 255, image_processor.on_trackbar_changed_hsv)
cv2.createTrackbar('V Max', 'HSV Filter', image_processor.vmax, 255, image_processor.on_trackbar_changed_hsv)



filtered_frame = None
while True:
    frame = image_loader.getCurrentImage()

    if frame is not None:
        cv2.imshow('Imagem Original', frame)

        filtered_frame = image_processor.apply(frame, 'blur', image_processor.current_scale)
        cv2.imshow('Blur', filtered_frame)

        image_processor.update_hsv_filter(filtered_frame)

        # Aplicar segmentação Watershed após OTSU
        if filtered_frame is not None:
            gray_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2GRAY)
            _, threshold_frame = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Aplicar segmentação Watershed
            markers = cv2.watershed(filtered_frame, markers=threshold_frame)
            segmented_frame = np.copy(filtered_frame)
            segmented_frame[markers == -1] = [0, 0, 255]  # Marcando as bordas com vermelho

            cv2.imshow('Watershed Segmentation', segmented_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('n'):
        frame = image_loader.getNextImage()
    elif key == ord('p'):
        frame = image_loader.getPreviosImage()
    elif key == ord('s'):
        if filtered_frame is not None:
            output_path = os.path.join(outputFolder, f"processed_image_blur.jpg")
            cv2.imwrite(output_path, filtered_frame)
            print(f"Saved image with blur filter to {output_path}")

cv2.destroyAllWindows()