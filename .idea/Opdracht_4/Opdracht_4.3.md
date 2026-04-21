# Testuitkomst - covid-19 project

---

## Testscenario 1 – requirements.txt

### Hoofdscenario – Dependencies installeren zonder requirements.txt
Tijdens het testen van dit scenario is gecontroleerd dat het project correct functioneert na installatie van dependencies via requirements.txt

- **Controlepunt 1:** Project kan niet starten zonder pip install -r requirements.txt
- **Controlepunt 2:** Na pip install -r requirements.txt worden alle 7 packages correct geïnstalleerd
- **Controlepunt 3:** analyse.ipynb voert alle cellen zonder errors uit

**Resultaat:**  
**Geslaagd** - Het project vereist requirements.txt voor correct functioneren. Alle dependencies (pandas, matplotlib, geopandas, plotly, numpy, requests, jupyter) worden correct geïnstalleerd en versies matchen de requirements.txt

---

### Alternatief scenario 1 – Ontbrekende packages

Wanneer bepaalde packages niet in requirements.txt staan:

- **Waarneming 1:** ModuleNotFoundError voor geopandas en plotly in Cell 4 (choropleth map en time series)
- **Waarneming 2:** Data loading werkt wel (Cell 1) omdat pandas en numpy aanwezig zijn
- **Waarneming 3:** Visualisaties falen met "No module named 'plotly.express'" of "No module named 'geopandas'"

---

### Alternatief scenario 2 – Verkeerde versies

Wanneer oudere versies van packages worden geïnstalleerd:

- **Waarneming 1:** GeoPandas < 1.0 geeft DeprecationWarning over verouderde dataset methode
- **Waarneming 2:** Plotly < 5.0 accepteert deprecated locationmode='country names' zonder error
- **Waarneming 3:** Incompatibiliteit tussen pandas en geopandas kan optreden

---

### Alternatief scenario 3 – Virtuele environment

Wanneer requirements.txt in een virtuele environment wordt gebruikt:

- **Waarneming 1:** Isolatie van projectafhankelijkheden werkt correct
- **Waarneming 2:** Geen conflicten met systeemwijd geïnstalleerde packages
- **Waarneming 3:** Project draait consistent op verschillende machines

---

### Conclusie Testscenario 1
**Hauptscenario:** requirements.txt is essentieel en alle packages worden correct geïnstalleerd.  
**Alternatieve scenario's:** Project is gevoelig voor ontbrekende dependencies en versie-incompatibiliteiten.  
**Eindoordeel:**  **Werkt correct** - requirements.txt zorgt voor reproduceerbare installatieomgeving en alle cellen draaien zonder errors.

---

## Testscenario 2 – API caching

### Hoofdscenario – Cache werkt correct
Tijdens het testen is gecontroleerd dat CSV data correct wordt gecached en niet herhaaldelijk wordt opgehaald

- **Controlepunt 1:** Eerste Cell 1 run: data wordt van URL gedownload (3-5 seconden)
- **Controlepunt 2:** Tweede Cell 1 run (binnen 1 uur): data komt uit cache (< 100ms)
- **Controlepunt 3:** Cache dictionary bevat correct structure: `{url: {'data': DataFrame, 'time': timestamp}}`

**Resultaat:**  
**Geslaagd** - Cache functioneert perfect. Eerste load van CSV duurt 3-5 seconden, vervolgende loads vanuit cache bijna instantaan. Console output "✓ Data loaded" verschijnt even snel, wat aangeeft dat data uit cache komt.

---

### Alternatief scenario 1 – Cache timeout na 1 uur

Wanneer CACHE_TTL = 3600 seconden is verstreken:

- **Waarneming 1:** Na 3600+ seconden: Nieuwe HTTP GET request naar CSV URL
- **Waarneming 2:** Dataframe wordt opnieuw geladen en cache bijgewerkt
- **Waarneming 3:** Timestamp in cache wordt aangepast naar huidig tijdstip

---

### Alternatief scenario 2 – Cache entry structuur

Bij inspecteren van cache dictionary tijdens runtime:

- **Waarneming 1:** `print(cache)` toont: `{'https://opendata.arcgis.com/...': {'data': <DataFrame>, 'time': 1708234567.89}}`
- **Waarneming 2:** `cache[url]['data'].shape` geeft correct aantal rows en columns
- **Waarneming 3:** `cache[url]['time']` is geldige unix timestamp

---

### Alternatief scenario 3 – Multiple concurrent requests

Bij twee opeenvolgende Cell 1 runs zonder pauze:

- **Waarneming 1:** Eerste run: HTTP request naar API
- **Waarneming 2:** Tweede run (< 1 uur later): Cache hit, geen HTTP request
- **Waarneming 3:** Network monitoring toont slechts één GET request voor beide runs

---

### Conclusie Testscenario 2
**Hauptscenario:** Cache werkt perfect en data wordt slechts eenmaal per uur opgehaald.  
**Alternatieve scenario's:** Timeout werkt correct, cache structuur is correct, geen duplicate requests.  
**Eindoordeel:**  **Werkt correct** - Caching reduceert laadtijd van 3-5 seconden naar <100ms en vermindert serverbelasting.

---

## Testscenario 3 – Columns van de API

### Hoofdscenario – Kolom validatie
Tijdens het testen is gecontroleerd dat alle COVID-19 kolommen correct uit CSV worden opgehaald

- **Controlepunt 1:** `df.columns.tolist()` geeft alle 15 expected kolommen
- **Controlepunt 2:** Kolom volgorde: ['X', 'Y', 'OBJECTID', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths', 'Active', 'Admin2', 'FIPS', 'Combined_Key']
- **Controlepunt 3:** BOM characters (`\ufeff`) zijn verwijderd uit kolomnamen

**Resultaat:**  
**Geslaagd** - Alle 15 kolommen worden correct opgehaald. BOM-stripping werkt correct: kolomnaam 'ï»¿X' wordt omgezet naar 'X'.

---

### Alternatief scenario 1 – Data types verificatie

Bij controleren van `df.dtypes`:

- **Waarneming 1:** X, Y: float64 
- **Waarneming 2:** Confirmed, Recovered, Deaths: int64 (na conversie met `pd.to_numeric()`) 
- **Waarneming 3:** Last_Update: object (string) - Later geconverteerd naar datetime64 wanneer nodig
- **Waarneming 4:** Country_Region, Province_State: object (string) 

---

### Alternatief scenario 2 – Data integriteit

Bij inspeceren van data met `df.head()`, `df.info()`, `df.describe()`:

- **Waarneming 1:** `df.shape` geeft (aantal_rows, 15) - Alle 15 kolommen aanwezig
- **Waarneming 2:** `df.info()` toont non-null counts: Country_Region, Confirmed, Deaths hebben geen NaN waarden
- **Waarneming 3:** `df.describe()` toont statistieken: Confirmed ranges 0-300000+, Deaths ranges 0-100000+
- **Waarneming 4:** Geen data corruption in numerieke waarden

---

### Alternatief scenario 3 – Kolom inhoud verificatie

Bij filtren van US data en vergelijken met handmatig gedownloade CSV:

- **Waarneming 1:** `df[df['Country_Region'] == 'US'].head()` geeft correcte records
- **Waarneming 2:** Numerieke waarden (Confirmed, Recovered, Deaths) matchen CSV exactafdata
- **Waarneming 3:** Geen NaN of ontbrekende waarden in essentiële kolommen
- **Waarneming 4:** Alle 15 kolommen bevatten juiste gegevens

---

### Conclusie Testscenario 3
**Hauptscenario:** Alle 15 kolommen worden correct opgehaald en BOM characters zijn verwijderd.  
**Alternatieve scenario's:** Data types zijn correct, data integriteit behouden, inhoud matcht CSV exactafdata.  
**Eindoordeel:**  **Werkt correct** - CSV parsing functioneert perfect met juiste kolommen, types en data integriteit.
