import csv
import os
import math
import pickle

def inOneJump(start,dest):
	"""
	Determine if it's available for capital ships to jump between two systems.
	Need systemInfo.pickle in directory: resources/
	@parameters: start system, destination system
	:return: The results of the calculations
	"""
	with open('resources/systemInfo.pickle','rb') as f:
		systemInfo=pickle.load(f)

	ssystem=dsystem=0
	# find coordinates for the two input systems
	systemNames=list(systemInfo.keys())
	for system in systemNames:
		if system.lower().startswith(start.lower()):
			ssystem=system
		elif system.lower().startswith(dest.lower()):
			dsystem=system
	if not ssystem or not dsystem:
		return '__At least one of the system names is NOT correct!__'
	x1, y1, z1= systemInfo[ssystem][1], systemInfo[ssystem][2], systemInfo[ssystem][3]
	x2, y2, z2= systemInfo[dsystem][1], systemInfo[dsystem][2], systemInfo[dsystem][3]
	# calculate the distance between two systems in light years
	distance = round(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2)),2)
	# s1 for Titans, Supercarriers, Carriers, Dreadnoughts, Rorquals
	# s2 for Black ops
	# s3 for Jumpfreighters
	if distance<=4.5:
		s1=s2=s3='JDC4, JDC5'
	elif distance>4.5 and distance<=5:
		s1='JDC5'
		s2=s3='JDC4, JDC5'
	elif distance>5 and distance<=7:
		s1='Negative'
		s2=s3='JDC4, JDC5'
	elif distance>7 and distance<=8:
		s1='Negative'
		s2='JDC5'
		s3='JDC4, JDC5'
	elif distance>8 and distance<=9:
		s1=s2='Negative'
		s3='JDC4, JDC5'
	elif distance>9 and distance<=10:
		s1=s2='Negative'
		s3='JDC5'
	elif distance>10:
		s1=s2=s3='Negative'

	result = """__**{0} -> {1}({2}ly)**__:

__Titans__: {3}
__Supercarriers__: {3}
__Carriers__: {3}
__Dreadnoughts__: {3}
__Rorquals__: {3}

__Black Ops__: {4}

__Jumpfreighters__: {5}
	""".format(ssystem,dsystem,distance,s1,s2,s3)
	return result
