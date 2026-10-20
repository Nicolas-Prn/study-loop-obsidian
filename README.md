# study-loop-obsidian

Un skill Claude qui transforme Claude en **professeur socratique exigeant**
pour étudier un cours, avec une **prise de notes Obsidian entièrement
automatique** en arrière-plan.

## La boucle

```
expliquer un concept  →  te tester (avec esprit critique)  →  maîtrisé ?
        ↑                                                     │
        └──────────── non : réexpliquer autrement ◄───────────┤
                                                              │ oui
                        sous-agent en arrière-plan ◄──────────┘
                 (écrit la note atomique dans ton coffre Obsidian,
                  la relie à tes notes existantes)
```

- **Un concept à la fois**, dans l'ordre du support de cours (PDF, slides),
  avec le formalisme exact du cours, des intuitions et des exemples concrets.
- **Un test après chaque concept** : cas nouveaux, cas pièges, « pourquoi ? ».
  Pas de « presque bon », pas de flatterie, justification exigée. Tant que ce
  n'est pas maîtrisé, on recommence sous un autre angle.
- **Zéro friction de prise de notes** : dès qu'un concept est validé, un
  sous-agent rédige une note Obsidian atomique (LaTeX, callouts, wikilinks),
  l'écrit dans ton coffre, et la relie aux notes déjà présentes. Tes erreurs
  pendant le test deviennent des encadrés « piège » dans la note.

## Contenu

```
professeur-socratique/
├── SKILL.md                  # le skill
├── scripts/update_note_list.py  # liste les titres de notes du coffre
└── assets/example.md         # référence de style pour les notes
```

## Installation

### Claude (app desktop / web)

1. Télécharge `professeur-socratique.zip` depuis la dernière
   [release](../../releases/latest) (ou zippe toi-même le dossier
   `professeur-socratique/`).
2. Dans Claude : **Paramètres → Capabilities → Skills → Upload skill**, et
   choisis le zip.

### Claude Code

```bash
git clone https://github.com/Nicolas-Prn/study-loop-obsidian.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/study-loop-obsidian/professeur-socratique" ~/.claude/skills/professeur-socratique
```

(Le lien symbolique permet de récupérer les mises à jour avec un simple
`git pull`.)

## Personnalisation

Ouvre `SKILL.md` et adapte la section **« Profil de l'apprenant »** : c'est
elle qui oriente les exemples concrets (DIY, finance, médecine, jeux
vidéo...).

## Première utilisation

Au début d'une session, donne à Claude :

- le **chemin de ton coffre Obsidian** ;
- l'emplacement de **`liste_notes.txt`** (liste centrale des titres de notes,
  un seul fichier pour tous tes cours) ;
- le **dossier du cours** où se trouvent les PDF/slides.

Claude a besoin d'un accès en lecture/écriture à ces dossiers (dans l'app :
dossiers connectés ; dans Claude Code : lancer la session depuis un dossier
parent ou les ajouter).

> ⚠️ Le sous-agent **écrit directement dans ton coffre**. Il n'ajoute que du
> contenu (jamais de suppression, jamais de modification de `.obsidian/`),
> mais fais une sauvegarde / un commit de ton coffre avant la première
> utilisation.

## Graphify (optionnel)

Si Graphify (paquet `graphifyy`) est installé et qu'un
graphe du coffre existe (`<coffre>/graphify-out/graph.json`), le sous-agent
s'en sert pour trouver les notes liées sans les ouvrir une à une. Le skill ne
l'installe jamais lui-même. Outil tiers, non maintenu par Anthropic : teste
d'abord sur un petit sous-dossier, la construction du graphe consomme du
quota.

```bash
uv tool install graphifyy
graphify <sous_dossier_test> --obsidian --obsidian-dir <sous_dossier_test>
```

## Licence

MIT
