"""Reproduction of "Randomly selected reconstructed samples on the Wafer dataset using the BeatGAN model"."""
# Samples are randomly selected from test set.
# The .pkl contains a nested list of [real_samples, fake_samples].
import pickle

import matplotlib.pyplot as plt
import numpy as np
import torch

with open("KDD/data/random_samples_beatgan_wafer.pkl", "rb") as f:
    samples = pickle.load(f)

print(len(samples), torch.min(samples[0]), torch.max(samples[0]))
print(len(samples), torch.min(samples[1]), torch.max(samples[1]))

real_samples = np.array(samples[0])
fake_samples = np.array(samples[1])

fig, axes = plt.subplots(2, 4, sharex=True, figsize=(15, 5))
data_lined = real_samples[0]
data_dashed = fake_samples[0]
COLOR_LINED = "#1A85FF"
COLOR_DASHED = "#D41159"

len_ = len(data_lined) if len(data_lined) > len(data_dashed) else len(data_dashed)
x_axis = np.arange(len_)

real_samples = np.array(samples[0])
fake_samples = np.array(samples[1])
for i in range(2):
    for j in range(4):
        ax = axes[i // 1][j]
        data_lined = real_samples[4 * i + j]
        data_dashed = fake_samples[4 * i + j]
        ax.plot(x_axis, data_lined, color=COLOR_LINED)
        ax.plot(x_axis, data_dashed, color=COLOR_DASHED, linestyle=(0, (1, 0.5)))
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

plt.tight_layout()
# plt.show()
plt.savefig('KDD/Figure_11.pgf')
# plt.savefig('KDD/wafer_grid.png', dpi=500)
