# Zonendaten

Die aktuelle Arbeitsdatei liegt als `zones.xlsx` vor. Das Tabellenblatt `Tabelle1` enthält zehn Spalten und 22 Datenzeilen. `zones.csv` bildet denselben Tabellenstand als UTF-8-Datei für Versionsvergleich und Weiterverarbeitung ab.

## Dateien

| Datei | Inhalt |
|---|---|
| `zones.xlsx` | aktuelle Excel-Arbeitsdatei der Zonenzuweisung |
| `zones.csv` | UTF-8-Export von `Tabelle1` mit Komma als Trennzeichen |
| `data_dictionary.md` | Bedeutung, Datentypen und beobachtete Werte der zehn Spalten |

SHA-256 der aktuellen Excel-Datei: `aae6512198033a36385b7ae0aa1fbdd1a500d446271e2ce554971f92c8c2617e`

## Prüfung

- `zone_id` enthält die eindeutigen ganzzahligen Werte 1 bis 22.
- Alle 22 Zeilen und zehn Spalten sind vollständig befüllt.
- Excel- und CSV-Datei enthalten dieselben Zonen und Attribute.
- Die Tabelle enthält keine Flächengrößen, Koordinaten, Personenzahlen oder quantitativen Umweltwirkungen.
- Die Spalte `Datenquelle` benennt projektinterne Quelltypen, aber keine vollständigen Metadaten oder URLs.

## Kurzüberblick

| Hauptkategorie | Zonen | Anzahl |
|---|---|---:|
| Naturschutzgebiet und natürlicher Lebensraum | 1–7, 9, 10, 13–15, 18 | 13 |
| Flughafenbestand / Denkmalschutz | 8, 11, 12 | 3 |
| Freizeit / Erholung | 16, 17, 19, 20 | 4 |
| Wohnen / Quartier | 21,22 | 2 |

Für die vollständige zonenweise Zuordnung sind `zones.xlsx` und `zones.csv` maßgeblich.
