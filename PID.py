from scipy import *
from numpy import *
from control import *

class PID(object):
	"""docstring for PID"""
	def __init__(self, kp, ki, kd, model):
		self.pid=0
		self.kp=kp
		self.ki=ki
		self.kd=kd
		self.model=model
		#print("PID construtor=",  self.kp, self.ki, self.kd)
		
	def toAmpOp(self):
		#print("AmpOpPID")
		pass