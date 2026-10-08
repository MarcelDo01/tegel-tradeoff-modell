# Tegel im Tausch

**Setzen. Tauschen. Folgen sichtbar machen.**

Dieses Repository dokumentiert unser physisches und datenbasiertes Modell für das ehemalige Flughafengelände Berlin-Tegel. Das Modell umfasst 22 Zonen. Auf jeder Zone liegt genau ein Nutzungsbaustein, der im Verlauf des Modells gegen eine andere Nutzung ausgetauscht werden kann.

![Physisches Modell auf der Grundkarte; Präsentation, Folie 10](docs/assets/modell_gesamt.png)

Ziel ist es, Nutzungskonflikte und mögliche Folgen räumlicher Entscheidungen verständlich zu machen. Das Modell richtet sich insbesondere an Kinder, jüngere Menschen und Interessierte ohne planerisches Fachwissen. Es berechnet keine optimale Planung, keine Flächenbilanz und keine Punktzahl.

## Spielanleitung

- [Spielanleitung als Text](SPIELANLEITUNG.md)
- Spielanleitung als Heft zum Blättern: `spielanleitung-heft.html` herunterladen und im Browser öffnen. Das Heft enthält eine Seite, auf der sich Tausche ausprobieren lassen.

Die Spielanleitung ist für alle Regeln maßgeblich.

## Dokumentation und Materialien

- [Technische Dokumentation](docs/technische-dokumentation.md) und [PDF-Fassung](docs/technische-dokumentation.pdf)
- [Modellregeln in Kurzform](model/modellregeln.md)
- [Tauschmatrix](model/tauschmatrix.md)
- [Zonendaten](data/README.md), [Excel-Datei](data/zones.xlsx), [CSV-Export](data/zones.csv) und [Data Dictionary](data/data_dictionary.md)
- [Quellen und Herkunft der Abbildungen](references/quellen.md)
- [KI-Verzeichnis](docs/ki-verzeichnis.md)
- [Abschlusspräsentation](presentation/abschlussprasentation.pdf)
- [Archivierter Website-Prototyp](docs/prototyp/tegel-im-tausch-prototyp.html)

Der Website-Prototyp zeigt einen frühen Arbeitsstand mit anderen Regeln. Er ist nicht mehr gültig.

## So funktioniert ein Zug

„Tegel im Tausch“ ist ein Einzelspiel ohne Punkte, ohne Gewinner und ohne festes Ende.

1. Eine Zone auswählen. Ihr Baustein zeigt die Nutzung, die da ist.
2. Die neue Nutzung wählen.
3. Den alten Baustein in die Verlust-Box legen und den neuen auf die Zone setzen. Bausteine werden nie gestapelt.
4. Die Tauschmatrix lesen: Spalte „ist da“, Zeile „wird zu“.
5. Die Marker bewegen.
6. Auf die Karte und in die Verlust-Box schauen.

Die Zeichen der Matrix:

- `+`: Der Marker wird verdrängt und kommt vom alten Baustein in die Verlust-Box.
- `−`: Der Marker kommt auf den neuen Baustein, aus der Verlust-Box oder sonst aus der Tauschbox.
- `0`: Nichts bewegt sich.

Versiegelung und Entsiegelung sind Aufwand. Wird grüner Boden bebaut, kommt ein Versiegelungsmarker (VSM) in die Verlust-Box. Wird bebauter Boden wieder grün, kommt ein Entsiegelungsmarker (ESM) dazu. Beide bleiben für den Rest des Spiels dort.

## Nutzungen

Die Tauschmatrix unterscheidet fünf vereinfachte Nutzungen:

- Koppel
- Grünanlage
- Wohnen
- Gewerbe
- Erholung/Freizeit

Alle 25 gerichteten Kombinationen sind im Modell erlaubt. Gleiche Ausgangs- und Zielnutzung ergibt `0`. Diese Modellregel ist keine Aussage über die reale planerische oder rechtliche Zulässigkeit einer Nutzung.

## Zonendaten

Die aktuelle Zonenzuweisung enthält 22 eindeutig nummerierte Zonen und zehn vollständig befüllte Merkmale pro Zone. Die Excel-Datei ist die Arbeitsgrundlage; die CSV-Fassung erleichtert Versionsvergleich und Weiterverarbeitung. Geometrien, Flächengrößen und quantitative Wirkungen sind nicht enthalten.

## Repository-Struktur

| Ort | Inhalt |
|---|---|
| `SPIELANLEITUNG.md` | Spielanleitung als Text |
| `spielanleitung-heft.html` | Spielanleitung als blätterbares Heft |
| `docs/` | technische Dokumentation, PDF-Fassung, Abbildungen, KI-Verzeichnis und archivierter Prototyp |
| `data/` | Excel-Datei, CSV-Export und Beschreibung der 22 Zonen |
| `model/` | Modellregeln in Kurzform und 25 gerichtete Nutzungstausche |
| `presentation/` | Abschlusspräsentation |
| `references/` | Quellen und Herkunftsnachweise |
| `tools/` | Skripte zum Erzeugen des PDF und des Hefts |

## Team

Thao Trang Le (Anny), Linda Izadi Sharifbad, Fatih Koc und Marcel Do

Alle Rechte vorbehalten; siehe [Rechtehinweis](LICENSE).
