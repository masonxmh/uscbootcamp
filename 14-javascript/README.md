# JavaScript Homework: UFO Sightings

This folder contains the JavaScript and DOM manipulation homework. The project builds an interactive UFO sightings table using JavaScript, D3, HTML, CSS, Bootstrap, and a local JavaScript dataset.

## Project Overview

The app loads UFO sighting records from `data.js`, renders them into an HTML table, and lets the user filter the displayed results from a form. The table includes the sighting date, city, state, country, shape, duration, and comments.

## Folder Structure

- `UFO-level-1/StarterCode/`: Basic UFO Finder app with a single date filter.
- `UFO-level-2/StarterCode/`: Advanced UFO Finder app with multiple search filters.
- `UFO-level-2 - old/StarterCode/`: Older copy of the Level 2 work kept for reference.

Each app includes:

- `index.html`: Main web page.
- `static/js/data.js`: UFO sightings dataset.
- `static/js/app.js`: JavaScript logic that renders and filters the table.
- `static/css/style.css`: Custom page styling.
- `static/images/`: Background and UFO image assets.

## Level 1: Automatic Table and Date Search

`UFO-level-1/StarterCode` renders the full sightings dataset when the page loads. The user can enter a date, click `Filter Table`, and the table updates to show only sightings matching that date.

Filter field:

- Date, using values such as `1/11/2010`

## Level 2: Multiple Search Categories

`UFO-level-2/StarterCode` expands the filter form so users can search across several fields. Blank fields are ignored, so users can filter by one field or combine multiple filters.

Filter fields:

- Date
- City
- State
- Country
- Shape

## How To Review

Open either app directly in a browser:

1. `UFO-level-1/StarterCode/index.html`
2. `UFO-level-2/StarterCode/index.html`

No local server is required because the apps use static HTML, CSS, JavaScript, and local image/data files.

## Notes

- The filtering logic is written in `static/js/app.js`.
- The dataset is stored as a JavaScript array in `static/js/data.js`.
- User-entered Level 2 text filters are converted to lowercase before comparison, matching the lowercase values in the dataset.
