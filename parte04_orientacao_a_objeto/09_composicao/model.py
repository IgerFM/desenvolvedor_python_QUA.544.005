#SECTION - C - Motor
class Motor:
    def __init__(self,potencia):
        self.__potencia = potencia

    #SECTION - S&G - Potencia
    @property
    def potencia(self):
        return self.__potencia
    @potencia.setter
    def potencia(self,potencia):
        self.__potencia = potencia

    #SECTION - M
    def info(self):
        return f"Potência: {self.__potencia} cv."

#SECTION - C - Carro
class Carro:
    def __init__(self,fabricante,modelo,ano,cor,potencia):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__motor = Motor(potencia) #FIXME - Composição

    #SECTION - S&G - fabricante
    @property
    def fabricante(self):
        return self.__fabricante
    @fabricante.setter
    def fabricante(self,fabricante):
        self.__fabricante = fabricante

    #SECTION - S&G - modelo
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo

    #SECTION - S&G - ano
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self,ano):
        self.__ano = ano

    #SECTION - S&G - cor
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self,cor):
        self.__cor = cor

    def exibir_detalhes(self):
        return f"\nFabricante: {self.__fabricante}\nModelo: {self.__modelo}\nAno: {self.__ano}\nCor: {self.__cor}\nMotor: {self.__motor.info()}"