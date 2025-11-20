import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("=== MODELOS DISPONÍVEIS PARA SUA CHAVE ===")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            
            print(f"Nome para usar no código: {m.name.replace('models/', '')}")
except Exception as e:
    print(f"Erro ao listar modelos: {e}")