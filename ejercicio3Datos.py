# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:36:51 2023

@author: brian
"""

from numpy import *

MB = zeros((8,5))
MA = zeros((8,8))

i=1
for x in range(len(MA)):
    for y in range(len(MA)):
        
        MA[x,y]=i
        i+=1 
        
MA=MA.T
print(MA)

for x in range(len(MA)):
  for y in range(len(MA)):
    for z in range(len(str(MA[x,y]))):
      if str(MA[x,y])[z] == '3':
        MA[x,y] = -99 

print("A = \n", MA)

i=0.4
for x in range(MB.shape[0]):
  for y in range(MB.shape[1]):
    MB[x,y] = i
    i += 0.01
print("B = \n" , MB)

MC = hstack((MA, MB))
print("C = \n" , MC)
print(MC.shape)

prome = zeros((13))
for x in range(MC.shape[1]):
  prome[x] = mean(MC[:,x])
print(prome)
MD = insert(MC, [8], prome, axis=0)
print(MD)
print(MD.shape)

maxi = zeros((9))
for x in range(MD.shape[0]):
  maxi[x] = max(MD[x,:])
  
print(maxi)
print(maxi.shape)

MR = insert(MD.T, [13], maxi, axis=0).T
print(MR)
print(MR.shape)
savetxt('resulatdo_matrices.txt', MR)