#!/usr/bin/env python3
"""
Scanne un coffre Obsidian et génère la liste à jour de tous les titres de
notes existantes (sans extension .md), pour permettre à l'agent de savoir
vers quelles notes il peut créer des wikilinks [[...]] sans jamais pointer
vers une note qui n'existe pas.

Usage:
    python3 update_note_list.py <chemin_vers_coffre_obsidian> [chemin_sortie]

Si chemin_sortie est omis, écrit dans ./liste_notes.txt (dossier courant).
"""

import os
import sys


def generer_liste(dossier_coffre: str, chemin_sortie: str) -> int:
    if not os.path.isdir(dossier_coffre):
        print(f"Erreur : le dossier '{dossier_coffre}' est introuvable.")
        return 1

    titres = []
    for root, dirs, files in os.walk(dossier_coffre):
        # On ignore le dossier de config caché d'Obsidian
        if ".obsidian" in dirs:
            dirs.remove(".obsidian")
        # On ignore aussi tout dossier caché (.git, .trash, etc.)
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for fichier in files:
            if fichier.endswith(".md"):
                titre = fichier[:-3]  # retire l'extension .md
                titres.append(titre)

    titres.sort(key=str.lower)

    os.makedirs(os.path.dirname(chemin_sortie) or ".", exist_ok=True)
    with open(chemin_sortie, "w", encoding="utf-8") as f:
        for titre in titres:
            f.write(titre + "\n")

    print(f"OK : {len(titres)} notes trouvées. Liste écrite dans {os.path.abspath(chemin_sortie)}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 update_note_list.py <chemin_vers_coffre_obsidian> [chemin_sortie]")
        sys.exit(1)

    dossier = sys.argv[1]
    sortie = sys.argv[2] if len(sys.argv) > 2 else "liste_notes.txt"
    sys.exit(generer_liste(dossier, sortie))
