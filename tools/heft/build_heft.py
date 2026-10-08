"""Baut das blätterbare Spielanleitungs-Heft.

Liest tools/heft/heft.src.html, setzt die Fotos aus tools/heft/img/ direkt
in die Seite ein und schreibt spielanleitung-heft.html.

Aufruf im Projektordner:  python tools/heft/build_heft.py
"""
import base64
import re
from pathlib import Path

HIER = Path(__file__).resolve().parent
QUELLE = HIER / "heft.src.html"
ZIEL = HIER.parents[1] / "spielanleitung-heft.html"


def foto(treffer):
    datei = HIER / "img" / (treffer.group(1) + ".jpg")
    return "data:image/jpeg;base64," + base64.b64encode(datei.read_bytes()).decode()


def build():
    seite = re.sub(r"\{\{IMG:(\w+)\}\}", foto, QUELLE.read_text(encoding="utf-8"))
    kopf, rest = seite.split("</style>", 1)
    html = (
        '<!DOCTYPE html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + kopf + "</style>\n</head>\n<body>\n" + rest + "\n</body>\n</html>\n"
    )
    ZIEL.write_text(html, encoding="utf-8", newline="\n")
    print(ZIEL)


if __name__ == "__main__":
    build()
