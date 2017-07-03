from scipy import *
from numpy import *
from control import *
from PID import PID
from matplotlib.pyplot import * 
from control.matlab import *

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t


class Analysis(object):
	"""docstring for Analisis"""
	# Step (frequence)


	def __init__(self,model,Kps,Kis,Kds):
		self.model=tf(model)
		self.Kps=Kps
		self.Kis=Kis
		self.Kds=Kds
		self.U = tf(1,[1,0])
		self.gain = 0.25

		self.Analyse()
		
	def Analyse(self):
		#self.allOpen()
		self.AnalysisPID()
		#print("Analyse")

	def AnalysisPID(self):
		kp=self.Kps[1]
		ki=self.Kis[1]
		kd=self.Kds[1]
		pidO = PID(kp,ki,kd,self.model,True)
		print("pidO", pidO)
		pid= pidO.pid
		print("pid", pidO ,"Kp=",pidO.Kp,"Ki=",pidO.Ki,"Kd=",pidO.Kd)
		self.allPID(pid)

		# kp=self.Kps[0]
		# pidO = PID(kp,ki,kd,self.model,True)
		# print("pidO", pidO)
		# pid=pidO.pid
		# print("pid", pidO ,"Kp=",pidO.Kp,"Ki=",pidO.Ki,"Kd=",pidO.Kd)
		# self.allPID(pid)
		# kp=self.Kps[1]

		
		# ki=self.Kis[0]
		# pidO = PID(kp,ki,kd,self.model,True)
		# print("pidO", pidO)
		# pid=pidO.pid
		# print("pid", pidO ,"Kp=",pidO.Kp,"Ki=",pidO.Ki,"Kd=",pidO.Kd)
		# self.allPID(pid)
		# ki=self.Kis[1]

		# kd=self.Kds[0]
		# pidO = PID(kp,ki,kd,self.model,True)
		# print("pidO", pidO)
		# pid=pidO.pid
		# print("pid", pidO ,"Kp=",pidO.Kp,"Ki=",pidO.Ki,"Kd=",pidO.Kd)
		# self.allPID(pid)

	def allOpen(self):
		self.zerosOpen()
		self.polesOpen()
		self.rootLocusOpen()
		self.step(self.model)
		#print("allmight")

	def zerosOpen(self):
		print(zero(self.model))
		#print("zero1")

	def polesOpen(self):
		print(pole(self.model))
		#print("polo1")

	def rootLocusOpen(self):
		root_locus(self.model)
		title("Raizes")
		grid()
		show()

	def allPID(self,pid):
		zero(pid)
		#print("zero")
		pole(pid)
		#print("polo")
		root_locus(pid)
		title("RaizesPID")
		grid()
		show()
		self.step(pid)
		#print("allmight2")

	def step(self,model, t_min=0, t_max=8):
		#resposta ao degrau
		Y = self.gain*tf(model)*self.U
		print ("Resposta ao degrau: ",Y)

		tempo, resposta = impulse_response(Y, linspace(t_min,t_max,10000))

		figure()
		plot(tempo, resposta.T)
		grid()
		if isinstance(model, PID):
			title('Resposta ao Degrau (Kp ='+str(model.Kp)+',Ki ='+str(model.Ki)+', Kd ='+str(model.Kd))
		else:
			title('Resposta ao Degrau')
		ylabel('Amplitude')
		xlabel('Tempo')
		show()