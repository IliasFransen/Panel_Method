import numpy as np

def z (x: list, m: int, p: int):
    z = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < p:
            z[i] = m/(p**2)*(2*p*x[i] - x[i]**2)
        else:
            z[i] = m/((1-p)**2)*(1-2*p + 2*p*x[i] - x[i]**2)
    return z

def angle_norm (x: list, z: list):
    angle = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        angle[i] = np.arctan2(z[i+1]-z[i],x[i+1]-x[i])+np.pi/2
    return angle

def Point14 (x: list, z: list):
    x_14 = np.zeros(len(x)-1)
    z_14 = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        x_14[i] = x[i] + 0.25*(x[i+1]-x[i])
        z_14[i] = z[i] + 0.25*(z[i+1]-z[i])
    return x_14, z_14

def Point34 (x: list, z: list):
    x_34 = np.zeros(len(x)-1)
    z_34 = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        x_34[i] = x[i] + 0.75*(x[i+1]-x[i])
        z_34[i] = z[i] + 0.75*(z[i+1]-z[i])
    return x_34, z_34

def norm (angle: list):
    norm = np.zeros((len(angle),2))
    for i in range(len(angle)):
        norm[i,0] = np.cos(angle[i])
        norm[i,1] = np.sin(angle[i])
    return norm