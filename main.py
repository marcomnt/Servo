from scipy import *
from numpy import *
from control import *
from Analysis import Analysis
from Modeling import Modeling
from PID import PID

mass = 0.111;   #mass of the ball == 0.11 kg
Radius = 0.015;	#radius of the ball  ==0.015 m
gravitty = -9.8;	#gravitational acceleration    ==9.8 m/s^2  
Lever = 1.0;	#lever arm offset    ==0.03 m
lengthBeam = 0.03;	#length of the beam            ==1.0 m
ballInertia = 9.99e-6; # ball's moment of inertia   ==9.99e-6 kg.m^2

Kps=[50,15] #Proporcional constant definition in format: [Absurd, Ideal]
Kis=[30,0] #Integrative constant definition in format: [Absurd, Ideal]
Kds=[10,40] #Derivative constant definition in format: [Absurd, Ideal]

# class to engage Modeling, analise and AMP OP modules

class main(object):
	"""docstring for main"""

	def __init__(self):
		self.modeler = Modeling(mass, Radius, gravitty, Lever, lengthBeam, ballInertia)
		analysor = Analysis(self.model()[0], Kps, Kis, Kds) #with trasfer function
		analysor = Analysis(self.model()[1], Kps, Kis, Kds) #with Space State

		pid = PID(Kps[1],Kis[1],Kds[1],self.model()[0])
		pid.toAmpOp()

		pid = PID(Kps[1],Kis[1],Kds[1],self.model()[1])
		pid.toAmpOp()

	def model(self):
		 return (self.modeler.modeTransferFunction(), self.modeler.modeSpaceState())

m=main()