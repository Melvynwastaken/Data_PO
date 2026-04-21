# UML Diagram lucidchart
- ## waarom de 2 uml diagrammen
![img.png](img.png)
- ## Flowchart 1 - data flow
- Dit proces beschrijft hoe COVID-data via de GitHub API in Jupyter wordt opgehaald, verwerkt en omgezet naar visualisaties. Eerst worden de Python-dependencies geladen, daarna wordt de API bevraagd, de data in een pandas DataFrame gezet en voorbereid voor grafieken. Als de aanvraag slaagt, worden visualisaties getoond; als die faalt, wordt een fout gelogd of opnieuw geprobeerd.
- 
- ## Ethiek
- De ethische aspecten van dit project zijn onder andere: anonimiteit van data,
- transparantie in de gebruikte methoden, 
- en het vermijden van bias in de visualisaties.

- ## privacy
- Het beshouwde data is afkomstig van publieke bronnen en bevat geen persoonlijke informatie,
- waardoor de privacy van individuen gewaarborgd blijft.
- 
- ## security
- De gegeven worden via een api opgehaald en er worden geen gevoelige gegevens opgeslagen of verwerkt,
- waardoor de security risico's minimaal zijn.
![img_1.png](img_1.png)
- ## ERD Diagram
- 
- De stroom is: brondata → import/versiebeheer → locatiegegevens → detailrecords → landensamenvatting → visualisaties.
- DATA_SOURCE → DATASET_VERSION is 1:N omdat één bron meerdere imports/versies kan hebben.
  COUNTRY_SUMMARY → VISUALIZATION is 1:N omdat één samenvatting meerdere soorten visualisaties kan opleveren.
- ## ethiek
De ethiek is van dit diagram niet van toepassing omdat het alleen de structuur van de database weergeeft 
en geen persoonlijke of gevoelige informatie bevat.
 - ## privacy
private data is niet van toepassing omdat er geen persoonlijke gegevens worden opgeslagen of verwerkt in deze database.
- ## security
De security van deze database is afhankelijk van de implementatie en het beheer ervan.
Er is een zoek functie bij een van de visualitaties maar deze is alleen gebaseerd op de data in de database.