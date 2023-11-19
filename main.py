from utils.inputImages import ImageLoader
from utils.processor import ImageProcessor
from utils.filters import Blur
import cv2
import os

# Diretório das imagens
diretorio_imagens = 'C:\\Users\\RamonFernandesViana\\Downloads\\Arquivos\\Auxiliar TCC\\PlantDoc-Dataset-master\\train\\Tomato leaf_verificado'

# Valor inicial do desfoque
valor_desfoque = 0

# Função chamada quando o valor da trackbar é alterado
def atualizar_desfoque(valor):
    global valor_desfoque
    valor_desfoque = valor
    aplicar_desfoque()

# Função para aplicar o desfoque na imagem atual
def aplicar_desfoque():
    desfoque = valor_desfoque * 2 + 1  # Valor ímpar para o tamanho do kernel de desfoque
    imagem_nome = imagens[indice_imagem_atual]
    imagem_caminho = os.path.join(diretorio_imagens, imagem_nome)
    imagem = cv2.imread(imagem_caminho)
    imagem_desfocada = cv2.blur(imagem, (desfoque, desfoque), 0)
    cv2.imshow('Imagem Desfocada', imagem_desfocada)

# Função principal
def main():
    global indice_imagem_atual
    global imagens

    # Lista de imagens no diretório
    imagens = os.listdir(diretorio_imagens)
    imagens = [img for img in imagens if img.endswith('.jpg') or img.endswith('.png')]

    # Verificar se existem imagens no diretório
    if len(imagens) == 0:
        print("Nenhuma imagem encontrada no diretório.")
        return

    # Índice da imagem atual
    indice_imagem_atual = 0

    cv2.namedWindow('Imagem Desfocada')
    cv2.createTrackbar('Desfoque', 'Imagem Desfocada', valor_desfoque, 10, atualizar_desfoque)

    # Aplicar o desfoque inicialmente
    aplicar_desfoque()

    # Loop principal
    while True:
        tecla = cv2.waitKey(0)

        if tecla == 27:  # Tecla 'Esc' para sair
            break
        elif tecla == ord('n'):  # Tecla 'n' para avançar para a próxima imagem
            indice_imagem_atual = (indice_imagem_atual + 1) % len(imagens)
            aplicar_desfoque()
            cv2.setTrackbarPos('Desfoque', 'Imagem Desfocada', valor_desfoque)  # Atualizar valor da trackbar
        elif tecla == ord('p'):  # Tecla 'p' para retroceder para a imagem anterior
            indice_imagem_atual = (indice_imagem_atual - 1) % len(imagens)
            aplicar_desfoque()
            cv2.setTrackbarPos('Desfoque', 'Imagem Desfocada', valor_desfoque)  # Atualizar valor da trackbar

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()