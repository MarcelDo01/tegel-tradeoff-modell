# Tauschmatrix - vorläufige Arbeitsfassung

Stand: 02.10.2026. Zeilen bezeichnen die Ausgangsnutzung, Spalten die Zielnutzung. Alle 25 gerichteten Kombinationen einschließlich fünf Diagonalfeldern sind enthalten.

Quelle: [Whiteboard-Original](../docs/assets/tauschmatrix_original.jpg). Die Beschriftung oben links ist missverständlich: „ist da“ steht am oberen Bereich, „wird zu“ links. Diese Dokumentation interpretiert die Einträge nach ihrem Inhalt wie die Übergabe: Zeile = Ausgang, Spalte = Ziel. Die Teamprüfung der Achsen bleibt erforderlich.

`+` = hinzufügen, `−` = entfernen, `0` = keine Änderung. ESM wird bei einem bestätigten Entsiegelungstausch in die Box gegeben; es ist kein zusätzlicher Akteur auf der Karte.

**Korrekturen gegenüber der Transkription:** GA → W erhält + VSM statt + ESM. W → GA erhält zusätzlich + ESM und entfernt VSM. Diese Marker wurden am 02.10.2026 von Marcel erläutert. Pflanzen in W → GA und Ge → GA stehen im Original in Klammern und bleiben ungeklärt. Akteursangaben sind nicht durch die Versiegelungserläuterung zusätzlich bestätigt.

In anderen Richtungen werden auffällige ESM-Einträge nicht stillschweigend auf VSM geändert. Eine logische Übertragung auf weitere Nutzungen wäre ein neuer Vorschlag, keine bestätigte Originalregel.

| Ausgang ↓ / Ziel → | Koppel | Grünanlage | Wohnen | Gewerbe | Erholung/Freizeit |
|---|---|---|---|---|---|
| Koppel | 0 | + Besucher; − Tiere; − NSM | + ESM; + Anwohner; − NSM; − Pflanzen; − Tiere **[prüfen]** | + ESM; + Beschäftigte; + DMS; − NSM; − Tiere; − Pflanzen **[prüfen]** | + ESM; + Besucher; − NSM; − Tiere **[prüfen]** |
| Grünanlage | + NSM; + Tiere; − Besucher | 0 | + VSM; + Anwohner; − Pflanzen; − Besucher **[prüfen]** | + ESM; + Beschäftigte; + DMS; − Tiere; − Pflanzen; − Besucher **[prüfen]** | + ESM; − Pflanzen **[prüfen]** |
| Wohnen | + Tiere; + NSM; + Pflanzen; − Anwohner; − VSM **[prüfen]** | + ESM; + Besucher; − VSM; − Anwohner **[prüfen]** | 0 | + Beschäftigte; + DMS; − Anwohner **[prüfen]** | + Besucher; − Anwohner |
| Gewerbe | + NSM; + Tiere; + Pflanzen; − Beschäftigte; − VSM **[prüfen]** | + Besucher; − VSM; − Beschäftigte **[prüfen]** | + Anwohner; − Beschäftigte **[prüfen]** | 0 | + Besucher; − Beschäftigte **[prüfen]** |
| Erholung/Freizeit | + NSM; + Tiere; − Besucher; − VSM **[prüfen]** | + Pflanzen; − VSM | + Anwohner; − Besucher **[prüfen]** | + Beschäftigte; + DMS; − Besucher **[prüfen]** | 0 |

## Hinweise je Transformation

| Ausgang | Ziel | Hinweis |
|---|---|---|
| Koppel | Wohnen | ESM/VSM ungeklärt |
| Koppel | Gewerbe | ESM/VSM und DMS ungeklärt |
| Koppel | Erholung/Freizeit | Entfernung Pflanzen?; ESM/VSM ungeklärt |
| Grünanlage | Wohnen | Original: ESM; korrigiert auf VSM laut Erläuterung |
| Grünanlage | Gewerbe | ESM/VSM und DMS ungeklärt; Tiere laut Original, obwohl GA-Legende keine Weidetiere vorsieht |
| Grünanlage | Erholung/Freizeit | ESM/VSM ungeklärt |
| Wohnen | Koppel | Original teilweise VM statt VSM |
| Wohnen | Grünanlage | Pflanzen in Klammern; ESM ergänzt laut Erläuterung |
| Wohnen | Gewerbe | DMS ungeklärt |
| Gewerbe | Koppel | Original teilweise VM statt VSM |
| Gewerbe | Grünanlage | Pflanze in Klammern, unsicher |
| Gewerbe | Wohnen | DMS-Entfernung nicht angegeben |
| Gewerbe | Erholung/Freizeit | DMS-Entfernung nicht angegeben |
| Erholung/Freizeit | Koppel | Pflanzen? |
| Erholung/Freizeit | Wohnen | Original: in Bezug auf Natur gleich |
| Erholung/Freizeit | Gewerbe | DMS ungeklärt |

## CSV-Schema

UTF-8, Komma als Spaltentrenner, Semikolon innerhalb der Listen. Eine Zeile pro gerichteter Transformation. Leere Listen bedeuten keine in dieser Transkription genannten Elemente; sie sind kein Nachweis einer vollständig validierten Regel.

| Feld | Bedeutung |
|---|---|
| ausgang, ziel | ausgeschriebene Nutzungskategorien |
| hinzugefuegt, entfernt | vorläufige Regel einschließlich der zwei erläuterten Markeränderungen |
| hinweis | Unsicherheiten, Lesart und Widersprüche |
| status | original_transkribiert, versiegelung_korrigiert oder keine_aenderung; ggf. offen |
| original_hinzugefuegt, original_entfernt | Transkription vor der Versiegelungskorrektur |

„Original“ bezeichnet hier die manuelle Transkription des Fotos, keine unabhängig verifizierte Regelfassung. Klammerzusätze zu Pflanzen stehen im Hinweisfeld. VM wird als VSM normalisiert. Andere Rechtschreibvarianten wie Tier/Tiere werden vereinheitlicht.

Die Matrix ist eine vom Team entwickelte didaktische Modellannahme, keine wissenschaftlich validierte planerische, ökologische oder rechtliche Bewertung. NSM und DMS sind Modellsymbole, keine rechtswirksamen Statusänderungen. Der aktuelle Arbeitsstand genügt zum Nachvollziehen der Regeln, aber nicht für eine ungeprüfte automatische Simulation.
