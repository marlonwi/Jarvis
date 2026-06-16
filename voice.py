import edge_tts
import asyncio
import pygame
import os

async def falar_async(texto):
    communicate = edge_tts.Communicate(texto, voice="pt-BR-AntonioNeural")
    await communicate.save("resposta.mp3")

def falar(texto):
    print(f"Jarvis: {texto}")
    asyncio.run(falar_async(texto))
    
    pygame.mixer.init()
    pygame.mixer.music.load("resposta.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.quit()
    os.remove("resposta.mp3")

# Teste
if __name__ == "__main__":
    falar("Olá, eu sou o Jarvis. Online e pronto para ajudar.")