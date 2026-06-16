import sounddevice as sd
import whisper
import tempfile
import soundfile as sf
import os

os.environ["PATH"] += os.pathsep + r"C:\Users\marlo\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"

model = whisper.load_model("base")

def ouvir():
    print("Ouvindo...")
    DURACAO = 5
    TAXA = 16000
    audio = sd.rec(int(DURACAO * TAXA), samplerate=TAXA, channels=1, dtype='float32')
    sd.wait()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio, TAXA)
        resultado = model.transcribe(f.name, language="pt")
    return resultado['text'].strip()