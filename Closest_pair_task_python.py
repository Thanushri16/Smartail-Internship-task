# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:11:50 2020

@author: HP
"""

import numpy
import math
import copy 

def stripdistance(strip, size, d):  
    min_val = d  
    #find distance within points in the strip based on their y-coordinates   
    for i in range(size): 
        j = i + 1
        while j < size and (strip[j].y - 
                            strip[i].y) < min_val: 
            min_val = dist(strip[i], strip[j]) 
            j += 1
  
    return min_val  

def dist(p1, p2): 
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * 
                     (p1.y - p2.y))

def pairandstrip(P, Q, n): 
    # Find the middle point  
    mid = n // 2
    midPoint = P[mid] 
  
    # Consider the vertical line passing  
    # through the middle point calculate  
    # the smallest distance dl on left  
    # of middle point and dr on right side  
    dl = pairandstrip(P[:mid], Q, mid) 
    dr = pairandstrip(P[mid:], Q, n - mid)  
  
    # Find the smaller of two distances  
    d = min(dl, dr) 
  
    # Build an array strip[] that contains  
    # points close (closer than d)  
    # to the line passing through the middle point  
    strip = []  
    for i in range(n):  
        if abs(Q[i].x - midPoint.x) < d:  
            strip.append(Q[i]) 
  
    # Find the closest points in strip.  
    # Return the minimum of d and closest  
    # distance is strip[]  
    return min(d, stripdistance(strip, len(strip), d)) 
  
def ptx(point):
    return point.x

def pty(point):
    return point.y
# The main function that finds 
# the smallest distance.  
# This method mainly uses closestUtil() 
def smallest_distance(P, n): 
    Q = copy.deepcopy(P)
    P.sort(key = ptx).all() #lambda point: point.x
    Q.sort(key = pty).all()  #lambda point: point.y  
    return pairandstrip(P, Q, n) #used to find distance b/w pairs and within a strip
  
class Point(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 


x=numpy.random.normal(5.0, 5.0, 10)
y=numpy.random.normal(10.0, 2.0, 10)
P=[]
for i in x:
    for j in y:
        P.append(Point(x,y))
n = len(P)
#print(P)
print(n)
print("The smallest distance within a pair is",  smallest_distance(P, n)) 