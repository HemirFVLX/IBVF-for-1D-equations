# Rezolvarea numerica a problemei mixte cu conditii Dirichlet pentru ecuatia undelor 1D prin metoda retelelor
import math as m
import numpy as np
import matplotlib.pyplot as ppl

def f(x, t): # neomogenitatea
    return x-2

def g(x): # pozitia initiala
    return m.sin(x*m.pi/2)

def h(x): # viteza initiala
    return 0

def phi(t): # conditia la frontiera, capatul x=0
    return 0

def psi(t): # conditia la frontiera, capatul x=lung_max
    return 0

def solution(u, l ,c, k):
    for j in range(c):
        u[0,j] = g(k*j) 
    for i in range(1,l):
        u[i,0] = phi(k*i)
        u[i,c-1] = psi(k*i)
    for j in range(1,c-1):
        u[1,j] = k * h(k*j) + u[0,j]
    for i in range(1,l-1):
        for j in range(1,c-1): 
            u[i+1,j] = u[i,j+1] + u[i,j-1] - u[i-1,j] + k**2 * f(k*j,k*i)
    for i in range(l):
        for j in range(c):
            print(f"u[{j},{i}] = {u[i,j]}")
        print("\n")
    return u

def disp_sol(u, length, t_max, l, c):
    vec_x = np.linspace(0,length,c)
    vec_t = np.linspace(0,t_max,l)
    mx, mt = np.meshgrid(vec_x, vec_t)
    ppl.contourf(mx, mt, u, cmap='jet')
    ppl.colorbar()
    ppl.show()
    

k = float(input("Pasul pe x si t: "));
length = float(input("Lungimea coardei: "));
t_max = float(input("Timpul maxim: "));

l = int(t_max/k) + 1
c = int(length/k) + 1

u = np.zeros((l,c))

v = solution(u, l ,c, k)
disp_sol(v, length, t_max, l, c)
