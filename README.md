# Predicting Types of Crime in the City of Boston

**NOTE: This analysis is currently under development and not yet complete, please check back later.**

This repository contains the analysis and predictive results for a project exploring the prediction of crime types, based on a number of different features.

An accompanying website presenting this analysis and associated findings can be found at: [https://sedelmeyer.github.io/predicting-crime/](https://sedelmeyer.github.io/predicting-crime/)

### Contributors:
- [Christopher Campion](https://github.com/ccampion)
- [Sheraz Choudhary](https://github.com/sherazch00)
- [Fabio Pruneri](https://github.com/FabioPru)
- [Mike Sedelmeyer](https://github.com/sedelmeyer)

### Step 1: Install and start the required conda virtual environment

- The `predict-crime.yml` file contains specifications for building your virtual environment and related dependencies using the `conda` package manager
- To install your virtual environment, first clone this repository.
- Navigate to your newly cloned repository via your terminal and run the following command:
    - `conda env update --prefix ./env --file predict-crime.yml`
- Once your dependencies are installed, if you are in a linux terminal, you can activate the resulting conda environment by running the following command:
    - `conda activate ./env`
- Once your environment is up and running, you can fire up your local Jupyter server by using the command:
    - `jupyter notebook`
- For additional information on creating, managing, and running `conda` environments, please see the official Anaconda documentation:
    - https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

### Step 2: Download the required data sources:

- An inventory of **raw data sources** used for this analysis can be found in this project's **"data-inventory"** file at [./data-inventory.csv](data-inventory.csv).
- Raw data sources required for this analysis can be downloaded by running the notebook found at [./notebooks/000_download_datasources.ipynb](notebooks/000_download_datasources.ipynb).
- If you would like to simply download a copy of the fully populated **raw data directory** from which this analysis is built, you can do so by:
    1. Downloading and extracting the `./raw/` data directory found at this link:
        - https://drive.google.com/file/d/1Pv5M-GmUY2Cvq92GDH3d_h7MvXFjgzID/view?usp=sharing
    2. Replacing your local "raw" data sub-directory found at [./data/raw/](data/raw) in this project repository.
    3. Please DO NOT commit any data files to your git history.
- **The final engineered feature-sets and train-test splits used to train and test our resulting models** can also be downloaded as a .zip archive directly from this link:
    - https://drive.google.com/file/d/1UHgtQniKHfJZBwWIY2Xj7Pk8aJSB5Flv/view?usp=sharing

<br>

### DISCLAIMER:
Please note that this project should not be interpreted as being any reflection of our socioeconomic  or  political views. We are not suggesting that one should try to predict crime for the sake of instituting targeted policing. We are aware of the harmful effects. This is purely an academic project whereby we are exploring data and making statistical predictions in an area that is vastly affected by many confounding, real-world complex factors. The goal for this project is to illustrate learned skills that align with the goals of the university course for which we are completing this project.
