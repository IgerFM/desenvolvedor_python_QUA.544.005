#NOTE - É recomendavel evitar utilizar herança multipla pois ela pode dificultar manutenções futuras

#SECTION - SC - Carro
class Carro:
    def __init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapamento):
        self.__cambio = cambio
        self.__buzina = buzina
        self.__estepe = estepe
        self.__porta_malas = porta_malas
        self.__volante = volante
        self.__retrovisor = retrovisor
        self.__escapamento = escapamento
    
    #SECTION - SG - cambio
    @property
    def cambio(self):
        return self.__cambio
    @cambio.setter
    def cambio(self,cambio):
        self.cambio = cambio
    
    #SECTION - SG - buzina
    @property
    def buzina(self):
        return self.__buzina
    @buzina.setter
    def buzina(self,buzina):
        self.buzina = buzina
    
    #SECTION - SG - estepe
    @property
    def estepe(self):
        return self.__estepe
    @estepe.setter
    def estepe(self,estepe):
        self.estepe = estepe
    
    #SECTION - SG - porta_malas
    @property
    def porta_malas(self):
        return self.__porta_malas
    @porta_malas.setter
    def porta_malas(self,porta_malas):
        self.porta_malas = porta_malas
    
    #SECTION - SG - volante
    @property
    def volante(self):
        return self.__volante
    @volante.setter
    def volante(self,volante):
        self.volante = volante
    
    #SECTION - SG - retrovisor
    @property
    def retrovisor(self):
        return self.__retrovisor
    @retrovisor.setter
    def retrovisor(self,retrovisor):
        self.retrovisor = retrovisor
    
    #SECTION - SG - escapamento
    @property
    def escapamento(self):
        return self.__escapamento
    @escapamento.setter
    def escapamento(self,escapamento):
        self.escapamento = escapamento
    
    #SECTION - SG - cambio
    @property
    def cambio(self):
        return self.__cambio
    @cambio.setter
    def cambio(self,cambio):
        self.cambio = cambio

#SECTION - SC - Avião
class Aviao:
    def __init__(self,asa,turbina,aerofolio,calda,manche,caixa_preta,transponder):
        self.__asa = asa
        self.__turbina = turbina
        self.__aerofolio = aerofolio
        self.__calda = calda
        self.__manche = manche
        self.__caixa_preta = caixa_preta
        self.__transponder = transponder

    #SECTION - SG - asa
    @property
    def asa(self):
        return self.__asa
    @asa.setter
    def asa(self,asa):
        self.asa = asa
    
    #SECTION - SG - turbina
    @property
    def turbina(self):
        return self.__turbina
    @turbina.setter
    def turbina(self,turbina):
        self.turbina = turbina
    
    #SECTION - SG - aerofolio
    @property
    def aerofolio(self):
        return self.__aerofolio
    @aerofolio.setter
    def aerofolio(self,aerofolio):
        self.aerofolio = aerofolio
    
    #SECTION - SG - calda
    @property
    def calda(self):
        return self.__calda
    @calda.setter
    def calda(self,calda):
        self.calda = calda
    
    #SECTION - SG - manche
    @property
    def manche(self):
        return self.__manche
    @manche.setter
    def manche(self,manche):
        self.manche = manche
    
    #SECTION - SG - caixa_preta
    @property
    def caixa_preta(self):
        return self.__caixa_preta
    @caixa_preta.setter
    def caixa_preta(self,caixa_preta):
        self.caixa_preta = caixa_preta
    
    #SECTION - SG - transponder
    @property
    def transponder(self):
        return self.__transponder
    @transponder.setter
    def transponder(self,transponder):
        self.transponder = transponder

#SECTION - C - CarroAviao
class CarroAviao(Carro,Aviao):
    def __init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapamento,asa,turbina,aerofolio,calda,manche,caixa_preta,transponder):
        Carro.__init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapamento)
        Aviao.__init__(self,asa,turbina,aerofolio,calda,manche,caixa_preta,transponder)