import numpy as np
import matplotlib.pyplot as plt

N_panels = np.array([2,5, 10, 25, 50, 100, 200, 400, 800, 1600])
dclda = np.array([6.266613515852391 , 6.2621236480010705 , 6.2614524280617125, 6.261126725689065, 6.261028078576645, 6.260980409940108, 6.2609569717634965, 6.260945349600414, 6.26093956248992, 6.26093956248992])
two_pi = 2*np.pi*np.ones(len(N_panels))

plt.scatter(N_panels, dclda, label = 'Simulation', s=10, color = 'red')
plt.plot(N_panels, two_pi, label = 'Theoretical Value')
#plt.xscale('log')
plt.xlabel('Number of Panels')
plt.ylabel('Value')
plt.title('Convergence of dCldAlpha')
plt.legend()
plt.show()