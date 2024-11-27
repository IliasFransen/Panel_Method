import numpy as np

from Discretizer import z, angle_norm, Point14, Point34, norm
from Vort2D import vel_vect, Q_inf, RHS, Coeff

#Conditions

AoA = 0

V_inf = 1

#NACA 4 digit airfoil

m = 2

p = 4

N_pts = 10

x = np.linspace(0,1,N_pts)

def main (m: int, p: int, N_pts: int):
    z = z(x, m, p)
    angle_norm = angle_norm(x, z)
    x14, z14 = Point14(x, z)
    x34, z34 = Point34(x, z)
    norm = norm(angle_norm)
    u, w = vel_vect(x14, z14, x34, z34)
    Q_inf = Q_inf(AoA, V_inf)
    RHS = RHS(norm, Q_inf)
    Coeff = Coeff(u, w, norm)
    Gamma = np.linalg.solve(Coeff, RHS)
