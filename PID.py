from scipy import *
from numpy import *
from control import *

class PID(object):
	"""docstring for PID"""
	def __init__(self, arg):
		super(PID, self).__init__()
		self.arg = arg
		