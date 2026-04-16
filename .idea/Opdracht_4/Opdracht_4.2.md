# Testscenarios – covid-19 data project

## Testscenario 1 – [requirements.txt]

**Doel:** Verifiëren dat alle benodigde libraries correct worden geïnstalleerd en het project volledig functioneert  
**Preconditie:** Python 3.8+ is geïnstalleerd, pip is beschikbaar, internetverbinding aanwezig

---

### Hoofdscenario – Dependencies installeren zonder requirements.txt

**Testdata**
- Project zonder pip install -r requirements.txt te draaien
- Poging om analyse.ipynb uit te voeren zonder geïnstalleerde dependencies
- Controleer foutmeldingen bij ontbrekende modules

**Stappen**
1. Open command prompt in project directory
2. Probeer analyse.ipynb uit te voeren zonder libraries te installeren
3. Observeer foutmeldingen

**Verwacht resultaat**
- ModuleNotFoundError voor pandas, matplotlib, geopandas, plotly
- Project kan niet starten zonder afhankelijkheden
- Duidelijke foutmelding: "No module named 'pandas'" (of ander)

---

### Alternatief 1 – Requirements.txt correct installeren

**Testdata:** pip install -r requirements.txt uitvoeren

**Stappen**
1. Open command prompt in project directory (C:\Users\Melvy\OneDrive\Documenten\Python\Data_PO)
2. Voer uit: `pip install -r requirements.txt`
3. Wacht tot installatie compleet is
4. Voer uit: `pip list` en controleer alle packages

**Verwacht resultaat**
- Alle packages geïnstalleerd: requests~=2.31.0, pandas~=2.1.4, numpy~=1.26.4, matplotlib~=3.8.0, jupyter~=1.0.0, geopandas~=1.1.2, plotly~=5.17.0
- Geen error messages
- Alle versies matchen de requirements.txt

---

### Alternatief 2 – Analyseer ipynb volledig uitvoeren

**Testdata:** analyse.ipynb met alle cellen

**Stappen**
1. Start Jupyter notebook in project directory
2. Open analyse.ipynb
3. Run all cells (Ctrl+Shift+Enter of via Cell menu)
4. Controleer output van alle cells

**Verwacht resultaat**
- Cell 1: Data succesvol geladen (✓ Data loaded. Columns: [...])
- Cell 2: Donut chart correct weergegeven
- Cell 3: Zoekfunctie werkt
- Cell 4: Top 10 bar chart, choropleth map, time series alle zichtbaar
- Geen errors of warnings

---

### Alternatief 3 – Individuele library verificatie

**Testdata:** Specifieke import tests

**Stappen**
1. Open Python interpreter in terminal
2. Test imports: `import pandas`, `import geopandas`, `import plotly.express`, `import matplotlib.pyplot`
3. Controleer versies: `import pandas; print(pandas.__version__)`

**Verwacht resultaat**
- Alle imports succesvol zonder errors
- Versies matchen requirements.txt
- Geen DeprecationWarnings

---

## Testscenario 2 – [API caching]

**Doel:** Verifiëren dat data correct wordt gecached en niet herhaaldelijk opnieuw wordt opgehaald  
**Preconditie:** Internetverbinding, requirements.txt geïnstalleerd, CSV URL bereikbaar

---

### Hoofdscenario – Cache werkt correct

**Testdata**
- CSV URL: https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_1.csv
- CACHE_TTL: 3600 seconden (1 uur)
- Cache dictionary: `cache = {}`

**Stappen**
1. Run Cell 1 van analyse.ipynb (data loading)
2. Observeer console output: "✓ Data loaded"
3. Note de load time
4. Run Cell 1 opnieuw
5. Vergelijk load times

**Verwacht resultaat**
- Eerste keer: CSV wordt gedownload van URL (enkele seconden)
- Tweede keer: Data komt uit cache (bijna instantaan, <100ms)
- Console toont geen herhaalde HTTP requests
- Dezelfde data in beide loads

---

### Alternatief 1 – Cache timeout na 1 uur

**Testdata:** time.time() vergelijken, CACHE_TTL = 3600

**Stappen**
1. Run Cell 1 op tijd T=0
2. Wacht (of simuleer wacht) tot T=3601 seconden
3. Run Cell 1 opnieuw
4. Controleer of nieuw request wordt gedaan

**Verwacht resultaat**
- Na 3600+ seconden: Nieuwe HTTP request naar CSV URL
- Data wordt opnieuw opgehaald
- Cache wordt bijgewerkt met nieuwe timestamp

---

### Alternatief 2 – Cache entry structuur verificatie

**Testdata:** Cache dictionary structure

**Stappen**
1. Run Cell 1
2. Print cache contents: `print(cache)`
3. Controleer structuur: `print(cache[url].keys())`

**Verwacht resultaat**
- Cache structure: `{url: {'data': DataFrame, 'time': timestamp}}`
- 'data' bevat pandas DataFrame met COVID-19 gegevens
- 'time' bevat unix timestamp van opslag

---

### Alternatief 3 – Multiple concurrent requests

**Testdata:** Twee simultane requests naar dezelfde URL

**Stappen**
1. Run Cell 1 twee keer achter elkaar zonder pauze
2. Monitor network activity en cache behavior
3. Controleer of slechts één HTTP request wordt gemaakt

**Verwacht resultaat**
- Eerste request: HTTP download
- Tweede request (nog in TTL): Geeft gecachede data terug
- Geen duplicate HTTP calls

---

## Testscenario 3 – [Columns van de API]

**Doel:** Verifiëren dat alle COVID-19 API kolommen correct worden opgehaald en verwerkt  
**Preconditie:** CSV file bereikbaar, analyse.ipynb geopend

---

### Hoofdscenario – Kolom validatie

**Testdata**
- CSV URL: https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_1.csv
- Expected columns: ['X', 'Y', 'OBJECTID', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths', 'Active', 'Admin2', 'FIPS', 'Combined_Key']
- Totaal: 15 kolommen

**Stappen**
1. Run Cell 1 (data laden)
2. Run in nieuwe cell: `print(df.columns.tolist())`
3. Run: `print(len(df.columns))`
4. Vergelijk met expected columns

**Verwacht resultaat**
- Alle 15 expected columns aanwezig
- Kolom volgorde correct
- Geen extra of ontbrekende kolommen
- BOM characters verwijderd uit kolomnamen

---

### Alternatief 1 – Data types verificatie

**Testdata:** Datatype mapping

**Stappen**
1. Run Cell 1
2. Run: `print(df.dtypes)`
3. Controleer per kolom:

**Verwacht resultaat**
- X, Y: float64
- OBJECTID: int64
- Province_State, Country_Region, Combined_Key: object (string)
- Last_Update: datetime64[ns] (na conversie)
- Lat, Long_: float64
- Confirmed, Recovered, Deaths, Active: int64 (na conversie)
- Admin2, FIPS: object (string)

---

### Alternatief 2 – Data integriteit checken

**Testdata:** Sample data van CSV

**Stappen**
1. Run Cell 1
2. Run: `print(df.head())`
3. Run: `print(df.info())`
4. Run: `print(df.describe())`

**Verwacht resultaat**
- Head toont eerste 5 rijen met alle 15 kolommen
- Info toont non-null counts per kolom
- Describe toont statistieken voor numerieke kolommen
- Geen NaN values in essentiële kolommen (Country_Region, Confirmed, Deaths)

---

### Alternatief 3 – Kolom inhoud sample verificatie

**Testdata:** Bekende waarden uit CSV

**Stappen**
1. Download CSV handmatig
2. Controleer enkele sample rows
3. Run Cell 1 en run: `print(df[df['Country_Region'] == 'US'].head())`
4. Vergelijk data met CSV

**Verwacht resultaat**
- Data in DataFrame matcht CSV inhoud exact
- US records correct gefilterd
- Numerieke waarden voor Confirmed, Recovered, Deaths correct
- Geen data corruption of omvormingsfouten
