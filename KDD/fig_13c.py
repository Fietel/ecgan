"""Plot distribution with beta=0."""
# pylint: skip-file
import matplotlib as mpl
import matplotlib.pyplot as plt
import torch

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
mpl.use("pgf")

plt.style.use('seaborn-colorblind')

latents = load_pickle('KDD/data/latent_data_500_beta_dot0.pkl')['latent_train']
title = 'KDD/chi_beta_dot0.pgf'

latent_norm_normal = torch.norm(latents.squeeze(), dim=1).cpu().numpy()
print(latents.shape)

plt.hist(latent_norm_normal, 50, density=True, alpha=0.75, label=r'$\mathfrak{L}$', color="#1A85FF")  # color='C5'
plt.legend(fontsize=10)
plt.gcf().set_size_inches(3.5, 2)
plt.tight_layout()
# plt.show()
plt.savefig(title)
