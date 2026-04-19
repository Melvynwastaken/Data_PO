# TestPlan covid-19 data project

---

## Case 1: Requirement.txt

### 1. Testscenario
De gebruiker laad het project goed af door middel van de requirements.txt file te runnen en controleert of alle benodigde libraries zijn geïnstalleerd en of het project correct functioneert

### 2. Testdata
- het Project zonder de requirements.txt file te runnen
- Laad het project correct af door middel van de requirements.txt file te runnen
- pip install -r requirements.txt runnen en controleren of alle libraries correct worden geïnstalleerd en er geen foutmeldingen zijn

### 3. Verwacht resultaat
- Er wordt een foutmelding gegeven dat er libraries ontbreken en dat het project niet correct functioneert
- Het project wordt correct afgeladen, alle benodigde libraries worden geïnstalleerd en het project functioneert correct
- de gebruiker checkt of pip install -r requirements.txt alle libraries correct geïnstalleerd zijn en er zijn geen foutmeldingen

---

## Case 2: API caching

### 1. Testscenario
De gebruiker test of de api correct gecached is en of de data correct wordt opgehaald en verwerkt

### 2. Testdata
- run de code block met de api caching en controleer of de data correct wordt opgehaald en verwerkt
- De gebruiker test of de code block de api cached door middel van het runnen van de code block en te kijken of de visuals na het runnen van de code block 10 min erna nog steeds dezelfde data laten zien
- de api hoeft maar 1 keer gecached te worden, dus de gebruiker hoeft maar 1 keer de code block te runnen en daarna te controleren of de visuals nog steeds dezelfde data laten zien na binne een uur.

### 3. Verwacht resultaat
- De data wordt correct opgehaald en verwerkt, en er is een duidelijke indicatie dat de api gecached is
- Na het runnen van de code block en 10 min erna laten de visuals nog steeds dezelfde data zien, wat aangeeft dat de api correct gecached is
- Na het runnen van de code block en binnen een uur laten de visuals nog steeds dezelfde data zien, wat bevestigt dat de api correct gecached is en dat er geen nieuwe data is opgehaald binnen die tijd

---

## Case 3: Columns van de API

### 1. Testscenario
De gebruiker test doormiddel van de csv file(https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_1.csv) of de columns van de API correct worden opgehaald en verwerkt.

### 2. Testdata
- open ded csv file en controleer of de columns die worden opgehaald in verzamelen.ipynb overeenkomen met de columns die in de csv file staan
- de gebruiker kijkt of de aantal weergegeven columns in de csv file overeenkomen met het aantal columns dat wordt opgehaald in verzamelen.ipynb
- doormiddel van de csv of columns lijst kijken of de data types kloppen met wat er in de csv file staat en wat er in de code block staat


### 3. Verwacht resultaat
- alle columns die worden opgehaald in verzamelen.ipynb komen overeen met de columns die in de csv file staan
- het aantal weergegeven columns in de csv file komen overeen met het aantal columns dat wordt opgehaald in verzamelen.ipynb
- door het runnen van de code block en het vergelijken van de data types in de csv file en de code block, wordt bevestigd dat de data types correct zijn opgehaald en verwerkt
