from utils.inputImages import ImageLoader
import cv2

def main():
    pathToImages = 'C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar TCC\\PlantDoc-Dataset-master\\train\\Tomato leaf_verificado'
    loader = ImageLoader(pathToImages)

    cv2.namedWindow('Imagens', cv2.WINDOW_NORMAL)


# manual, sem avanço e recuo
    frame, path = next(loader.imageGenerator)
    while frame is not None:
        cv2.imshow('Imagens', frame)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('n'):
            loader.nextImage()
        frame, path = next(loader.imageGenerator, (None, None))

    cv2.destroyAllWindows()


# #Com as setas, mas não está funcionando
#     frame = loader.read()
#     while frame is not None:
#         cv2.imshow('Imagens', frame)
#         key = cv2.waitKey(0) & 0xFF
#         if key == ord('q'):
#             break
#         elif key == 83: # seta para direita
#             loader.nextImage()
#             frame = loader.read()
#         elif key == 81: # seta para esquerda
#             loader.prevImage()
#             frame = loader.read()

#     cv2.destroyAllWindows()

# # automatico
#     for frame, path in loader.imageGenerator:
#         cv2.imshow('Imagens', frame)
#         key = cv2.waitKey(1000) & 0xFF
#         if key == ord('q'):
#             break

#     cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

