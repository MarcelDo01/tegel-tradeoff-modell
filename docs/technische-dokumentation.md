# Tegel im Tausch

**Setzen. Tauschen. Folgen sichtbar machen.**

Technische Dokumentation

Stand: 7. Oktober 2026

Team: Thao Trang Le (Anny), Linda Izadi Sharifbad, Fatih Koc und Marcel Do

## 1. Projekt und Zielsetzung

Flächen wirken in Planungsprozessen mitunter frei oder ungenutzt. Tatsächlich erfüllen sie bereits ökologische, räumliche und gesellschaftliche Funktionen. Eine neue Nutzung kann Wohnraum, Arbeitsplätze oder Freizeitangebote schaffen und zugleich andere Funktionen verändern oder verdrängen.

Mit unserem physischen, datenbasierten Modell machen wir solche Nutzungskonflikte anschaulich. Eine Zone wird ausgewählt und ihre Nutzung verändert. Die daraus entstehenden Markerbewegungen zeigen, was die Entscheidung verdrängt und welchen Aufwand sie verursacht. Im Mittelpunkt steht das Verständnis von Zielkonflikten, nicht die Ermittlung einer optimalen Planung.

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

Das Entwicklungs- und Pflegekonzept (EPK, 2022) für die Tegeler Stadtheide diente als fachliche Hintergrundgrundlage. Die vollständigen Links und Herkunftsnachweise stehen in [Quellen und Herkunft](../references/quellen.md).

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
| Freizeit / Erholung | 4 |
| Wohnen / Quartier | 2 |

16 Zonen sind als eingeschränkt und sechs als öffentlich zugänglich erfasst. Für 13 Zonen ist Beweidung mit `Ja`, für neun mit `Nein` angegeben.

Die Tabellenbegriffe sind nicht automatisch mit den fünf vereinfachten Nutzungen der Tauschmatrix gleichzusetzen. Die Datei enthält keine Geometrien, Flächengrößen, Personenzahlen oder quantitativen Umweltwirkungen.

## 6. Bestandteile des physischen Modells

Das Modell besteht aus:

- einer Karte mit 22 Zonen,
- Nutzungsbausteinen,
- Akteursmarkern,
- Naturschutz- und Denkmalschutzmarkern (NSM, DMS),
- Aufwandsmarkern für Versiegelung und Entsiegelung (VSM, ESM),
- einer Tauschbox,
- einer Verlust-Box,
- der Tauschmatrix.

Auf jeder Zone liegt genau ein Nutzungsbaustein. Auf dem Baustein liegen die Marker, die zu seiner Nutzung gehören. VSM und ESM liegen nie auf der Karte.

### 6.1 Nutzungsbausteine

| Kürzel | Nutzung | Boden | Aufsatz |
|---|---|---|---|
| K | Koppel | dunkelgrün | – |
| GA | Grünanlage | hellgrün | – |
| W | Wohnen | weiß | Haus |
| Ge | Gewerbe | weiß | Tonblöcke |
| Er/Fr | Erholung/Freizeit | weiß | Fahrrad |

Der Boden zeigt die Versiegelung. Dunkelgrüner Boden steht für Naturschutz und natürlichen Lebensraum mit Koppeln für Tiere und ohne Zugang für Besucher. Hellgrüner Boden steht für Grünflächen mit Besucherzugang und ohne Weidetiere. Weißer Boden steht für betonierten Boden als Grundlage für Wohnen, Gewerbe und Erholung/Freizeit.

Jeder Baustein steht für eine Nutzungskategorie. Er repräsentiert keine festgelegte Fläche, Gebäudezahl oder Personenzahl.

### 6.2 Marker

| Marker | Kürzel | Liegt zum Start auf |
|---|---|---|
| Tiere | – | Koppel |
| Pflanzen | – | Koppel, Grünanlage |
| Naturschutzmarker | NSM | Koppel |
| Besucher | – | Grünanlage, Erholung/Freizeit |
| Anwohner | – | Wohnen |
| Beschäftigte | – | Gewerbe |
| Denkmalschutzmarker | DMS | drei Gewerbebausteinen |
| Versiegelungsmarker | VSM | keinem Baustein, Tauschbox |
| Entsiegelungsmarker | ESM | keinem Baustein, Tauschbox |

NSG bezeichnet ein Naturschutzgebiet und ist nicht mit NSM gleichzusetzen. Kein Marker erzeugt einen rechtlichen Schutzstatus oder bestätigt die planerische Zulässigkeit einer Nutzung.

![Herstellung von Bausteinen und Markern, Präsentation, Folie 7](assets/bausteine_herstellung.png)

### 6.3 Ausgangsaufbau

Der Ausgangsaufbau der Bausteine folgt dem Foto des Modells. Die Marker werden nach der Tabelle in Abschnitt 6.2 auf die Bausteine gelegt. Alle VSM und ESM und alle übrigen Bausteine und Marker liegen in der Tauschbox. Die Verlust-Box ist leer.

![Ausgangsaufbau des Modells, Präsentation, Folie 10](assets/modell_gesamt.png)

Das Foto zeigt einen früheren Stand des Prototyps. Die meisten Marker liegen dort noch nicht auf den Bausteinen, und ein Baustein für Erholung/Freizeit trägt eine Bank, die inzwischen durch ein Fahrrad ersetzt wurde. Der Prototyp enthält aus Budgetgründen fünf Marker je Sorte.

## 7. Die beiden Boxen

### 7.1 Tauschbox

Die Tauschbox ist der Vorrat. In ihr liegen alle Bausteine und Marker, die gerade nicht im Spiel sind.

### 7.2 Verlust-Box

Die Verlust-Box ist die „Hand“ der spielenden Person. Sie ist zum Start leer. In ihr landet alles, was durch einen Tausch von der Karte verdrängt wird, sowie der Aufwand für Versiegelung und Entsiegelung.

Bausteine und Akteursmarker aus der Verlust-Box können durch einen späteren Tausch wieder auf die Karte kommen. VSM, ESM und DMS bleiben dauerhaft in der Verlust-Box.

## 8. Tauschmatrix und Zeichenlogik

Die Tauschmatrix enthält fünf Ausgangs- und fünf Zielnutzungen und damit 25 gerichtete Kombinationen.

- Die Spalte bezeichnet die Nutzung, die da ist.
- Die Zeile bezeichnet die Nutzung, zu der die Fläche wird.
- Gleiche Ausgangs- und Zielnutzung ergibt `0`.
- Alle Kombinationen sind im Modell erlaubt.

Die Zeichen haben folgende Bedeutung:

| Zeichen | Bedeutung | Weg |
|---|---|---|
| `+` Akteursmarker, NSM, DMS | wird verdrängt | vom alten Baustein in die Verlust-Box |
| `+` VSM, ESM | Aufwand entsteht | aus der Tauschbox in die Verlust-Box |
| `−` | kommt neu dazu | aus der Verlust-Box, sonst aus der Tauschbox, auf den neuen Baustein |
| `0` | keine Änderung | – |

Versiegelung und Entsiegelung sind als Aufwand modelliert. Jeder Wechsel von grünem zu weißem Boden bringt einen VSM in die Verlust-Box, jeder Wechsel in die Gegenrichtung einen ESM. Beide Marker lassen sich nicht wieder abgeben. Der DMS steht in der Matrix nur mit Plus: Ein verlorenes Denkmal kommt nicht zurück auf die Karte.

Die Regeln sind gerichtet: Ein Wechsel von A nach B ist nicht die Umkehrung des Wechsels von B nach A. Die vollständige [Tauschmatrix](../model/tauschmatrix.md) ist separat dokumentiert.

Die Matrix wurde im Team an einem Whiteboard entwickelt. Gegenüber dem Whiteboard-Foto gelten zwei Festlegungen: Der VSM steht als Aufwandsmarker mit Plus, und die dort eingeklammerten Pflanzen-Einträge gelten.

## 9. Ablauf eines Modellzugs

Das Modell wird als Einzelspiel gespielt. Eine Person gestaltet das Feld nach ihren Vorstellungen. Es gibt kein festes Ende.

1. Eine Zone auswählen. Ihr Baustein zeigt die Nutzung, die da ist.
2. Die neue Nutzung wählen.
3. Den alten Baustein in die Verlust-Box legen und den neuen Baustein auf die Zone setzen. Pro Zone liegt immer genau ein Baustein.
4. Die Matrixzelle aus Spalte „ist da“ und Zeile „wird zu“ bestimmen.
5. Alle dort genannten Marker einmal bewegen.
6. Auf die Karte und in die Verlust-Box schauen.

Neue Bausteine und Minus-Marker werden zuerst aus der Verlust-Box genommen, falls sie dort liegen, sonst aus der Tauschbox. Liegt ein Plus-Marker nicht auf dem Baustein oder ist ein Minus-Marker in keiner Box vorhanden, entfällt dieser Schritt.

Die ausführliche Fassung für Spielende steht in der [Spielanleitung](../SPIELANLEITUNG.md). Sie liegt zusätzlich als blätterbares Heft in `spielanleitung-heft.html` vor.

## 10. Beispiele

### 10.1 Koppel zu Wohnen

Die Matrixzelle in Spalte Koppel und Zeile Wohnen lautet:

`+ VSM; + Tiere; + NSM; + Pflanzen; − Anwohner`

Der Koppelbaustein kommt in die Verlust-Box, ein Wohnbaustein aus der Tauschbox auf die Zone. Tiere, NSM und Pflanzen kommen vom Baustein in die Verlust-Box. Ein VSM kommt aus der Tauschbox in die Verlust-Box. Ein Anwohnermarker aus der Tauschbox kommt auf den Wohnbaustein.

### 10.2 Wohnen zu Grünanlage

Die Matrixzelle in Spalte Wohnen und Zeile Grünanlage lautet:

`+ ESM; + Anwohner; − Pflanzen; − Besucher`

Ein Wohnbaustein kommt in die Verlust-Box, ein Grünanlagenbaustein auf die Zone. Der Anwohnermarker kommt in die Verlust-Box, ein ESM aus der Tauschbox ebenfalls. Der Pflanzenmarker liegt seit dem ersten Beispiel in der Verlust-Box und kommt von dort auf die Grünanlage. Ein Besuchermarker aus der Tauschbox kommt dazu.

Nach beiden Zügen liegen VSM und ESM in der Verlust-Box. Der Aufwand für das Bebauen und das spätere Begrünen bleibt sichtbar.

## 11. Modellannahmen und Grenzen

Die Zonierung ist eine projektbezogene Interpretation und wurde an die physische Darstellbarkeit angepasst. Auch die Nutzungs- und Markerkategorien sind bewusst vereinfacht.

Die Tauschmatrix beschreibt qualitative Modellannahmen. Ein Marker entspricht weder einer bestimmten Fläche noch einer standardisierten Umweltwirkung. Der Inhalt der Verlust-Box darf deshalb nicht als Punktzahl oder quantitative Schadensbilanz interpretiert werden.

Das Modell ist keine GIS-Simulation, ökologische Bilanz, wissenschaftliche Prognose oder rechtliche Prüfung. Es dient dazu, Zusammenhänge und Zielkonflikte sichtbar zu machen und zum Nachdenken und zum Gespräch anzuregen.

## 12. Nachbau und Reproduzierbarkeit

Für einen Nachbau werden eine druckfähige Grundkarte, eine transparente Folie, Nutzungsbausteine, Akteurs- und Zusatzmarker, eine Tauschbox, eine Verlust-Box, die Zonenzuweisung und die Tauschmatrix benötigt.

Der dokumentierte Arbeitsablauf lautet:

1. Kartenebenen und Konzeptgrundlagen auswählen und ihre Datenstände dokumentieren.
2. Luftbild, Versiegelung, Projektgrenze, Schutz- und Nutzungsinformationen vergleichen.
3. Die Grundkarte im benötigten Format vorbereiten und drucken.
4. Die 22 Zonen auf transparenter Folie einzeichnen und mit den Bausteinabmessungen abstimmen.
5. Nutzungsbausteine und Marker gemäß den Legenden herstellen.
6. Karte, Marker und beide Boxen nach dem Ausgangsaufbau in Abschnitt 6.3 aufbauen.
7. Die Tauschmatrix bereitlegen und einen Beispielzug durchführen.
8. Die Veränderungen anhand der Karte und der Verlust-Box auswerten.

Fotos und Präsentationsabbildungen dokumentieren den Aufbau, ersetzen jedoch keine vollständige Maß- oder Stückliste.

## 13. Ergebnisse

Entstanden sind vier Dinge:

- ein physisches Modell des Tegel-Geländes mit Grundkarte, Nutzungsbausteinen, Markern und zwei Boxen,
- eine Tauschmatrix mit 25 gerichteten Nutzungswechseln,
- eine Zonentabelle mit zehn Merkmalen je Zone,
- eine Spielanleitung als Text und als blätterbares Heft mit einer Seite zum Ausprobieren.

Beim Spielen zeigt das Modell vier Zusammenhänge:

- **Jede Nutzung verdrängt eine andere.** Kein Tausch bleibt ohne Eintrag in der Verlust-Box.
- **Aufwand bleibt.** Versiegelung und Entsiegelung hinterlassen Marker, die sich nicht wieder abgeben lassen. Wer eine Fläche bebaut und später wieder begrünt, hat beide in der Verlust-Box.
- **Zurücktauschen stellt den alten Zustand nicht her.** Wird aus Wohnen wieder eine Grünanlage, kommen Pflanzen und Besucher zurück, Tiere und Naturschutz aber nicht.
- **Manches ist endgültig.** Ein abgebauter Denkmalschutzmarker kommt nicht zurück auf die Karte.

## 14. Kritische Auseinandersetzung

### Erprobung

Wir haben das Spiel in drei Situationen durchgespielt: untereinander im Team, mit unserer Betreuerin im CityLAB Berlin und in Beispieldurchgängen vor dem Publikum der Abschlusspräsentation. Unsere Betreuerin zeigte sich begeistert, und ihre Rückmeldungen haben wir aufgenommen. Auch beim Publikum kam das Spiel positiv an.

Mit Kindern haben wir das Spiel noch nicht erprobt. Ob sie die Regeln ohne Begleitung verstehen, ist deshalb offen. Die Altersangabe ab 6 Jahren ist eine Sicherheitsvorgabe: Das Spiel enthält Kleinteile, die verschluckt werden können. Eine inhaltliche Altersgrenze gibt es nicht.

### Erkannte Probleme und unser Umgang damit

- **Übertragung der Tauschmatrix:** Beim Abgleich mit dem Whiteboard-Foto haben wir festgestellt, dass die Matrix in einer früheren Fassung gespiegelt übertragen worden war. Zeilen und Spalten waren vertauscht, sodass jeder Tausch bei seiner Gegenrichtung stand. Wir haben die Matrix korrigiert und Zelle für Zelle gegen das Foto geprüft.
- **Versiegelung und Entsiegelung:** Am Whiteboard standen die beiden Marker mit unterschiedlichen Vorzeichen. Im Spiel ergab das keinen stimmigen Ablauf. Wir haben beide als Aufwandsmarker festgelegt, die in der Verlust-Box bleiben.
- **Anzahl der Marker:** Der Prototyp enthält aus Budgetgründen fünf Marker je Sorte. Bei längeren Partien reichen sie nicht aus, und einzelne Schritte entfallen. Ein vollständiges Spiel braucht so viele Marker, dass jeder Baustein seine Marker tragen kann.

### Grenzen, die bleiben

- **Die Tauschmatrix beruht auf unserer Einschätzung.** Welche Marker bei welchem Wechsel betroffen sind, haben wir im Team hergeleitet. Die Einträge sind nicht empirisch belegt, und andere Gruppen kämen zu anderen Ergebnissen.
- **Jeder Tausch wiegt gleich.** Ein Marker steht für eine Art von Betroffenheit, nicht für eine Menge. Ob eine Zone groß oder klein ist und wie viele Tiere oder Menschen betroffen wären, bildet das Modell nicht ab.
- **Die Zonen folgen den Bausteinen.** Wir haben die Zonengrenzen an die rechteckigen Grundplatten angepasst. Sie entsprechen deshalb nicht genau den realen Flächen.
- **Fünf Nutzungen sind eine starke Vereinfachung.** Mischformen, zum Beispiel Wohnen mit Grünanteil, lassen sich nicht darstellen.

## 15. Eigenleistung und Innovationsgrad

Idee, Regeln und Umsetzung des Modells stammen von uns. Alle Teile haben wir gemeinsam erarbeitet.

- **Idee:** Wir wollten zeigen, dass jede neue Nutzung auf dem Tegel-Gelände etwas Bestehendes verdrängt. Daraus entstand das Prinzip mit Tauschbox und Verlust-Box.
- **Karten und Zonen:** Wir haben die Kartenebenen des Geoportals und das Entwicklungs- und Pflegekonzept ausgewertet und die Informationen zusammengetragen. Daraus haben wir die Zonen hergeleitet. 
- **Regeln und Marker:** Die Tauschmatrix, die Marker und alle Spielregeln haben wir selbst hergeleitet und auf das Spiel übertragen, zunächst am Whiteboard und danach beim Aufbau des Modells.
- **Bau:** Karte, Bausteine und Marker haben wir von Hand hergestellt.
- **Spielanleitung und Dokumentation:** Beide haben wir mit KI-Unterstützung erstellt.

Welche KI-Werkzeuge wir wofür eingesetzt haben, steht im [KI-Verzeichnis](ki-verzeichnis.md).

Neu an unserem Ansatz ist die Form. Planungswerkzeuge für Flächen arbeiten meist digital und berechnen Kennzahlen oder eine beste Lösung. Unser Modell ist zum Anfassen, kommt ohne Punkte und Gewinner aus und macht sichtbar, was eine Entscheidung verdrängt und welchen Aufwand sie hinterlässt. So wird erfahrbar, dass sich ein Eingriff nicht folgenlos zurücknehmen lässt.

## 16. Fazit

Das Modell erreicht sein Ziel: Es macht sichtbar, dass es für das Tegel-Gelände keinen Aufbau gibt, mit dem alle Beteiligten zufrieden sind. Wer spielt, sieht nach wenigen Zügen, dass jede Entscheidung etwas kostet und dass sich ein Eingriff nicht folgenlos zurücknehmen lässt. Dafür braucht es keine Punkte und keinen Gewinner.

Das Modell ersetzt keine Planung. Es vereinfacht stark und beruht auf unseren eigenen Einschätzungen. Seine Stärke liegt darin, einen Zielkonflikt begreifbar zu machen, auch für Menschen ohne Planungswissen.

Als nächste Schritte sehen wir eine Erprobung mit Kindern, einen vollständigen Markersatz und eine eindeutige Zuordnung der Zonen aus den Daten zu den Bausteinen im Startaufbau.

## 17. Quellen und weitere Unterlagen

- **Quellen:** Die verwendeten Kartenebenen, Konzeptgrundlagen und Abbildungsnachweise stehen in [Quellen und Herkunft](../references/quellen.md).
- **KI-Einsatz:** Welche KI-Werkzeuge wir wofür eingesetzt haben, steht im [KI-Verzeichnis](ki-verzeichnis.md).
- **Spielregeln:** Maßgeblich ist die [Spielanleitung](../SPIELANLEITUNG.md). Die [Tauschmatrix](../model/tauschmatrix.md) ist zusätzlich einzeln dokumentiert.
- **Zonendaten:** Die Zonentabelle liegt als [Excel-Datei](../data/zones.xlsx) und als [CSV-Datei](../data/zones.csv) vor; das [Data Dictionary](../data/data_dictionary.md) erläutert die Felder.
