# Python Homework: Py Me Up, Charlie

This folder contains Python scripting challenges from the bootcamp Python homework. The primary assignment includes PyBank and PyPoll, with additional completed exercises for PyBoss and PyParagraph.

## Background

The homework focuses on using Python to read files, process CSV and text data, calculate summary metrics, print results to the terminal, and export analysis output files.

## Files

- `Pybank/main.py` - analyzes financial records from `Pybank/Resources/budget_data.csv`.
- `Pybank/financial_analysis.txt` - exported PyBank analysis results.
- `Pybank/main.ipynb` - notebook version of the PyBank work.
- `PyPoll/main.py` - analyzes election results from `PyPoll/Resources/election_data.csv`.
- `PyPoll/PyPollResult.txt` - exported PyPoll election results.
- `PyPoll/main.ipynb` - notebook version of the PyPoll work.
- `PyBoss/main.py` - reformats employee records from `PyBoss/employee_data.csv`.
- `PyBoss/summary.csv` - exported cleaned employee summary.
- `PyBoss/main.ipynb` - notebook version of the PyBoss work.
- `PyParagraph/paragraph_1.py` - analyzes `PyParagraph/raw_data/paragraph_1.txt`.
- `PyParagraph/paragraph_2.py` - analyzes `PyParagraph/raw_data/paragraph_2.txt`.
- `PyParagraph/paragraph_1_output.txt` - exported paragraph 1 analysis.
- `PyParagraph/paragraph_2_output.txt` - exported paragraph 2 analysis.
- `HW guideline/README.md` - original homework instructions used as the project guideline.

## PyBank

The PyBank script calculates:

- Total number of months in the dataset.
- Net total profit/loss over the full period.
- Average change in profit/loss over the full period.
- Greatest increase in profits, including date and amount.
- Greatest decrease in profits, including date and amount.

Run from the `Pybank` folder:

```powershell
python main.py
```

## PyPoll

The PyPoll script calculates:

- Total number of votes cast.
- Candidate names.
- Vote percentage for each candidate.
- Total votes for each candidate.
- Election winner based on popular vote.

Run from the `PyPoll` folder:

```powershell
python main.py
```

## Additional Challenges

`PyBoss` reformats employee data by splitting names, reformatting dates, masking Social Security numbers, and converting state names to abbreviations.

`PyParagraph` analyzes text files for word count, sentence count, average letter count, and average sentence length.

## Notes

- Scripts use relative file paths, so run each script from its own challenge folder.
- Jupyter checkpoint folders and Python cache files are ignored by `03-python/.gitignore`.
