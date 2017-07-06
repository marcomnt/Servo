from scipy import *
from numpy import *

class Parametros(object):
    """Parametros do sistema"""
    def __init__(self, m = 0.111, R = 0.015, d = 0.03, L = 1.0, J = 9.99e-6, g = -9.8):
        """ Definindo os valores Sistema padrão: m = 0.111, R = 0.015, d = 0.03, L = 1.0, J = 9.99e-6, g = -9.8"""
        ## Massa da bola
        self.m = m
        ## Raio da bola
        self.R = R
        ## Deslocamento da bola
        self.d = d
        ## Aceleração gravitacional
        self.g = g
        ## Comprimento da barra
        self.L = L
        ## Momento de inércia da bola
        self.J = J
        
    def setMassa(self, m):
        """ Massa da bola"""
        self.m = m
        self.calculatePlant()
            
    def getMassa(self):
        """ Massa da bola"""
        return self.m

    def setRaio(self,R):
        """ Raio da bola """
        self.R = R
        self.calculatePlant()
            
    def getRaio(self):
        """ Raio da bola """
        return self.R

    def setDeslocamento(self, d):
        """ Deslocamento da bola """
        self.d = d
        self.calculatePlant()
            
    def getDeslocamento(self):
        """ Deslocamento da bola """
        return self.d
            
    def setGravidade(self, g):
        """ Aceleração gravitacional """
        self.g = g
        self.calculatePlant()
            
    def getGravidade(self):
        """ Aceleração gravitacional """
        return self.g
            
    def setComprimento(self,L):
        """ Comprimento da barra """
        self.L = L
        self.calculatePlant()
            
    def getComprimento(self):
        """ Comprimento da barra """
        return self.L
            
    def setMomentoInercia(self, J):
        """ Momento de inércia da bola """
        self.J = J
        self.calculatePlant()
            
    def getMomentoInercia(self):
        """ Momento de inércia da bola """
        return self.J
