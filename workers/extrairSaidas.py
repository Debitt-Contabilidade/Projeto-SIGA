import datetime
import pandas as pd
import requests
from time import sleep
import json
import os
from pathlib import Path
import uuid
import math

def baixarSaidasCompetencia(api_token,competencia,cnpj,codigo_dominio):

    id_execucao = uuid.uuid4()

    numDocumentoFiscal = []
    chaveAcesso = []
    vlrDocumento = []
    evento = []
    resultadoProcessamento = []
    grupoCfop = []
    papelOperacao = []
    tipoOperacao = []
    datReferencia = []
    datEmissao = []

    print("Processando CNPJ: ", cnpj, " Competência: ", competencia)
    data_inicio = f"{competencia}-01"
    if competencia.endswith("-02"):
        data_fim = f"{competencia}-28"
    elif competencia.endswith("-04") or competencia.endswith("-06") or competencia.endswith("-09") or competencia.endswith("-11"):
        data_fim = f"{competencia}-30"
    else:
        data_fim = f"{competencia}-31"

    link_consulta = f"https://siga.sefaz.ce.gov.br/api/v1/unidades/{cnpj}/documentos-fiscais/nf-e?size=10&page=1&sort=datEmissao,asc&dat-referencia={data_inicio},{data_fim}&tipo-operacao=SAIDA"

    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    consulta = requests.get(link_consulta, headers=headers)
    json_data = consulta.json()
    print(json_data)
    qtd_documentos = json_data["totalElements"]
    qtd_iteracoes = 0
    print(qtd_documentos)
    if qtd_documentos <= 10:
        qtd_iteracoes = 1
    else:
        qtd_iteracoes = math.ceil(qtd_documentos / 10) + 1

    for i in range(1, int(qtd_iteracoes)+1):

        try:
            link_consulta = f"https://siga.sefaz.ce.gov.br/api/v1/unidades/{cnpj}/documentos-fiscais/nf-e?size=50&page={i}&sort=datEmissao,asc&dat-referencia={data_inicio},{data_fim}&tipo-operacao=SAIDA"
            consulta = requests.get(link_consulta, headers=headers)
            json_data = consulta.json()

            print(consulta.status_code)
            print(consulta.text)
            
            with open(f"./temp/temp_json/temp_json_saidas_competencia/saidas_competencia_{cnpj}_{competencia}_{i}_{id_execucao}.json", "w") as arquivo:
                json.dump(json_data, arquivo, indent=4)

            with open(f"./input/token.txt", "r") as arquivo:
           
                api_token = arquivo.read()
        
        except Exception as e:
            print(f"Erro na consulta: {e}")
            continue

        sleep(1)

        pasta_json = Path("./temp/temp_json/temp_json_saidas_competencia")
        pasta = Path(pasta_json)
        for arquivo in pasta.glob('*.json'):
            if str(id_execucao) in arquivo.name:     
                with open(arquivo, "r") as file:
                    data = json.load(file)
                    for saida in json_data["data"]:
                        numDocumentoFiscal.append(saida["numDocumentoFiscal"])
                        chaveAcesso.append(saida["chaveAcesso"])
                        vlrDocumento.append(saida["vlrDocumento"])
                        evento.append(saida["evento"])
                        resultadoProcessamento.append(saida["resultadoProcessamento"])
                        grupoCfop.append(saida["grupoCfop"])
                        papelOperacao.append(saida["papelOperacao"])
                        tipoOperacao.append(saida["tipoOperacao"])
                        datReferencia.append(saida["datReferencia"])
                        datEmissao.append(saida["datEmissao"])        

                os.remove(arquivo)
                print(arquivo)

        df_final = pd.DataFrame({
        "cnpj": cnpj,
        "numDocumentoFiscal": numDocumentoFiscal,
        "chaveAcesso": chaveAcesso,
        "vlrDocumento": vlrDocumento,
        "evento": evento,
        "resultadoProcessamento": resultadoProcessamento,
        "grupoCfop": grupoCfop,
        "papelOperacao": papelOperacao,
        "tipoOperacao": tipoOperacao,
        "datReferencia": datReferencia,
        "datEmissao": datEmissao})

        df_final.to_csv(f"./dados/saidas_competencia/saidas_competencia_{codigo_dominio}_{cnpj}_{competencia.replace("-","_")}.csv", index=False)

    return {"consulta": json_data, "consulta_status_code": consulta.status_code, "consulta_text": consulta.text}

def main():

    with open(f"./input/token.txt", "r") as arquivo:
        api_token = arquivo.read()

    competencia = "2026-05"
    cnpj = "12345678000195"    
    # exemplo de uso: extrai empresas via API
    dados = baixarSaidasCompetencia(api_token,competencia,cnpj)
    

if __name__ == "__main__":
    main()
        