import os
import json
import csv
import pandas as pd 

def step_coletar_dados():
    print("\n   >> Procurando arquivos de dados na pasta...")
    

    if os.path.exists("dados.xlsx"):
        print("   [!] Arquivo Excel 'dados.xlsx' encontrado.")
        try:

            df = pd.read_excel("dados.xlsx")
            
            if df.empty:
                print("   [AVISO] O Excel está vazio.")
                return None

            dados_texto = df.to_csv(index=False)
            
            return f"--- DADOS DO EXCEL ---\n{dados_texto}"
            
        except Exception as e:
            print(f"   [ERRO] Falha ao ler o Excel: {e}")
            exit()


    elif os.path.exists("dados.json"):
        print("   [!] Arquivo 'dados.json' encontrado.")
        with open("dados.json", "r", encoding="utf-8") as f:
            return json.dumps(json.load(f), indent=2, ensure_ascii=False)


    elif os.path.exists("dados.csv"):
        print("   [!] Arquivo 'dados.csv' encontrado.")
        with open("dados.csv", "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            linhas = [" | ".join(row) for row in leitor]
            return "\n".join(linhas)


    elif os.path.exists("dados.txt"):
        print("   [!] Arquivo 'dados.txt' encontrado.")
        with open("dados.txt", "r", encoding="utf-8") as f:
            return f.read()


    else:
        print("   [X] Nenhum arquivo encontrado (dados.xlsx, .json, .csv ou .txt).")
        print("   Crie um arquivo 'dados.xlsx' na pasta para testar!")
        exit()

def step_processar_dados(dados):

    return dados

def step_gerar_relatorio(processado):
    return processado