from dataclasses import dataclass

@dataclass
class Status:
    continuaCaida: bool
    continuaOnline: bool
    caiu: bool
    subiu: bool
    novaConexao: bool
    subiuCaiu: bool