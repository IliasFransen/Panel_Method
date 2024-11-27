import numpy as np

def vel_vect (x14: list, z14: list, x34: list, z34: list):
    u = np.zeros((len(x14), len(x14)))
    w = np.zeros((len(x14), len(x14)))
    for i in range(len(x34)):
        for j in range(len(x14)):
            u[i,j] = 1/(2*np.pi)*(x34[i]-x14[j])/((x34[i]-x14[j])**2+(z34[i]-z14[j])**2)
            w[i,j] = -1/(2*np.pi)*(z34[i]-z14[j])/((x34[i]-x14[j])**2+(z34[i]-z14[j])**2)

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
