# Tuto Make pas-à-pas : le robot éditorial Seasonly en 45 minutes

> Tutoriel clic-par-clic pour monter le scénario **sans rien connaître à Make**. Deux chemins possibles :
> - **Chemin A (rapide)** : importer le blueprint [`make-blueprint-seasonly.json`](make-blueprint-seasonly.json) puis reconnecter les comptes (§7).
> - **Chemin B (pédagogique, recommandé pour la démo)** : tout construire à la main en suivant ce tuto — vous saurez expliquer chaque module au jury.

---

## 0. Prérequis (10 min)

1. **Compte Make** : [make.com](https://www.make.com) → *Get started free* (le plan gratuit suffit : 1 000 opérations/mois — attention, à 30 min d'intervalle le quota part vite, voir §8).
2. **Compte Google** (Sheets + Docs + Gmail) : votre compte étudiant fonctionne.
3. **Clé API Anthropic** : [console.anthropic.com](https://console.anthropic.com) → *API Keys* → *Create Key* → copiez la clé `sk-ant-…` (5 $ de crédit d'essai suffisent largement).
4. *(Optionnel)* **Bot Telegram** : dans Telegram, cherchez **@BotFather** → `/newbot` → suivez les instructions → copiez le **token**. Ajoutez le bot à votre groupe projet, puis récupérez le chat ID en visitant `https://api.telegram.org/bot<TOKEN>/getUpdates` après avoir envoyé un message dans le groupe.

## 1. Préparer le Google Sheet (5 min)

1. [sheets.new](https://sheets.new) → nommez le fichier `Articles SEO Seasonly`, renommez l'onglet `Articles`.
2. Ligne 1, tapez les en-têtes : `Titre` | `Résumé` | `Mots clés` | `Objectif` | `Date de création` | `Statut` | `Lien Doc` (colonnes A→G).
3. Copiez le backlog de 12 sujets depuis [`step3-automatisation-make.md`](step3-automatisation-make.md) §2 : colonne A = titre, colonne D = objectif, colonne F = `À générer`. Laissez B, C, E, G vides (le robot les remplira).

## 2. Créer le scénario et le planifier (3 min)

1. Make → *Scenarios* → **+ Create a new scenario**.
2. En bas de l'écran, cliquez sur l'horloge **Schedule setting** : *Run scenario* = `At regular intervals`, *Minutes* = `30`. C'est l'exigence « toutes les 30 minutes » du brief.
3. Nommez le scénario (crayon en haut à gauche) : `Seasonly — Robot éditorial SEO`.

## 3. Module 1 : Google Sheets « Search Rows » (5 min)

1. Cliquez sur le grand `+` → cherchez **Google Sheets** → action **Search Rows**.
2. *Connection* → **Add** → connectez votre compte Google (autorisez tout ce qui est demandé).
3. *Spreadsheet* : `Articles SEO Seasonly` · *Sheet* : `Articles` · *Table contains headers* : Yes.
4. *Filter* : `Statut` | `Equal to` | `À générer`.
5. *Maximum number of returned rows* : `1`.
6. **Test** : clic droit sur le module → *Run this module only* → vous devez voir sortir la ligne 2 (votre premier sujet). ✅

## 4. Module 2 : Anthropic Claude « Create a Message » (10 min)

1. `+` à droite du module Sheets → cherchez **Anthropic Claude** → **Create a Message**.
2. *Connection* → **Add** → collez votre clé `sk-ant-…`.
3. *Model* : `claude-sonnet-5` · *Max Tokens* : `4096`.
4. *System* : collez le prompt système complet depuis [`step3-automatisation-make.md`](step3-automatisation-make.md) §3 (celui qui encode les patterns GEO et exige une sortie JSON).
5. *Messages* → *Role* : `user` → *Content* : cliquez dans le champ, le panneau violet de mapping s'ouvre ; composez :
   ```
   Sujet : {{Titre de la ligne trouvée}}      ← cliquez la pastille "Titre (A)" du module 1
   Objectif marketing : {{Objectif (D)}}      ← pastille "Objectif (D)"
   Date du jour : {{formatDate(now; "DD/MM/YYYY")}} (adapte les conseils à la saison)
   ```
   (`now` et `formatDate` sont dans l'onglet « fonctions » du panneau de mapping, icône calendrier.)
6. **Test** : *Run this module only* avec la sortie du module 1 → la réponse `text` doit être un JSON `{"titre": …, "resume": …, "mots_cles": …, "article": …}`. ✅

## 5. Module 3 : JSON « Parse JSON » (2 min)

1. `+` → **JSON** → **Parse JSON**.
2. *JSON string* : mappez la pastille **Text** du module Claude.
3. Après un premier run réussi, Make apprend la structure : les champs `titre`, `resume`, `mots_cles`, `article` deviennent mappables partout.

> 💡 Si Claude renvoie parfois le JSON entouré de \`\`\`json … \`\`\`, insérez la fonction `replace()` dans le champ : `{{replace(replace(3.text; "```json"; ""); "```"; "")}}` — ou ajoutez « sans backticks » au prompt (déjà fait dans le nôtre).

## 6. Modules 4 à 7 : Doc, Sheet, Gmail, Telegram (10 min)

**Module 4 — Google Docs : Create a Document**
- *Name* : pastille `titre` (module JSON) · *Content* : pastille `article` · *Folder* : choisissez/créez `Seasonly/Articles SEO` dans votre Drive.

**Module 5 — Google Sheets : Update a Row**
- Même spreadsheet/sheet que le module 1 · *Row number* : pastille **Row number** du module 1.
- `Résumé (B)` = `resume` · `Mots clés (C)` = `mots_cles` · `Date de création (E)` = `{{formatDate(now; "DD/MM/YYYY HH:mm")}}` · `Statut (F)` = `Généré` · `Lien Doc (G)` = pastille **Web View Link** du module Docs.

**Module 6 — Gmail : Send an Email**
- *To* : les adresses du groupe · *Subject* : `✅ Nouvel article SEO généré : {{titre}}`.
- *Content* : recopiez le corps proposé dans [`step3-automatisation-make.md`](step3-automatisation-make.md) §3 (résumé, mots clés, objectif, statut, lien Doc).

**Module 7 — Telegram Bot : Send a Text Message or a Reply** *(optionnel, très visuel en démo)*
- *Connection* : collez le token de @BotFather · *Chat ID* : celui du groupe · *Text* : `📝 {{titre}}` + résumé + mots clés + lien.

> Pour envoyer Gmail **et** Telegram en parallèle, clic droit sur la liaison après le module Sheets Update → **Add a router**, puis accrochez Gmail et Telegram aux deux branches.

## 7. Chemin A : import du blueprint (si vous ne construisez pas à la main)

1. Make → *Scenarios* → **⋯** (en bas) → **Import Blueprint** → sélectionnez `make-blueprint-seasonly.json`.
2. Ouvrez chaque module marqué d'un ⚠️ et re-sélectionnez votre *Connection* (Sheets, Claude, Docs, Gmail, Telegram).
3. Remplacez les placeholders : ID du spreadsheet, dossier Drive, e-mail destinataire, chat ID Telegram.
4. Vérifiez le Schedule (30 min) et passez au §8.

## 8. Tester, activer, et survivre à la démo

1. **Run once** (bouton ▶ en bas à gauche) : suivez les bulles de données au-dessus de chaque module. La ligne du Sheet doit passer `À générer` → `Généré`, le Doc apparaître dans Drive, l'e-mail et le message Telegram arriver.
2. Si un module casse : cliquez sur la bulle blanche au-dessus de lui pour voir l'entrée/sortie exacte — 90 % des erreurs sont un mapping vide ou un JSON mal parsé (§5).
3. Activez l'interrupteur **Scheduling ON** en bas à gauche : le robot tourne désormais toutes les 30 minutes.
4. **Gestion du quota gratuit** : 7 modules × 2 exécutions/heure ≈ 340 opérations/jour → le plan gratuit (1 000/mois) tient ~3 jours. Pour le projet : activez le scénario seulement pendant les phases de test/démo, ou passez l'intervalle à 6 h hors démo.
5. **Le jour de la soutenance** : gardez le scénario ouvert, cliquez **Run once** en direct — effet garanti quand le Telegram du jury sonne.

## 9. Ce que vous devez savoir expliquer au jury

- Pourquoi le filtre `Statut = À générer` + l'update immédiat en `Généré` empêche les doublons.
- Pourquoi le system prompt encode les patterns GEO du Step 1 (réponse directe, chiffres, FAQ, fraîcheur).
- Pourquoi rien ne se publie automatiquement (human-in-the-loop : `Généré` → relecture → `Publié`) — cohérent avec le discours E-E-A-T.
- Le coût : ~1 500 tokens de sortie par article ≈ quelques centimes avec claude-sonnet-5.
