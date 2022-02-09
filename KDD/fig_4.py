"""Reproduction of "Change of optimal lambda values"."""
# Samples are exported from the corresponding Weights and Biases run.
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('KDD/data/lambda.csv', delimiter=';', skip_header=1, names=['x', 'model_1', 'model_2'])


plt.plot(data['x'], 1 - data['model_1'], color="#1A85FF", lw=0.8)
plt.plot(data['x'], 1 - data['model_2'], color="#D41159", lw=0.8)
plt.xlabel('Epoch', fontsize=7)
plt.ylabel('$\lambda$', fontsize=7)  # pylint: disable=W1401
fig_width, fig_height = plt.gcf().get_size_inches()
print(fig_width, fig_height)
plt.gcf().set_size_inches(3.5, 2)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
# plt.show()
plt.savefig('KDD/Figure_4_lambda.pgf', dpi=400, bbox_inches='tight', pad_inches=0.0001)
