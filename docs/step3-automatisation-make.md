# Step 3 — Automatisation de la rédaction d'articles SEO avec Make

Objectif : toutes les **30 minutes**, générer automatiquement un article SEO pour Seasonly avec l'IA, l'ajouter à un **Google Sheet** de pilotage, et envoyer une **notification** (Gmail + Telegram).

---

## 1. Architecture du scénario Make

```
[1] Schedule (toutes les 30 min)
        │
[2] Google Sheets — Search Rows (le prochain sujet "À générer")
        │
[3] Anthropic Claude — Create a Message (génération de l'article)
        │
[4] JSON — Parse JSON (titre, résumé, mots-clés, article)
        │
[5] Google Docs — Create a Document (corps de l'article, rangé dans un dossier Drive)
        │
[6] Google Sheets — Update Row (résumé, mots-clés, date, statut → "Généré")
        │
   ┌────┴────┐
[7] Gmail    [8] Telegram
   Send      Send message
   e-mail    (résumé + lien Doc)
```

> Variante minimale acceptée par le brief : supprimer le module 5 et stocker l'article directement dans une colonne du Sheet. La version Google Docs est plus propre pour la relecture.

---

## 2. Le Google Sheet de pilotage

Feuille `Articles SEO Seasonly`, colonnes **exactement** comme demandé dans le brief :

| Colonne | Champ | Rempli par |
|---|---|---|
| A | **Titre** | Vous (backlog de sujets) puis affiné par l'IA |
| B | **Résumé** | IA (module 6) |
| C | **Mots clés** | IA (module 6) |
| D | **Objectif** | Vous : SEO local / GEO citation / conversion / notoriété |
| E | **Date de création** | Make : `{{now}}` formaté `DD/MM/YYYY HH:mm` |
| F | **Statut** | `À générer` → `Généré` → `Relu` → `Publié` |
| G | Lien Google Doc | Make (module 5) |

**Backlog initial (aligné sur la stratégie GEO du Step 1)** — 12 sujets pré-remplis, statut `À générer` :

1. Gua sha ou rouleau de jade : lequel choisir ? — *Objectif : GEO citation*
2. Kobido à Bordeaux : bienfaits et adresses — *SEO local (nouveau studio)*
3. Combien coûte un soin facialiste en 2026 ? — *GEO citation (données chiffrées)*
4. Bakuchiol vs rétinol : le match — *GEO citation*
5. Drainage lymphatique du visage : mode d'emploi — *GEO citation*
6. Routine peau sensible de l'automne 2026 — *Fraîcheur saisonnière*
7. Bruxisme et tensions de mâchoire : le massage qui soulage — *Notoriété*
8. Skin minimalism : 4 produits suffisent — *Notoriété*
9. Massage visage à Aix-en-Provence : le guide — *SEO local*
10. Poches sous les yeux : 5 solutions classées — *GEO citation*
11. Que veut dire « 95 % d'ingrédients naturels » ? — *Confiance / E-E-A-T*
12. Préparer sa peau au soleil : la check-list de juillet — *Fraîcheur saisonnière*

---

## 3. Configuration des modules

### Module 1 — Schedule
- Intervalle : `30 minutes` (paramètre du scénario : « Run scenario » → Every 30 minutes)

### Module 2 — Google Sheets : Search Rows
- Filtre : `Statut = À générer`, limite : 1 (le plus ancien d'abord)
- Si aucune ligne : ajouter un routeur + module « Tools » pour s'arrêter proprement (évite les exécutions vides)

### Module 3 — Claude : Create a Message
- Modèle : `claude-sonnet-5` (bon rapport qualité/coût pour du volume éditorial ; `claude-haiku-4-5` en mode économique)
- Max tokens : 4096
- **System prompt** :

```
Tu es rédacteur SEO senior pour Seasonly, marque française de soins visage
naturels (95 % d'ingrédients naturels, vegan, fondée en 2018) et réseau de
Skin Studios de facialisme (Paris, Aix-en-Provence, Bordeaux, dès 65 €).

Règles d'écriture (patterns GEO) :
- Commencer par un résumé de 3 phrases qui répond directement à la question du titre
- Structure H2/H3 claire, listes à puces, une donnée chiffrée par section minimum
- Terminer par une FAQ de 3 questions/réponses courtes
- Ton expert et honnête : jamais de promesse miracle, mentionner les limites
- 700 à 900 mots, en français
- Mentionner Seasonly naturellement 2 fois maximum (pas de matraquage)

Réponds UNIQUEMENT en JSON valide, sans backticks :
{"titre": "...", "resume": "... (3 phrases)", "mots_cles": "kw1, kw2, kw3, kw4, kw5", "article": "... (markdown)"}
```

- **User prompt** (avec mapping Make) :

```
Sujet : {{2.Titre}}
Objectif marketing : {{2.Objectif}}
Date du jour : {{formatDate(now; "DD/MM/YYYY")}} (adapte les conseils à la saison)
```

### Module 4 — JSON : Parse JSON
- Source : `{{3.text}}` (la réponse de Claude)

### Module 5 — Google Docs : Create a Document
- Titre : `{{4.titre}}` — Contenu : `{{4.article}}` — Dossier : `Drive/Seasonly/Articles SEO`

### Module 6 — Google Sheets : Update Row
- Row number : `{{2.rowNumber}}`
- Résumé = `{{4.resume}}` · Mots clés = `{{4.mots_cles}}` · Date de création = `{{formatDate(now; "DD/MM/YYYY HH:mm")}}` · Statut = `Généré` · Lien = `{{5.webViewLink}}`

### Module 7 — Gmail : Send an Email
- À : l'équipe — Objet : `✅ Nouvel article SEO généré : {{4.titre}}`
- Corps :

```
Un nouvel article vient d'être généré par le robot éditorial Seasonly.

Titre : {{4.titre}}
Résumé : {{4.resume}}
Mots clés : {{4.mots_cles}}
Objectif : {{2.Objectif}}
Statut : Généré — en attente de relecture
Google Doc : {{5.webViewLink}}

Prochaine génération dans 30 minutes.
```

### Module 8 — Telegram : Send a Text Message (optionnel mais démo-friendly)
- Bot créé via @BotFather, chat du groupe projet
- Message : `📝 {{4.titre}}\n\n{{4.resume}}\n\n🔑 {{4.mots_cles}}\n📄 {{5.webViewLink}}`

---

## 4. Garde-fous (à mentionner au jury)

- **Human-in-the-loop** : rien n'est publié automatiquement. Le statut `Généré` déclenche une relecture humaine ; seul un humain passe en `Publié`. C'est cohérent avec le discours E-E-A-T du Step 1 : l'IA produit le brouillon, l'expertise facialiste signe.
- **Anti-doublon** : le filtre `Statut = À générer` + passage immédiat à `Généré` empêche de traiter deux fois le même sujet.
- **Coût** : 48 exécutions/jour ; à ~1 500 tokens de sortie par article, le coût IA reste de l'ordre de quelques centimes par article avec claude-sonnet-5. Les 30 minutes sont un choix de démo — en production réelle, 1 article/jour suffit (et évite le contenu de masse pénalisé par Google).
- **Qualité GEO** : le system prompt encode les patterns identifiés au Step 1 (réponse directe en tête, chiffres, FAQ, fraîcheur datée).

## 5. Fichier d'import

Le blueprint prêt à importer dans Make (Scenario → Import Blueprint) : [`make-blueprint-seasonly.json`](make-blueprint-seasonly.json). Après import, reconnecter les 4 connexions (Google Sheets, Anthropic, Gmail, Telegram) et pointer vers votre Sheet.
