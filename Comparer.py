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

Lengths = np.zeros(len(x_list)-1)
cp_avg = np.zeros(len(x_list)-1)

for i in range(len(x_list)-1):
    Lengths[i] = np.sqrt((x_list[i+1]-x_list[i])**2+(y_list[i+1]-y_list[i])**2)
    cp_avg[i] = (Cp_list[i]+Cp_list[i+1])/2


#split in upper and lower part
Lengths_upper = Lengths[: len(Lengths)//2+1]
Lengths_lower = Lengths[len(Lengths)//2:]
cp_avg_upper = cp_avg[: len(cp_avg)//2+1]
cp_avg_lower = cp_avg[len(cp_avg)//2:]

D_cp = -cp_avg_upper + cp_avg_lower

plt.plot(x_list[:len(x_list)//2], D_cp)
plt.show()
