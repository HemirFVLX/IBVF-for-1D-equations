# Rezolvarea numerica a problemei mixte pentru ecuatia caldurii 1D prin metoda retelelor
import math as m
import numpy as np
import matplotlib.pyplot as ppl

def f(x, t): # neomogenitatea
    return 0

def g(x): # pozitia initiala
    return (x-1)**2

def phi(t): # conditia la frontiera, capatul x=0
    return 1

def psi(t): # conditia la frontiera, capatul x=lung_max
    return 4

def solution(u, l ,c, k_x, k_t):
    k = k_t/k_x**2
    for j in range(c):
        u[0,j] = g(k_x*j) 
    for i in range(1,l):
        u[i,0] = phi(k_t*i)
        u[i,c-1] = psi(k_t*i)
    for i in range(l-1):
        for j in range(1,c-1): 
            u[i+1,j] = k*(u[i,j+1] + u[i,j-1]) + (1-2*k)*u[i,j] + k_t * f(k*j,k*i)
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
    

k_x = float(input("Pasul pe x: "));
k_t = float(input("Pasul pe t: "));
length = float(input("Lungimea coardei: "));
t_max = float(input("Timpul maxim: "));

k = k_t/k_x**2

l = int(t_max/k_t) + 1
c = int(length/k_x) + 1

u = np.zeros((l,c))

print(k)
if k <= 0.5:
    v = solution(u, l ,c, k_x, k_t)
    disp_sol(v, length, t_max, l, c)
else:
    print("Nu exista convergenta si stabilitate pentru datele introduse")