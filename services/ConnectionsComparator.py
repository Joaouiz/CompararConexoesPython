from datetime import date

from models.Conexao import Conexao
from models.Status import Status


class ConnectionsComparator:
    def comparar(self, listaInicio, listaFinal):
        relatorio = []
        mapaInicio: dict[str, Conexao] = {}
        mapaFinal: dict[str, Conexao] = {}

        for conexao in listaInicio:
            mapaInicio[conexao.id] = conexao
        for conexao in listaFinal:
            mapaFinal[conexao.id] = conexao

        for f in mapaFinal.values():
            i = mapaInicio.get(f.id)

            if i is None:
                # NOVA CONEXAO
                relatorio.append(Status(False, False, False, False, True, False))
                continue
            else:
                if i.status == f.status:
                    if not i.status:
                        #COMECOU E TERMINOU CAIDA
                        relatorio.append(Status(True, False, False, False, False, False))
                        if f.last_sync is not None and f.last_shutdown is not None:
                            #SUBIU CAIU
                            hoje = date.today()

                            if f.last_shutdown > f.last_sync and f.last_shutdown.date() == hoje and f.last_sync.date() == hoje:
                                relatorio.append(Status(False, False, False, False, False, True))

                    else:
                        #COMECOU E TERMINOU ONLINE
                        relatorio.append(Status(False, True, False, False, False, False))
                elif i.status and not f.status:
                    #CAIU
                    relatorio.append(Status(False, False, True, False, False, False))
                elif not i.status and f.status:
                    #SUBIU
                    relatorio.append(Status(False, False, False, True, False, False))

        return relatorio