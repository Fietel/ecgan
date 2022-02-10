"""Plot distribution with high beta."""
# pylint: skip-file
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy
import torch
from scipy.stats import kstest

from ecgan.utils.miscellaneous import load_pickle

mpl.rcParams["mathtext.fontset"] = "stix"

mpl.rc('text.latex', preamble=r'\usepackage{amssymb}')
mpl.rcParams.update(
    {
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
        # Use LaTeX default serif font.
        'text.usetex': True,
        'pgf.rcfonts': False,
        "pgf.preamble": r"\usepackage{amssymb}",  # load additional packages
        #'mathtext.fallback_to_cm': True
    }
)
plt.style.use('seaborn-colorblind')
mpl.use("pgf")


beta = 0.0001
if beta == 0.0001:
    latents = load_pickle('KDD/data/latent_data_500_beta_dot0001.pkl')['latent_train']
elif beta == 0.1:
    latents = load_pickle('KDD/data/latent_data_250_beta_dot1.pkl')['latent']
else:
    print("wrong beta", beta)
    exit()

latent_norm_normal = torch.norm(latents.squeeze(), dim=1).cpu().numpy()

dist_name = 'chi'

dist = getattr(scipy.stats, dist_name)
params = dist.fit(latent_norm_normal)
arg = params[:-2]
loc = params[-2]
scale = params[-1]

test_result = kstest(latent_norm_normal, dist_name, args=params)
x = np.linspace(
    getattr(scipy.stats, dist_name).ppf(0.0001, arg), getattr(scipy.stats, dist_name).ppf(0.99999, arg), 100
)
dist_plot = getattr(scipy.stats, dist_name)(arg, loc, scale).pdf(x)
plt.plot(x, dist_plot, label='$\mathsf{\chi}$', color="#D41159")  # {5.548}}$')  color='C2'
plt.hist(latent_norm_normal, 50, density=True, alpha=0.75, label=r'$\mathfrak{L}$', color="#1A85FF")  # color='C5'
plt.legend(fontsize=10)
plt.gcf().set_size_inches(3.5, 2)
plt.tight_layout()
# plt.show()
beta_string = 'dot1' if beta == 0.1 else 'dot0001'
plt.savefig('KDD/chi_beta_{}.pgf'.format(beta_string))
print("plotted beta ", beta_string)
