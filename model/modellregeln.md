# Modellregeln und Markerlogik

## Ziel des Modells

Das Modell zeigt, welche Folgen eine veränderte Flächennutzung haben kann. Eine bestehende Nutzung wird gegen eine neue Nutzung ausgetauscht. Die dabei verdrängten Bausteine und Marker werden in der Verlust-Box sichtbar.

Es gibt keine Punktzahl und keine optimale Lösung. Nach jedem Tausch werden die Veränderungen gemeinsam besprochen.

## Bestandteile

Das Modell besteht aus:

- einer Karte mit den Zonen,
- Nutzungsbausteinen,
- Akteursmarkern,
- VSM-, ESM-, NSM- und DMS-Markern,
- einer Tauschbox,
- einer Verlust-Box,
- der Tauschmatrix.

Auf der Karte liegen ausschließlich die Nutzungsbausteine. Akteurs- und Ereignismarker befinden sich immer in einer der beiden Boxen.

## Die beiden Boxen

### Tauschbox

In der Tauschbox befinden sich die Bausteine und Marker, die aktuell verfügbar sind.

Der Inhalt der Tauschbox zählt nicht als Verlust.

### Verlust-Box

In der Verlust-Box befinden sich die Bausteine und Marker, die durch die bisherigen Tausche verdrängt wurden.

Die Elemente in der Verlust-Box dürfen später wieder verwendet werden. Sobald ein Baustein oder Marker aus der Verlust-Box entnommen wird, zählt er nicht mehr als aktueller Verlust.

Die Verlust-Box zeigt deshalb den aktuellen Zustand und nicht die gesamte Geschichte aller vorherigen Tausche.

## Vorbereitung

1. Die Karte wird mit dem festgelegten Ausgangszustand aufgebaut.
2. Auf jeder Zone liegt der zugehörige Nutzungsbaustein.
3. Alle übrigen Bausteine und Marker werden auf die Tauschbox und die Verlust-Box verteilt.
4. Die beiden Boxen werden klar voneinander getrennt aufgestellt.
5. Die Tauschmatrix wird gut sichtbar bereitgelegt.

## Ablauf eines Tauschs

### 1. Zone auswählen

Eine Zone auf der Karte wird ausgewählt. Der dort liegende Nutzungsbaustein zeigt die aktuelle Nutzung.

### 2. Neue Nutzung auswählen

Ein neuer Nutzungsbaustein wird aus der Tauschbox oder aus der Verlust-Box genommen.

### 3. Alten Baustein entfernen

Der bisherige Nutzungsbaustein wird von der ausgewählten Zone genommen und in die Verlust-Box gelegt.

### 4. Neuen Baustein einsetzen

Der neue Nutzungsbaustein wird auf die Zone gelegt.

In jeder Zone liegt immer nur ein Nutzungsbaustein. Bausteine werden ausgetauscht und nicht übereinandergestapelt.

### 5. Tauschmatrix lesen

In der Tauschmatrix wird die Regel für den Wechsel von der bisherigen zur neuen Nutzung gesucht.

- Die Zeile steht für die bisherige Nutzung.
- Die Spalte steht für die neue Nutzung.
- Gleiche Ausgangs- und Zielnutzung ergibt `0`.

### 6. Marker zwischen den Boxen bewegen

Die Tauschmatrix legt fest, welche Akteurs- und Ereignismarker zwischen den beiden Boxen bewegt werden.

Die Zeichen haben für alle Marker dieselbe Bedeutung:

- `+ Marker`: Den genannten Marker aus der Tauschbox nehmen und in die Verlust-Box legen.
- `− Marker`: Den genannten Marker aus der Verlust-Box nehmen und zurück in die Tauschbox legen.
- `0`: Es wird kein Marker bewegt.

Diese Regel gilt für:

- Tiere,
- Pflanzen,
- Besucher,
- Anwohner,
- Beschäftigte,
- VSM,
- ESM,
- NSM,
- DMS,
- alle weiteren Marker der Tauschmatrix.

Marker werden niemals auf die Karte gelegt.

Ist ein benötigter Marker nicht in der vorgesehenen Box vorhanden, wird kein negativer Bestand erzeugt. Die fehlende Verfügbarkeit wird notiert und der Modellzug wird gemeinsam besprochen.

### 7. Ergebnis besprechen

Nach dem Tausch wird gemeinsam betrachtet:

- Welche Nutzung befindet sich jetzt in der Zone?
- Welcher Nutzungsbaustein wurde verdrängt?
- Welcher Baustein wurde aus der Verlust-Box zurückgeholt?
- Welche Marker wurden in die Verlust-Box gelegt?
- Welche Marker wurden aus der Verlust-Box entfernt?
- Welche Folgen und Nutzungskonflikte macht der Tausch sichtbar?

## Beispiel: Grünanlage zu Wohnen

1. Eine Zone mit Grünanlage wird ausgewählt.
2. Der Wohnbaustein wird aus der Tauschbox oder Verlust-Box genommen.
3. Der Grünanlagenbaustein wird von der Karte genommen und in die Verlust-Box gelegt.
4. Der Wohnbaustein wird auf die Zone gesetzt.
5. Die Regel für Grünanlage zu Wohnen wird in der Tauschmatrix gelesen.
6. Steht dort beispielsweise `+ VSM`, wird ein VSM aus der Tauschbox in die Verlust-Box gelegt.
7. Anschließend werden der neue Zustand und die sichtbaren Folgen besprochen.

## Wichtige Regeln

- Auf jeder Zone liegt genau ein Nutzungsbaustein.
- Nutzungsbausteine werden ausgetauscht und nicht gestapelt.
- Neue Bausteine dürfen aus beiden Boxen genommen werden.
- Der entfernte Baustein kommt in die Verlust-Box.
- Bausteine und Marker aus der Verlust-Box dürfen später wiederverwendet werden.
- Der Inhalt der Tauschbox zählt nicht als Verlust.
- Marker liegen niemals auf der Karte.
- `+` bedeutet Bewegung in die Verlust-Box.
- `−` bedeutet Bewegung aus der Verlust-Box zurück in die Tauschbox.
- Gleiche Ausgangs- und Zielnutzung ergibt `0`.
- Alle in der Tauschmatrix enthaltenen Kombinationen sind im Modell erlaubt.
- Die Marker zeigen qualitative Veränderungen. Sie bilden keine wissenschaftliche Umweltbilanz und keine rechtliche Bewertung.

## Begriffe

- **VSM:** Versiegelungsmarker
- **ESM:** Entsiegelungsmarker
- **NSM:** Naturschutzmarker
- **DMS:** Denkmalschutzmarker
- **NSG:** Naturschutzgebiet

NSG und NSM haben unterschiedliche Bedeutungen. Ein Marker erzeugt keinen rechtlichen Schutzstatus und bestätigt keine planerische Zulässigkeit.
