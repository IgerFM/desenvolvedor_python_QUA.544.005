#NOTE - Assim como o operador ternario e o lamba, é uma forma simplificade de fazer uma classe
#SECTION - Biblioteca
from dataclasses import dataclass

#SECTION - DC - Pessoa
@dataclass
class Pessoa:
    #NOTE - Os atribulos devem ser definidos encapsulados
    nome: str
    cpf: str
    email: str
    idade: int
    altura: float
    #NOTE - Isto esta fazendo o trabalho do  __init__ e tambem o do Set & Get