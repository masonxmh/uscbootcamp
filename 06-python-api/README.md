# Python API Homework: What's The Weather Like?

This project uses Python, `citipy`, OpenWeatherMap API requests, Pandas, and Matplotlib to analyze weather patterns for 500+ cities across a wide range of latitudes.

## Background

The assignment asks how weather changes as cities approach the equator. To answer that question, the notebooks generate random latitude and longitude pairs, find the nearest unique cities, retrieve current weather data from OpenWeatherMap, and visualize weather metrics against latitude.

## Files

- `WeatherPy.ipynb` - main WeatherPy notebook for city generation, API calls, data cleanup, CSV export, plots, and written observations.
- `WeatherPy_method 2.ipynb` - alternate implementation of the same WeatherPy workflow.
- `api_keys.py` - local Python file imported by the notebooks for the OpenWeatherMap API key.
- `output_data/cities.csv` - exported city weather dataset from `WeatherPy.ipynb`.
- `output_data/cities_method2.csv` - exported city weather dataset from `WeatherPy_method 2.ipynb`.
- `output_data/*.png` - exported scatter plot images.
- `HW guideline/README.md` - original homework instructions used as the project guideline.

## Python File Setup

The notebooks expect an `api_keys.py` file in this folder with this variable:

```python
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
```

This file is ignored by `06-python-api/.gitignore` because API keys should stay local.

## Analysis

The notebooks perform the required WeatherPy workflow:

- Randomly generate latitude and longitude coordinates.
- Use `citipy` to identify nearby unique cities.
- Query the OpenWeatherMap API for weather data.
- Print processing logs while cities are retrieved.
- Build a weather DataFrame with city, country, date, latitude, longitude, max temperature, humidity, cloudiness, and wind speed.
- Export retrieved data to CSV.
- Create scatter plots for weather relationships by latitude.
- Include written observations about the results.

## Visualizations

### Latitude vs. Temperature

![Latitude vs. Temperature Plot](output_data/Latitude%20vs.%20Temperature%20Plot.png)

### Latitude vs. Humidity

![Latitude vs. Humidity Plot](output_data/Latitude%20vs.%20Humidity%20Plot.png)

### Latitude vs. Cloudiness

![City Latitude vs. Cloudiness Plot](output_data/City%20Latitude%20vs.%20Cloudiness%20Plot.png)

### Latitude vs. Wind Speed

![City Latitude vs. Wind Speed](output_data/City%20Latitude%20vs.%20Wind%20Speed.png)

## How To Review

1. Open `WeatherPy.ipynb` or `WeatherPy_method 2.ipynb` in Jupyter Notebook, JupyterLab, VS Code, or another notebook viewer.
2. Confirm `api_keys.py` exists locally if rerunning API calls.
3. Run cells from top to bottom to regenerate the weather data and plots.
4. Review the CSV and PNG outputs in `output_data`.

## Notes

- The notebooks use relative paths, so run them from the `06-python-api` folder.
- Generated datasets and plots are already saved in `output_data`.
- API keys, Python cache files, Jupyter checkpoint folders, and homework guideline files are ignored by `06-python-api/.gitignore`.
