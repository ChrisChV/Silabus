import numpy as np
from mf import MF
import re
""" Data De prueba
matrix=[]
for i in range(500):  #943
	matrix.append([0]*1682)
file=open("u.data","r")
contador=0
for z in file:
	if(contador==500): 
		break
	w=re.split(r'\t+', z)
	if(int(w[0])==1):
		print(w)
	matrix[int(w[0])-1][int(w[1])-1]=int(w[2])
	contador+=1
"""  
matrix=[]
for i in range(51):  #943
	matrix.append([0]*7)
file=open("silabuz.txt","r")
for z in file:
	w=z.split(',')
	matrix[int(w[0])][int(w[1])]=int(w[2])
print(matrix)

#print(matrix[285])
#print("-----------------------------")
#print("here-> ",1./2)
# A rating matrix with ratings from 5 users on 4 items
# zero entries are unknown values
"""
R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])
"""
R = np.array(matrix)
# Perform training and obtain the user and item matrices 
mf = MF(R, K=2, alpha=0.1, beta=0.01, iterations=20)
training_process = mf.train()
print("proceso de entrenamiento:", training_process)
print(mf.P)
print(mf.Q)
print("=================")
#print(mf[0])
print(mf.full_matrix())