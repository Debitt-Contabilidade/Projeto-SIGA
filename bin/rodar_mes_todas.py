import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from workers.extrairEmpresas import extrairListaEmpresas
from workers.extrairEntradas import baixarEntradasCompetencia
from workers.extrairSaidas import baixarSaidasCompetencia
from workers.extrairNFCE import baixarNFCECompetencia

def main():

    with open(f"./input/token.txt", "r") as arquivo:
        api_token = arquivo.read()
    
    empresas = extrairListaEmpresas(api_token)["Empresas"]
    cnpj_lista = empresas["cnpj"].tolist()
    razao_lista = empresas["razaoSocial"].tolist()
    codigo_dominio_lista = empresas["cadastro_dominio"].tolist()

    with open("./temp/temp_json/temp_execucao/executados.txt","r") as arquivo:
        executados = arquivo.read().splitlines()
    
    for cnpj, razao, codigo_dominio in zip(cnpj_lista, razao_lista, codigo_dominio_lista):
        if cnpj in executados:
            print(f"CNPJ: {cnpj} - Razão Social: {razao} (já executado)")
            continue
        print(f"CNPJ: {cnpj} - Razão Social: {razao}")

        baixarEntradasCompetencia(api_token, f"2026-06", cnpj, codigo_dominio)
        baixarSaidasCompetencia(api_token, f"2026-06", cnpj, codigo_dominio)
        baixarNFCECompetencia(api_token, f"2026-06", cnpj, codigo_dominio)
        with open(f"./input/token.txt", "r") as arquivo:
           api_token = arquivo.read()

        with open("./temp/temp_json/temp_execucao/executados.txt","a") as arquivo:
            arquivo.write(f"{cnpj}\n")

if __name__ == "__main__":

    main()