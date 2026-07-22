import json
import requests


class DigisacService:
    def gerarListaConexoes(self, token):
        url = "https://eggeremesquita.digisac.app//api/v1/services?query=%7B%22where%22%3A%7B%22archivedAt%22%3A%7B%22%24eq%22%3Anull%7D%7D%2C%22order%22%3A%5B%5B%22name%22%2C%22asc%22%5D%5D%2C%22page%22%3A1%2C%22perPage%22%3A200%7D"
        payload = {}
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)

        dados = response.json()
        #print(json.dumps(dados, indent=4))
        #PRINTA O JSON

        conexoes = []
        contador = 0

        for i in range(dados["total"]):
            if dados["data"][i]["type"] == "whatsapp":
                contador += 1

        print(contador)