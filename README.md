# Seasonly × GEO — Projet SEO / Generative Engine Optimization

Étude de cas complète pour **[Seasonly](https://seasonly.fr/)** (skincare naturelle & Skin Studios de facialisme) : comment faire exister la marque dans les résultats Google **et** dans les réponses des IA (ChatGPT, Perplexity, Claude).

## Livrables

| Step | Livrable | Fichier |
|---|---|---|
| **1** | Analyse SERP & GEO : 5 requêtes testées, concurrents cités, patterns des sources reprises par les IA, enjeu robots.txt, stratégie en 3 actions + KPIs | [`docs/step1-analyse-serp-geo.md`](docs/step1-analyse-serp-geo.md) |
| **2** | 6 landing pages GEO-optimisées (vibecoding) + hub + `llms.txt` | [`pages/`](pages/) — ouvrir [`pages/index.html`](pages/index.html) |
| **2b** | 12 landing pages articles (le backlog Make, en version publiée) + générateur | [`pages/articles/`](pages/articles/) + [`scripts/generate_articles.py`](scripts/generate_articles.py) |
| **3** | Robot éditorial Make : article SEO toutes les 30 min → Google Sheet → Gmail/Telegram | [`docs/step3-automatisation-make.md`](docs/step3-automatisation-make.md) + [**tuto pas-à-pas**](docs/step3-tuto-make-pas-a-pas.md) + [blueprint JSON](docs/make-blueprint-seasonly.json) |
| **4** | Pitch deck de restitution (9 slides, navigation clavier ← →) | [`pitch-deck.html`](pitch-deck.html) |

## Les 6 pages (Step 2)

Chaque page cible une requête où Seasonly est aujourd'hui absente et applique les 7 patterns identifiés au Step 1 : réponse directe en premier paragraphe, données chiffrées, FAQ, JSON-LD (`FAQPage`, `HowTo`, `LocalBusiness`, `DefinedTerm`, `ItemList`), date de mise à jour et auteur expert.

1. `facialisme-definition.html` — page de référence de l'entité « facialisme »
2. `massage-kobido-paris.html` — requête locale « kobido Paris »
3. `gua-sha-guide.html` — mode d'emploi HowTo « gua sha utilisation »
4. `soin-anti-age-sans-injection.html` — dossier « notox / botox naturel »
5. `routine-soin-visage-saison.html` — ADN saisonnier de la marque, mise à jour trimestrielle
6. `meilleur-soin-visage-paris.html` — comparatif assumé « meilleur soin visage Paris »

Aperçu local : ouvrir `pages/index.html` dans un navigateur (aucun build requis).

## Charte graphique

Toutes les pages partagent [`pages/_style.css`](pages/_style.css), aligné sur la charte Seasonly reconstituée (écru `#F7F3EC`, vert sapin `#1E3A2B`, accent pêche `#E8875D`, wordmark serif bas-de-casse, ton complice et didactique) — détails et procédure de recalage sur les couleurs officielles dans [`docs/charte-graphique-seasonly.md`](docs/charte-graphique-seasonly.md).

## Les 12 articles (Step 2b × Step 3)

Chaque sujet du backlog Make existe aussi en landing page publiée dans [`pages/articles/`](pages/articles/) (générées par `python3 scripts/generate_articles.py`) : même structure GEO que les guides (réponse directe, stats, FAQ, JSON-LD `Article` + `FAQPage`), même charte.

## Idée clé

> Les IA ne citent pas « la meilleure marque » : elles citent **la source la plus facile à extraire** — structurée, chiffrée, datée, signée, et ouverte aux crawlers (`GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`) dans le robots.txt.
