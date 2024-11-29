import numpy as np
import matplotlib.pyplot as plt

def z (x: list, m: int, p: int):
    z = np.zeros(len(x))
    m = 0.01*m
    p = 0.1*p
    for i in range(len(x)):
        if x[i] < p:
            z[i] = m/(p**2)*(2*p*x[i] - x[i]**2)
        else:
            z[i] = m/((1-p)**2)*(1-2*p + 2*p*x[i] - x[i]**2)
    return z

#x = np.linspace(0,1,20)

#plt.plot(x,z(x, 2, 4) )
#plt.gca().set_aspect('equal', adjustable='box')
#plt.show()


def angle_norm (x: list, z: list):
    angle = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        angle[i] = np.arctan2(z[i+1]-z[i],x[i+1]-x[i])+np.pi/2
    return angle

#x = np.linspace(0,1,20)

#plt.plot(x[:-1],np.degrees(angle_norm(x, z(x, 2, 4))) )
#plt.plot
#plt.show()

def Point14 (x: list, z: list):
    x_14 = np.zeros(len(x)-1)
    z_14 = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        x_14[i] = x[i] + 0.25*(x[i+1]-x[i])
        z_14[i] = z[i] + 0.25*(z[i+1]-z[i])
    return x_14, z_14

#print(Point14([0,1], z([0,1], 2, 4))[1])

def Point34 (x: list, z: list):
    x_34 = np.zeros(len(x)-1)
    z_34 = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        x_34[i] = x[i] + 0.75*(x[i+1]-x[i])
        z_34[i] = z[i] + 0.75*(z[i+1]-z[i])
    return x_34, z_34

#print(Point34([0,1], z([0,1], 2, 4))[0])

def norm (angle: list):
    norm = np.zeros((len(angle),2))
    for i in range(len(angle)):
        norm[i,0] = np.cos(angle[i])
        norm[i,1] = np.sin(angle[i])
    return norm

#x = np.linspace(0,1,20)

#plt.plot(x[:-1],(norm(angle_norm(x, z(x, 0,0)))[:,1]) )
#plt.plot
#plt.show()