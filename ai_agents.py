# ai_agents.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configuração inicial (acontece automaticamente ao importar esse arquivo)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Erro: Chave API não encontrada no .env")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def _limpar_markdown(texto):
    """Função interna (privada) para limpar ```html etc"""
    if not texto: return ""
    return texto.replace("```html", "").replace("```", "").strip()

def agente_desenvolvedor(dados):
    """AGENTE 1: Gera o primeiro rascunho do código"""
    print("🤖 [Agente Dev] Analisando dados e escrevendo código...")
    
    prompt = (
        f"Tarefa: Gere um código HTML completo usando Chart.js para visualizar os dados abaixo.\n"
        f"Estilo: Dark Mode moderno.\n"
        f"Regra: Retorne APENAS o código, sem explicações.\n\n"
        f"DADOS:\n{dados}"
    )
    
    try:
        response = model.generate_content(prompt)
        return _limpar_markdown(response.text)
    except Exception as e:
        print(f"Erro no Agente Dev: {e}")
        return None

def agente_revisor(codigo_rascunho):
    """AGENTE 2: Refina e corrige o código do Agente 1"""
    print("🧐 [Agente QA] Revisando e corrigindo bugs...")
    
    prompt = (
        f"Analise o código HTML abaixo. Corrija erros de sintaxe, tags abertas e garanta que o Chart.js funcione.\n"
        f"Se o código estiver perfeito, apenas retorne ele.\n"
        f"Retorne APENAS o HTML corrigido.\n\n"
        f"CÓDIGO PARA REVISÃO:\n{codigo_rascunho}"
    )
    
    try:
        response = model.generate_content(prompt)
        return _limpar_markdown(response.text)
    except Exception as e:
        print(f"Erro no Agente Revisor: {e}")
        return None