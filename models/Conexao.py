from datetime import datetime
from dataclasses import dataclass

@dataclass
class Conexao:
    nome: str
    id: str
    status: bool
    last_sync: datetime | None
    last_shutdown: datetime | None