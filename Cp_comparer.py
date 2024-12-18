import numpy as np
import matplotlib.pyplot as plt

#alpha	CL	CM
data_xfoil = np.loadtxt("1412.csv",
                 delimiter=";", dtype=float)

AoA_xfoil = data_xfoil[:,0]
Cl_xfoil = data_xfoil[:,1]
Cm_xfoil = data_xfoil[:,2]

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

plt.plot(x_list[1:int(len(x_list)/2)], (-cp_avg+Cp_lower)[1:])
plt.show()