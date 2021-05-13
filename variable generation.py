import random
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# generating exponential random variables

def inv_exp(u, lmda):
    return -(1/lmda)*math.log(1 - u)

exp_sim = []

for i in range(100000):
    num = random.random()
    exp_sim.append(inv_exp(num, 0.5))

exp_med = np.random.exponential(2, 100000) # 2 = 1 / lambda

plt.hist(exp_sim, 40, alpha=0.5, label='simulated')
plt.hist(exp_med, 40, alpha=0.5, label='exp method')
plt.legend(loc='upper right')
plt.show()

