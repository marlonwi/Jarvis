import pyautogui
import subprocess
import os

# Segurança — move o mouse pro canto pra cancelar se travar
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def abrir_programa(nome):
    programas = {
        "chrome": "chrome",
        "navegador": "chrome",
        "vscode": "code",
        "vs code": "code",
        "notepad": "notepad",
        "bloco de notas": "notepad",
        "explorador": "explorer",
        "spotify": "spotify",
        "discord": "discord",
    }
    
    comando = programas.get(nome.lower())
    if comando:
        subprocess.Popen(comando)
        return f"{nome} aberto com sucesso."
    return f"Não sei como abrir {nome}."

def digitar_texto(texto):
    pyautogui.typewrite(texto, interval=0.05)
    return f"Texto digitado: {texto}"

def pressionar_tecla(tecla):
    pyautogui.press(tecla)
    return f"Tecla {tecla} pressionada."

def clicar(x, y):
    pyautogui.click(x, y)
    return f"Clicado em {x}, {y}."

def tirar_screenshot(caminho="screenshot.png"):
    pyautogui.screenshot(caminho)
    return f"Screenshot salvo em {caminho}."

# Teste
if __name__ == "__main__":
    print(abrir_programa("notepad"))