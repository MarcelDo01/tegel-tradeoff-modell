# Tauschmatrix

Die Tauschmatrix legt für jeden Nutzungswechsel fest, welche Marker sich bewegen. Wie ein Zug abläuft, steht in der [Spielanleitung](../SPIELANLEITUNG.md). Sie ist für alle Regeln maßgeblich.

## So wird die Matrix gelesen

- Die **Spalte** bezeichnet die Nutzung, die da ist.
- Die **Zeile** bezeichnet die Nutzung, zu der die Fläche wird.
- Die Zelle am Schnittpunkt enthält die Markerbewegungen für diesen Tausch.
- Gleiche Ausgangs- und Zielnutzung ergibt `0`.

## Bedeutung der Zeichen

| Zeichen | Bedeutung | Weg |
|---|---|---|
| `+` Akteursmarker, NSM, DMS | wird verdrängt | vom alten Baustein in die Verlust-Box |
| `+` VSM, ESM | Aufwand entsteht | aus der Tauschbox in die Verlust-Box, bleibt dort |
| `−` | kommt neu dazu | aus der Verlust-Box, sonst aus der Tauschbox, auf den neuen Baustein |
| `0` | keine Änderung | – |

Jede Angabe einer Zelle wird pro Tausch genau einmal ausgeführt.

## Abkürzungen

- **NSM:** Naturschutzmarker
- **DMS:** Denkmalschutzmarker
- **VSM:** Versiegelungsmarker
- **ESM:** Entsiegelungsmarker

## Nutzungswechsel als Matrix

| wird zu ↓ / ist da → | Koppel | Grünanlage | Wohnen | Gewerbe | Erholung/Freizeit |
|---|---|---|---|---|---|
| **Koppel** | 0 | + Besucher<br>− Tiere<br>− NSM | + ESM<br>+ Anwohner<br>− NSM<br>− Pflanzen<br>− Tiere | + ESM<br>+ Beschäftigte<br>+ DMS<br>− NSM<br>− Tiere<br>− Pflanzen | + ESM<br>+ Besucher<br>− NSM<br>− Tiere<br>− Pflanzen |
| **Grünanlage** | + Tiere<br>+ NSM<br>− Besucher | 0 | + ESM<br>+ Anwohner<br>− Pflanzen<br>− Besucher | + ESM<br>+ Beschäftigte<br>+ DMS<br>− Tiere<br>− Pflanzen<br>− Besucher | + ESM<br>− Pflanzen |
| **Wohnen** | + VSM<br>+ Tiere<br>+ NSM<br>+ Pflanzen<br>− Anwohner | + VSM<br>+ Pflanzen<br>+ Besucher<br>− Anwohner | 0 | + Beschäftigte<br>+ DMS<br>− Anwohner | + Besucher<br>− Anwohner |
| **Gewerbe** | + VSM<br>+ NSM<br>+ Tiere<br>+ Pflanzen<br>− Beschäftigte | + VSM<br>+ Pflanzen<br>+ Besucher<br>− Beschäftigte | + Anwohner<br>− Beschäftigte | 0 | + Besucher<br>− Beschäftigte |
| **Erholung/Freizeit** | + VSM<br>+ NSM<br>+ Tiere<br>+ Pflanzen<br>− Besucher | + VSM<br>+ Pflanzen | + Anwohner<br>− Besucher | + Beschäftigte<br>+ DMS<br>− Besucher | 0 |

## Nutzungswechsel als Liste

| Ist da | Wird zu | In die Verlust-Box (+) | Auf den neuen Baustein (−) |
|---|---|---|---|
| Koppel | Grünanlage | Tiere, NSM | Besucher |
| Koppel | Wohnen | VSM, Tiere, NSM, Pflanzen | Anwohner |
| Koppel | Gewerbe | VSM, NSM, Tiere, Pflanzen | Beschäftigte |
| Koppel | Erholung/Freizeit | VSM, NSM, Tiere, Pflanzen | Besucher |
| Grünanlage | Koppel | Besucher | Tiere, NSM |
| Grünanlage | Wohnen | VSM, Pflanzen, Besucher | Anwohner |
| Grünanlage | Gewerbe | VSM, Pflanzen, Besucher | Beschäftigte |
| Grünanlage | Erholung/Freizeit | VSM, Pflanzen | – |
| Wohnen | Koppel | ESM, Anwohner | NSM, Pflanzen, Tiere |
| Wohnen | Grünanlage | ESM, Anwohner | Pflanzen, Besucher |
| Wohnen | Gewerbe | Anwohner | Beschäftigte |
| Wohnen | Erholung/Freizeit | Anwohner | Besucher |
| Gewerbe | Koppel | ESM, Beschäftigte, DMS | NSM, Tiere, Pflanzen |
| Gewerbe | Grünanlage | ESM, Beschäftigte, DMS | Tiere, Pflanzen, Besucher |
| Gewerbe | Wohnen | Beschäftigte, DMS | Anwohner |
| Gewerbe | Erholung/Freizeit | Beschäftigte, DMS | Besucher |
| Erholung/Freizeit | Koppel | ESM, Besucher | NSM, Tiere, Pflanzen |
| Erholung/Freizeit | Grünanlage | ESM | Pflanzen |
| Erholung/Freizeit | Wohnen | Besucher | Anwohner |
| Erholung/Freizeit | Gewerbe | Besucher | Beschäftigte |

## Regelmäßigkeiten

- **Versiegelung:** Jeder Wechsel von Koppel oder Grünanlage zu Wohnen, Gewerbe oder Erholung/Freizeit bringt einen VSM in die Verlust-Box.
- **Entsiegelung:** Jeder Wechsel in die Gegenrichtung bringt einen ESM in die Verlust-Box.
- **Denkmalschutz:** Der DMS steht nur mit Plus. Er kommt nie zurück auf die Karte.
- **Wechsel innerhalb derselben Bodenart** erzeugen weder VSM noch ESM.

## Herkunft

Die Matrix wurde im Team an einem Whiteboard entwickelt: [Originalfoto](../docs/assets/tauschmatrix_original.jpg). Auf dem Foto stehen die Spalten für „ist da“ und die Zeilen für „wird zu“.

Gegenüber dem Foto haben wir zwei Dinge festgelegt:

1. Der VSM ist wie der ESM ein Aufwandsmarker. Er steht deshalb mit Plus und nicht, wie am Whiteboard, mit Minus.
2. Die am Whiteboard eingeklammerten Pflanzen-Einträge gelten.

Die Matrix beschreibt qualitative Annahmen des Projektteams. Sie ist keine wissenschaftliche Umweltbilanz und keine rechtliche Bewertung.
