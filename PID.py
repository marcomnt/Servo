from scipy import *
from numpy import *
from control import *
from matplotlib.pyplot import * 
from control.matlab import *

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t

from Analise import Analise
from Parametros import Parametros

class PID(object):
    """ PID - Proportional Integral Derivative controlador """
    def __init__(self, Kp = 15, Ki = 0, Kd = 40, gain = 0.25, analise = Analise(), Feedback = True):
        """ Inicializando o controlador PID """
        self.Feedback = Feedback

        self.Kd = Kd            #componente derivativo
        self.Ki = Ki            #componente integrativo
        self.Kp = Kp            #componente proporcional

        self.gain = gain        #ganho

        self.U = tf(1,[1,0])    #função Step no domínio da frequência

        self.plant = analise.getPlant() #função transferencia da planta

        self.defineAll()
        
    def pid(self, Kp, Ki, Kd, gain):
        """ definindo controlador PID """
        self.Kd = Kd            #componente derivativo
        self.Ki = Ki            #componente integrativo
        self.Kp = Kp            #componente proporcional
        self.gain = gain		#ganho do sistema
        self.defineAll()
        
    def step(self,t_min, t_max):
        """Plotar resposta ao degrau"""
        if (self.Kd != 0 or self.Ki != 0): 
            tempo, resposta = impulse_response(self.gain*self.stepResponse, T=linspace(t_min,t_max,10000))
            return (tempo, resposta, linspace(t_min,t_max,10000))
        else:
            print("PID >> Quadratic has a nontrivial imaginary part")
    
# Definições do sistema
    def define_controlador(self):
        """ Cria função transferencia do controle PID """
        #função transferencia do controlador
        if (self.Kd != 0 or self.Ki != 0 or self.Kp != 0): 
            self.controlador = tf([self.Kd, self.Kp, self.Ki],[1,0])
        else:
            self.controlador = 1

    def define_sistem(self, Feedback = True):
        """ Cria a função do sistema completo, com PID e feedback (se True) """
        #funcão transferencia total do sistema
        self.sistem = self.controlador*self.plant     #sem feedback
        if (Feedback):
            self.sistem = feedback(self.sistem,1)   #com feedback

    def define_step_response(self):
        """ Encontra a resposta ao Step no dominio da frequência """
        self.stepResponse = self.U*self.sistem      #resposta ao degrau

    def defineAll(self):
        """ Todas as definições do sistema """
        self.define_controlador()
        self.define_sistem(self.Feedback)
        self.define_step_response()

# Gets e Sets
    def getKd(self):
        return self.Kd

    def setKd(self, Kd):
        self.Kd = Kd
        self.defineAll()
    
    def getKi(self):
        return self.Ki

    def setKi(self, Ki):
        self.Ki = Ki
        self.defineAll()
        
    def getKp(self):
        return self.Kp

    def setKp(self, Kp):
        self.Kp = Kp
        self.defineAll()
        
    def getPlant(self):
        return self.plant
    
    def setPlant(self, plant):
        self.plant = plant
        self.defineAll()

    def getGain(self):
        return self.gain
    
    def setGain(self, gain):
        self.gain = gain
        self.defineAll()

    def getFeedback(self):
        return self.Feedback
    
    def setFeedback(self, Feedback = True):
        self.Feedback = Feedback
        self.defineAll()

    def getControlador(self):
        return self.controlador

    def getSistem(self):
        return self.sistem

    def getStepResponse(self):
        return self.stepResponse
