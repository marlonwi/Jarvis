import pyautogui
import pytesseract
from PIL import Image
import os

# Aponta pro Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ver_tela():
    # Captura screenshot da tela inteira
    screenshot = pyautogui.screenshot()
    screenshot.save("tela.png")
    
    # Lê o texto da imagem
    texto = pytesseract.image_to_string(Image.open("tela.png"), lang="por")
    os.remove("tela.png")
    
    return texto.strip()

def ver_regiao(x, y, largura, altura):
    # Captura só uma região da tela
    screenshot = pyautogui.screenshot(region=(x, y, largura, altura))
    texto = pytesseract.image_to_string(screenshot, lang="por")
    return texto.strip()

# Teste
if __name__ == "__main__":
    print("Lendo a tela...")
    texto = ver_tela()
    print(f"Texto encontrado:\n{texto[:500]}")