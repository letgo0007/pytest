# -*- coding: utf-8 -*-

## list = variable , defined use []
## tuple = const   , defined use ()

## list examle 1
L = ["Apple","Google","Microsoft"]

print(L)
print(L[2])
print(L[2][2])

L.append("Sharp")   ## Add to list tail
print(L)

L.insert(2,"Sony")  ## Add to certain position
print(L)

L.pop()             ## Remove from list tail
print(L)

L.pop(0)            ## Remove from certain position
print(L)

## list examle 2 

M = list()          ## Build empty list
N = list(L)         ## Build list initialize from another list

print("M=",M)
print("N=",N)

M = N.copy()        ## Copy list
print("M=",M)
print("N=",N)

## tuple example 1

E = ('SUCCESS','FAIL','TBD','SUCCESS')
print(E)
print(E[1])
print(E[1][1])

print(E.count('SUCCESS'))   ## get how many number of a element exsit in tuple

print(len(E))           ## get size of a tuple

## tuple example 2
## namedtuple is a build in module og python

from collections import namedtuple

Point = namedtuple("Point",['x','y'])

P1 = Point(1920,1080)
P2 = Point(3840,2160)

print(P1)
print(P1.x)
print(P2)



