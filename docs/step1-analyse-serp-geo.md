# Step 1 — Analyse SERP & GEO : Seasonly (seasonly.fr)

> Projet SEO/GEO — Juillet 2026
> Entreprise étudiée : **Seasonly** — marque française de skincare (fondée en 2018 par Fany Péchiodat), 95 % d'ingrédients naturels, vegan, pionnière du « facialisme moderne » avec ses **Skin Studios** (objectif : 100 studios en France et en Europe d'ici 2027).

---

## 1. La marque et son problème de visibilité

Seasonly a deux moteurs de business :
1. **E-commerce** : soins visage naturels (sérums, crèmes, huiles) + accessoires (gua sha, rouleaux de jade).
2. **Skin Studios** : soins du visage par massage (facialisme), en expansion nationale (Paris, Aix-en-Provence, Bordeaux, bientôt Nice).

**Le problème** : sur les requêtes génériques à forte intention (« meilleur soin visage Paris », « gua sha comment utiliser », « alternative naturelle au botox »), Seasonly est quasi absente des SERP Google **et** des réponses des IA génératives (ChatGPT, Perplexity, Claude, AI Overviews). La marque n'est visible que sur ses requêtes de marque (« Seasonly avis ») et quelques listicles kobido.

C'est un manque à gagner critique : ces requêtes non-marque sont exactement celles que tapent les clients *avant* de connaître la marque — et de plus en plus souvent dans un chatbot plutôt que sur Google.

---

## 2. Méthodologie de test

5 requêtes types testées (juillet 2026) sur moteur de recherche, à répliquer sur ChatGPT, Perplexity et Claude avec la grille fournie en §6 :

| # | Requête | Intention |
|---|---------|-----------|
| R1 | meilleur soin du visage institut Paris | Locale / commerciale |
| R2 | massage kobido Paris meilleure adresse | Locale / commerciale |
| R3 | meilleure marque cosmétique naturelle française | Comparateur / notoriété |
| R4 | soin anti-âge sans injection, alternative naturelle au botox | Informationnelle → conversion |
| R5 | gua sha visage : bienfaits, comment l'utiliser | Informationnelle produit |

---

## 3. Résultats : qui est cité à la place de Seasonly ?

### R1 — « meilleur soin du visage institut Paris » → **Seasonly ABSENTE**
Cités à la place :
- **Agrégateurs de réservation** : Planity (« Les meilleurs soins du visage à Paris 75 »), Treatwell (« Top 20 »), Funbooker (« dès 30 € »)
- **Instituts indépendants avec pages optimisées** : Eden des Sens (Paris 10), Facemodeling (Paris 6), Les Bains du Marais, La Paris'zen Institut (14e — met en avant « 2 000 avis, 4,9/5 »)

### R2 — « massage kobido Paris » → **Seasonly citée partiellement**
- Seasonly apparaît dans des roundups tiers (blog Funbooker « 18 massages Kobido à Paris », journal Oh My Cream) : « référence du massage facial nouvelle génération, 4 adresses, prix raisonnables ».
- Mais dominent : **Planity, Resalib** (10 meilleurs praticiens), blogs de concurrents (Cocoon Paris « Les 5 meilleures adresses », Oryzalab), praticiennes indépendantes (Barbara Sand — citée avec ses prix exacts : 130 €/1 h, 180 €/1 h 30).
- ⚠️ Seasonly n'a **aucune page dédiée « kobido »** sur son propre site : elle dépend de la citation des autres.

### R3 — « meilleure marque cosmétique naturelle française » → **Seasonly ABSENTE**
Cités à la place :
- **Blogs comparateurs / affiliés** : Naturellement Mieux, OnParleBeauté, Cayenn (« Les 15 meilleures marques »), Raquels
- **Marques qui s'auto-positionnent via leur blog** : Celesta Skincare (« notée 100/100 sur Yuka »), Green Spa, Demain Beauty
- **Marques établies** : Melvita, La Canopée, Yves Rocher

### R4 — « anti-âge sans injection / botox naturel » → **Seasonly ABSENTE**
Cités : **Aroma-Zone** (page ingrédient « botox naturel »), SkinClinik (blog de clinique), Notino, Maison Yoko, NatStory. Le concept « notox » et le **massage facial / gua sha** sont cités comme solutions… sans que Seasonly, spécialiste du sujet, ne soit mentionnée.

### R5 — « gua sha bienfaits comment utiliser » → **Seasonly ABSENTE (le plus frappant)**
Seasonly **vend des gua sha** mais laisse la SERP à : Mademoiselle bio (blog), Secrets de Miel, **NIVEA** (page conseils), Lac de la Gimone (« avis dermatologue »), Melusine Cosmetics, Beautigloo, See My Cosmetics (« avant/après »).

---

## 4. Patterns : pourquoi ces sources sont-elles reprises par les IA ?

Analyse des pages citées (structure, données, fraîcheur, autorité) :

| Pattern | Exemples observés | Pourquoi l'IA le reprend |
|---|---|---|
| **Format listicle chiffré** (« Top 20 », « Les 5 meilleures adresses », « 15 marques ») | Treatwell, Cocoon Paris, Cayenn | Réponse pré-mâchée : l'IA n'a qu'à extraire la liste |
| **Données chiffrées précises** : prix (130 €/1 h), notes (4,9/5), volume d'avis (2 000+), scores Yuka (100/100) | Barbara Sand, La Paris'zen, Celesta | Les chiffres = « faits » citables qui crédibilisent la réponse |
| **Structure extractible** : H2/H3 clairs, étapes numérotées, tableaux, FAQ | NIVEA, Secrets de Miel, Mademoiselle bio | Chunks autonomes faciles à découper pour le RAG |
| **Signaux E-E-A-T** : « avis dermatologue », auteur identifié, « on a testé » | Lac de la Gimone, Oh My Cream, Et Aurélie Alors | L'IA privilégie l'expertise et l'expérience vécue |
| **Fraîcheur affichée** : millésime dans le titre (« 2026 »), dates de mise à jour | Naturellement Mieux, Zemedical, Green Spa | Les moteurs IA sur-pondèrent le contenu récent |
| **Autorité d'agrégateur** : gros volume d'avis structurés, données locales | Planity, Treatwell, Resalib | Base de données exhaustive + schema.org LocalBusiness |
| **Réponse à la question dès le 1er paragraphe** (définition, « c'est quoi ») | NIVEA, Mademoiselle bio | Le résumé en tête devient LE snippet cité |

**Conclusion** : les IA ne citent pas « la meilleure marque », elles citent **la source la plus facile à extraire** : structurée, chiffrée, datée, signée, et accessible aux crawlers.

---

## 5. L'enjeu robots.txt (et llms.txt)

seasonly.fr tourne sur **Shopify** (robots.txt standard Shopify par défaut). Point critique : **une page invisible pour les crawlers IA ne sera jamais citée**, quel que soit son contenu.

### Bots à autoriser explicitement

| Bot | Alimente | Si bloqué |
|---|---|---|
| `GPTBot` / `OAI-SearchBot` | ChatGPT (entraînement + recherche) | Invisible dans ChatGPT |
| `ClaudeBot` / `Claude-SearchBot` | Claude (Anthropic) | Invisible dans Claude |
| `PerplexityBot` | Perplexity | Invisible dans Perplexity |
| `Google-Extended` | Gemini / AI Overviews (part IA) | Absent des réponses IA de Google |
| `Googlebot` / `Bingbot` | SEO classique + Copilot | Désindexation totale |

### Recommandation robots.txt (à ajouter au thème Shopify via `robots.txt.liquid`)

```
# --- Ouverture explicite aux crawlers IA (stratégie GEO) ---
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

# Zones à garder fermées (toutes user-agents)
User-agent: *
Disallow: /cart
Disallow: /checkout
Disallow: /account

Sitemap: https://seasonly.fr/sitemap.xml
```

### Bonus : `llms.txt`
Publier `https://seasonly.fr/llms.txt` — un sommaire en markdown des pages clés (guides, studios, FAQ) pour guider les agents IA vers le contenu citables. Standard émergent, coût quasi nul.

**La logique à présenter au jury** : le robots.txt est un *arbitrage stratégique*. Beaucoup de médias bloquent GPTBot pour protéger leur contenu ; pour une PME en quête de notoriété, c'est l'inverse — **être crawlé = être cité = exister dans la réponse**. Le contenu de Seasonly n'a de valeur défensive que s'il est déjà visible ; aujourd'hui il ne l'est pas, donc on ouvre tout (sauf tunnel d'achat et données client).

---

## 6. Grille de réplication sur les IA (à remplir en TP)

Pour chaque requête R1→R5, poser la question telle quelle à ChatGPT, Perplexity et Claude et noter :

| Requête | IA | Seasonly citée ? | Marques citées à la place | Sources citées (type : avis / wiki / comparateur / blog / marque) |
|---|---|---|---|---|
| R1 | ChatGPT / Perplexity / Claude | ☐ | … | … |
| R2 | " | ☐ | … | … |
| … | | | | |

Hypothèses à vérifier (issues de l'analyse SERP) : Perplexity citera surtout Planity/Treatwell et les listicles récents ; ChatGPT citera les marques à forte empreinte éditoriale (Aroma-Zone, NIVEA) ; aucune IA ne citera Seasonly hors requête « kobido Paris ».

---

## 7. Stratégie GEO : 3 actions

### Action 1 — Hub de contenu « citable » (owned media)
Créer 6 pages guides GEO-optimisées (→ voir Step 2, dossier `/pages`) sur les requêtes où Seasonly est légitime mais absente : gua sha, kobido, notox, facialisme, routine saisonnière, comparatif instituts. Chaque page applique les 7 patterns du §4 : réponse directe en tête, FAQ + JSON-LD (`FAQPage`, `HowTo`, `Article`, `LocalBusiness`), données chiffrées, date de mise à jour, auteur expert.

### Action 2 — Autorité tierce (earned media)
Les IA croisent les sources : il faut que Seasonly apparaisse **chez les autres**. (a) Compléter/optimiser les fiches Planity, Treatwell, Google Business Profile de chaque Skin Studio (photos, prix, réponse aux avis — viser 4,8+/5 et volume) ; (b) RP digitale ciblée : figurer dans 5 listicles « meilleur kobido/facialiste [ville] » (Funbooker, Cocoon, médias beauté) ; (c) page Wikipédia impossible à court terme → viser les fiches presse (Vogue, ELLE, Marie Claire) que les IA citent.

### Action 3 — Infrastructure GEO (technique)
(a) robots.txt ouvert aux bots IA + llms.txt (§5) ; (b) données structurées schema.org sur tout le site (Organization avec `sameAs` vers presse et réseaux, Product avec avis agrégés, LocalBusiness par studio) ; (c) flux de fraîcheur : blog alimenté automatiquement (→ Step 3, workflow Make) pour maintenir un signal de mise à jour continu.

### KPIs
- **Part de voix IA** : % des 5 requêtes où Seasonly est citée (baseline : ~10 % → objectif 60 % à 6 mois), mesuré mensuellement via la grille §6
- **Citations tierces** : nb de listicles/articles mentionnant Seasonly (baseline 2 → objectif 10)
- **Trafic référent IA** : sessions depuis chatgpt.com / perplexity.ai (Google Analytics 4)
- **SEO classique** : positions Google sur R1–R5 (Search Console), impressions non-marque
- **Business** : réservations studio attribuées au canal organique/IA

---

*Sources principales de l'analyse : SERP Google (juillet 2026) sur les 5 requêtes ; pages citées : Planity, Treatwell, Funbooker, Resalib, blog Oh My Cream, Cocoon Paris, NIVEA Conseils, Mademoiselle bio, Aroma-Zone, Cayenn, Naturellement Mieux ; presse : Slife Mag (expansion Seasonly), Rapporteuses, Beauty Decoded (test Seasonly).*
