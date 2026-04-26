# Web Scraping Homework: Mission to Mars

This folder contains the Mission to Mars web scraping challenge. The project scrapes Mars-related content from multiple websites, stores the scraped data in MongoDB, and displays the results in a Flask web application.

## Project Overview

The assignment is completed in two parts:

- `mission_to_mars.ipynb`: Jupyter Notebook used to develop and test the scraping workflow.
- `scrape_mars.py` and `app.py`: Python scripts used by the Flask application to scrape, store, and render the Mars data.

The Flask page includes a "Scrape New Data" button that runs the scraper, updates MongoDB, and redirects back to the dashboard.

## Scraped Data

The scraper collects:

- Latest Mars news title and paragraph text from NASA Mars News.
- Featured Mars image URL from JPL Space Images.
- Current Mars weather text from the Mars weather report page.
- Mars facts table from Space Facts, converted to HTML with Pandas.
- Full-resolution Mars hemisphere image URLs and titles from the USGS Astrogeology site.

## Application Files

- `app.py`: Flask application with the home route and `/scrape` route.
- `scrape_mars.py`: Scraping script with the `scrape()` function.
- `mission_to_mars.ipynb`: Notebook containing the scraping workflow.
- `templates/index.html`: Bootstrap template that renders the scraped Mars data.
- `static/css/style.css`: Custom CSS for the Flask app.
- `Screenshot/`: Screenshots of the completed application.

## Flask Routes

- `/`: Queries MongoDB for the stored Mars data and renders `templates/index.html`.
- `/scrape`: Runs `scrape_mars.scrape()`, updates MongoDB, and redirects to the home page.

## Screenshots

![Mission to Mars Screenshot 1](Screenshot/Screenshot%201.png)

![Mission to Mars Screenshot 2](Screenshot/Screenshot%202.png)

## How To Run

Install the required Python packages:

```bash
pip install flask flask-pymongo splinter beautifulsoup4 pandas requests
```

Start MongoDB locally, then run the Flask application:

```bash
python app.py
```

Open the app in a browser:

```text
http://127.0.0.1:5000/
```

Click `Scrape New Data` to collect fresh data and update the dashboard.

## Notes

- The app expects MongoDB to be available at `mongodb://localhost:27017/mission_to_mars`.
- The scraper uses Splinter with Chrome. A local ChromeDriver executable is ignored by `.gitignore`, so install or provide a compatible driver locally before running the scraper.
- The external websites used in the original homework may change over time, so scraping selectors may need updates if a source page structure changes.
