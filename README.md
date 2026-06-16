# J — Assistente Pessoal com IA

> Agente de inteligência artificial com controle por voz, memória persistente e visão computacional, rodando 100% local.

---

## Demonstração

O J ouve sua voz, interpreta o comando com um LLM local, vê a tela do computador e executa ações — tudo sem depender de serviços pagos externos.

```
🎤 Você fala → 📝 Whisper transcreve → 🧠 LLaMA 3 interpreta → 🔊 J responde
```

---

## Funcionalidades

- **Controle por voz** — reconhecimento de fala em português com OpenAI Whisper
- **IA local e gratuita** — cérebro powered by LLaMA 3 via Ollama (sem custo de API)
- **Voz natural** — respostas em áudio com Microsoft Edge TTS
- **Visão computacional** — lê e interpreta o conteúdo da tela com OCR
- **Execução de tarefas** — abre programas, digita texto e controla o computador
- **Memória de conversa** — histórico persistente no Supabase (PostgreSQL)
- **Memória permanente** — salva informações importantes do usuário que nunca são esquecidas

---

## Arquitetura

```
jarvis/
├── main.py          # Loop principal — orquestra todos os módulos
├── listener.py      # Captura de voz e transcrição com Whisper
├── brain.py         # Cérebro — integração com LLaMA 3 via Ollama
├── voice.py         # Síntese de voz com Edge TTS + Pygame
├── vision.py        # Visão computacional com OCR (Tesseract)
├── executor.py      # Execução de tarefas no sistema operacional
└── .env             # Credenciais (não versionado)
```

### Fluxo de dados

```
Microfone
    │
    ▼
Whisper (transcrição)
    │
    ▼
brain.py
    ├── Supabase (memória permanente + histórico)
    ├── vision.py (captura de tela, se necessário)
    ├── executor.py (execução de ações, se necessário)
    └── LLaMA 3 via Ollama (raciocínio)
         │
         ▼
    Edge TTS + Pygame (resposta em voz)
```

---

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Reconhecimento de voz | OpenAI Whisper |
| Modelo de linguagem | LLaMA 3 (via Ollama) |
| Síntese de voz | Microsoft Edge TTS |
| Áudio | Pygame, SoundDevice |
| Visão computacional | Tesseract OCR, PyAutoGUI |
| Automação | PyAutoGUI |
| Banco de dados | Supabase (PostgreSQL) |
| Linguagem | Python 3.11 |

---

## Pré-requisitos

- Python 3.11
- [Ollama](https://ollama.com) instalado e rodando
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) instalado
- [FFmpeg](https://ffmpeg.org) instalado
- Conta no [Supabase](https://supabase.com) (gratuito)

---

## Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/jarvis.git
cd jarvis
```

**2. Crie o ambiente virtual**
```bash
py -3.11 -m venv venv
.\venv\Scripts\Activate  # Windows
```

**3. Instale as dependências**
```bash
pip install openai-whisper sounddevice soundfile python-dotenv openai edge-tts pygame pillow pytesseract pyautogui supabase
```

**4. Baixe o modelo LLaMA 3**
```bash
ollama pull llama3
```

**5. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```
SUPABASE_URL=sua-url-aqui
SUPABASE_KEY=sua-chave-aqui
```

**6. Configure o banco de dados**

No Supabase, execute:
```sql
CREATE TABLE historico (
  id SERIAL PRIMARY KEY,
  role TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE memoria (
  id SERIAL PRIMARY KEY,
  chave TEXT NOT NULL,
  valor TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

ALTER TABLE historico DISABLE ROW LEVEL SECURITY;
ALTER TABLE memoria DISABLE ROW LEVEL SECURITY;
```

**7. Inicie o J**
```bash
python main.py
```

---

## Como usar

1. Certifique-se que o Ollama está rodando em segundo plano
2. Ative o ambiente virtual e rode `python main.py`
3. Pressione **ENTER** para falar
4. Fale seu comando em português
5. Para encerrar, diga **"desligar"**

### Exemplos de comandos

| Comando | Ação |
|---|---|
| "Abre o Chrome" | Abre o navegador |
| "Abre o bloco de notas" | Abre o Notepad |
| "O que está na minha tela?" | Lê e resume o conteúdo da tela |
| "Meu nome é Marlon" | Salva na memória permanente |
| "Qual é meu nome?" | Recupera da memória |
| "Desligar" | Encerra o programa |

---

## Roadmap

### ✅ Fase 1 — Base do agente
- [x] Captura e transcrição de voz com Whisper
- [x] Integração com LLM
- [x] Resposta por voz com Edge TTS

### ✅ Fase 2 — Memória e contexto
- [x] Migração para LLaMA 3 local via Ollama
- [x] Memória de conversa persistente no Supabase
- [x] Memória permanente de informações do usuário

### 🚧 Fase 3 — Visão e automação (em andamento)
- [x] Visão computacional com OCR
- [x] Execução de tarefas no sistema
- [ ] Integração com Google Calendar
- [ ] Busca na web em tempo real

### 🔜 Fase 4 — Multi-agente e IoT
- [ ] Agentes especializados com CrewAI
- [ ] Controle de dispositivos IoT
- [ ] API REST com FastAPI
- [ ] Acesso via celular

### 🔜 Fase 5 — Nível Jarvis
- [ ] Fine-tuning do modelo com LoRA
- [ ] Reconhecimento de voz biométrico
- [ ] Interface HUD com overlay na tela
- [ ] Aprendizado contínuo com feedback

---

## Decisões técnicas

**Por que LLaMA 3 em vez de GPT-4?**
Rodar o modelo localmente elimina custos de API, garante privacidade total dos dados e permite uso offline.

**Por que Supabase?**
PostgreSQL gerenciado na nuvem com SDK Python simples. Permite que a memória do J persista entre sessões e seja acessível de qualquer dispositivo futuramente.

**Por que Python 3.11?**
Versões mais recentes (3.12+) ainda não têm suporte completo das libs de ML utilizadas no projeto.

---

## Autor

**Marlon** — Estudante de Engenharia de Software (7º período)

[![GitHub](https://img.shields.io/badge/GitHub-marlonwi-black?logo=github)](https://github.com/marlonwi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-marlonwilliam-blue?logo=linkedin)](https://www.linkedin.com/in/marlonwilliam/)
