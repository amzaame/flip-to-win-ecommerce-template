# Charte graphique Seasonly — version reconstituée pour le projet

> ⚠️ seasonly.fr et les études de cas branding (Distinct Studio, Paris Packaging Week) bloquent l'accès automatisé : les codes hex exacts n'ont pas pu être extraits. La charte ci-dessous est **reconstituée** à partir des éléments documentés publiquement, et conçue pour être recalée en 5 minutes (voir §4).

## 1. Ce qui est documenté publiquement

- Identité **minimaliste**, pensée pour mettre en avant les produits et leurs composants (étude de cas Paris Packaging Week 2022, branding par Distinct Studio / D.A. Héloïse Asselin)
- **Logo fort** en wordmark, **couleurs douces**, packaging sobre où la couleur sert à signaler les ingrédients
- **Ton complice et didactique**, approche pédagogique de la routine de soin
- Univers : naturalité (95 % d'ingrédients naturels, vegan), saisonnalité, clean beauty à la française

## 2. Palette utilisée dans le projet (`pages/_style.css`)

| Rôle | Variable CSS | Hex | Usage |
|---|---|---|---|
| Fond signature | `--cream` | `#F7F3EC` | Fond de toutes les pages (écru chaleureux) |
| Texte | `--ink` | `#1F2D24` | Corps de texte (vert quasi noir, plus doux que #000) |
| Vert sapin | `--deep` | `#1E3A2B` | Titres, logo, tableaux, bloc CTA |
| Vert sauge | `--sage` | `#9DB29A` | Accents doux, citations |
| Pêche / abricot | `--gold` | `#E8875D` | Accent chaleureux : kickers, CTA, numéros d'étapes |
| Sable | `--sand` | `#EDE5D6` | Fonds secondaires (footer) |
| Ligne | `--line` | `#E5DCCC` | Bordures discrètes |

Logique : le duo **écru + vert sapin** porte la naturalité ; la **pêche** apporte la chaleur "saison" et guide l'œil vers l'action (un seul accent vif, conformément au minimalisme de la marque).

## 3. Typographies

- **Titres** : serif douce et ronde — pile CSS `"Recoleta", "Cormorant Garamond", Georgia, serif`. Le wordmark est en bas-de-casse (`seasonly.`) avec un point pêche, clin d'œil au logo.
- **Texte courant** : sans-serif neutre — `"Helvetica Neue", Helvetica, system-ui`.
- Hiérarchie : titres généreux (clamp 30→46 px), texte 16 px interligne 1.65, kickers en capitales espacées.

## 4. Recaler sur la charte officielle (5 min, à faire par le groupe)

1. Ouvrir seasonly.fr dans Chrome → clic droit → **Inspecter**.
2. Onglet **Elements** : cliquer sur le header, lire `background-color` et `color` dans le panneau Styles → remplacer `--cream`, `--deep` dans `pages/_style.css` (une seule modification restyle les 19 pages).
3. Onglet **Network → Fonts** : recharger la page, noter les noms des fichiers de police → remplacer le premier nom de la pile serif/sans.
4. Récupérer le logo SVG : onglet Network → Img, ou clic droit sur le logo → « Ouvrir l'image dans un nouvel onglet ».

## 5. Ton éditorial (appliqué dans toutes les pages et le prompt Make)

- **Complice** : on tutoie l'expertise, pas la lectrice (« Honnêteté de facialiste : … »)
- **Didactique** : chaque affirmation est expliquée, chiffrée, structurée en étapes
- **Honnête** : jamais de promesse miracle ; les limites sont dites (c'est aussi un pattern E-E-A-T qui favorise la citation par les IA)
