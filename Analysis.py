from scipy import *
from numpy import *
from control import *
from PID import PID


class Analysis(object):
	"""docstring for Analisis"""
	def __init__(self,model,Kps,Kis,Kds):
		self.model=model
		self.Kps=Kps
		self.Kis=Kis
		self.Kds=Kds
		self.Analyse()

	def Analyse(self):
		self.allOpen()
		self.AnalysisPID()
		#print("Analyse")

	def AnalysisPID(self):
		kp=self.Kps[1]
		ki=self.Kis[1]
		kd=self.Kds[1]
		pid = PID(kp,ki,kd,self.model)
		self.allPID(pid)

		kp=self.Kps[0]
		pidO = PID(kp,ki,kd,self.model)
		pid=pidO.pid
		self.allPID(pid)
		kp=self.Kps[1]

		
		ki=self.Kis[0]
		pidO = PID(kp,ki,kd,self.model)
		pid=pidO.pid
		self.allPID(pid)
		ki=self.Kis[1]

		kd=self.Kds[0]
		pidO = PID(kp,ki,kd,self.model)
		pid=pidO.pid
		self.allPID(pid)

	def allOpen(self):
		self.zerosOpen()
		self.polesOpen()
		self.rootLocusOpen()
		#print("allmight")

	def zerosOpen(self):
		pass

	def polesOpen(self,):
		pass

	def rootLocusOpen(self):
		pass

	def allPID(self,pid):
		self.zerosPID(pid)
		self.polesPID(pid)
		self.rootLocusPID(pid)
		#print("allmight2")

	def zerosPID(self,pid):
		pass

	def polesPID(self,pid):
		pass

	def rootLocusPID(self,pid):
		pass