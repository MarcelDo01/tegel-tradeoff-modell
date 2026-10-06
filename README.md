# Setzen. Tauschen. Folgen sichtbar machen.

Dieses Repository dokumentiert unser physisches und datenbasiertes Modell für das ehemalige Flughafengelände Berlin-Tegel. Das Modell umfasst 22 Zonen. Auf jeder Zone liegt genau ein Nutzungsbaustein, der im Verlauf des Modells gegen eine andere Nutzung ausgetauscht werden kann.

![Physisches Modell auf der Grundkarte; Präsentation, Folie 10](docs/assets/modell_gesamt.png)

Ziel ist es, Nutzungskonflikte und mögliche Folgen räumlicher Entscheidungen verständlich zu machen. Das Modell richtet sich insbesondere an Kinder, jüngere Menschen und Interessierte ohne planerisches Fachwissen. Es berechnet keine optimale Planung, keine Flächenbilanz und keine Punktzahl.

## Dokumentation und Materialien

- [Technische Dokumentation](docs/technische-dokumentation.md) und [PDF-Fassung](docs/technische-dokumentation.pdf)
- [Modellregeln](model/modellregeln.md)
- [Tauschmatrix](model/tauschmatrix.md)
- [Zonendaten](data/README.md), [Excel-Datei](data/zones.xlsx), [CSV-Export](data/zones.csv) und [Data Dictionary](data/data_dictionary.md)
- [Quellen und Herkunft der Abbildungen](references/quellen.md)
- [KI-Verzeichnis](docs/ki-verzeichnis.md)
- [Abschlusspräsentation](presentation/abschlussprasentation.pdf)
- [Archivierter Website-Prototyp](docs/prototyp/tegel-im-tausch-prototyp.html)

Der Website-Prototyp zeigt einen frühen Arbeitsstand. Für die aktuelle Spielmechanik sind ausschließlich die Modellregeln und die Tauschmatrix in diesem Repository maßgeblich.

## So funktioniert ein Modellzug

1. Mit dem festgelegten Ausgangsaufbau beginnen und eine Zone auswählen.
2. Eine neue Nutzung bestimmen und den passenden Nutzungsbaustein aus der Tauschbox oder der Verlust-Box nehmen.
3. Den bisherigen Nutzungsbaustein von der Zone entfernen und in die Verlust-Box legen.
4. Den neuen Nutzungsbaustein auf die Zone setzen. Bausteine werden ausgetauscht und nicht gestapelt.
5. Die gerichtete Regel in der Tauschmatrix ablesen.
6. Die genannten Marker zwischen Tauschbox und Verlust-Box bewegen.
7. Die sichtbaren Veränderungen und Nutzungskonflikte gemeinsam besprechen.

Auf der Karte liegen ausschließlich Nutzungsbausteine. Akteursmarker sowie VSM, ESM, NSM und DMS befinden sich immer in einer der beiden Boxen.

- `+ Marker`: aus der Tauschbox in die Verlust-Box
- `− Marker`: aus der Verlust-Box zurück in die Tauschbox
- `0`: keine Markerbewegung

Elemente aus der Verlust-Box dürfen bei späteren Tauschen erneut verwendet werden. Ihr Inhalt zeigt deshalb den aktuellen Modellzustand und nicht die gesamte Geschichte aller Tausche.

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

| Ordner | Inhalt |
|---|---|
| `docs/` | technische Dokumentation, PDF-Fassung, Abbildungen, KI-Verzeichnis und archivierter Prototyp |
| `data/` | Excel-Datei, CSV-Export und Beschreibung der 22 Zonen |
| `model/` | Modellregeln und 25 gerichtete Nutzungstausche |
| `presentation/` | Abschlusspräsentation |
| `references/` | Quellen und Herkunftsnachweise |

## Team

Thao Trang Le (Anny), Linda Izadi Sharifbad, Fatih Koc und Marcel Do

Eine Veröffentlichungslizenz wurde noch nicht gewählt; siehe [Rechtehinweis](LICENSE).
