from scipy import *
from numpy import *
from control import *
import AmpOp
import Analysis

# class to engage Modeling, analise and AMP OP modules

class main(object):
	"""docstring for main"""
	def __init__(self, arg):
		super(main, self).__init__()
		self.arg = arg
		