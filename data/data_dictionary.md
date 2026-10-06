# Data Dictionary der Zonenzuweisung

Grundlage ist `Tabelle1` aus `data/zones.xlsx`. Die beobachteten Werte beschreiben den aktuellen Datenstand. Sie sind keine allgemeingültigen zulässigen Werte und keine rechtliche Validierung.

| Spalte | Datentyp | Bedeutung | Beobachtete Werte oder Form | Bezug zum Modell |
|---|---|---|---|---|
| `zone_id` | Ganzzahl | eindeutige Kennung des Zoneneintrags | 1 bis 22, ohne Lücken | Verknüpfung zur Zonendarstellung |
| `Hauptkategorie` | Text/Kategorie | übergeordnete räumliche oder nutzungsbezogene Einordnung | Naturschutzgebiet und natürlicher Lebensraum; Flughafenbestand / Denkmalschutz; Freizeit / Erholung; Wohnen / Quartier | beschreibt den Ausgangskontext einer Zone |
| `Unterkategorie` | Text/Kategorie | nähere Einordnung innerhalb der Hauptkategorie | unter anderem Heide, Trockenrasen, Gehölzgruppen; Rundbogenantenne / Denkmalschutz; Grün- und Parkfläche; Schumacher Quartier | differenziert ähnliche Zonen; nicht identisch mit den fünf Tauschmatrix-Nutzungen |
| `Aktuelle Nutzung` | Text/Kategorie | in der Datei zugewiesene bestehende oder berücksichtigte Nutzung | unter anderem Biotoperhalt & Artenschutz; Biotopentwicklung; historischer Bestand & Landmarke; Naherholung & Freizeit; Baufeld / städtische Entwicklung | Ausgangsinformation für die physische Belegung; die Zuordnung zur vereinfachten Modellnutzung erfolgt separat |
| `Flächentyp` | Text/Kategorie | beschreibender Flächen- oder Habitattyp | unter anderem Sandmagerrasen, Heide, Parkwiese, technisches Bauwerk, urbanes Baufeld | fachlicher Kontext der Zone; keine Flächengröße |
| `Zugang` | Text/Kategorie | dokumentierter Zugangsstatus | Eingeschränkt; Öffentlich | unterstützt die Darstellung von Besucherzugang; keine rechtliche Zugangsprüfung |
| `Akteure` | Textliste | beteiligte, betroffene oder dargestellte Akteure und Artengruppen | kommagetrennte Bezeichnungen, unter anderem Besucher:innen, Anwohner:innen, Grün Berlin, Brutvögel und Insekten | Informationsgrundlage für Akteursmarker; Begriffe sind nicht vollständig auf die vereinfachte Markerlegende normiert |
| `Schutzstatus` | Text/Kategorie | in der Arbeitsdatei angegebener Schutz-, Planungs- oder Landschaftsbezug | unter anderem § 30 BNatSchG, Denkmalschutz-Prüfung, Landschaftspark, Bebauungsplan (B-Plan) | Kontextinformation; das physische Modell ersetzt keine Schutz- oder Zulässigkeitsprüfung |
| `Beweidung` | Text/Kategorie | Angabe, ob Beweidung vorgesehen oder vorhanden ist | Ja; Nein | relevant für Koppel-, Schäfer- und Tierdarstellungen |
| `Datenquelle` | Text | projektinterner Hinweis auf die herangezogene Grundlage | Kartenfolie / EPK; Kartenfolie / Denkmalkarte; Kartenfolie / Freiraumplanung; Kartenfolie / Kompensationskonzept; Kartenfolie / Masterplan Schumacher Quartier | Herkunftshinweis; weiterführende Quellen stehen in `references/quellen.md` |

## Vollständigkeit und fehlende Werte

Alle 220 Datenzellen des Tabellenbereichs sind befüllt. Die Datei enthält keine leeren Werte. `Nein` in `Beweidung` ist ein expliziter Wert und kein Ersatz für fehlende Daten.

## Beziehungen und Grenzen

`zone_id` ist der Primärschlüssel des aktuellen Tabellenstands. Es gibt keine geometrische Spalte und keinen direkten Schlüssel zu einem GIS-Layer. Die Zonenattribute sind von der Tauschmatrix in `model/` zu unterscheiden: Die Tabelle beschreibt den Ausgangskontext, die Matrix qualitative Veränderungen zwischen fünf vereinfachten Nutzungen.
