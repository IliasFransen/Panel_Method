import numpy as np

from Discretizer import z, angle_norm, Point14, Point34, norm
from Vort2D import vel_vect, Q_inf, RHS, Coeff

#Conditions

AoA = 0

V_inf = 1

#NACA 4 digit airfoil

NACA1 = 0

NACA2 = 0

N_pts = 4

x = np.linspace(0,1,N_pts)

def main (NACA1: int, NACA2: int, N_pts: int):
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
    #print(w)
    Q_infty = Q_inf(AoA, V_inf)
    rhs = RHS(normal, Q_infty)
    a_ij = Coeff(u, w, normal)
    Gamma = np.linalg.solve(a_ij, rhs)
    #print(Gamma)

if __name__ == "__main__":
    main(NACA1, NACA2, N_pts)
