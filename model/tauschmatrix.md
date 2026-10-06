# Tauschmatrix

## Zweck der Matrix

Die Tauschmatrix beschreibt, welche Akteurs- und Zusatzmarker bei einem Nutzungswechsel zwischen der Tauschbox und der Verlust-Box bewegt werden.

Der Austausch des Nutzungsbausteins erfolgt immer zusätzlich zu den Angaben in der Matrix:

1. Den neuen Nutzungsbaustein aus der Tauschbox oder der Verlust-Box nehmen.
2. Den bisherigen Nutzungsbaustein der Zone in die Verlust-Box legen.
3. Den neuen Nutzungsbaustein auf die Zone setzen.
4. Die zugehörigen Marker gemäß der Tauschmatrix bewegen.

Die Marker werden nicht auf die Karte gelegt. Sie befinden sich immer in einer der beiden Boxen.

## Aufbau der Matrix

- Die Zeile bezeichnet die bisherige Nutzung der Zone.
- Die Spalte bezeichnet die neue Nutzung der Zone.
- Die Zelle am Schnittpunkt enthält die Markerbewegungen für diesen Tausch.
- Gleiche Ausgangs- und Zielnutzung ergibt `0`.

Beispiel: Für einen Wechsel von Grünanlage zu Wohnen wird die Zeile `Grünanlage` und die Spalte `Wohnen` gelesen.

## Bedeutung der Zeichen

Die Zeichen haben für alle Akteurs- und Zusatzmarker dieselbe Bedeutung:

- `+ Marker`: Den genannten Marker aus der Tauschbox nehmen und in die Verlust-Box legen.
- `− Marker`: Den genannten Marker aus der Verlust-Box nehmen und zurück in die Tauschbox legen.
- `0`: Es wird kein Marker bewegt.

Ist ein benötigter Marker nicht in der vorgesehenen Box vorhanden, wird kein negativer Bestand erzeugt. Der Marker wird nicht bewegt und die Abweichung wird für die gemeinsame Besprechung festgehalten.

Jede Angabe in einer Matrixzelle wird pro Tausch genau einmal ausgeführt.

## Abkürzungen

- **VSM:** Versiegelungsmarker
- **ESM:** Entsiegelungsmarker
- **NSM:** Naturschutzmarker
- **DMS:** Denkmalschutzmarker

Akteursmarker sind beispielsweise Tiere, Pflanzen, Besucher, Anwohner und Beschäftigte.

## Nutzungswechsel als Matrix

| Bisherige Nutzung | Koppel | Grünanlage | Wohnen | Gewerbe | Erholung/Freizeit |
|---|---|---|---|---|---|
| **Koppel** | 0 | + Besucher; − Tiere; − NSM | + ESM; + Anwohner; − NSM; − Pflanzen; − Tiere | + ESM; + Beschäftigte; + DMS; − NSM; − Tiere; − Pflanzen | + ESM; + Besucher; − NSM; − Tiere |
| **Grünanlage** | + NSM; + Tiere; − Besucher | 0 | + VSM; + Anwohner; − Pflanzen; − Besucher | + ESM; + Beschäftigte; + DMS; − Tiere; − Pflanzen; − Besucher | + ESM; − Pflanzen |
| **Wohnen** | + Tiere; + NSM; + Pflanzen; − Anwohner; − VSM | + ESM; + Besucher; − VSM; − Anwohner | 0 | + Beschäftigte; + DMS; − Anwohner | + Besucher; − Anwohner |
| **Gewerbe** | + NSM; + Tiere; + Pflanzen; − Beschäftigte; − VSM | + Besucher; − VSM; − Beschäftigte | + Anwohner; − Beschäftigte | 0 | + Besucher; − Beschäftigte |
| **Erholung/Freizeit** | + NSM; + Tiere; − Besucher; − VSM | + Pflanzen; − VSM | + Anwohner; − Besucher | + Beschäftigte; + DMS; − Besucher | 0 |

## Nutzungswechsel als Liste

| Ausgang | Ziel | In die Verlust-Box | Aus der Verlust-Box in die Tauschbox |
|---|---|---|---|
| Koppel | Koppel | Keine Änderung | Keine Änderung |
| Koppel | Grünanlage | Besucher | Tiere, NSM |
| Koppel | Wohnen | ESM, Anwohner | NSM, Pflanzen, Tiere |
| Koppel | Gewerbe | ESM, Beschäftigte, DMS | NSM, Tiere, Pflanzen |
| Koppel | Erholung/Freizeit | ESM, Besucher | NSM, Tiere |
| Grünanlage | Koppel | NSM, Tiere | Besucher |
| Grünanlage | Grünanlage | Keine Änderung | Keine Änderung |
| Grünanlage | Wohnen | VSM, Anwohner | Pflanzen, Besucher |
| Grünanlage | Gewerbe | ESM, Beschäftigte, DMS | Tiere, Pflanzen, Besucher |
| Grünanlage | Erholung/Freizeit | ESM | Pflanzen |
| Wohnen | Koppel | Tiere, NSM, Pflanzen | Anwohner, VSM |
| Wohnen | Grünanlage | ESM, Besucher | VSM, Anwohner |
| Wohnen | Wohnen | Keine Änderung | Keine Änderung |
| Wohnen | Gewerbe | Beschäftigte, DMS | Anwohner |
| Wohnen | Erholung/Freizeit | Besucher | Anwohner |
| Gewerbe | Koppel | NSM, Tiere, Pflanzen | Beschäftigte, VSM |
| Gewerbe | Grünanlage | Besucher | VSM, Beschäftigte |
| Gewerbe | Wohnen | Anwohner | Beschäftigte |
| Gewerbe | Gewerbe | Keine Änderung | Keine Änderung |
| Gewerbe | Erholung/Freizeit | Besucher | Beschäftigte |
| Erholung/Freizeit | Koppel | NSM, Tiere | Besucher, VSM |
| Erholung/Freizeit | Grünanlage | Pflanzen | VSM |
| Erholung/Freizeit | Wohnen | Anwohner | Besucher |
| Erholung/Freizeit | Gewerbe | Beschäftigte, DMS | Besucher |
| Erholung/Freizeit | Erholung/Freizeit | Keine Änderung | Keine Änderung |
## Beispiel: Grünanlage zu Wohnen

Die bisherige Nutzung ist Grünanlage. Die neue Nutzung ist Wohnen.

Die entsprechende Matrixzelle enthält:

`+ VSM; + Anwohner; − Pflanzen; − Besucher`

Damit werden folgende Schritte ausgeführt:

1. Einen VSM aus der Tauschbox in die Verlust-Box legen.
2. Einen Anwohnermarker aus der Tauschbox in die Verlust-Box legen.
3. Einen Pflanzenmarker aus der Verlust-Box zurück in die Tauschbox legen.
4. Einen Besuchermarker aus der Verlust-Box zurück in die Tauschbox legen.

Die Marker bleiben in den Boxen und werden nicht auf die Karte gelegt.

## Beispiel: Wohnen zu Grünanlage

Die bisherige Nutzung ist Wohnen. Die neue Nutzung ist Grünanlage.

Die entsprechende Matrixzelle enthält:

`+ ESM; + Besucher; − VSM; − Anwohner`

Damit werden folgende Schritte ausgeführt:

1. Einen ESM aus der Tauschbox in die Verlust-Box legen.
2. Einen Besuchermarker aus der Tauschbox in die Verlust-Box legen.
3. Einen VSM aus der Verlust-Box zurück in die Tauschbox legen.
4. Einen Anwohnermarker aus der Verlust-Box zurück in die Tauschbox legen.

## Regeln für die Anwendung

- Die Matrix wird erst nach dem Austausch des Nutzungsbausteins angewendet.
- Alle Angaben einer Matrixzelle werden einmal ausgeführt.
- Marker werden ausschließlich zwischen den beiden Boxen bewegt.
- Marker werden niemals auf die Karte gelegt.
- Bausteine und Marker aus der Verlust-Box dürfen später erneut verwendet werden.
- Ein aus der Verlust-Box entnommenes Element zählt nicht mehr als aktueller Verlust.
- Der Inhalt der Verlust-Box zeigt den aktuellen Zustand und nicht die gesamte Tauschhistorie.
- Ist ein Marker nicht verfügbar, wird kein Ersatz erfunden und kein negativer Bestand erzeugt.
- Alle in der Matrix enthaltenen Nutzungskombinationen sind im Modell erlaubt.
- Die Matrix beschreibt qualitative Folgen. Sie ist keine wissenschaftliche Umweltbilanz und keine rechtliche Bewertung.

## Quelle

Die Matrix wurde aus dem [Whiteboard-Original](../docs/assets/tauschmatrix_original.jpg) in eine lesbare Tabelle übertragen. Für die Anwendung des Modells ist die in diesem Dokument dargestellte Matrix maßgeblich.
