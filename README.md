# Notes for KDD review
This work was part of a larger framework for open source arrhythmia detection, information which may allow
identification is marked as REDACTED.
After installation (see sections below):

1. Reproduction of the experiments: the configuration files are in the configs/ folder. Make sure that you are inside
the virtual environment. First: preprocess the data using a training config from either the MITBIH or Wafer dataset to
   download and preprocess the data (e.g. `ecgan-preprocess configs/train/mitbih_beatgan.yml`).
   Afterwards you can start training (e.g. `ecgan-train configs/train/mitbih_beatgan.yml`) or anomaly detection.
   Note: All tracking was performed using weights and biases. Since we offer the original configuration files here, the
   `TRACKER_NAME` needs to be changed to `local` for local experiments!
   The trained models are stored at Weights and Biases. starting an anomaly detection config automatically downloads
   and loads the model (e.g. `ecgan-detect configs/anomaly_detection/mitbih/vaegan_plus/vaegan_fold_1_onlyrec.yml`, again:
   make sure to change the tracker). Detection as well as training required running the preprocessing for each dataset
   once before starting it.

2. Figures and required data can be found in the KDD directory. Figure 2 was created using draw.io and not automatically,
Figures 10 and 12 where directly taken from the Weights and Biases runs.

3. Additional notes: The original BeatGAN paper utilizes a sequence length of 320 (we use 160) and a different preprocessing,
including the removal of some classes. We use a more common and complete preprocessing in our experiments with a similar hidden
   "true" dimension (both datasets use single heartbeats, the centering and sampling differs). We have also performed
   experiments using the original beatgan dataset with the same results as reported in the paper. To utilize the beatgan dataset,
   please initialize a configuration file specifying the dataset
   (e.g. `ecgan-init ENTITY PROJECT EXPERIMENT_NAME -d mitbih_beatgan -o beatgan_config.yml`), preprocess the data
   (`ecgan-preprocess beatgan_config.yml`) and start training  (`ecgan-train beatgan_config.yml`). Training is mainly
   feasible on GPU for this model, even though CPU training is possible in this framework without any additional configurations.
   After preprocessing you can also simply use the configurations from the other training runs, only needing to change the
   dataset in the respective configuration file.


# ECGAN

ECGAN is a modular repository to train ML algorithms - and especially Generative Adversarial Networks (GANs) -
on electrocardiographic data, even though the setup is generally suitable for arbitrary time series.
While ECGAN also supports other tasks, such as classification using simple RNNs/CNNs, the focus lies on
the generation of data using GANs.
The GANs are trained on only the ''normal'' (for ECGs: healthy) class to learn the underlying representation of
this class. The resulting GAN can be used to generate new healthy data or detect anomalies by comparing
the synthetic data with the test data.
ECGAN follows modular setup allows easy modifications to the different parts of this project, allowing researchers to
simply  download and preprocess various ECG datasets, train a variety models to generate realistic time series and
apply a variety of anomaly detection mechanisms. ECGAN is built to be reproducible and easily expandable to allow fast
prototyping and foster comparability and open source implementations by reducing the time required to implement
models or preprocessing scenarios.

**Parts of the implementation are still in an experimental state.**

### Installation
#### Unix
Make sure to have installed python3.8 and git.

0. Clone the repository (using `git clone`)
1. Setup the virtual environment (e.g.`make env` which executes `virtualenv --python=/usr/bin/python3.8 .venv`
    and activate the environment `source .venv/bin/activate`)
2. Run `make setup_dev` in root if you want to develop. Run `make setup` if you only want to execute experiments.
3. During Step 2, ecgan and all requirements will be installed.

#### Windows

If you want to use ecgan on Windows, you cannot use `make` without additional tools. You can either use chocolatey
or similar tools to install `make` and use it. Otherwise, you can manually recreate the steps:
Install virtualenv (`pip install virtualenv`), create the environment `virtualenv --python=python3.8 .venv` and
activate the env (`.venv\Scripts\activate`) and install the packages (`pip install -U -r requirements.txt`)

### How to use

The package comes with a convenient CLI and configuration over YAML-Files.
By calling `ecgan-init -d DATASET -m MODULE -o FILE_NAME PROJECT NAME` a configuration file
is generated. This can be manually updated and contains most relevant hyperparameters.
After applying changes to the config file if desired you can start the preprocessing of
the chosen DATASET using `ecgan-preprocess` before training the model by invoking `ecgan-train`.
To perform anomaly detection, the `-a model_reference` flag is used (see [docs](REDACTED) for more
information).

### Data
We support several datasets will be used for evaluation: MIT-BIH (small amount of patients, long recordings, often
used), the PTB ECG dataset as well as the Shaoxing dataset (many patients, smaller recordings, published recently).

Some of the datasets require setting up kaggle credentials or downloading it manually (see [docs](REDACTED))

## About

### Project

REDACTED
