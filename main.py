from listener import ouvir
from brain import pensar
import re

print("Jarvis online. Pode falar!\n")
pensar("Se apresente brevemente em português.")

while True:
    input("[ Pressione ENTER para falar ]")
    comando = ouvir()

    comando_limpo = re.sub(r'[^\w\s]', '', comando.lower())
    
    if not comando:
        print("Não entendi, tente novamente.")
        continue

    if comando_limpo.lower() == "desligar":
        pensar("Até logo!")
        break
    
    print(f"Você disse: {comando}")
    pensar(comando)