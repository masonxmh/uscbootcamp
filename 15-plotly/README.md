# Plotly Homework: Belly Button Biodiversity

This folder contains the Plotly homework dashboard for the Belly Button Biodiversity dataset. The app uses D3 to load `samples.json` and Plotly to build interactive charts for each test subject.

## Project Overview

The dashboard lets users select a test subject ID from a dropdown menu. When a subject is selected, the page updates the demographic information panel and all charts to match that subject's sample data.

The dataset includes 153 subject IDs, metadata records, and sample records.

## Dashboard Features

- Dropdown selector for test subject ID numbers.
- Demographic information panel for the selected subject.
- Horizontal bar chart showing the top 10 OTUs found in the selected subject.
- Bubble chart showing all OTU sample values for the selected subject.
- Bonus gauge chart showing belly button washing frequency in scrubs per week.

## Files

- `index.html`: Main dashboard page.
- `data/samples.json`: Belly Button Biodiversity dataset.
- `static/js/app.js`: Dashboard logic for loading data, populating the dropdown, rendering metadata, and building/updating the bar and bubble charts.
- `static/js/bonus.js`: Bonus gauge chart logic.

## Data Fields

The app uses three main sections from `samples.json`:

- `names`: Subject ID values used in the dropdown.
- `metadata`: Demographic details such as ethnicity, gender, age, location, belly button type, and washing frequency.
- `samples`: OTU IDs, sample values, and OTU labels used for the charts.

## Charts

### Bar Chart

The bar chart displays the selected subject's top 10 OTUs by sample value. OTU IDs are shown on the y-axis and sample values on the x-axis.

### Bubble Chart

The bubble chart displays all OTUs for the selected subject. OTU IDs appear on the x-axis, sample values appear on the y-axis, marker size represents sample value, and marker color is based on OTU ID.

### Gauge Chart

The bonus gauge chart displays the selected subject's washing frequency (`wfreq`) on a 0-9 scale.

## How To Review

Open `index.html` in a browser to use the dashboard.

If browser security settings block loading the local JSON file, run a simple local server from this folder:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

## Notes

- The dashboard is built with static HTML and JavaScript.
- The charts update through the `optionChanged()` function when a new subject is selected.
- The bonus gauge needle is drawn with a Plotly path shape and recalculated for each subject's washing frequency.
