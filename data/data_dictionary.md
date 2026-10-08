# Data Dictionary

## startaufbau.csv und startaufbau.xlsx

Eine Zeile je Feld mit Startbaustein, 21 Zeilen. Primärschlüssel ist `feld`.

| Spalte | Typ | Bedeutung | Werte |
|---|---|---|---|
| `feld` | Ganzzahl | Nummer des Felds auf der Karte | 1 bis 22 ohne 10 |
| `lage` | Text | grobe Lage des Felds auf der Karte | zum Beispiel „Nordreihe“ |
| `startbaustein` | Kategorie | Nutzung des Bausteins zum Spielstart | Koppel, Grünanlage, Wohnen, Gewerbe, Erholung/Freizeit |
| `kuerzel` | Kategorie | Kürzel wie in der Tauschmatrix | K, GA, W, Ge, Er |
| `boden` | Kategorie | Farbe des Bodens | dunkelgrün, hellgrün, weiß |
| `versiegelt` | ja/nein | weißer, betonierter Boden im Spiel | ja, nein |
| `marker_start` | Liste | Marker auf dem Baustein zum Start, durch Semikolon getrennt | Tiere, Pflanzen, NSM, Besucher, Anwohner, Beschäftigte |
| `denkmalschutz` | ja/nein | Denkmalschutzmarker beim Baustein zum Start | ja, nein |
| `gebiet` | Kategorie | Teilgebiet des früheren Flughafens | Tegeler Stadtheide, Landschaftspark Tegeler Stadtheide, Landebahn und Nordfuge, Urban Tech Republic, Schumacher Quartier |
| `bebauungsplan` | Text | Bebauungsplan, in dessen Geltungsbereich das Feld liegt | 12-61, 12-51, 12-50, 12-62 |
| `flaechennutzungsplan` | Text | Darstellung im Flächennutzungsplan, soweit abgelesen | Text oder „–“ |
| `geschuetzte_biotope` | Kategorie | geschützte Biotope nach § 30 BNatSchG laut EPK-Biotopkarte | ja, außerhalb der EPK-Kartierung |
| `naturschutzgebiet_entwurf` | ja/nein | innerhalb des Entwurfs der Naturschutzgebietsgrenze | ja, nein |
| `versiegelung_bestand` | Kategorie | Versiegelung heute | überwiegend unversiegelt, teilweise versiegelt, Landebahn teilweise versiegelt, überwiegend versiegelt |
| `bemerkung` | Text | Hinweise zum einzelnen Feld | frei |

Die Spalten von `gebiet` bis `versiegelung_bestand` sind durch Abgleich der Folie mit den Karten im EPK entstanden und gelten für das Teilgebiet, nicht für die genaue Fläche. VSM und ESM kommen in dieser Tabelle nicht vor, weil sie nie auf der Karte liegen.

## tauschmatrix.csv

Eine Zeile je Nutzungswechsel. Wechsel zur gleichen Nutzung fehlen, weil sich dabei nichts bewegt.

| Spalte | Typ | Bedeutung |
|---|---|---|
| `ist_da` | Kategorie | Nutzung, die vor dem Tausch auf dem Feld liegt |
| `wird_zu` | Kategorie | Nutzung, zu der das Feld wird |
| `in_die_verlust_box` | Liste | Marker mit Plus: werden verdrängt oder entstehen als Aufwand und kommen in die Verlust-Box |
| `auf_den_neuen_baustein` | Liste | Marker mit Minus: kommen auf den neuen Baustein |

Die Tabelle enthält dieselben Angaben wie die Tauschmatrix in `model/tauschmatrix.md` und in der Spielanleitung.

## belege.csv

Eine Zeile je belegter Regel.

| Spalte | Typ | Bedeutung |
|---|---|---|
| `element` | Kategorie | Marker oder Regel, die belegt wird |
| `regel_im_spiel` | Text | was die Regel im Spiel bewirkt |
| `beleg` | Text | sinngemäße Wiedergabe der Quellenaussage |
| `quelle` | Text | Kurzangabe der Quelle; vollständig in `README.md` |
| `fundstelle` | Text | Seite oder Folie in der Quelle |

## eckdaten.csv

Eine Zeile je Kennzahl.

| Spalte | Typ | Bedeutung |
|---|---|---|
| `kennzahl` | Text | was gemessen oder geplant ist |
| `wert` | Text | Wert wie in der Quelle angegeben, mit deutschem Dezimalkomma |
| `einheit` | Text | Einheit des Werts |
| `quelle` | Text | Kurzangabe der Quelle |
| `fundstelle` | Text | Seite oder Folie in der Quelle |
