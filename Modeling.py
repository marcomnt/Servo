from scipy import *
from numpy import *
from control import *

class Modeling(object):
	"""docstring for Modeling"""
	def __init__(self, mass, Radius, gravitty, Lever, lengthBeam, ballInertia):
		self.mass=mass
		self.Radius=Radius
		self.gravitty=gravitty
		self.Lever=Lever
		self.lengthBeam=lengthBeam
		self.ballInertia=ballInertia
		#print("modeled")

	def modeTransferFunction(self):
		H = -self.mass*self.gravitty/(self.ballInertia/(self.Radius**2)+self.mass);
		ball_tf=tf([H],[1,0])
		print(ball_tf)
		
		return 0

	def modeSpaceState(self):
		H = -self.mass*self.gravitty/(self.ballInertia/(self.Radius**2)+self.mass);
		A = [[0, 1, 0, 0],[0,0, H, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
		B = [[0],[0],[0],[1]]
		C = [[1, 0, 0, 0]]
		D = [[0]];
		ball_ss = ss(A,B,C,D)
		#print(ball_ss)
		return 0

	def toAmpOp(self):
		print(0)
