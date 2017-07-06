from scipy import *
from numpy import *
from control import *
from matplotlib.pyplot import * 
from Parametros import Parametros

class Analise(object):
    """docstring for Analisis"""
    def __init__(self, param=Parametros()):
        """Analise da planta do sistema"""
        self.param = param;
        ## Massa da bola
        m = param.getMassa()
        ## Raio da bola
        R = param.getRaio()
        ## Deslocamento da bola
        d = param.getDeslocamento()
        ## Aceleração gravitacional
        g = param.getGravidade()
        ## Comprimento da barra
        L = param.getComprimento()
        ## Momento de inércia da bola
        J = param.getMomentoInercia()

        s = tf([1,0],1)
        
        self.Plant = -m*g*d/L/(J/R**2+m)/s**2

    def getPlant(self):
        return self.Plant

    def getZeros(self):
        return self.Plant.zero()

    def getPolos(self):
        return self.Plant.pole()
        
    def getStepResponse(self):
        U = tf(1,[1,0])  #step
        stepR = U*self.Plant
        tempo, resposta = impulse_response(stepR, T=linspace(0,100,10000))
        return (tempo, resposta, linspace(0,100,10000), stepR)

    def plotRoots(self):
        root_locus(self.Plant)
        title('Raizes do sistema')
        grid()
