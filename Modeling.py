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
		print("modeled")

	def modeTransferFunction(self):
		return 0

	def modeSpaceState(self):
		return 0

	def toAmpOp(self):
		print(0)
