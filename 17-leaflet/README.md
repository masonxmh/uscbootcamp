# Leaflet Homework: Earthquake Visualization

This folder contains the Leaflet mapping homework. The project visualizes recent earthquake activity from the USGS GeoJSON feed and, in the advanced version, overlays tectonic plate boundaries.

## Project Overview

The maps use Leaflet, D3, Mapbox tiles, and GeoJSON data to display earthquakes from the past seven days. Earthquake markers are sized by magnitude, colored by magnitude range, and include popups with location, time, and magnitude details.

## Folder Structure

- `Leaflet-Step-1/`: Required earthquake map.
- `Leaflet-Step-2/`: Advanced map with additional base maps and tectonic plate overlay.

Each step includes:

- `index.html`: Main map page.
- `static/js/logic.js`: Leaflet and D3 map logic.
- `static/js/config.js`: Local Mapbox API key configuration.
- `static/css/style.css`: Full-screen map and legend styling.

## Step 1: Earthquake Map

`Leaflet-Step-1` loads the USGS all-week earthquake GeoJSON feed:

```text
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson
```

Features included:

- Light Mapbox base map.
- Circle markers for earthquake locations.
- Marker radius based on earthquake magnitude.
- Marker color based on earthquake magnitude.
- Popups with place, time, and magnitude.
- Legend for the magnitude color scale.

## Step 2: Earthquakes and Tectonic Plates

`Leaflet-Step-2` extends Step 1 by loading tectonic plate boundary GeoJSON data:

```text
https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json
```

Additional features included:

- Satellite, grayscale, and outdoors base maps.
- Layer control for switching map styles.
- Overlay controls for earthquakes and fault lines.
- Orange tectonic plate boundary overlay.
- Default map view with earthquake and plate layers enabled.

## Magnitude Colors

Earthquakes are colored by magnitude:

- `0-1`: Green
- `1-2`: Yellow-green
- `2-3`: Yellow
- `3-4`: Orange
- `4-5`: Light red-orange
- `5+`: Red

## How To Review

Add a valid Mapbox API key in each step's `static/js/config.js` file:

```javascript
const API_KEY = "YOUR_MAPBOX_API_KEY";
```

Then open either page in a browser:

1. `Leaflet-Step-1/index.html`
2. `Leaflet-Step-2/index.html`

If browser settings block remote GeoJSON requests from a local file, run a simple local server from this folder:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/Leaflet-Step-1/
http://localhost:8000/Leaflet-Step-2/
```

## Notes

- The maps use Leaflet 1.6.0 and D3 v5.
- `config.js` should contain only a local API key and should not be committed with a real secret.
- The earthquake data updates as the USGS feed changes.
