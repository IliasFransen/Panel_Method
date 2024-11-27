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
    z_pt = z(x, m, p)
    angle_normal = angle_norm(x, z_pt)
    x14, z14 = Point14(x, z_pt)
    x34, z34 = Point34(x, z_pt)
    normal = norm(angle_normal)
    u, w = vel_vect(x14, z14, x34, z34)
    Q_infty = Q_inf(AoA, V_inf)
    rhs = RHS(normal, Q_infty)
    a_ij = Coeff(u, w, normal)
    Gamma = np.linalg.solve(a_ij, rhs)
    print(Gamma)

if __name__ == "__main__":
    main(m, p, N_pts)
