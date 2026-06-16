from openai import OpenAI
from dotenv import load_dotenv
from voice import falar
from supabase import create_client
import os
from vision import ver_tela


load_dotenv()

client = OpenAI(
    base_url="http://localhost:11434/v1",  # aponta pro seu PC
    api_key="ollama"
    )
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def carregar_memoria_permanente():
    resposta = supabase.table("memoria").select("*").execute()
    if not resposta.data:
        return ""
    memoria = "Informações importantes sobre o usuário:\n"
    for row in resposta.data:
        memoria += f"- {row['chave']}: {row['valor']}\n"
    return memoria

def salvar_memoria_permanente(chave, valor):
    # Verifica se já existe e atualiza, senão cria
    existente = supabase.table("memoria").select("*").eq("chave", chave).execute()
    if existente.data:
        supabase.table("memoria").update({"valor": valor}).eq("chave", chave).execute()
    else:
        supabase.table("memoria").insert({"chave": chave, "valor": valor}).execute()

def carregar_historico(memoria_permanente):
    system_prompt = f"""Você é Jarvis, um assistente pessoal inteligente e eficiente.
Responda de forma curta e objetiva, como um assistente pessoal.
Sempre responda em português.

{memoria_permanente}

Quando o usuário mencionar informações importantes como nome, preferências ou hábitos,
extraia e salve usando o formato: SALVAR_MEMORIA[chave]=[valor]
Exemplo: SALVAR_MEMORIA[nome]=Marlon"""

    resposta = supabase.table("historico").select("*").order("created_at").execute()
    mensagens = [{"role": "system", "content": system_prompt}]
    for row in resposta.data:
        mensagens.append({"role": row["role"], "content": row["content"]})
    return [mensagens[0]] + mensagens[-20:]

def salvar_mensagem(role, content):
    supabase.table("historico").insert({"role": role, "content": content}).execute()

def processar_memorias(texto):
    import re
    memorias = re.findall(r'SALVAR_MEMORIA\[(.+?)\]=(.+?)(?:\n|$)', texto)
    for chave, valor in memorias:
        salvar_memoria_permanente(chave.strip(), valor.strip())
    # Remove as tags da resposta final
    texto_limpo = re.sub(r'SALVAR_MEMORIA\[.+?\]=.+?(?:\n|$)', '', texto).strip()
    return texto_limpo

def pensar(comando):
    print(f"\nProcessando: '{comando}'")

    # Se o comando mencionar a tela, captura e adiciona ao contexto
    contexto_tela = ""
    palavras_tela = ["tela", "screen", "aberto", "vendo", "está escrito", "janela"]
    if any(palavra in comando.lower() for palavra in palavras_tela):
        print("Capturando tela...")
        contexto_tela = f"\n\nConteúdo atual da tela do usuário:\n{ver_tela()}"
        comando = comando + contexto_tela

    # Verifica se é um comando de ação
    if any(p in comando.lower() for p in ["abrir", "abre", "abra"]):
        for programa in ["chrome", "navegador", "vscode", "vs code", "notepad", "bloco de notas", "spotify", "discord", "explorador"]:
            if programa in comando.lower():
                resultado = abrir_programa(programa)
                falar(resultado)
                return resultado

    if any(p in comando.lower() for p in ["digita", "escreve", "escreva", "digite"]):
        texto = comando.lower()
        for p in ["digita", "escreve", "escreva", "digite"]:
            texto = texto.replace(p, "").strip()
        resultado = digitar_texto(texto)
        falar("Texto digitado.")
        return resultado
    memoria_permanente = carregar_memoria_permanente()
    historico = carregar_historico(memoria_permanente)
    historico.append({"role": "user", "content": comando})
    salvar_mensagem("user", comando)
    # ... resto do código
    memoria_permanente = carregar_memoria_permanente()
    historico = carregar_historico(memoria_permanente)
    historico.append({"role": "user", "content": comando})
    salvar_mensagem("user", comando)

    resposta = client.chat.completions.create(
        model="llama3",
        messages=historico
    )

    texto = resposta.choices[0].message.content
    texto_limpo = processar_memorias(texto)

    salvar_mensagem("assistant", texto_limpo)
    texto_limpo = processar_memorias(texto)

# Proteção caso texto fique vazio
    if not texto_limpo:
        texto_limpo = "Informação salva com sucesso."

        salvar_mensagem("assistant", texto_limpo)
        falar(texto_limpo)
        return texto_limpo
    falar(texto_limpo)
    return texto_limpo