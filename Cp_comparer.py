import numpy as np
import matplotlib.pyplot as plt

pres=False
Lift = True

# X Y Cp
data_xfoil_CP = np.loadtxt("cp_xfoi.csv",
                 delimiter=";", dtype=float)
x_list = data_xfoil_CP[:,0]
y_list = data_xfoil_CP[:,1]
Cp_list = data_xfoil_CP[:,2]

Cp_upper = Cp_list[:int(len(Cp_list)/2)+1]
Cp_lower = np.flip(Cp_list[int(len(Cp_list)/2):])

cp_avg = np.zeros(len(Cp_upper)-1)
for i in range(len(cp_avg)):
    cp_avg[i] = (Cp_upper[i]+Cp_upper[i+1])/2

dcp_thin = np.loadtxt("Dcp_thin.csv",
                    delimiter=";", dtype=float)

N_pts = 150
x = np.linspace(0,1,N_pts)

if pres:
    plt.plot(x[:-1], dcp_thin, label = "Thin airfoil")
    plt.plot(x_list[:len(x_list)//2], (-cp_avg+Cp_lower)[:], label = "XFoil")
    plt.xlabel(r'$x/c$ [-]')
    plt.ylabel(r'$\Delta C_p$ [-]')
    plt.legend()
    plt.show()

#########################################################################

#alpha	CL	CM
data_xfoil = np.loadtxt("1412.csv",
                 delimiter=";", dtype=float)
AoA_xfoil = data_xfoil[:,0]
Cl_xfoil = data_xfoil[:,1]
Cm_xfoil = data_xfoil[:,2]

AoA = np.degrees(np.arange(np.radians(-2), np.radians(8), np.radians(0.5)))

Cl = np.fromfile('Cl_thin.csv', sep = ';')
Cm = np.fromfile('Cm_thin.csv', sep = ';')

cl_a_real = np.loadtxt('Cl_a_test.csv', delimiter=";", dtype=float)
cm_a_real = np.loadtxt('cm_a_test.csv', delimiter=",", dtype=float)     #scaling is wrong

cl_test = cl_a_real[:,1]
cm_test = cm_a_real[:,1]
AoA_test_cl = cl_a_real[:,0]
AoA_test_cm = cm_a_real[:,0]

if Lift:
    plt.plot(AoA, Cl, label = "Cl Thin airfoil", linewidth = 2)
    plt.plot(AoA_xfoil, Cl_xfoil, label = "Cl XFoil", linewidth = 2)
    plt.plot(AoA_test_cl, cl_test, label = "Cl Test", linewidth = 2)
    plt.plot(AoA_test_cm, cm_test, label = "Cm Test", linewidth = 2)
    plt.plot(AoA, Cm, label = "Cm Thin airfoil", linewidth = 2)
    plt.plot(AoA_xfoil, Cm_xfoil, label = "Cm XFoil", linewidth = 2, color = 'Gold')
    plt.xlabel(r'$\alpha$ [deg]')
    plt.ylabel(r'$C_l$ and $C_m$ [-]')
    plt.legend()
    plt.show()

