from scipy import *
from numpy import *
from control import *
from PID import PID
from matplotlib.pyplot import * 
from control.matlab import *

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t


class Modeling(object):
	"""docstring for Modeling"""

	def __init__(self, mass, Radius, Lever, gravitty, lengthBeam, ballInertia):
		self.mass=mass
		self.Radius=Radius
		self.Lever=Lever
		self.gravitty=gravitty
		self.lengthBeam=lengthBeam
		self.ballInertia=ballInertia
		#print("modeled")

	def modeTransferFunction(self):
		H = -self.mass*self.gravitty*self.Lever/self.lengthBeam/(self.ballInertia/(self.Radius**2)+self.mass);
		ball_tf=tf([H],[1,0])
		#print(ball_tf)

		return ball_tf

	def modeSpaceState(self):
		H = -self.mass*self.gravitty/(self.ballInertia/(self.Radius**2)+self.mass);
		A = [[0, 1, 0, 0],[0,0, H, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
		B = [[0],[0],[0],[1]]
		C = [[1, 0, 0, 0]]
		D = [[0]];
		ball_ss = ss(A,B,C,D)
		#print(ball_ss)

		return ball_ss