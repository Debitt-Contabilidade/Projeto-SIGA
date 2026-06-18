# ========================================================================
# ===================== IMPORTAÇÃO DE BIBLIOTECAS ========================
# ========================================================================

# Bibliotecas de terceiros

# Biblioteca para manipulação de Requisições REST
import requests

# Bibliotecas nativas

# Biblioteca para manipulação de tempo
from time import sleep
from datetime import datetime

# ========================================================================
# ===================== CONFIGURAÇÕES INICIAIS ============================
# ========================================================================

def main():

    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyWEptZFlLMkhTZS1qQWQ3VnlzVURqbDFWZG1DSHBvei15eVpfX2dCTmJZIn0.eyJleHAiOjE3ODE3OTU2NTgsImlhdCI6MTc4MTc5NTM1OCwiYXV0aF90aW1lIjoxNzgxNzk0ODI0LCJqdGkiOiJkNTFkOTc2Ny0zZjgxLTRlZTMtOTQ3My0xYTM2NDM2ZjNiMjUiLCJpc3MiOiJodHRwczovL3Nzby5zZWZhei5jZS5nb3YuYnIvYXV0aC9yZWFsbXMvc2VmYXotYWQtcmVhbG0iLCJhdWQiOlsicGFpbmVsaW5kLWJhY2tlbmQiLCJicm9rZXIiLCJhY2NvdW50Il0sInN1YiI6IjFjYWJmODA1LTRkNjItNDU1Ni04N2RiLTgzNDU0NzVmYzhkYyIsInR5cCI6IkJlYXJlciIsImF6cCI6InBhaW5lbGluZC1mcm9udGVuZCIsIm5vbmNlIjoiYTBkNGMyMzctNDRkYy00NDQ2LTk2YjItYTE5YzAzMzNlNmIwIiwic2Vzc2lvbl9zdGF0ZSI6ImRmOTU5MzJhLTI4OGMtNDg5My1iNWYxLTc1OGI5ODMyOTUwZiIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zaWdhLnNlZmF6LmNlLmdvdi5iciJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtc2VmYXotYWQtcmVhbG0iXX0sInJlc291cmNlX2FjY2VzcyI6eyJwYWluZWxpbmQtZnJvbnRlbmQiOnsicm9sZXMiOlsiRW1wcmVzYXM6Z2V0IiwiRG9jdW1lbnRvc0Zpc2NhaXM6Z2V0IiwiTWFsaGFzRmlzY2FpczphbGxvd0FsbCIsIk1laW9zUGFnYW1lbnRvOmdldCIsIkluZGljYWRvcmVzOmdldCIsIkV4Y2Vjb2VzOmdldCIsIlNpbXBsZXNOYWNpb25hbDpnZXQiLCJNYWxoYXNGaXNjYWlzOmdldCIsIkRlYml0b3NGaXNjYWlzOmdldCJdfSwicGFpbmVsaW5kLWJhY2tlbmQiOnsicm9sZXMiOlsiRW1wcmVzYXM6Z2V0IiwiRG9jdW1lbnRvc0Zpc2NhaXM6Z2V0IiwiTWFsaGFzRmlzY2FpczphbGxvd0FsbCIsIk1laW9zUGFnYW1lbnRvOmdldCIsIkluZGljYWRvcmVzOmdldCIsIkV4Y2Vjb2VzOmdldCIsIlNpbXBsZXNOYWNpb25hbDpnZXQiLCJNYWxoYXNGaXNjYWlzOmdldCIsIkRlYml0b3NGaXNjYWlzOmdldCJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJkZjk1OTMyYS0yODhjLTQ4OTMtYjVmMS03NThiOTgzMjk1MGYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkRFTklTIEJSQUdBIEdPTUVTIiwiY25waiI6IjQyMDc3NTEwMDAwMTA3IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiMDQwMTIxNjIzMzAiLCJnaXZlbl9uYW1lIjoiREVOSVMgQlJBR0EiLCJmYW1pbHlfbmFtZSI6IkdPTUVTIiwiZW1haWwiOiJkZW5pc2JyYWdhZEBnbWFpbC5jb20ifQ.dDZdNtatIPStS56oSfHyMqRzO2gfyWzlrbDVyiq0EsUSo4eCYTnMugBDSUG5atlT9bwQdGrpUsw4mCTKTdS1uY_Fp-VrGpAFfbxk56tAvAOSRYyt9oLbWasWoar9Yx0Yqh_wCylBC5YDZeJisb22HxA-51plhO5N2EzgJ8g0z0vYjLDVNXCuXD_1fTNkFaDb9NrVvanJOSJf9WsRCUOyR2ec5UDyiE8ZjHm72mbzItV79Aku88VYr7rcqxETAU-VdT55mMt_XmJFN_xRamB8LyygcFDNs7HzBmgoGmcAyo-yguWbbbdDpkN661sPVOMOQI8kNhVNPoD5pprjhmfAOA"
    refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0MTM0MDI1ZS0yZTc0LTQwODktOWQ1ZC1hNGM3OGM1MDMwMjkifQ.eyJleHAiOjE3ODE3OTcxNTUsImlhdCI6MTc4MTc5NTM1OCwianRpIjoiODU2NmFjZTMtMzhmMC00MTA1LTlmNGYtNGI1Y2VmOTFkMGEwIiwiaXNzIjoiaHR0cHM6Ly9zc28uc2VmYXouY2UuZ292LmJyL2F1dGgvcmVhbG1zL3NlZmF6LWFkLXJlYWxtIiwiYXVkIjoiaHR0cHM6Ly9zc28uc2VmYXouY2UuZ292LmJyL2F1dGgvcmVhbG1zL3NlZmF6LWFkLXJlYWxtIiwic3ViIjoiMWNhYmY4MDUtNGQ2Mi00NTU2LTg3ZGItODM0NTQ3NWZjOGRjIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InBhaW5lbGluZC1mcm9udGVuZCIsIm5vbmNlIjoiYTBkNGMyMzctNDRkYy00NDQ2LTk2YjItYTE5YzAzMzNlNmIwIiwic2Vzc2lvbl9zdGF0ZSI6ImRmOTU5MzJhLTI4OGMtNDg5My1iNWYxLTc1OGI5ODMyOTUwZiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJkZjk1OTMyYS0yODhjLTQ4OTMtYjVmMS03NThiOTgzMjk1MGYifQ.q_9hQjHVihtiM7iAzxRPF57l2HoQ4nUfjQwhqZgY8Ko"

    urL_requisicao = "https://sso.sefaz.ce.gov.br/auth/realms/sefaz-ad-realm/protocol/openid-connect/token"

    while True:
        
        payload = {
                    "grant_type": "refresh_token",
                    "client_id": "painelind-frontend",
                    "refresh_token": refresh_token
                }

        response = requests.post(
            url = urL_requisicao,
            data = payload,
            headers={
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
        )

        print(response.status_code)

        token = response.json().get("access_token")
        refresh_token = response.json().get("refresh_token")

        print(f"Token atualizado com sucesso! ({datetime.now()})")

        sleep(120)

if __name__ == "__main__":

    main()
