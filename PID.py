from scipy import *
from numpy import *
from control import *
from matplotlib.pyplot import * 
from control.matlab import *

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t

class PID(object):
	"""docstring for PID"""

	def __init__(self, Kp, Ki, Kd, model, Feedback=True):
		self.model=model
		self.Kp = Kp
		self.Kd = Kd
		self.Ki = Ki
		Cs=1
		# Função PID
		if Kd != 0 or Kp != 0 or Ki != 0:
			Cs = tf([Kd, Kp, Ki],[1,0])   

		# funcao transferencia do sistema
		Y = Cs*tf(model)

		if Feedback:
			self.pid = tf(feedback(Y,1))
		else:
			self.pid = tf(Y)