import cv2 as cv
import numpy as np
from typing import Any

def exibir_imagem(imagem: np.ndarray) -> Any:
    '''
    Exibe a imagem em uma janela e aguarda até que uma tecla seja pressionada.

    Parâmetros:
    imagem (np.ndarray): A imagem a ser exibida.
    '''
    cv.imshow('img', imagem)
    cv.waitKey()

def main():
    # Lendo a imagem bolhas.png em escala de cinza
    imagem: np.ndarray = cv.imread('bolhas.png', cv.IMREAD_GRAYSCALE)

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        print("Não foi possível abrir 'bolhas.png'")
        return  # Encerra o programa se a imagem não foi aberta

    # Exibe a imagem em escala de cinza
    exibir_imagem(imagem)

    # Pintando um retângulo preto na imagem em escala de cinza
    for i in range(200, 210):
        for j in range(10, 200):
            imagem[i, j] = 0

    # Exibe a imagem com o retângulo preto adicionado
    exibir_imagem(imagem)

    # Lendo a imagem bolhas.png em cores (BGR)
    imagem = cv.imread('bolhas.png', cv.IMREAD_COLOR)

    # Os argumentos mais comuns para o segundo parâmetro de imread() são:
    # - cv.IMREAD_COLOR: carrega a imagem em BGR, sem canal alfa.
    # - cv.IMREAD_UNCHANGED: carrega a imagem como está, incluindo canal alfa.
    # - cv.IMREAD_GRAYSCALE: carrega a imagem em escala de cinza.
    # Documentação: https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html

    # Pintando um retângulo vermelho na imagem colorida
    for i in range(200, 210):
        for j in range(10, 200):
            imagem[i, j] = (0, 0, 255)  # Define o pixel para vermelho (BGR)

    # Exibe a imagem colorida com o retângulo vermelho adicionado
    exibir_imagem(imagem)

if __name__ == '__main__':
    main()
