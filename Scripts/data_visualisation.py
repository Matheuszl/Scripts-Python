import numpy as np
import matplotlib.pyplot as plt 

n1 = np.array([0,20,30,40]) 

n = np.linspace(-0.75,1., 50)

fig, axes = plt.subplots(1,2, figsize=(10,3))

axes[0].scatter(n, n+0.25*np.random.randn(len(n)))
axes[1].step(n1, n1**2, lw=2)