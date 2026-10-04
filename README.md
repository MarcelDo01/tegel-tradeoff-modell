# Setzen. Tauschen. Folgen sichtbar machen.

Ein physisches, datenbasiertes Modell für das gesamte ehemalige Flughafengelände Berlin-Tegel. Die Projektbeschreibung nennt 22 manuell abgeleitete Zonen; die inzwischen bereitgestellte Zonenzuweisung enthält 23 Einträge. Auf den Zonen lassen sich Nutzungsbausteine austauschen. Akteure, Marker und eine gemeinsame Verlustbox machen sichtbar, was durch eine Entscheidung entsteht und was sich verändert.

![Physisches Modell auf der Grundkarte; Präsentation, Folie 10](docs/assets/modell_gesamt.png)

Das Modell richtet sich besonders an Kinder und jüngere Menschen sowie an Interessierte ohne planerisches Fachwissen. Es vermittelt Nutzungskonflikte und Trade-offs. Es berechnet keine optimale Planung, keine Flächenbilanz und keine Punktzahl.

## Dokumentation und Materialien

- [Technische Dokumentation](docs/technische-dokumentation.md) und [PDF-Fassung](docs/technische-dokumentation.pdf)
- [Modellregeln und vorgeschlagene Markerlogik](model/modellregeln.md)
- [Tauschmatrix mit Bearbeitungsstatus](model/tauschmatrix.md) und [CSV](model/tauschmatrix.csv)
- [Zonendaten](data/README.md), [Original-Excel](data/zones.xlsx), [CSV-Export](data/zones.csv) und [Data Dictionary](data/data_dictionary.md)
- [Originalpräsentation](presentation/abschlussprasentation.pdf)
- [Datenquellen und Herkunft der Abbildungen](references/quellen.md)
- [Offene Punkte](docs/offene-punkte.md)

## Ein Modellzug

Zone wählen → vorhandenen Baustein entfernen → neuen Baustein einsetzen → passende Matrixregel lesen → Akteure und Marker verändern → Folgen über die Box besprechen.

Die Bausteine werden ersetzt, nicht übereinander gestapelt. Alle Nutzungskombinationen sind im Modell erlaubt; daraus folgt keine reale planerische Zulässigkeit.

## Stand: 4. Oktober 2026

Dokumentierte Arbeitsfassung mit der unverändert übernommenen Excel-Zonenzuweisung und einem UTF-8-CSV-Export. Die Datei enthält 23 eindeutige Zonen-IDs, während die Projektbeschreibung und Karte 22 Zonen nennen; diese Abweichung bleibt als offener Abgleich dokumentiert. Die Matrix ist eine vorläufige Transkription mit zwei erläuterten Versiegelungskorrekturen. Vorschläge zur dauerhaften Handhabung der Marker sind ausdrücklich als Vorschläge gekennzeichnet.

## Team

Thao Trang Le (Anny), Linda Izadi Sharifbad, Fatih Koc, Marcel Do. Schreibweise gemäß Titelfolie der Präsentation.

## Repository-Struktur

| Ordner | Inhalt |
|---|---|
| `docs/` | Dokumentation, PDF, Abbildungen und offene Punkte |
| `data/` | Original-Excel, CSV-Export und Beschreibung der Zonenzuweisung |
| `model/` | Regeln und 25 gerichtete Nutzungstausche |
| `maps/` | Hinweise zu Arbeitskarten und Reproduktion |
| `presentation/` | bereitgestellte Abschlusspräsentation |
| `references/` | Quellen und Herkunftsnachweise |
| `tools/` | Erzeugung der PDF aus Markdown; kein Modellalgorithmus |

## PDF aktualisieren

Markdown ist die maßgebliche Textfassung. Mit Python 3 und `reportlab` lässt sich die PDF aus dem Dokumentationstext neu erzeugen:

```bash
python -m pip install -r tools/requirements.txt
python tools/build_pdf.py
```

Der Build ist nur ein Dokumentationswerkzeug. Der zuvor verworfene Python-Ansatz zur räumlichen Datenaufbereitung gehört nicht zum finalen Modellworkflow.

Eine Veröffentlichungslizenz wurde noch nicht gewählt; siehe [Rechtehinweis](LICENSE).
