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

# Portfolio Hoofddocument

**Naam:**Melvyn Nibigira  
**Studentnummer:** 41231 
**Opleiding:**  Bit Academy
**Instituut:**  Media college Amsterdam
**Datum:** 17-04-2026

---

## Inhoudsopgave

1. [Inleiding](#inleiding)
2. [Opbouw van het portfolio](#opbouw-van-het-portfolio)
3. [Overzicht van de opdrachten](#overzicht-van-de-opdrachten)
4. [Reflectie op het leerproces](#reflectie-op-het-leerproces)
5. [Conclusie](#conclusie)
6. [Bijlagen / Links naar opdrachten](#bijlagen--links-naar-opdrachten)

---

## Inleiding

---

## Opbouw van het portfolio

- **Opdrachtbeschrijving**
- **Uitwerking / Product**
- **Bewijsmateriaal**
- **Reflectie**

---

## Overzicht van de opdrachten

| Nr. | Opdracht | Korte Beschrijving|
|-----|---------|-------------------|
| 1 | https://github.com/Melvynwastaken/Data_PO/blob/13ae7a7d5b6629a0d9c4d26375f42d75b164445e/.idea/Opdracht_1| Je gaat in dit examenonderdeel bewijzen dat je de eisen en wensen van een klant kan omzetten naar user stories. Vervolgens dat je op basis van die user stories een globale planning kan maken en dat je tijdens je project de voortgang in de gaten kan houden met behulp van je planning.  |
| 2 | https://github.com/Melvynwastaken/Data_PO/blob/13ae7a7d5b6629a0d9c4d26375f42d75b164445e/.idea/Opdracht_2|  Je gaat in dit examenonderdeel bewijzen dat je een programma kan ontwerp voordat je begint met bouwen. Let op: hier wordt het technische ontwerp bedoeld (UML) en niet het ontwerp van de user interface. |
| 3 | https://github.com/Melvynwastaken/Data_PO/blob/c3f5c86cf2691320b23b7f96a7922ab23a0148d9/.idea/Opdracht_3| Je gaat in dit examenonderdeel bewijzen dat je kan programmeren. Dat je hierbij hoge kwaliteit code kan opleveren die voldoet aan conventies en dat je dit kan beheren met behulp van versiebeheer (git).  |
| 4 | https://github.com/Melvynwastaken/Data_PO/blob/e2c1e890c34099ff069003255c5cfd641787ce92/.idea/Opdracht_4| Je gaat in dit examenonderdeel bewijzen dat je jouw applicatie (geautomatiseerd) kan testen. Je gaat hiervoor testen schrijven en je test resultaten uitwerken in een rapport. |
| 5 | https://github.com/Melvynwastaken/Data_PO/blob/13ae7a7d5b6629a0d9c4d26375f42d75b164445e/.idea/Opdracht_5|  Je gaat in dit examenonderdeel bewijzen dat je na het bouwen van je product, hierop kan terugkijken en verbetervoorstellen kan aandragen|
| 6 | https://github.com/Melvynwastaken/Data_PO/blob/c3f5c86cf2691320b23b7f96a7922ab23a0148d9/.idea/Opdracht_6|  Je gaat in dit examenonderdeel bewijzen dat je een actieve bijdrage kan leveren in meetings, notulen + afspraken kan vastleggen en je ook aan deze afspraken kan houden. |
| 7 | https://github.com/Melvynwastaken/Data_PO/blob/c3f5c86cf2691320b23b7f96a7922ab23a0148d9/.idea/Opdracht_7|  Je gaat in dit examenonderdeel bewijzen dat je een presentatie kan geven om je product te presenteren.|
| 8 | https://github.com/Melvynwastaken/Data_PO/blob/c3f5c86cf2691320b23b7f96a7922ab23a0148d9/.idea/Opdracht_8|  Je gaat in dit examenonderdeel bewijzen dat je een retrospective kan bijwonen en een actieve bijdrage kan leveren aan het verbeteren van het proces. |

---

## Reflectie op het leerproces

### Belangrijkste leerpunten

-Team verbanden verbeteren, communicatie verbeteren, en meer ownership nemen over taken.
-Scrum ceremonies beter benutten voor planning, feedback, en samenwerking.
-Agile mindset ontwikkelen: flexibel zijn, openstaan voor feedback, en continu verbeteren.
-

---

## Conclusie

-Ik weet nu wat meer over covid-19 data, dit was zeker een leerzaam project. 
Ik heb geleerd hoe ik data kan verzamelen, verwerken en visualiseren. 
Ook heb ik geleerd hoe ik een project kan plannen en organiseren, en hoe ik kan samenwerken met anderen. Ik ben trots op wat ik heb bereikt en ik ben blij dat ik deze ervaring heb opgedaan.

## Bijlagen / Links naar opdrachten

-Zie de opdrachten bestanden in .idea/Opdracht_1 t/m .idea/Opdracht_8 repository voor de volledige uitwerkingen, bewijsmateriaal en reflecties.

---

