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

    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyWEptZFlLMkhTZS1qQWQ3VnlzVURqbDFWZG1DSHBvei15eVpfX2dCTmJZIn0.eyJleHAiOjE3ODIxNDk2MTUsImlhdCI6MTc4MjE0OTMxNSwiYXV0aF90aW1lIjoxNzgyMTQ0NzQyLCJqdGkiOiI0NGU0Y2QzYi1lMzE4LTQ1ZDAtOTg0YS1hZmJmOWI3MjRhNjciLCJpc3MiOiJodHRwczovL3Nzby5zZWZhei5jZS5nb3YuYnIvYXV0aC9yZWFsbXMvc2VmYXotYWQtcmVhbG0iLCJhdWQiOlsicGFpbmVsaW5kLWJhY2tlbmQiLCJicm9rZXIiLCJhY2NvdW50Il0sInN1YiI6IjFjYWJmODA1LTRkNjItNDU1Ni04N2RiLTgzNDU0NzVmYzhkYyIsInR5cCI6IkJlYXJlciIsImF6cCI6InBhaW5lbGluZC1mcm9udGVuZCIsIm5vbmNlIjoiMDQxOTQ5OTEtM2RkMS00ZmEzLWE4OTgtM2MxNWQ5OTJjOWY2Iiwic2Vzc2lvbl9zdGF0ZSI6IjU1MDNkMWM4LWJiODktNGMyMC04ZmJmLWM1YzEwZDE3MDkyMSIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zaWdhLnNlZmF6LmNlLmdvdi5iciJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtc2VmYXotYWQtcmVhbG0iXX0sInJlc291cmNlX2FjY2VzcyI6eyJwYWluZWxpbmQtZnJvbnRlbmQiOnsicm9sZXMiOlsiRW1wcmVzYXM6Z2V0IiwiRG9jdW1lbnRvc0Zpc2NhaXM6Z2V0IiwiTWFsaGFzRmlzY2FpczphbGxvd0FsbCIsIk1laW9zUGFnYW1lbnRvOmdldCIsIkluZGljYWRvcmVzOmdldCIsIkV4Y2Vjb2VzOmdldCIsIlNpbXBsZXNOYWNpb25hbDpnZXQiLCJNYWxoYXNGaXNjYWlzOmdldCIsIkRlYml0b3NGaXNjYWlzOmdldCJdfSwicGFpbmVsaW5kLWJhY2tlbmQiOnsicm9sZXMiOlsiRW1wcmVzYXM6Z2V0IiwiRG9jdW1lbnRvc0Zpc2NhaXM6Z2V0IiwiTWFsaGFzRmlzY2FpczphbGxvd0FsbCIsIk1laW9zUGFnYW1lbnRvOmdldCIsIkluZGljYWRvcmVzOmdldCIsIkV4Y2Vjb2VzOmdldCIsIlNpbXBsZXNOYWNpb25hbDpnZXQiLCJNYWxoYXNGaXNjYWlzOmdldCIsIkRlYml0b3NGaXNjYWlzOmdldCJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI1NTAzZDFjOC1iYjg5LTRjMjAtOGZiZi1jNWMxMGQxNzA5MjEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkRFTklTIEJSQUdBIEdPTUVTIiwiY25waiI6IjQyMDc3NTEwMDAwMTA3IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiMDQwMTIxNjIzMzAiLCJnaXZlbl9uYW1lIjoiREVOSVMgQlJBR0EiLCJmYW1pbHlfbmFtZSI6IkdPTUVTIiwiZW1haWwiOiJkZW5pc2JyYWdhZEBnbWFpbC5jb20ifQ.eLqDxRr6Cfvvs1KMDuelvykPzH8QtoCLHIMJgeCTjI_8voxgJWtxpmbrk5j0bCjZ4pIj0BMrchBVXLcIQz2wuoWLKLHUAbQc9y_zrNikgkbP3hCanoHaSuCDECROm7gxqCuD1W6cuVizEkHqSlxkM9pS4HISmMPms5aN91-dSF8aYZGiuNV84NZdwkDyT3muvWf0vYeYwEHzhnjbUzS-IrN3J4swVxNyJ6A7pOXFfJfJpYOyy5LDoTaKvttiIDXVW9xbDfCu5HaX3x14C8TnQtSREw8Ia5R-zS1co0gxBrXsgMs5NUrlz90pLdOhJJroKdO9H3CZ3ClSCHMtkcV6tw"
    refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0MTM0MDI1ZS0yZTc0LTQwODktOWQ1ZC1hNGM3OGM1MDMwMjkifQ.eyJleHAiOjE3ODIxNTExMTMsImlhdCI6MTc4MjE0OTMxNSwianRpIjoiNjdkODlmYTctODJiMy00ZmIxLTkyNzUtNjQwNDc4YWUxY2NkIiwiaXNzIjoiaHR0cHM6Ly9zc28uc2VmYXouY2UuZ292LmJyL2F1dGgvcmVhbG1zL3NlZmF6LWFkLXJlYWxtIiwiYXVkIjoiaHR0cHM6Ly9zc28uc2VmYXouY2UuZ292LmJyL2F1dGgvcmVhbG1zL3NlZmF6LWFkLXJlYWxtIiwic3ViIjoiMWNhYmY4MDUtNGQ2Mi00NTU2LTg3ZGItODM0NTQ3NWZjOGRjIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InBhaW5lbGluZC1mcm9udGVuZCIsIm5vbmNlIjoiMDQxOTQ5OTEtM2RkMS00ZmEzLWE4OTgtM2MxNWQ5OTJjOWY2Iiwic2Vzc2lvbl9zdGF0ZSI6IjU1MDNkMWM4LWJiODktNGMyMC04ZmJmLWM1YzEwZDE3MDkyMSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI1NTAzZDFjOC1iYjg5LTRjMjAtOGZiZi1jNWMxMGQxNzA5MjEifQ.JLfBH6_43gqUCgHbuTUGOX2wgieXuVQNqb-J_Luq6OI"

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
