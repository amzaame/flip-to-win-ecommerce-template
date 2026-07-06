# Brief Claude Design — Landing pages Seasonly (SEO/GEO)

Mode d'emploi : collez le **Prompt maître** tel quel dans Claude Design, puis enchaînez avec le **mini-prompt de la page** voulue. Le contenu texte existe déjà (dossier `pages/` du repo) : le but est de le faire re-designer, pas de le réécrire — collez le texte de la page existante à la suite du mini-prompt.

---

## PROMPT MAÎTRE (à coller en premier, une seule fois)

```
Tu vas designer des landing pages pour Seasonly (seasonly.fr), marque française
de soins visage naturels (95 % d'ingrédients naturels, vegan, fondée en 2018)
et réseau de Skin Studios de massage du visage (facialisme) — Paris,
Aix-en-Provence, Bordeaux, dès 65 €.

── CHARTE GRAPHIQUE (à respecter strictement) ──
• Fond principal : écru #F7F3EC · fonds secondaires sable #EDE5D6 · cartes blanches
• Texte : vert très sombre #1F2D24 · Titres et logo : vert sapin #1E3A2B
• UN SEUL accent vif : pêche/abricot #E8875D (CTA, kickers, numéros d'étapes)
• Vert sauge #9DB29A pour les accents doux · bordures discrètes #E5DCCC
• Typo titres : serif douce et ronde (Recoleta ou équivalent, fallback Georgia)
• Typo texte : sans-serif neutre (Helvetica/Inter), 16px, interligne 1.6+
• Logo : wordmark bas-de-casse "seasonly." avec le point en pêche
• Style : minimalisme clean, beaucoup de blanc, coins arrondis (12-16px),
  pas d'ombres lourdes, pas de dégradés criards. Ton complice et didactique.

── RÈGLES SEO/GEO NON NÉGOCIABLES (le design ne doit JAMAIS les casser) ──
1. Tout le texte reste du vrai texte HTML — jamais de texte dans des images,
   jamais de contenu rendu uniquement en JavaScript.
2. HTML sémantique : UN SEUL h1 par page, hiérarchie h2/h3 logique, balises
   <header> <main> <section> <footer> <table> <ol> <ul> réelles.
3. La page commence par un "answer box" : un encadré juste sous le h1 qui
   répond à la question de la page en 3-4 phrases, avec les chiffres clés
   en gras. C'est le bloc que Google et les IA citent : il doit être mis en
   valeur visuellement (bordure gauche pêche, fond carte) mais rester du texte.
4. Un bandeau de 4 statistiques chiffrées sous le hero (gros chiffre serif +
   légende courte).
5. La FAQ utilise de vrais <details>/<summary> (jamais d'accordéon JS qui
   cache le texte au chargement) — les questions doivent être lisibles dans
   le HTML brut.
6. Conserver INTÉGRALEMENT le bloc <script type="application/ld+json"> de la
   page d'origine (schema.org Article/FAQPage/HowTo) — ne pas le modifier.
7. Conserver <title>, <meta name="description">, <link rel="canonical"> et
   la date de mise à jour visible ("Mis à jour le …") près du h1 et en footer.
8. Performance : page autonome (CSS inline ou un seul fichier), pas de
   framework lourd, pas de webfonts bloquantes (font-display: swap), images
   en lazy loading avec alt descriptifs. Objectif : rendu instantané.
9. Mobile-first : tout doit être lisible à 375px ; les tableaux défilent
   horizontalement dans leur conteneur, jamais la page entière.
10. Un seul CTA principal par page (bouton pêche, coins très arrondis) répété
    en fin de page dans un bloc vert sapin.
11. Contraste AA minimum partout (le pêche #E8875D ne sert jamais pour du
    texte long sur fond clair).
12. Maillage interne visible : le fil d'Ariane et les liens vers les autres
    guides restent de vrais liens <a> textuels.

── STRUCTURE TYPE D'UNE PAGE ──
header (logo + nav) → fil d'Ariane → hero (kicker pêche en capitales, h1,
answer box, ligne de méta avec date + auteur) → bandeau 4 stats → sections
de contenu (tableaux comparatifs, listes d'étapes numérotées avec pastilles
pêche) → FAQ details/summary → bloc CTA vert sapin → footer (badges
"95 % naturel / Vegan / Mis à jour le …").

Confirme que tu as compris, puis attends que je te donne la page à designer.
```

---

## MINI-PROMPTS PAR PAGE (coller après le prompt maître, un par page)

Pour chaque page : collez le mini-prompt, puis **le contenu texte de la page existante** (copier tout le texte visible du fichier HTML correspondant, ou le fichier entier — Claude Design saura extraire).

### Guides (6)

**1. facialisme-definition.html**
```
Page à designer : "Le facialisme, c'est quoi ?" — page de DÉFINITION de référence.
Requête cible : "facialisme définition" / "facialiste c'est quoi".
Ambiance : la plus éditoriale des 6, presque une page d'encyclopédie premium.
Éléments clés à mettre en scène : l'answer box de définition (c'est LE snippet
à faire citer), le tableau facialiste vs esthéticienne vs dermatologue, la
frise des 4 techniques. Voici le contenu : [COLLER LE CONTENU]
```

**2. massage-kobido-paris.html**
```
Page à designer : "Massage kobido à Paris" — guide LOCAL commercial.
Requête cible : "kobido paris" / "massage kobido paris prix".
Ambiance : guide urbain élégant. Éléments clés : le tableau comparatif des
adresses avec prix (le différenciateur), le déroulé de séance en 4 étapes,
le CTA "4 studios à Paris dès 65 €". Voici le contenu : [COLLER LE CONTENU]
```

**3. gua-sha-guide.html**
```
Page à designer : "Gua sha : guide complet" — page TUTORIEL (HowTo).
Requête cible : "gua sha comment utiliser".
Ambiance : mode d'emploi visuel. Éléments clés : les 4 étapes numérotées très
visuelles (c'est un HowTo schema), le tableau des 5 erreurs, la stat "15°"
mise en avant. Prévoir des emplacements d'illustration par étape (placeholders
avec alt descriptifs). Voici le contenu : [COLLER LE CONTENU]
```

**4. soin-anti-age-sans-injection.html**
```
Page à designer : "Anti-âge sans injection (notox)" — page DOSSIER expert.
Requête cible : "alternative naturelle botox" / "notox".
Ambiance : sérieux médical adouci par la charte. Éléments clés : le bloc
d'honnêteté ("rien ne remplace le botox, mais…") à traiter comme une citation
mise en valeur — c'est notre signal E-E-A-T — et le classement des 5 piliers.
Voici le contenu : [COLLER LE CONTENU]
```

**5. routine-soin-visage-saison.html**
```
Page à designer : "Routine visage par saison" — la page ADN de marque.
Requête cible : "routine soin visage saison".
Ambiance : la plus saisonnière et vivante — c'est le concept fondateur de
Seasonly. Éléments clés : le tableau des 4 saisons (traiter chaque saison
avec une nuance de la palette SANS sortir de la charte), le bandeau
"édition été 2026" qui montre la fraîcheur. Voici le contenu : [COLLER LE CONTENU]
```

**6. meilleur-soin-visage-paris.html**
```
Page à designer : "Meilleur soin du visage à Paris" — page COMPARATIF.
Requête cible : "meilleur soin visage paris".
Ambiance : comparateur premium et honnête. Éléments clés : le grand tableau
des 5 formats avec prix (la ligne Seasonly légèrement mise en avant, fond
sable, sans écraser les autres), la section "Pourquoi nous assumons ce
comparatif" en encart. Voici le contenu : [COLLER LE CONTENU]
```

### Articles (12) — prompt générique

```
Page à designer : article de blog "[TITRE]" — gabarit ARTICLE du magazine.
Même structure que les guides mais plus compacte : hero + answer box,
4 stats, 2-3 sections, FAQ 3 questions, CTA final.
Contrainte supplémentaire : ce gabarit sera décliné sur 12 articles — le
design doit être un template réutilisable où seuls textes/stats/tableaux
changent. Voici le contenu : [COLLER LE CONTENU]
```

(Articles : gua sha ou rouleau de jade · kobido Bordeaux · prix soin facialiste 2026 · bakuchiol vs rétinol · drainage lymphatique · routine peau sensible automne · bruxisme/mâchoire · skin minimalism · massage visage Aix · poches sous les yeux · 95 % ingrédients naturels · préparer sa peau au soleil — fichiers dans `pages/articles/`.)

### Hub

```
Page à designer : "Les Guides Seasonly" — page HUB (sommaire).
Grille de cartes (6 guides + accès aux 12 articles), une intro courte qui
explique la promesse éditoriale ("réponses directes, chiffrées, à jour").
Chaque carte : kicker pêche, titre serif, 1 phrase, vrai lien <a>.
Voici le contenu : [COLLER LE CONTENU]
```

---

## CHECKLIST DE RECETTE (à vérifier sur chaque page produite par Claude Design)

- [ ] Un seul `<h1>`, hiérarchie h2/h3 intacte
- [ ] Answer box présente sous le h1, texte réel, chiffres en gras
- [ ] Le `<script type="application/ld+json">` d'origine est toujours là, inchangé
- [ ] `<title>` + meta description + canonical + date "Mis à jour le…" conservés
- [ ] FAQ en `<details>/<summary>` natifs
- [ ] Zéro texte dans des images ; images avec `alt` descriptif
- [ ] Lisible à 375 px, tableaux scrollables dans leur conteneur
- [ ] Palette respectée : écru/vert sapin + un seul accent pêche
- [ ] CTA unique, liens internes réels
- [ ] La page s'ouvre en local sans réseau (autonome, pas de CDN)
