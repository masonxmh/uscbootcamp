# Matplotlib Homework: The Power of Plots

This folder contains the Pymaceuticals Matplotlib challenge. The notebook analyzes mouse clinical trial data for anti-cancer drug treatments and visualizes how selected treatments compare over a 45-day study.

## Background

Pymaceuticals Inc. is evaluating drug-based treatments for squamous cell carcinoma. The assignment uses animal study data to compare treatment response for Capomulin, Infubinol, Ketapril, and Placebo.

## Files

- `pymaceuticals.ipynb` - Jupyter notebook with the Pandas analysis and Matplotlib visualizations.
- `data/clinicaltrial_data.csv` - clinical trial measurements by mouse and timepoint.
- `data/mouse_drug_data.csv` - mouse-to-drug treatment mapping.
- `Tumor Response to Treatment.png` - exported tumor volume response chart.
- `Metastatic Response to Treatment.png` - exported metastatic site response chart.
- `Survival During Treatment.png` - exported survival rate chart.
- `Total Change During 45 Days Treatment.png` - exported tumor volume change chart.
- `HW guideline/README.md` - original homework instructions used as the project guideline.

## Analysis

The notebook includes:

- Loading and merging mouse drug data with clinical trial data.
- Mean tumor volume by drug and timepoint.
- Standard error calculations for tumor volume and metastatic sites.
- Tumor response plot with error bars.
- Metastatic response plot with error bars.
- Mouse survival rate over time.
- Percent tumor volume change over the full 45-day treatment period.
- Written observations based on the generated plots.

## Visualizations

### Tumor Response To Treatment

![Tumor Response to Treatment](Tumor%20Response%20to%20Treatment.png)

### Metastatic Response To Treatment

![Metastatic Response to Treatment](Metastatic%20Response%20to%20Treatment.png)

### Survival During Treatment

![Survival During Treatment](Survival%20During%20Treatment.png)

### Total Change During 45 Days Treatment

![Total Change During 45 Days Treatment](Total%20Change%20During%2045%20Days%20Treatment.png)

## How To Review

1. Open `pymaceuticals.ipynb` in Jupyter Notebook, JupyterLab, VS Code, or another notebook viewer.
2. Run cells from top to bottom to regenerate the analysis and chart images.
3. Review the exported PNG files for the final visual outputs.

## Notes

- The notebook uses relative paths to the local `data` folder.
- Run the notebook from the `05-matplotlib` folder so the CSV paths resolve correctly.
- Jupyter checkpoint folders and homework guideline files are ignored by `05-matplotlib/.gitignore`.
