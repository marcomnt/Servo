from scipy import *
from numpy import *
from control import *
import Analysis
import Modeling

# class to engage Modeling, analise and AMP OP modules

class main(object):
	"""docstring for main"""
	mass = 0.111;   #mass of the ball == 0.11 kg
	Radius = 0.015;	#radius of the ball  ==0.015 m
	gravitty = -9.8;	#gravitational acceleration    ==9.8 m/s^2  
	Lever = 1.0;	#lever arm offset    ==0.03 m
	lengthBeam = 0.03;	#length of the beam            ==1.0 m
	ballInertia = 9.99e-6; # ball's moment of inertia   ==9.99e-6 kg.m^2
	Kps=[50,15] #Proporcional constant definition in format: [Absurd, Ideal]
	Kis=[30,0] #Integrative constant definition in format: [Absurd, Ideal]
	Kds=[10,40] #Derivative constant definition in format: [Absurd, Ideal]
	


	def __init__(self):
		modeler = Modeling(mass, Radius, gravitty, Lever, lengthBeam, ballInertia)
		analysor = Analysis(model()[0], Kps, Kis, Kds) #with trasfer function
		analysor = Analysis(model()[1], Kps, Kis, Kds) #with Space State
		ampOp()

	def model(self):
		 return (modeler.modeTransferFunction(), modeSpaceState())
		
	def analise(self):
		analysor.analyse()

	def ampOp(self):
		model.toAmpOp()

m=main()