import numpy as np
import pandas as pd
import sklearn
import pickle
import cv2


def trainning_history(filepath):
	
	with open(filepath, 'rb') as f:
	    history = pickle.load(f)

	return history


#def f1report(filepath):
	
#	with open(filepath, 'rb') as f:
#	    report = pickle.load(f)

#	f1head = [x for x in (report.split('\n\n')[0].split(' ')) if x.isalpha()]
#	f1head.insert(0, ' ')


#	f1body = report.split('\n\n')[1].spit('\n')  # list
#	f1foot = report.split('\n\n')[2
#	].spit('\n')


#	return history

#print(trainning_history('../static/history/trainHistoryDict.txt'))