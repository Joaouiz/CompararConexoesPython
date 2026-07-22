from datetime import date

from services.ConnectionsComparator import ConnectionsComparator
from services.DigisacService import DigisacService
from services.ArchiveService import ArquiveService

if __name__ == '__main__':
    TOKEN = ""
    digisacService = DigisacService()
    arquiveService = ArquiveService()

    escolha = input("1 - Comeco dia\n2 - Fim dia\n")

    if escolha == "1":
        listaInicio = digisacService.gerarListaConexoes(TOKEN)
        arquiveService.gerarJson(listaInicio, "./snapshots/listaInicio.json")

    elif escolha == "2":
        listaInicio = arquiveService.lerJson("./snapshots/listaInicio.json")
        listaFinal = digisacService.gerarListaConexoes(TOKEN)
        arquiveService.gerarJson(listaFinal, "./snapshots/listaFinal.json")

        comparator = ConnectionsComparator()
        relatorio = comparator.comparar(listaInicio, listaFinal)

        hoje = date.today()
        caminhoLog = f"./logs/{hoje.day}-{hoje.month}-{hoje.year}.log"
        arquiveService.gerarLog(relatorio, caminhoLog)

    else:
        print("Por favor ne...")