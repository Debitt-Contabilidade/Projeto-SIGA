import json
import pandas as pd
import requests
import datetime 
import uuid
import os
from pathlib import Path

def extrairListaEmpresas(api_token):

    id_execucao = uuid.uuid4()

    link_consulta = "https://siga.sefaz.ce.gov.br/api/v1/unidades-resumo-malha?size=10&page=1&sort=indicadores,desc"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    consulta = requests.get(link_consulta, headers=headers)
    print(consulta.status_code)
    print(consulta.text)
    print(consulta.json())
    json_data = consulta.json()
    qtd_empresas = json_data["totalElements"]
    qtd_paginas = qtd_empresas / 10 + 1
    print(f"Quantidade de empresas: {qtd_empresas}")

    for i in range(1, int(qtd_paginas)):
        link_consulta = f"https://siga.sefaz.ce.gov.br/api/v1/unidades-resumo-malha?size=10&page={i}&sort=indicadores,desc"
        consulta = requests.get(link_consulta, headers=headers)
        json_data = consulta.json()

        with open(f"./temp/temp_json/temp_json_cadastro_empresas/cadastro_empresas_{i}_{id_execucao}.json", "w") as arquivo:
            json.dump(json_data, arquivo, indent=4)
        
        
    cnpj = []
    cgf = []
    razaoSocial = []
    regime = []
    cadastro_dominio = []
    empresas_dominio = pd.read_csv("./input/empresas.csv", sep = ",",encoding="latin1",quotechar="'",dtype={"cgce_emp": str, "codi_emp": int})
    empresas_dominio["cgce_emp"] = empresas_dominio["cgce_emp"].str.replace(r'\D', '', regex=True).str.zfill(14)
    
    pasta_json = Path("./temp/temp_json/temp_json_cadastro_empresas")
    pasta = Path(pasta_json)
    
    for arquivo in pasta.glob('*.json'):
        if str(id_execucao) in arquivo.name:
            with open(arquivo, "r") as file:
                data = json.load(file)
                for empresa in data["data"]:
                    tamanho_cnpj = len(str(empresa["cnpj"]))
                    if tamanho_cnpj < 14:
                        cnpj_formatado = str(empresa["cnpj"]).zfill(14)
                    else:
                        cnpj_formatado = str(empresa["cnpj"])
                    cnpj.append(cnpj_formatado)
                    cgf.append(empresa["cgf"])
                    razaoSocial.append(empresa["razaoSocial"])
                    regime.append(empresa["regime"])    

                    try:
                        empresa_dominio_cod = empresas_dominio[empresas_dominio["cgce_emp"] == cnpj_formatado]["codi_emp"].tolist()[0]
                    except IndexError:
                        empresa_dominio_cod = 0

                    if not empresa_dominio_cod < 0:
                        cadastro_dominio.append(empresa_dominio_cod)
                    else:
                        cadastro_dominio.append("Não cadastrada")    

            os.remove(arquivo)
            print(arquivo)

    df_final = pd.DataFrame({
        "cnpj": cnpj,
        "cgf": cgf,
        "razaoSocial": razaoSocial,
        "regime": regime,
        "cadastro_dominio": cadastro_dominio
    })

    df_final = df_final[df_final["cadastro_dominio"] != 0]

    df_final.to_csv(f"./dados/cadastro_empresas/cadastro_empresas.csv", index=False)

    return {"Quantidade de Empresas": qtd_empresas,
            "Quantidade de Páginas": qtd_paginas,
            "Empresas": df_final}

def main():
    
    with open(f"./input/token.txt", "r") as arquivo:
        api_token = arquivo.read()
        
    # exemplo de uso: extrai empresas via API
    dados = extrairListaEmpresas(api_token)

if __name__ == "__main__":
    
    main()

