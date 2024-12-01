import numpy as np
import matplotlib.pyplot as plt

from Discretizer import z, angle_norm, Point14, Point34, norm
from Vort2D import vel_vect, Q_inf, RHS, Coeff, ClCm

#Conditions

AoA = np.linspace(np.radians(-2), np.radians(8), 30)

V_inf = 1

c = 1

#NACA 4 digit airfoil

NACA1 = 2

NACA2 = 4

N_pts = 150


x = np.linspace(0,1,N_pts)

def calc (NACA1: int, NACA2: int, N_pts: int, c, AoA: float, V_inf: float):
    z_pt = z(x, NACA1, NACA2)
    #print(z_pt)
    angle_normal = angle_norm(x, z_pt)
    #print(np.degrees(angle_normal))
    x14, z14 = Point14(x, z_pt)
    x34, z34 = Point34(x, z_pt)
    #print(x14)
    #print(z14)
    #print(x34)
    #print(z34)
    normal = norm(angle_normal)
    #print(normal)
    u, w = vel_vect(x14, z14, x34, z34)
    #print(u)
    Q_infty = Q_inf(AoA, V_inf)
    #print(Q_infty)
    rhs = RHS(normal, Q_infty)
    #print(rhs)
    a_ij = Coeff(u, w, normal)
    #print(a_ij)
    Gamma = np.linalg.solve(a_ij, rhs)
    #print(Gamma)
    Cl, Cm = ClCm(Gamma, V_inf, c, x14)
    return Cl, Cm

def main (NACA1: int, NACA2: int, N_pts: int, c, AoA: list, V_inf: float):
    Cl = np.zeros(len(AoA))
    Cm = np.zeros(len(AoA))
    
    for i in range(len(AoA)):
        Cl[i] = calc(NACA1, NACA2, N_pts, c, AoA[i], V_inf)[0]
        Cm[i] = calc(NACA1, NACA2, N_pts, c, AoA[i], V_inf)[1]
    
    plt.plot(np.degrees(AoA), Cl)
    plt.plot(np.degrees(AoA), Cm)
    plt.xlabel('Angle of Attack [deg]')
    plt.ylabel('Cl')
    plt.show()


if __name__ == "__main__":
    main(NACA1, NACA2, N_pts, c, AoA, V_inf)
