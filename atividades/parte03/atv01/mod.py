#SECTION - Bibliotecas
import os

#SECTION - Lambdas
limp = lambda: os.system("cls" if os.name == "nt" else "clear") and print("")
mercurio  = lambda p: p * 3.8
venus = lambda p: p * 8.82
terra = lambda p: p * 9.8
marte = lambda p: p * 3.71
jupiter = lambda p: p * 23.13
saturno = lambda p: p * 9.01
urano = lambda p: p * 8.72
neturno = lambda p: p * 10.97
plutao = lambda p: p * 0.65
sol = lambda p: p * 274

#SECTION - Função Verificadora de planeta
def planeta(world, p):

    match world:

        case "mercurio":
            return f"O seu peso em Mercurio é de {mercurio(p):.2f}"

        case "venus":
            return f"O seu peso em Venus é de {venus(p):.2f}"

        case "terra":
            return f"O seu peso na Terra é de {terra(p):.2f}"

        case "marte":
            return f"O seu peso em Marte é de {marte(p):.2f}"

        case "jupiter":
            return f"O seu peso em Jupiter é de {jupiter(p):.2f}"

        case "saturno":
            return f"O seu peso em Saturno é de {saturno(p):.2f}"

        case "urano":
            return f"O seu peso em Urano é de {urano(p):.2f}"

        case "neturno":
            return f"O seu peso em Neturno é de {neturno(p):.2f}"

        case "plutao":
            return f"O seu peso em Plutão é de {plutao(p):.2f}"

        case "sol":
            return f"O seu peso no Sol é de {sol(p):.2f}"

        case _:
            return "Esse planeta não esta dentro do sistema solar"