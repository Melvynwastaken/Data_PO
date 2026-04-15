# Data_PO

A COVID-19 data analysis project that collects cases from APIs and public datasets, aggregates data by country, and creates map visualizations and charts.

## What This Project Does

- Fetches COVID-19 case data (Confirmed, Deaths, Recovered) from public sources
- Cleans and prepares the data for analysis
- Aggregates statistics by country
- Creates choropleth maps showing case distribution across countries
- Generates stacked bar charts comparing case statistics

## How to Run

### 1. Install Dependencies

Using Conda (recommended on Windows):
```bash
conda create -n data_po python=3.11 -y
conda activate data_po
conda install -c conda-forge geopandas geodatasets fiona shapely pyproj rtree matplotlib pandas requests jupyterlab -y
```

Or using pip:
```bash
python -m pip install -r requirements.txt
python -m pip install geodatasets
```

### 2. Run the Map Script

Generate a map and stacked chart for a specific country:
```bash
python python.py --country "France"
```

Output files will be saved to the `outputs/` folder.

Optional arguments:
- `--csv <path>` — Use a local CSV file instead of downloading
- `--out <path>` — Specify output directory (default: `outputs`)

### 3. Run the Jupyter Notebooks

Open Jupyter Lab or Notebook:
```bash
jupyter lab
```

Then open:
- `verzamelen.ipynb` — Data collection and preparation
- `analyse.ipynb` — Analysis and visualizations

## Data Sources

- ArcGIS COVID-19 dataset
- mmediagroup COVID API (optional)
- Natural Earth geometries for mapping

## details
 the project is structured to allow easy extension, such as adding more countries,
 incorporating additional data sources, or creating new types of visualizations.
 The code is modular and well-documented for clarity and maintainability.

## License

