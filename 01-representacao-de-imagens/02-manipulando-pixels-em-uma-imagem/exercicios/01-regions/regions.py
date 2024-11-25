import cv2 as cv
import numpy as np

def solicitar_coordenadas(ponto: str) -> tuple[int, int]:
    """
    Solicita as coordenadas de um ponto ao usuário, verificando se estão dentro dos limites válidos da imagem.
    
    Args:
    ponto (str): Nome do ponto (P1 ou P2) para exibir na mensagem de solicitação.
    
    Returns:
    tuple[int, int]: Coordenadas (x, y) do ponto fornecido.
    
    Raises:
    ValueError: Se as coordenadas estiverem fora dos limites válidos.
    """
    print(f"Digite as coordenadas do ponto {ponto} (x, y): ")
    x, y = map(int, input().split())
    
    if 0 <= x <= 256 and 0 <= y <= 256:
        return (x, y)
    else:
        raise ValueError(f"Coordenadas {ponto} inválidas. Devem estar entre 0 e 256.")

def carregar_imagem(caminho: str) -> np.ndarray:
    """
    Carrega uma imagem em escala de cinza a partir de um arquivo.
    
    Args:
    caminho (str): Caminho para o arquivo de imagem.
    
    Returns:
    np.ndarray: Imagem carregada.
    
    Raises:
    FileNotFoundError: Se o arquivo de imagem não for encontrado.
    """
    imagem = cv.imread(caminho, cv.IMREAD_GRAYSCALE)
    if imagem is None:
        raise FileNotFoundError(f"Erro ao carregar a imagem de {caminho}. Verifique o arquivo.")
    return imagem

def aplicar_negativo(imagem: np.ndarray, p1: tuple[int, int], p2: tuple[int, int]) -> np.ndarray:
    """
    Aplica o efeito de negativo na região da imagem definida pelos pontos P1 e P2.
    
    Args:
    imagem (np.ndarray): Imagem original a ser modificada.
    p1 (tuple[int, int]): Coordenadas do ponto P1 (x1, y1) da região.
    p2 (tuple[int, int]): Coordenadas do ponto P2 (x2, y2) da região.
    
    Returns:
    np.ndarray: Imagem modificada com o negativo aplicado na região definida pelos pontos.
    """
    for i in range(p1[0], p1[1]):  # Para a coordenada y (linhas)
        for j in range(p2[0], p2[1]):  # Para a coordenada x (colunas)
            imagem[i, j] = 255 - imagem[i, j]  # Inverter os valores de cor (negativo)
    return imagem

def exibir_imagem(imagem: np.ndarray, titulo: str) -> None:
    """
    Exibe a imagem em uma janela até que uma tecla seja pressionada.
    
    Args:
    imagem (np.ndarray): A imagem a ser exibida.
    titulo (str): Título da janela.
    """
    cv.imshow(titulo, imagem)
    cv.waitKey()

def main():
    """
    Função principal que solicita os pontos, carrega a imagem, aplica o negativo e exibe os resultados.
    """
    try:
        # Solicitar coordenadas dos pontos P1 e P2
        p1 = solicitar_coordenadas('P1')
        p2 = solicitar_coordenadas('P2')
        
        # Carregar a imagem
        imagem = carregar_imagem('biel.png')
        
        # Exibir a imagem original
        exibir_imagem(imagem, 'Imagem Original')
        
        # Aplicar o negativo na região definida pelos pontos P1 e P2
        imagem_modificada = aplicar_negativo(imagem.copy(), p1, p2)
        
        # Exibir a imagem modificada
        exibir_imagem(imagem_modificada, 'Imagem com Negativo')

        cv.imwrite('biel-negativo.png', imagem_modificada)
    
    except (ValueError, FileNotFoundError) as e:
        print(e)
    finally:
        cv.destroyAllWindows()

# Executar o programa
if __name__ == '__main__':
    main()
