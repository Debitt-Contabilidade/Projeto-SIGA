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

    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyWEptZFlLMkhTZS1qQWQ3VnlzVURqbDFWZG1DSHBvei15eVpfX2dCTmJZIn0.eyJleHAiOjE3ODE4MDAwNDcsImlhdCI6MTc4MTc5OTc0NywiYXV0aF90aW1lIjoxNzgxNzk0ODI0LCJqdGkiOiI3MjcxZTBmMC0xNzMxLTQzNWQtYWUwOS02NGZhMWJkYTc5ODEiLCJpc3MiOiJodHRwczovL3Nzby5zZWZhei5jZS5nb3YuYnIvYXV0aC9yZWFsbXMvc2VmYXotYWQtcmVhbG0iLCJhdWQiOlsicGFpbmVsaW5kLWJhY2tlbmQiLCJicm9rZXIiLCJhY2NvdW50Il0sInN1YiI6IjFjYWJmODA1LTRkNjItNDU1Ni04N2RiLTgzNDU0NzVmYzhkYyIsInR5cCI6IkJlYXJlciIsImF6cCI6InBhaW5lbGluZC1mcm9udGVuZCIsIm5vbmNlIjoiNTE3NTc4Y2ItM2M4NC00YjJkLWFlMGEtNjA0ZDBiYmZhYzI1Iiwic2Vzc2lvbl9zdGF0ZSI6ImRmOTU5MzJhLTI4OGMtNDg5My1iNWYxLTc1OGI5ODMyOTUwZiIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zaWdhLnNlZmF6LmNlLmdvdi5iciJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtc2VmYXotYWQtcmVhbG0iXX0sInJlc291cmNlX2FjY2VzcyI6eyJwYWluZWxpbmQtZnJvbnRlbmQiOnsicm9sZXMiOlsiRW1wcmVzYXM6Z2V0IiwiRG9jdW1lbnRvc0Zpc2NhaXM6Z2V0IiwiTWFsaGFzRmlzY2FpczphbGxvd0FsbCIsIk1laW9zUGFnYW1lbnRvOmdldCIsIkluZGljYWRvcmVzOmdldCIsIkV4Y2Vjb2VzOmdldCIsIlNpbXBsZXNOYWNpb25hbDpnZXQiLCJNYWxoYXNGaXNjYWlzOmdldCIsIkRlYml0b3NGaXNjYWlzOmdldCJdfSwicGFpbmVsaW5kLWJhY2tlbmQiOnsicm9sZXMiOlsiRW1wcmVzYXM6Z2V0IiwiRG9jdW1lbnRvc0Zpc2NhaXM6Z2V0IiwiTWFsaGFzRmlzY2FpczphbGxvd0FsbCIsIk1laW9zUGFnYW1lbnRvOmdldCIsIkluZGljYWRvcmVzOmdldCIsIkV4Y2Vjb2VzOmdldCIsIlNpbXBsZXNOYWNpb25hbDpnZXQiLCJNYWxoYXNGaXNjYWlzOmdldCIsIkRlYml0b3NGaXNjYWlzOmdldCJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJkZjk1OTMyYS0yODhjLTQ4OTMtYjVmMS03NThiOTgzMjk1MGYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkRFTklTIEJSQUdBIEdPTUVTIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiMDQwMTIxNjIzMzAiLCJnaXZlbl9uYW1lIjoiREVOSVMgQlJBR0EiLCJmYW1pbHlfbmFtZSI6IkdPTUVTIiwiZW1haWwiOiJkZW5pc2JyYWdhZEBnbWFpbC5jb20ifQ.XZZ8I1gSAhFiQ4qzvtgJiOKZsDdqxfJhtJCknbfNJux2wSrIasmd6zSChcxX_ZYQhA3OcjpJoXiWHxbw6L_cD25e4h-_AOui98Q2G5OubPm65EzxA5fCHelWLURnl0Tlu7CWlnROw8bOIE4X817dT4-EG6epMzHYD7jLxPEd49PwdX3svKaZqR1x9NSOBO63b64uwOm8F9FtW3AR2lM5ULmyggaCSsLn_FlI4Ur7Jv-2bn0u0YK7FoFciXzRCOCcM5I1BLqWAaCup4EgabDlLpuCOelfPfsl785vIgfQp_jxkOklXHEEpmd2OSjRgF2jvWruTLiOdmIa8h_DV74Wxw"
    refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0MTM0MDI1ZS0yZTc0LTQwODktOWQ1ZC1hNGM3OGM1MDMwMjkifQ.eyJleHAiOjE3ODE4MDE1NDUsImlhdCI6MTc4MTc5OTc0NywianRpIjoiYWFjYzhlMjMtNTdkMi00YzUxLWIxZjItMWQ2NDI3N2NjMzY1IiwiaXNzIjoiaHR0cHM6Ly9zc28uc2VmYXouY2UuZ292LmJyL2F1dGgvcmVhbG1zL3NlZmF6LWFkLXJlYWxtIiwiYXVkIjoiaHR0cHM6Ly9zc28uc2VmYXouY2UuZ292LmJyL2F1dGgvcmVhbG1zL3NlZmF6LWFkLXJlYWxtIiwic3ViIjoiMWNhYmY4MDUtNGQ2Mi00NTU2LTg3ZGItODM0NTQ3NWZjOGRjIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InBhaW5lbGluZC1mcm9udGVuZCIsIm5vbmNlIjoiNTE3NTc4Y2ItM2M4NC00YjJkLWFlMGEtNjA0ZDBiYmZhYzI1Iiwic2Vzc2lvbl9zdGF0ZSI6ImRmOTU5MzJhLTI4OGMtNDg5My1iNWYxLTc1OGI5ODMyOTUwZiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJkZjk1OTMyYS0yODhjLTQ4OTMtYjVmMS03NThiOTgzMjk1MGYifQ.TYzx43SrE1fJtm4Z9poE1JnQhbhMp3ozaxIrvfxb7II"

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

        with open("./input/token.txt", "w") as arquivo:
            arquivo.write(token)

        print(f"Token atualizado com sucesso! ({datetime.now()})")

        sleep(120)

if __name__ == "__main__":

    main()
