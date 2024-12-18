import numpy as np
import matplotlib.pyplot as plt

from Discretizer import z, angle_norm, Point14, Point34, norm
from Vort2D import vel_vect, Q_inf, RHS, Coeff, ClCm, Dcp

#Conditions

AoA = np.arange(np.radians(-2), np.radians(8), np.radians(0.5))
#AoA = [0]

V_inf = 1

c = 1

#NACA 4 digit airfoil

NACA1 = 1

NACA2 = 4

N_pts = 150


x = np.linspace(0,1,N_pts)

def calc (NACA1: int, NACA2: int, N_pts: int, c, AoA: float, V_inf: float):
    z_pt = z(x, NACA1, NACA2)
    angle_normal = angle_norm(x, z_pt)
    x14, z14 = Point14(x, z_pt)
    x34, z34 = Point34(x, z_pt)
    normal = norm(angle_normal)
    u, w = vel_vect(x14, z14, x34, z34)
    Q_infty = Q_inf(AoA, V_inf)
    rhs = RHS(normal, Q_infty)
    a_ij = Coeff(u, w, normal)
    Gamma = np.linalg.solve(a_ij, rhs)
    Cl, Cm = ClCm(Gamma, V_inf, c, x14)
    dCp = Dcp(Gamma, V_inf, x, z_pt)
    return Cl, Cm, dCp

def main (NACA1: int, NACA2: int, N_pts: int, c, AoA: list, V_inf: float):
    Cl = np.zeros(len(AoA))
    Cm = np.zeros(len(AoA))
    Dcp = np.zeros((len(AoA), N_pts-1))
    Gamma = np.zeros((len(AoA), N_pts-1))
    
    for i in range(len(AoA)):
        Cl[i], Cm[i], Dcp[i], = calc(NACA1, NACA2, N_pts, c, AoA[i], V_inf)
        if AoA[i] == 0:
            Dcp[i].tofile('Dcp_thin.csv', sep = ';')

    Cl.tofile('Cl_thin.csv', sep = ';')
    Cm.tofile('Cm_thin.csv', sep = ';')

if __name__ == "__main__":
    main(NACA1, NACA2, N_pts, c, AoA, V_inf)
