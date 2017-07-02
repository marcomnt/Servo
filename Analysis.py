from scipy import *
from numpy import *
from control import *

class Analysis(object):
	"""docstring for Analisis"""
	def __init__(self,model,Kps,Kis,Kds):
		self.model=model
		self.Kps=Kps
		self.Kis=Kis
		self.Kds=Kds

	def Analyse(self):
		self.allOpen()
		self.AnalysisPID()

	def AnalysisPID(self):
		Kp=Kps[1]
		Ki=Kis[1]
		kd=Kds[1]
		pid = PID(kp,ki,kd,model)
		self.allPID(pid)

		Kp=self.Kps[0]
		pidO = PID(kp,ki,kd,model)
		pid=pidO.pid
		self.allPID(pid)
		Kp=self.Kps[1]

		
		Ki=self.Kis[0]
		pidO = PID(kp,ki,kd,model)
		pid=pidO.pid
		self.allPID(pid)
		Ki=self.Kis[1]

		Kd=self.Kds[0]
		pidO = PID(kp,ki,kd,model)
		pid=pidO.pid
		self.allPID(pid)

	def allOpen(self):
		self.zerosOpen()
		self.polesOpen()
		self.rootLocusOpen()

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

	def zerosPID(self,pid):
		pass

	def polesPID(self,pid):
		pass

	def rootLocusPID(self,pid):
		pass