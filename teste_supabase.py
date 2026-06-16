from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print(f"URL: {url}")
print(f"KEY: {key[:20]}...")

supabase = create_client(url, key)
resposta = supabase.table("historico").select("*").execute()
print(f"Historico: {resposta.data}")