# Daten zum Spiel

Die Dateien in diesem Ordner beschreiben, wie das Spiel aufgebaut wird, wie ein Tausch wirkt und auf welche Planungsgrundlagen sich das Spiel stützt.

## Dateien

| Datei | Inhalt |
|---|---|
| `startaufbau.csv` | ein Eintrag je Feld mit Baustein: Startbaustein, Marker, Denkmalschutz und Merkmale aus den Planungsunterlagen |
| `startaufbau.xlsx` | dieselbe Tabelle als Excel-Datei |
| `tauschmatrix.csv` | die 20 Nutzungswechsel mit ihren Markerbewegungen |
| `belege.csv` | für jeden Marker und die Aufwandsregeln eine Belegstelle aus Planungsunterlagen und öffentlichen Quellen |
| `data_dictionary.md` | Bedeutung der Spalten |

## Startaufbau

Das Spielfeld hat 21 Felder, auf jedem liegt zum Start ein Baustein. Die Nummerierung folgt der Folie über der Grundkarte (Abschlusspräsentation, Folie 6); ein Feld ohne Baustein aus der Planungsphase haben wir nicht übernommen und die Felder ab dort durchgezählt.

| Startbaustein | Felder | Anzahl |
|---|---|---:|
| Koppel | 1, 2, 3, 4, 6, 7, 10 | 7 |
| Grünanlage | 5, 8, 11, 14 | 4 |
| Erholung/Freizeit | 13, 17, 19 | 3 |
| Wohnen | 18, 20, 21 | 3 |
| Gewerbe | 9, 12, 15, 16 | 4 |

Ein Denkmalschutzmarker liegt bei den Gewerbefeldern 9, 15 und 16.

## Benötigte Marker für den Startaufbau

| Marker | Anzahl |
|---|---:|
| Pflanzen | 11 |
| Tiere | 7 |
| Naturschutzmarker (NSM) | 7 |
| Besucher | 7 |
| Beschäftigte | 4 |
| Anwohner | 3 |
| Denkmalschutzmarker (DMS) | 3 |

Dazu kommen Vorräte in der Tauschbox, vor allem Versiegelungs- und Entsiegelungsmarker (VSM, ESM) sowie Ersatzmarker. Der Prototyp enthält aus Budgetgründen fünf Marker je Sorte und reicht für den vollständigen Startaufbau nicht aus.

## Merkmale aus den Planungsunterlagen

Für jedes Feld haben wir festgehalten, in welchem Teilgebiet es liegt und was die Planungsunterlagen dort zeigen:

- **Gebiet und Bebauungsplan:** Geltungsbereiche der Bebauungspläne, EPK Abbildung 3 (S. 9).
- **Flächennutzungsplan:** EPK Kapitel 3.1.1 (S. 17) und Ausschnitt aus dem Flächennutzungsplan.
- **Geschützte Biotope:** Biotoptypenkarte, EPK Abbildung 24 (S. 31).
- **Naturschutzgebiet (Entwurf):** Entwurf der Grenze, EPK Abbildung 81 (S. 105).
- **Versiegelung im Bestand:** EPK Kapitel 4.1.1 (S. 25) und Luftbild.

Die Felder haben keine Koordinaten. Wir haben die Folie mit dem Auge über die Karten gelegt. Die Werte gelten deshalb für das Teilgebiet, in dem ein Feld liegt, und nicht für die genaue Fläche.

Der Abgleich zeigt, dass der Startaufbau der Planung folgt:

| Gebiet | Felder | Startbausteine |
|---|---|---|
| Tegeler Stadtheide, geplantes Naturschutzgebiet | 1, 2, 3, 4, 6, 7, 10 | alle sieben Koppeln |
| Landebahn und Nordfuge, laut EPK für Sport und Freizeit vorgesehen | 5, 8, 11, 14 | alle vier Grünanlagen |
| Landschaftspark | 13, 17 | Erholung/Freizeit |
| Urban Tech Republic | 9, 12, 15, 16, 18 | vier Gewerbebausteine, ein Wohnbaustein |
| Schumacher Quartier | 19, 20, 21 | zwei Wohnbausteine, eine Erholungsfläche |

Abweichungen von der Planung gibt es bei Feld 18 (Wohnen im Gebiet der Urban Tech Republic) und Feld 19 (Erholung im Schumacher Quartier).

## Herkunft und Grenzen

Die Zuordnung der Bausteine zu den Feldern haben wir aus der nummerierten Folie und dem Foto des Ausgangsaufbaus (Folie 10) abgeleitet. Die Felder sind Modellfelder und keine amtlichen Flächen. Die Tabelle enthält keine Flächengrößen, Koordinaten oder Messwerte. Die Belege stützen die Regeln qualitativ; ein Marker steht für eine Art von Betroffenheit und nicht für eine bestimmte Menge.

## Quellen

- Senatsverwaltung für Umwelt, Mobilität, Verbraucher- und Klimaschutz (2022): Entwicklungs- und Pflegekonzept für die Tegeler Stadtheide. Bearbeitung: gruppe F, Berlin. Seitenangaben beziehen sich auf die PDF-Fassung.
- Grün Berlin GmbH (2026): Landschaftsraum der Tegeler Stadtheide. Vorstellung des Betriebs und zukünftige Entwicklung. Präsentation, R. Hain.
- Grün Berlin GmbH (2026): Digital Greencare. Landschaftspark der Tegeler Stadtheide. Präsentation, R. Hain, 22.04.2026.
- entwicklungsstadt.de (2026): Nach Jahren der Planung: Auf dem Flughafen Tegel beginnt der Wohnungsbau. 07.08.2026.
- Landesdenkmalamt Berlin (2019): Newsletter Mai 2019.
- FUTR HUB Geoportal Berlin TXL: Kartenebenen Versiegelung 2021, Flächennutzungsplan, Landschaftsprogramm, Denkmalkarte, Orthophotos.
