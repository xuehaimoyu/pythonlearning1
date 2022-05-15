print("CREATED BY ZSR VERSION 1")
import time
import tkinter as tk 
import random 
import threading  
scale =10
print("--------ASTEROID SIMULATION CALCULATER -----------")
for i in range(scale+1):
    a,b = '**' * i,'..' * (scale - i)
    c = (i/scale)*100
    print("%{:^3.0f}[{}-{}]" .format (c,a,b))
    time.sleep(0.2)
print("--------------Loading successfully-----------------")
print(' ')
print(' ')
print("--------PYTHON3.9 LOADING -----------")
for i in range(scale+1):
    a,b = '**' * i,'..' * (scale - i)
    c = (i/scale)*100
    print("%{:^3.0f}[{}-{}]" .format (c,a,b))
    time.sleep(0.1)
print("--------------Loading successfully-----------------")
print()
print()
print()
print()
import math
import numpy as np
import sympy as sp
class MV():
    def __init__(self,R,h,v):#R distance away from center,h height of a deep-water wave ,v 
        self.R=R
        self.h=h
        self.v=v
    def Energy(self):
        y = sp.Symbol('y')
        equ1 = 22.7*(y/10)**0.54*1000/self.R-self.h
        solution = sp.solve(equ1,y)
        item=solution[0]
        b=item*10**12*420*10**4
        return b,item
    def Msolve(self):#v km*s-1
        b,item=self.Energy()
        m=2*b/(self.v*10**3)**2
        return m
    def earthquake(self):
        b,item=self.Energy()
        item=item*10**6
        Y=3.9+0.7*math.log10(item)
        print("Richard Magnitude",Y)
class Msun():
    def __init__(self,R,v,c=6*10**(-8),H=7254,r=100*10**3,p=1.2256):
        self.R=R
        self.v=v*10**3
        self.c=c
        self.H=H
        self.r=r
        self.p=p
    def mt(self,t):
        A=np.pi*self.R**2
        v=self.v
        t=self.t
        m=-1/2*A*self.c*self.H*self.p*v**2*np.exp(-(self.r-v*t)/self.H)
        return m
    def Ms(self):
        A=np.pi*self.R**2
        v=self.v
        t1=104*10**3/v
        m1=1/2*A*self.c*self.H**2*self.p*v*np.exp(-(self.r-v*t1)/self.H)
        t2=0
        m2=1/2*A*self.c*self.H**2*self.p*v*np.exp(-(self.r-v*t2)/self.H)
        M=m1-m2
        return M
class Mtotal():
    def __init__(self,R,h,v,p):
        self.R=R
        self.h=h
        self.v=v
        self.p=p
    def mtotal(self):
        test=MV(self.R,self.h,self.v)
        M=test.Msolve()
        R1=(M/self.p/np.pi*3/4)**(1/3)
        test=Msun(R1,self.v)
        a=test.Ms()
        Mt=M+a
        return Mt
    def sun(self):
        test=Msun(R1,self.v)
        a=test.Ms()
        rate=a/self.mtotal()
        return rate
    def me(self):
        test=MV(self.R,self.h,self.v)
        test.earthquake()
    def mR(self):
        test=MV(self.R,self.h,self.v)
        M=test.Msolve()
        R1=(M/self.p/np.pi*3/4)**(1/3)
        return R1
R=eval(input("impact distance from coast:"))
h=eval(input("Tsunami heights:"))
h=h/40
v=eval(input("impact velocity:"))
s=eval(input("type:iron 1;iron-stone 2;stone 3;comet 4  :"))
if s==1:
    p=7860
if s==2:
    p=5500
if s==3:
    p=3500
if s==4:
    p=1000
test=MV(R,h,v)
M=test.Msolve()
R1=(M/p/np.pi*3/4)**(1/3)
x1=Mtotal(R,h,v,p)
print("MASS IN SPACE=",x1.mtotal(),"DAMAGE RATE=",x1.sun(),'D=',x1.mR()*2)
test.earthquake()
print()
print()
print()
print()
input("PRESS ENTER TO EXIT")
