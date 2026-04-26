# D3 Homework: Data Journalism

This folder contains the D3 data journalism homework. The project builds an interactive scatter plot for the D3Times page using state-level health and demographic data.

## Project Overview

The visualization compares health risk factors with demographic measures from `data.csv`. Each state is represented by a circle labeled with its state abbreviation. Users can switch between different X-axis and Y-axis variables to explore relationships in the data.

The published version of the app is in `docs/`, which is the folder structure commonly used for GitHub Pages deployment.

## Dashboard Features

- Responsive D3 scatter plot that redraws when the browser window changes size.
- State abbreviation labels inside each circle.
- Interactive X-axis labels:
  - In Poverty (%)
  - Age (Median)
  - Household Income (Median)
- Interactive Y-axis labels:
  - Lacks Healthcare (%)
  - Smokes (%)
  - Obese (%)
- Animated transitions when the selected axes change.
- D3 tooltips showing the selected state and active metric values.

## Files

- `docs/index.html`: Main D3Times page for the deployed app.
- `docs/assets/js/app.js`: Main D3 chart logic.
- `docs/assets/data/data.csv`: State-level source dataset.
- `docs/assets/css/style.css`: General page styling.
- `docs/assets/css/d3Style.css`: Chart, axis label, circle, tooltip, and mobile styling.
- `D3_data_journalism/level1/`: Initial static scatter plot version.
- `D3_data_journalism/level2/`: Interactive version with multiple selectable axes.
- `D3_data_journalism/test/`: Test copy of the project files.

## Data Fields Used

The chart uses fields from `assets/data/data.csv`, including:

- `state` and `abbr`
- `poverty`
- `age`
- `income`
- `healthcare`
- `smokes`
- `obesity`

## Level 1

`D3_data_journalism/level1` creates a static scatter plot comparing poverty rate with lack of healthcare. It parses the CSV values, builds linear scales, appends axes, draws state circles, and labels each circle with the state abbreviation.

## Level 2 / Docs

`D3_data_journalism/level2` and `docs` include the interactive version. This version allows users to click axis labels to change the displayed comparison, updates the scales and axes, moves the circles and state labels with transitions, and refreshes tooltip content for the selected metrics.

## How To Review

Open the deployed-ready app from:

```text
docs/index.html
```

Because the app loads a CSV file with D3, a local server may be needed depending on browser security settings. From the `16-D3` folder, run:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/docs/
```

## Notes

- The app uses D3 v5 and d3-tip.
- The chart defaults to `poverty` on the X-axis and `healthcare` on the Y-axis.
- CSS media queries hide state text on smaller screens to keep the chart readable.
