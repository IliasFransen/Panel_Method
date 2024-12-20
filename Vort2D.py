import numpy as np
import matplotlib.pyplot as plt

def vel_vect (x14: list, z14: list, x34: list, z34: list):
    u = np.zeros((len(x14), len(x14)))
    w = np.zeros((len(x14), len(x14)))
    for i in range(len(x34)):
        for j in range(len(x14)):
            u[i,j] = 1/(2*np.pi)*(z34[i]-z14[j])/((x34[i]-x14[j])**2+(z34[i]-z14[j])**2)
            w[i,j] = -1/(2*np.pi)*(x34[i]-x14[j])/((x34[i]-x14[j])**2+(z34[i]-z14[j])**2)

    return u, w

def Q_inf (AoA: float, V_inf: float):
    Q_inf = np.zeros(2)
    Q_inf[0] = V_inf*np.cos(AoA)
    Q_inf[1] = V_inf*np.sin(AoA)
    return Q_inf

def RHS (norm: list, Q_inf: list):
    RHS = np.zeros((len(norm)))
    for i in range(len(norm)):
        RHS[i] = -np.dot(Q_inf, norm[i])
    return RHS

def Coeff (u: list, w: list, norm: list):
    Coeff = np.zeros((len(u), len(u)))
    for i in range(len(norm)):
        for j in range(len(u)):
            Coeff[i,j] = np.dot([u[i,j],w[i,j]], norm[i])
    return Coeff

def ClCm (gamma: list, V_inf: float, c: float, x14: list):
    Gamma = np.sum(gamma)
    cl = 2*Gamma /(V_inf *c)
    cm = 2/(V_inf*c**2) * -np.sum(np.dot(gamma, x14)) 
    return cl, cm

def Dcp (gamma: list, V_inf: float, x: list, z: list):
    Dcp = np.zeros((len(x)-1))
    for i in range(len(x)-1):
        a = np.sqrt((x[i+1]-x[i])**2+(z[i+1]-z[i])**2)
        Dcp[i] = 2*gamma[i]/(V_inf*a)
    return Dcp

