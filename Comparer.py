import numpy as np
import matplotlib.pyplot as plt

AoA_thin = np.linspace(np.radians(-2), np.radians(8), 25)


Cl_thin = np.array([-0.10649362, -0.06079584 ,-0.01509485,  0.03060694,  0.07630711 , 0.12200325,
                    0.16769293 , 0.21337374  ,0.25904328 , 0.30469911 , 0.35033882  ,0.39596001,
                    0.44156026 , 0.48713716  ,0.5326883  , 0.57821126 , 0.62370365  ,0.66916305,
                    0.71458706 , 0.75997329  ,0.80531932 , 0.85062276 , 0.89588122  ,0.9410923,
                    0.98625361])

Cm_thin = np.array([ 5.09574746e-06, -1.14226445e-02, -2.28497806e-02, -3.42757083e-02,
                    -4.56998234e-02, -5.71215216e-02, -6.85401990e-02, -7.99552516e-02,
                    -9.13660759e-02, -1.02772068e-01, -1.14172626e-01, -1.25567145e-01,
                    -1.36955024e-01, -1.48335659e-01, -1.59708451e-01, -1.71072796e-01,
                    -1.82428094e-01, -1.93773744e-01, -2.05109146e-01, -2.16433702e-01,
                    -2.27746811e-01, -2.39047876e-01, -2.50336299e-01, -2.61611484e-01,
                    -2.72872832e-01])

#alpha	CL	CM
data_xfoil = np.loadtxt("1412.csv",
                 delimiter=";", dtype=float)

AoA_xfoil = data_xfoil[:,0]
Cl_xfoil = data_xfoil[:,1]
Cm_xfoil = data_xfoil[:,2]

# X Y Cp
data_xfoil_CP = np.loadtxt("cp_xfoi.csv",
                 delimiter=";", dtype=float)



plt.plot(np.degrees(AoA_thin), Cl_thin, label = 'Cl Thin Airfoil Theory')
plt.plot(AoA_xfoil, Cl_xfoil, label = 'Cl Xfoil')
plt.plot(np.degrees(AoA_thin), Cm_thin, label = 'Cm Thin Airfoil Theory')
plt.plot(AoA_xfoil, Cm_xfoil, label = 'Cm Xfoil')
plt.legend()
plt.xlabel('Angle of Attack [degr]')
plt.ylabel('Coefficient')
plt.show()

