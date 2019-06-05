#!/usr/bin/python3.6
def iMFF(fileName):
	fileContents=[]
	with open(fileName) as f:
		for line in f:
			fileContents.append(line.split(","))
			fileContents[-1][-1]=fileContents[-1][-1].strip()
	print("fileContents:",fileContents)
	return fileContents