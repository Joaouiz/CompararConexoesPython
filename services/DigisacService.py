import json
from datetime import datetime

import requests

from models.Conexao import Conexao


class DigisacService:
    def gerarListaConexoes(self, token):
        url = "https://eggeremesquita.digisac.app//api/v1/services?query=%7B%22where%22%3A%7B%22archivedAt%22%3A%7B%22%24eq%22%3Anull%7D%7D%2C%22order%22%3A%5B%5B%22name%22%2C%22asc%22%5D%5D%2C%22page%22%3A1%2C%22perPage%22%3A200%7D"
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)

        dados = response.json()
        #print(json.dumps(dados, indent=4))
        #PRINTA O JSON

        conexoes = []

        for conexao in dados["data"]:
            if conexao["type"] == "whatsapp":
                nome = conexao["name"]
                ide = conexao["id"]
                status = conexao["data"]["status"].get("isConnected", False)
                last_sync = conexao["data"]["lastSyncAt"]
                last_shutdown = conexao["data"].get("lastShutdownAt")

                last_sync = datetime.fromisoformat(last_sync.replace("Z", "+00:00"))
                if last_shutdown is not None:
                    last_shutdown = datetime.fromisoformat(last_shutdown.replace("Z", "+00:00"))

                conexoes.append(Conexao(nome, ide, status, last_sync, last_shutdown))

        return conexoes