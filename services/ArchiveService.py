import json
from dataclasses import asdict
from datetime import datetime, date

from models.Conexao import Conexao

class ArquiveService:
    def gerarJson(self, lista, caminho):
        with open(caminho, "w") as arquivo:
            json.dump(
                [asdict(c) for c in lista],
                arquivo,
                indent=4,
                ensure_ascii=False,
                default=str
            )

    def lerJson(self, caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        lista = []

        for conexao in dados:
            lista.append(Conexao(
                nome=conexao["nome"],
                id=conexao["id"],
                status=conexao["status"],
                last_sync=datetime.fromisoformat(conexao["last_sync"]) if conexao["last_sync"] else None,
                last_shutdown=datetime.fromisoformat(conexao["last_shutdown"]) if conexao["last_shutdown"] else None
            ))

        return lista

    def gerarLog(self, relatorio, caminho):

        subiu = 0
        caiu = 0
        subiu_caiu = 0

        for i in relatorio:
            if i.subiu:
                subiu += 1
            elif i.caiu:
                caiu += 1
            elif i.subiuCaiu:
                subiu_caiu += 1

        with open(caminho, "w", encoding="utf-8") as arquivo:
            linha = (f"{subiu};"
                     f"{caiu};"
                     f"{subiu_caiu};")
            arquivo.write(linha)