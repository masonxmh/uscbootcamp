# Machine Learning Homework: Exoplanet Exploration

This folder contains the machine learning homework using NASA Kepler exoplanet candidate data. The goal is to build and compare classification models that predict `koi_disposition`, which labels Kepler objects of interest as confirmed planets, candidates, or false positives.

## Background

Over nine years, the NASA Kepler space telescope collected data while searching for planets outside our solar system. This project uses the Kepler dataset to train supervised machine learning models that classify exoplanet candidates from observed features.

Data source:

- [NASA Kepler Exoplanet Search Results on Kaggle](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)

## Project Requirements

The homework workflow includes:

- Preprocess the dataset before fitting models.
- Perform feature selection and remove unnecessary features.
- Scale numerical data.
- Split the data into training and testing sets.
- Use `GridSearchCV` to tune model parameters.
- Train and compare at least two classifiers.

## Files

- `exoplanet_data.csv`: Original Kepler exoplanet dataset used for modeling.
- `exoplanet_data_select.csv`: Reduced feature dataset created after feature selection.
- `model_1.ipynb`: Support Vector Machine workflow.
- `model_2.ipynb`: Logistic Regression workflow.
- `svc.sav`: Saved SVM model.
- `logicreg.sav`: Saved Logistic Regression model.

## Feature Selection

The notebooks use a filter-based feature selection approach. Features were reviewed using correlation analysis and then reduced to a selected subset stored in `exoplanet_data_select.csv`.

The selected dataset keeps `koi_disposition` as the target variable and includes features such as:

- False-positive flags
- Orbital period error fields
- Transit timing error fields
- Impact and duration error fields
- Transit depth
- Equilibrium temperature
- Signal-to-noise ratio
- Stellar gravity fields
- Right ascension, declination, and Kepler magnitude

## Model 1: Support Vector Machine

Notebook:

- `model_1.ipynb`

Workflow:

- Read and clean the Kepler dataset.
- Select modeling features.
- Split data into training and testing sets.
- Scale the data.
- Train an SVM classifier.
- Tune parameters with `GridSearchCV`.
- Save the fitted model as `svc.sav`.

Reported tuned parameters:

```text
{'C': 200, 'gamma': 1e-05, 'kernel': 'linear'}
```

Reported GridSearch score:

```text
0.8640077063579273
```

## Model 2: Logistic Regression

Notebook:

- `model_2.ipynb`

Workflow:

- Reuse the cleaned and selected feature data.
- Split data into training and testing sets.
- Scale the data.
- Train a Logistic Regression classifier.
- Tune `C` and `max_iter` with `GridSearchCV`.
- Save the fitted model as `logicreg.sav`.

Reported tuned parameters:

```text
{'C': 800, 'max_iter': 200}
```

Reported GridSearch score:

```text
0.8632459849074727
```

## Conclusion

Both the SVM and Logistic Regression models performed similarly on this dataset. The SVM model produced a slightly higher tuned score, so it was the stronger model in this comparison.

## How To Review

Open the notebooks in Jupyter Notebook or JupyterLab:

1. `model_1.ipynb`
2. `model_2.ipynb`

The saved model files are already included for review:

- `svc.sav`
- `logicreg.sav`

## Notes

- Notebook checkpoints and generated cache files are ignored by `.gitignore`.
- The existing `.sav` files are intentionally kept trackable because they are final model outputs for the assignment.
