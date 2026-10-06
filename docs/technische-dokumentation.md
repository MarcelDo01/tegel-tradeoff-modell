# Setzen. Tauschen. Folgen sichtbar machen.

Technische Dokumentation des physischen Tegel-Modells
Stand: 6. Oktober 2026

Team: Thao Trang Le (Anny), Linda Izadi Sharifbad, Fatih Koc und Marcel Do

## 1. Projekt und Zielsetzung

Flächen wirken in Planungsprozessen mitunter frei oder ungenutzt. Tatsächlich erfüllen sie bereits ökologische, räumliche und gesellschaftliche Funktionen. Eine neue Nutzung kann Wohnraum, Arbeitsplätze oder Freizeitangebote schaffen und zugleich andere Funktionen verändern oder verdrängen.

Mit unserem physischen, datenbasierten Modell machen wir solche Nutzungskonflikte anschaulich. Eine Zone wird ausgewählt, ihre Nutzung verändert und die daraus entstehenden Markerbewegungen werden gemeinsam besprochen. Im Mittelpunkt steht das Verständnis von Zielkonflikten, nicht die Ermittlung einer optimalen Planung.

Das Modell richtet sich vor allem an Kinder, jüngere Menschen und Interessierte ohne planerisches Fachwissen. Es vereinfacht komplexe Zusammenhänge und schafft einen Gesprächsanlass. Die Regeln liefern keine räumliche Prognose, Umweltbilanz oder rechtliche Bewertung.

## 2. Untersuchungsgebiet und Zonierung

Betrachtet wird das gesamte Gelände des ehemaligen Flughafens Berlin-Tegel, nicht ausschließlich die Tegeler Stadtheide. Für das Modell wurde das Gebiet in 22 Zonen gegliedert.

![Zonendarstellung aus der Präsentation, Folie 2](assets/zonierung.png)

Die Zonierung entstand durch den Vergleich verschiedener Karteninformationen. Berücksichtigt wurden insbesondere Naturschutz, Biotop- und Artenschutz, Erholung und Freiraumnutzung, Denkmalschutz, Versiegelung, bestehende und geplante Nutzungen sowie die Projektgrenze.

Wir haben die Zonengrenzen manuell entwickelt und zusätzlich an die rechteckigen Grundplatten der physischen Bausteine angepasst. Die Zonen sind deshalb projektbezogene Modelleinteilungen und keine amtlichen Verwaltungs-, Schutzgebiets- oder Planungseinheiten.

## 3. Datengrundlagen

### 3.1 Externe Karten- und Konzeptgrundlagen

Für die räumliche Einordnung und die Entwicklung der Zonierung wurden folgende Ebenen im FUTR HUB Geoportal verwendet:

- Versiegelung 2021
- LaPro Beschlussfassung: Erholung und Freiraumnutzung
- LaPro Beschlussfassung: Biotop- und Artenschutz
- Flächennutzungsplan, aktuelle Arbeitskarte
- Denkmalkarte Berlin
- Digitale Orthophotos 2025
- Projektgrenze
- Hintergrundkarte farbig

Das Pflege- und Entwicklungskonzept für die Tegeler Stadtheide diente als fachliche Hintergrundgrundlage. Die vollständigen Links und Herkunftsnachweise stehen in [Quellen und Herkunft](../references/quellen.md).

### 3.2 Projektdateien

| Grundlage | Verwendung | Datei |
|---|---|---|
| Abschlusspräsentation | Projektidee, Arbeitsprozess, Modellaufbau, Fotos und Legenden | `presentation/abschlussprasentation.pdf` |
| Whiteboard-Foto | Grundlage der Tauschmatrix | `docs/assets/tauschmatrix_original.jpg` |
| Excel-Arbeitsdatei | Zonenbezeichnungen und Zonenattribute | `data/zones.xlsx` |
| CSV-Export | maschinenlesbare Fassung der Zonendaten | `data/zones.csv` |

Die Quellen wurden als Arbeitsgrundlagen für ein didaktisches Modell verwendet. Aus ihnen werden keine ungeprüften rechtlichen Aussagen abgeleitet.

## 4. Arbeitsprozess und Werkzeuge

Im FUTR HUB Geoportal wurden die relevanten Kartenebenen betrachtet und miteinander verglichen. QGIS wurde genutzt, um das Luftbild zu importieren, den benötigten Ausschnitt festzulegen und die Grundkarte für den Druck im A1-Format vorzubereiten.

Die eigentliche Zonierung erfolgte manuell. Wir haben die Informationen der Kartenebenen verglichen, die Grundkarte ausgedruckt und die Zonengrenzen auf einer transparenten Folie skizziert. Eine automatisierte Zonierung oder weitergehende GIS-Analyse war nicht Bestandteil des finalen Vorgehens.

![Kartenvergleich und Arbeit an der Grundkarte, Präsentation, Folie 6](assets/arbeitsprozess.png)

## 5. Zonendatenmodell

Die Excel-Datei enthält im Tabellenblatt `Tabelle1` 22 Datenzeilen und zehn vollständig befüllte Spalten. Die `zone_id`-Werte reichen ohne Lücken von 1 bis 22. Der CSV-Export bildet denselben Tabellenstand ab; das [Data Dictionary](../data/data_dictionary.md) erläutert die einzelnen Felder.

| Feldgruppe | Spalten | Funktion |
|---|---|---|
| Identifikation | `zone_id` | eindeutige Kennung der Zone |
| räumliche Einordnung | `Hauptkategorie`, `Unterkategorie`, `Aktuelle Nutzung`, `Flächentyp` | Beschreibung des Ausgangskontexts |
| Zugang und Beteiligte | `Zugang`, `Akteure`, `Beweidung` | Hinweise auf Nutzung, Beteiligte und Tierhaltung |
| Schutz und Herkunft | `Schutzstatus`, `Datenquelle` | fachlicher Kontext und projektinterner Quellenhinweis |

Die 22 Zonen verteilen sich auf folgende Hauptkategorien:

| Hauptkategorie | Anzahl |
|---|---:|
| Naturschutzgebiet und natürlicher Lebensraum | 13 |
| Flughafenbestand / Denkmalschutz | 3 |
| Freizeit / Erholung | 5 |
| Wohnen / Quartier | 1 |

16 Zonen sind als eingeschränkt und sechs als öffentlich zugänglich erfasst. Für 13 Zonen ist Beweidung mit `Ja`, für neun mit `Nein` angegeben.

Die Tabellenbegriffe sind nicht automatisch mit den fünf vereinfachten Nutzungen der Tauschmatrix gleichzusetzen. Die Datei enthält keine Geometrien, Flächengrößen, Personenzahlen oder quantitativen Umweltwirkungen.

## 6. Bestandteile des physischen Modells

Das Modell besteht aus:

- einer Karte mit 22 Zonen,
- Nutzungsbausteinen,
- Akteursmarkern,
- VSM-, ESM-, NSM- und DMS-Markern,
- einer Tauschbox,
- einer Verlust-Box,
- der Tauschmatrix.

Auf der Karte liegen ausschließlich die Nutzungsbausteine. Alle Akteurs- und Zusatzmarker befinden sich immer in einer der beiden Boxen.

### 6.1 Nutzungsbausteine

| Kürzel | Nutzung | Vereinfachte Darstellung |
|---|---|---|
| K | Koppel | Koppelbaustein auf dunkelgrünem Boden |
| GA | Grünanlage | hellgrüner Flächenbaustein |
| W | Wohnen | Haus oder Quartier |
| Ge | Gewerbe | Unternehmen oder Bildungseinrichtung |
| Er/Fr | Erholung/Freizeit | Fahrrad |

Jeder Baustein steht für eine Nutzungskategorie. Er repräsentiert keine festgelegte Fläche, Gebäudezahl oder Personenzahl.

### 6.2 Akteurs- und Zusatzmarker

Akteursmarker sind Tiere, Pflanzen, Besucher, Anwohner und Beschäftigte. Zusätzlich verwendet das Modell folgende Kürzel:

| Kürzel | Bedeutung |
|---|---|
| NSM | Naturschutzmarker |
| VSM | Versiegelungsmarker |
| ESM | Entsiegelungsmarker |
| DMS | Denkmalschutzmarker |

NSG bezeichnet ein Naturschutzgebiet und ist nicht mit NSM gleichzusetzen. Kein Marker erzeugt einen rechtlichen Schutzstatus oder bestätigt die planerische Zulässigkeit einer Nutzung.

![Herstellung von Bausteinen und Markern, Präsentation, Folie 7](assets/bausteine_herstellung.png)

## 7. Die beiden Boxen

### 7.1 Tauschbox

In der Tauschbox liegen die aktuell verfügbaren Nutzungsbausteine und Marker. Ihr Inhalt zählt nicht als Verlust.

### 7.2 Verlust-Box

In der Verlust-Box liegen die Nutzungsbausteine und Marker, die durch die bisherigen Tausche verdrängt wurden. Diese Elemente dürfen bei späteren Tauschen erneut verwendet werden.

Wird ein Baustein oder Marker aus der Verlust-Box entnommen, zählt er nicht mehr als aktueller Verlust. Die Box zeigt daher den aktuellen Modellzustand und nicht die vollständige Geschichte aller Tausche.

## 8. Tauschmatrix und Zeichenlogik

Die Tauschmatrix enthält fünf Ausgangs- und fünf Zielnutzungen und damit 25 gerichtete Kombinationen.

- Die Zeile bezeichnet die bisherige Nutzung.
- Die Spalte bezeichnet die neue Nutzung.
- Gleiche Ausgangs- und Zielnutzung ergibt `0`.
- Alle Kombinationen sind im Modell erlaubt.

Die Zeichen beschreiben ausschließlich Bewegungen zwischen den beiden Boxen:

- `+ Marker`: den Marker aus der Tauschbox in die Verlust-Box legen
- `− Marker`: den Marker aus der Verlust-Box zurück in die Tauschbox legen
- `0`: keinen Marker bewegen

Diese Logik gilt für alle Akteurs- und Zusatzmarker. Marker werden niemals auf die Karte gelegt. Ist ein benötigter Marker nicht in der vorgesehenen Box vorhanden, wird kein negativer Bestand erzeugt. Die fehlende Verfügbarkeit wird festgehalten und gemeinsam besprochen.

Die Regeln sind gerichtet: Ein Wechsel von A nach B ist nicht automatisch die genaue Umkehrung des Wechsels von B nach A. Die vollständige [Tauschmatrix](../model/tauschmatrix.md) und ihre [CSV-Fassung](../model/tauschmatrix.csv) sind separat dokumentiert.

## 9. Ablauf eines Modellzugs

1. Mit dem festgelegten Ausgangsaufbau beginnen.
2. Eine Zone auswählen und ihre bisherige Nutzung bestimmen.
3. Eine Zielnutzung wählen und den passenden Nutzungsbaustein aus der Tauschbox oder der Verlust-Box nehmen.
4. Den bisherigen Nutzungsbaustein von der Zone entfernen und in die Verlust-Box legen.
5. Den neuen Nutzungsbaustein auf die Zone setzen. Pro Zone liegt immer genau ein Nutzungsbaustein.
6. Die passende Matrixzelle aus bisheriger Nutzung und Zielnutzung bestimmen.
7. Alle dort genannten Marker nach der `+`- und `−`-Logik zwischen den Boxen bewegen.
8. Die Veränderungen, Nutzungskonflikte und zugrunde liegenden Annahmen gemeinsam besprechen.

Nutzungsbausteine werden ausgetauscht und nicht übereinandergestapelt. Ein Baustein aus der Verlust-Box kann erneut eingesetzt werden; der ausgetauschte Baustein kommt anschließend in die Verlust-Box.

## 10. Beispiele

### 10.1 Grünanlage zu Wohnen

Der Grünanlagenbaustein wird von der Zone genommen und in die Verlust-Box gelegt. Ein Wohnbaustein aus der Tauschbox oder der Verlust-Box wird auf die Zone gesetzt.

Die Matrixzelle lautet:

`+ VSM; + Anwohner; − Pflanzen; − Besucher`

Damit werden VSM und Anwohnermarker aus der Tauschbox in die Verlust-Box gelegt. Pflanzen- und Besuchermarker werden aus der Verlust-Box zurück in die Tauschbox gelegt.

### 10.2 Wohnen zu Grünanlage

Der Wohnbaustein wird von der Zone genommen und in die Verlust-Box gelegt. Ein Grünanlagenbaustein aus der Tauschbox oder der Verlust-Box wird auf die Zone gesetzt.

Die Matrixzelle lautet:

`+ ESM; + Besucher; − VSM; − Anwohner`

Damit werden ESM und Besuchermarker aus der Tauschbox in die Verlust-Box gelegt. VSM und Anwohnermarker werden aus der Verlust-Box zurück in die Tauschbox gelegt.

## 11. Modellannahmen und Grenzen

Die Zonierung ist eine projektbezogene Interpretation und wurde an die physische Darstellbarkeit angepasst. Auch die Nutzungs- und Markerkategorien sind bewusst vereinfacht.

Die Tauschmatrix beschreibt qualitative Modellannahmen. Ein Marker entspricht weder einer bestimmten Fläche noch einer standardisierten Umweltwirkung. Der Inhalt der Verlust-Box darf deshalb nicht als Punktzahl oder quantitative Schadensbilanz interpretiert werden.

Das Modell ist keine GIS-Simulation, ökologische Bilanz, wissenschaftliche Prognose oder rechtliche Prüfung. Es dient dazu, Zusammenhänge und Zielkonflikte sichtbar zu machen und gemeinsam zu diskutieren.

Einzelne Inhalte der Tauschmatrix sind weiterhin fachlich zu prüfen. Diese Punkte sind direkt in der Matrix gekennzeichnet und betreffen nicht die bestätigte Zwei-Box-Mechanik.

## 12. Nachbau und Reproduzierbarkeit

Für einen Nachbau werden eine druckfähige Grundkarte, eine transparente Folie, Nutzungsbausteine, Akteurs- und Zusatzmarker, eine Tauschbox, eine Verlust-Box, die Zonenzuweisung und die Tauschmatrix benötigt.

Der dokumentierte Arbeitsablauf lautet:

1. Kartenebenen und Konzeptgrundlagen auswählen und ihre Datenstände dokumentieren.
2. Luftbild, Versiegelung, Projektgrenze, Schutz- und Nutzungsinformationen vergleichen.
3. Die Grundkarte im benötigten Format vorbereiten und drucken.
4. Die 22 Zonen auf transparenter Folie einzeichnen und mit den Bausteinabmessungen abstimmen.
5. Nutzungsbausteine und Marker gemäß den Legenden herstellen.
6. Karte und beide Boxen nach dem festgelegten Ausgangszustand aufbauen.
7. Die Tauschmatrix bereitlegen und einen Beispielzug durchführen.
8. Die Veränderungen anhand der beiden Boxen gemeinsam auswerten.

Fotos und Präsentationsabbildungen dokumentieren den Aufbau, ersetzen jedoch keine vollständige Maß- oder Stückliste.

## 13. Dokumentationsstand

Die Markdown-Dateien enthalten den aktuellen Text- und Regelstand. Die Tauschmatrix wird zusätzlich als CSV und die Zonenzuweisung als Excel- und CSV-Datei bereitgestellt.

Die Quellen, externen Links und Abbildungsnachweise sind in [Quellen und Herkunft](../references/quellen.md) zusammengefasst. Der Einsatz von KI bei Konzeptentwicklung, Dokumentation, Bildgenerierung und Website-Prototyp ist im [KI-Verzeichnis](ki-verzeichnis.md) beschrieben.
