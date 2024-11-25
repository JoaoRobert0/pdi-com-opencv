import cv2 as cv
import numpy as np
from typing import Any

def exibir_duas_imagens(imagem_1: np.ndarray, imagem_2: np.ndarray) -> Any:
    """
    Exibe duas imagens em janelas separadas.

    Parâmetros:
    imagem_1 (np.ndarray): A primeira imagem a ser exibida.
    imagem_2 (np.ndarray): A segunda imagem a ser exibida.

    A função cria duas janelas com os títulos 'original' e 'modificada', 
    exibindo as imagens correspondentes. Ela aguarda a interação do usuário 
    antes de fechar as janelas.
    """
    # Exibe a imagem original
    cv.imshow('original', imagem_1)
    # Exibe a imagem modificada
    cv.imshow('modificada', imagem_2)
    # Aguarda uma tecla ser pressionada para fechar as janelas
    cv.waitKey()
    cv.destroyAllWindows()

def main():
    """
    Função principal que realiza a manipulação de uma imagem e exibe 
    a imagem original e a imagem modificada.

    O programa realiza a troca de quadrantes da imagem:
    - O quadrante superior esquerdo troca com o inferior direito.
    - O quadrante superior direito troca com o inferior esquerdo.
    O objetivo é demonstrar a manipulação de regiões em uma imagem.
    """
    # Lendo a imagem em tom de cinza
    imagem: np.ndarray = cv.imread('biel.png', cv.IMREAD_GRAYSCALE)

    # Criando uma cópia da imagem original, para realizar as alterações
    imagem_modificada: np.ndarray = imagem.copy()

    # Troca de quadrantes:
    # Quadrante 1 (superior esquerdo) com Quadrante 4 (inferior direito)
    imagem_modificada[:128, :128] = imagem[128:, 128:]
    
    # Quadrante 2 (superior direito) com Quadrante 3 (inferior esquerdo)
    imagem_modificada[:128, 128:] = imagem[128:, :128]
    
    # Quadrante 3 (inferior esquerdo) com Quadrante 2 (superior direito)
    imagem_modificada[128:, :128] = imagem[:128, 128:]
    
    # Quadrante 4 (inferior direito) com Quadrante 1 (superior esquerdo)
    imagem_modificada[128:, 128:] = imagem[:128, :128]

    # Exibindo a imagem original e a imagem modificada
    exibir_duas_imagens(imagem, imagem_modificada)

    cv.imwrite('biel-invertido.png', imagem_modificada)

if __name__ == '__main__':
    main()