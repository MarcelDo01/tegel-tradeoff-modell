# Zonendaten

Die am 04.10.2026 bereitgestellte Arbeitsdatei liegt unverändert als `zones.xlsx` vor. Das einzige Tabellenblatt `Tabelle1` enthält zehn Spalten und 23 Datenzeilen. `zones.csv` ist ein verlustfreier UTF-8-Export derselben Tabelle für Versionsvergleich und Weiterverarbeitung.

## Dateien

| Datei | Inhalt |
|---|---|
| `zones.xlsx` | unveränderte Originaldatei, ursprünglich `Zonen Zuweisung.xlsx` |
| `zones.csv` | UTF-8-Export von `Tabelle1`, Komma als Trennzeichen, Text bei Bedarf in doppelten Anführungszeichen |
| `data_dictionary.md` | Bedeutung, Datentypen und beobachtete Werte der zehn Spalten |

SHA-256 des Originals und der abgelegten Kopie: `ca3043ec950930373df0f6048b2f7ea2f4a5acd0bb3420f8cf07143e850e21b8`.

## Prüfung

- `zone_id` enthält die eindeutigen ganzzahligen Werte 1 bis 23.
- Alle 23 Zeilen und zehn Spalten sind vollständig befüllt.
- Die Projektbeschreibung und die Zonendarstellung nennen 22 Zonen. Die Tabelle enthält dagegen 23 Einträge. Es wird keine Zeile entfernt oder zusammengelegt, bis die Zuordnung zur Karte geklärt ist.
- Die Tabelle enthält keine Flächengrößen, Koordinaten, Personenzahlen oder quantitativen Umweltwirkungen.
- Die Spalte `Datenquelle` benennt projektinterne Quelltypen, aber keine vollständigen Metadaten oder URLs.

## Kurzüberblick

| Hauptkategorie | Zonen | Anzahl |
|---|---|---:|
| Naturschutzgebiet und natürlicher Lebensraum | 1–7, 9, 10, 13–15, 18 | 13 |
| Flughafenbestand / Denkmalschutz | 8, 11, 12 | 3 |
| Freizeit / Erholung | 16, 17, 19–21 | 5 |
| Wohnen / Quartier | 22, 23 | 2 |

Für die vollständige zonenweise Zuordnung ist `zones.csv` maßgeblich; `zones.xlsx` bleibt der unveränderte Herkunftsnachweis.
