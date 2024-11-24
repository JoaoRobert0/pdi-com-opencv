import cv2 as cv
import numpy as np

# Ler a imagem, em escala de cinza, que esta no meu diretorio
image: np.ndarray = cv.imread('biel.png', cv.IMREAD_GRAYSCALE)

# Exbir a imagem em uma janela com o nome 'biel'
cv.imshow('biel', image)

# Esperar qualquer tecla para fechar a janela
cv.waitKey()

# Fechar todas as janelas, se tiver mais de uma (boa pratica)
cv.destroyAllWindows()