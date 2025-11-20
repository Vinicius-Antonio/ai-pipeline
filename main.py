
import os
from pipeline.pipeline import Pipeline
from pipeline.steps import step_coletar_dados, step_processar_dados, step_gerar_relatorio


from ai_agents import agente_desenvolvedor, agente_revisor

if __name__ == "__main__":

    pipeline = Pipeline([
        step_coletar_dados,
        step_processar_dados,
        step_gerar_relatorio
    ])

    print("--- 1. INICIANDO COLETA DE DADOS ---")
    dados = pipeline.run()

    if not dados or len(dados) < 10:
        print("❌ Erro: Não há dados suficientes para gerar gráficos.")
        exit()


    html_rascunho = agente_desenvolvedor(dados)

    if html_rascunho:

        html_final = agente_revisor(html_rascunho)
        
        if html_final:

            nome_arquivo = "dashboard_final.html"
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(html_final)
            
            print("\n" + "="*40)
            print(f"✅ PROCESSO CONCLUÍDO!")
            print(f"📊 Dashboard salvo em: {nome_arquivo}")
            print("="*40)
        else:
            print("❌ Falha na revisão do código.")
    else:
        print("❌ Falha na geração do rascunho.")