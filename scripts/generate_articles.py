#!/usr/bin/env python3
"""Génère les landing pages articles Seasonly (pages/articles/*.html).

Chaque page applique la structure GEO du Step 1 : réponse directe, stats
chiffrées, sections structurées, FAQ + JSON-LD (Article + FAQPage), date,
charte graphique Seasonly (pages/_style.css).

Usage : python3 scripts/generate_articles.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "pages" / "articles"
DATE = "2026-07-06"
DATE_FR = "6 juillet 2026"

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{metatitle} | Seasonly</title>
<meta name="description" content="{metadesc}">
<link rel="canonical" href="https://seasonly.fr/pages/articles/{slug}">
<link rel="stylesheet" href="../_style.css">
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>
<header class="site">
  <div class="logo">seasonly</div>
  <nav><a href="../index.html">Guides</a><a href="index.html">Articles</a><a href="https://seasonly.fr">Boutique &amp; studios</a></nav>
</header>
<p class="breadcrumb"><a href="../index.html">Les Guides Seasonly</a> › <a href="index.html">Articles</a> › {title}</p>

<section class="hero">
  <div class="kicker">{kicker}</div>
  <h1>{title}</h1>
  <div class="answer"><strong>En résumé :</strong> {answer}</div>
  <p class="meta">Mis à jour le {date_fr} · Par l'équipe de facialistes Seasonly · Objectif éditorial : {objectif}</p>
</section>

<div class="stats">
{stats}
</div>

<main>
{sections}
  <section class="faq">
    <h2>Questions fréquentes</h2>
{faq}
  </section>

  <div class="cta">
    <h2>{cta_h}</h2>
    <p>{cta_p}</p>
    <a class="btn" href="https://seasonly.fr">{cta_btn}</a>
  </div>
</main>

<footer>
  <span class="badge">95 % naturel</span><span class="badge">Vegan</span><span class="badge">Mis à jour {date_fr}</span>
  <p style="margin-top:10px">© 2026 Seasonly — Contenu expert rédigé selon la ligne éditoriale des Guides Seasonly. Ne remplace pas un avis médical.</p>
</footer>
</body>
</html>
"""

def build_jsonld(a):
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": a["title"],
                "description": a["metadesc"],
                "datePublished": DATE,
                "dateModified": DATE,
                "inLanguage": "fr",
                "author": {"@type": "Organization", "name": "Seasonly — équipe facialistes"},
                "publisher": {"@type": "Organization", "name": "Seasonly", "url": "https://seasonly.fr"},
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": r},
                    }
                    for q, r in a["faq"]
                ],
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=2)


def render(a):
    stats = "\n".join(
        f'  <div class="stat"><b>{b}</b><span>{s}</span></div>' for b, s in a["stats"]
    )
    sections = "\n".join(
        f"  <h2>{h}</h2>\n{body}" for h, body in a["sections"]
    )
    faq = "\n".join(
        f"    <details><summary>{q}</summary><p>{r}</p></details>" for q, r in a["faq"]
    )
    return TEMPLATE.format(
        slug=a["slug"], metatitle=a["metatitle"], metadesc=a["metadesc"],
        kicker=a["kicker"], title=a["title"], answer=a["answer"],
        objectif=a["objectif"], date_fr=DATE_FR, stats=stats, sections=sections,
        faq=faq, cta_h=a["cta"][0], cta_p=a["cta"][1], cta_btn=a["cta"][2],
        jsonld=build_jsonld(a),
    )


ARTICLES = [
    # 1 ────────────────────────────────────────────────────────────────
    dict(
        slug="gua-sha-ou-rouleau-de-jade.html",
        metatitle="Gua sha ou rouleau de jade : lequel choisir en 2026 ?",
        metadesc="Gua sha pour sculpter et drainer en profondeur, rouleau de jade pour décongestionner en douceur : le comparatif des facialistes Seasonly, avec prix (15-35 €) et protocoles.",
        kicker="Accessoires · Comparatif",
        title="Gua sha ou rouleau de jade : lequel choisir ?",
        objectif="citation GEO",
        answer="le <strong>gua sha</strong> sculpte et draine en profondeur (ovale, mâchoire) grâce à son bord incliné à 15° ; le <strong>rouleau de jade</strong> décongestionne en douceur et convient mieux aux débutantes et au contour des yeux. Prix comparables (15-35 €). Si vous ne deviez en choisir qu'un pour un objectif fermeté : le gua sha.",
        stats=[("15°", "l'angle du gua sha contre la peau"), ("5 min", "par jour, quel que soit l'outil"), ("15-35 €", "prix des deux accessoires"), ("2 outils", "pour 2 objectifs différents")],
        sections=[
            ("Le match en un tableau", """  <div class="table-wrap"><table>
    <tr><th></th><th>Gua sha</th><th>Rouleau de jade</th></tr>
    <tr><td>Drainage / dégonflage</td><td>★★★</td><td>★★</td></tr>
    <tr><td>Fermeté, sculpture de l'ovale</td><td>★★★</td><td>★</td></tr>
    <tr><td>Facilité de prise en main</td><td>★★</td><td>★★★</td></tr>
    <tr><td>Contour des yeux</td><td>★★ (petit bord)</td><td>★★★ (petit rouleau)</td></tr>
    <tr><td>Effet frais au réveil</td><td>★★</td><td>★★★ (sorti du frigo)</td></tr>
  </table></div>"""),
            ("Notre verdict selon votre profil", """  <ul>
    <li><strong>Objectif fermeté / mâchoire tendue</strong> → gua sha, sans hésiter : c'est le seul des deux qui mobilise vraiment les tissus.</li>
    <li><strong>Débutante, peau réactive, poches au réveil</strong> → rouleau de jade au réfrigérateur, 3 minutes le matin.</li>
    <li><strong>Les deux en routine idéale</strong> : rouleau frais le matin (décongestion), gua sha le soir sur huile (sculpture) — le protocole complet est dans <a href="../gua-sha-guide.html">notre guide gua sha</a>.</li>
  </ul>"""),
        ],
        faq=[
            ("Peut-on utiliser gua sha et rouleau le même jour ?", "Oui : rouleau frais le matin pour dégonfler, gua sha le soir sur une huile pour sculpter. Ne cumulez pas les deux sur une peau irritée."),
            ("Faut-il les mettre au réfrigérateur ?", "C'est un plus pour l'effet décongestionnant, surtout le rouleau le matin. Jamais au congélateur : le froid extrême agresse les capillaires."),
            ("Quartz rose ou jade, ça change quoi ?", "Rien sur l'efficacité : la différence est sensorielle et esthétique. Regardez plutôt la qualité de taille et la forme de l'outil."),
        ],
        cta=("Apprenez le bon geste en studio", "Chaque soin Seasonly se termine par la transmission des gestes d'automassage — avec votre outil ou le nôtre.", "Réserver un soin · dès 65 €"),
    ),
    # 2 ────────────────────────────────────────────────────────────────
    dict(
        slug="kobido-bordeaux.html",
        metatitle="Kobido à Bordeaux : bienfaits, prix et adresses (2026)",
        metadesc="Où faire un massage kobido à Bordeaux ? Bienfaits du lifting japonais, prix constatés 2026 (60-150 €) et l'arrivée du Skin Studio Seasonly, dès 65 €.",
        kicker="Guide local · Bordeaux",
        title="Kobido à Bordeaux : bienfaits et adresses",
        objectif="SEO local (nouveau studio)",
        answer="le kobido, massage japonais anti-âge né au XV<sup>e</sup> siècle, arrive en force à Bordeaux : comptez <strong>60 à 150 €</strong> la séance selon le format. Effet éclat immédiat, effet liftant après une cure de 4 à 6 séances. Le <strong>Skin Studio Seasonly de Bordeaux</strong> le décline en version facialisme sur diagnostic, dès 65 €.",
        stats=[("60-150 €", "fourchette constatée à Bordeaux"), ("dès 65 €", "au Skin Studio Seasonly Bordeaux"), ("50", "muscles du visage travaillés"), ("4-6", "séances pour une cure liftante")],
        sections=[
            ("Où pratiquer le kobido à Bordeaux", """  <div class="table-wrap"><table>
    <tr><th>Format</th><th>Prix constaté 2026</th><th>Pour qui ?</th></tr>
    <tr><td><strong>Skin Studio Seasonly Bordeaux</strong></td><td>dès 65 € / 30 min · 95-120 € / 1 h</td><td>Facialisme sur diagnostic (kobido + sculpting + drainage), cures accessibles</td></tr>
    <tr><td>Praticienne kobido indépendante</td><td>90-150 € / 1 h</td><td>Kobido traditionnel pur, suivi personnalisé</td></tr>
    <tr><td>Institut avec option « massage japonais »</td><td>60-90 €</td><td>Découverte, si 20 min de massage manuel minimum</td></tr>
  </table></div>
  <p>Réflexe utile : sur les plateformes de réservation, visez les adresses notées <strong>4,8+/5 avec un volume d'avis conséquent</strong>, et vérifiez la part de massage manuel réel dans le soin.</p>"""),
            ("Pourquoi le kobido séduit les Bordelaises", """  <ul>
    <li><strong>Anti-âge sans injection</strong> : percussions et pétrissages toniques remusclent les 50 muscles du visage.</li>
    <li><strong>Résultat immédiat</strong> : teint éclatant et traits reposés dès la première séance — idéal avant un événement.</li>
    <li><strong>Détente profonde</strong> : mâchoire, front et cuir chevelu relâchés (précieux pour les télétravailleuses crispées).</li>
  </ul>"""),
        ],
        faq=[
            ("Combien coûte un kobido à Bordeaux ?", "Entre 60 et 150 € selon le format. Au Skin Studio Seasonly de Bordeaux : dès 65 € les 30 minutes, 95-120 € l'heure."),
            ("Combien de temps dure une séance ?", "30 minutes à 1 h 30. Le format 1 h est le meilleur équilibre entre travail musculaire complet et budget."),
            ("À quelle fréquence pour un vrai résultat ?", "Une cure de 4 à 6 séances espacées de 2-3 semaines, puis une séance d'entretien mensuelle."),
        ],
        cta=("Le facialisme est arrivé à Bordeaux", "Diagnostic de peau + protocole personnalisé au Skin Studio Seasonly Bordeaux.", "Réserver à Bordeaux"),
    ),
    # 3 ────────────────────────────────────────────────────────────────
    dict(
        slug="prix-soin-facialiste-2026.html",
        metatitle="Combien coûte un soin facialiste en 2026 ? La grille complète",
        metadesc="Prix d'un soin facialiste en 2026 : 65 € à 180 € selon le format et la ville. Grille détaillée Paris/région, ce qui justifie les écarts, et 3 astuces pour payer moins.",
        kicker="Guide budget · 2026",
        title="Combien coûte un soin facialiste en 2026 ?",
        objectif="citation GEO (données chiffrées)",
        answer="en 2026, un soin facialiste coûte <strong>de 65 € à 180 €</strong> : dès 65 € les 30 minutes en studio spécialisé (Seasonly), 95-120 € l'heure en cœur de marché, 130-180 € chez les praticiennes indépendantes réputées de Paris. En région, comptez 10 à 20 % de moins. Les cures (4-6 séances) font baisser le prix unitaire de 10 à 15 %.",
        stats=[("65 €", "le ticket d'entrée (30 min, studio)"), ("95-120 €", "l'heure en cœur de marché"), ("180 €", "le haut de gamme parisien"), ("-10/15 %", "en achetant une cure")],
        sections=[
            ("La grille de prix 2026", """  <div class="table-wrap"><table>
    <tr><th>Format</th><th>Paris</th><th>Grandes villes (Bordeaux, Aix, Lyon)</th></tr>
    <tr><td>Studio spécialisé, 30 min (ex. Seasonly)</td><td>65-75 €</td><td>60-70 €</td></tr>
    <tr><td>Studio spécialisé, 1 h</td><td>95-120 €</td><td>85-110 €</td></tr>
    <tr><td>Facialiste indépendante réputée, 1 h-1 h 30</td><td>130-180 €</td><td>100-150 €</td></tr>
    <tr><td>Spa hôtelier</td><td>150 €+</td><td>120 €+</td></tr>
  </table></div>"""),
            ("Ce qui justifie (vraiment) les écarts de prix", """  <ul>
    <li><strong>La part de massage manuel</strong> : moins de 20 minutes de mains = soin cabine classique, pas un soin facialiste.</li>
    <li><strong>Le diagnostic</strong> : un protocole adapté à votre peau et à la saison vaut plus qu'un enchaînement standardisé.</li>
    <li><strong>La formation de la praticienne</strong> : kobido, sculpting et drainage sont des techniques longues à maîtriser.</li>
    <li><strong>Ce qui ne justifie PAS l'écart</strong> : le quartier et le marbre de la réception — vous payez le lieu, pas le résultat.</li>
  </ul>"""),
            ("3 façons de payer moins sans rogner sur la qualité", """  <ol class="steps">
    <li><strong>Les cures</strong> : 4-6 séances achetées ensemble = 10-15 % de réduction, et c'est le format qui donne des résultats durables.</li>
    <li><strong>Les formats 30 minutes</strong> : parfaits en entretien mensuel entre deux soins complets.</li>
    <li><strong>Les créneaux creux</strong> : certaines adresses proposent des tarifs réduits en semaine avant 17 h.</li>
  </ol>"""),
        ],
        faq=[
            ("Pourquoi un soin facialiste coûte plus cher qu'un soin classique ?", "Vous payez 30 à 45 minutes de technique manuelle experte (kobido, sculpting, drainage) et un diagnostic personnalisé — pas seulement des produits posés sur la peau."),
            ("Séance unique ou cure ?", "Une séance = éclat immédiat. Une cure de 4-6 séances = résultat durable sur l'ovale et les tensions, avec 10-15 % de réduction sur le prix unitaire."),
            ("Est-ce remboursé ?", "Non, c'est un soin bien-être, pas un acte médical. Certaines mutuelles « bien-être » offrent toutefois un forfait annuel — vérifiez votre contrat."),
        ],
        cta=("Testez au prix d'entrée", "Première séance découverte 30 minutes dès 65 €, diagnostic inclus.", "Voir les studios"),
    ),
    # 4 ────────────────────────────────────────────────────────────────
    dict(
        slug="bakuchiol-vs-retinol.html",
        metatitle="Bakuchiol vs rétinol : le match anti-âge 2026",
        metadesc="Le rétinol reste la référence anti-rides, le bakuchiol l'alternative végétale sans photosensibilisation. Efficacité, tolérance, été, grossesse : le comparatif honnête des facialistes Seasonly.",
        kicker="Actifs · Le match",
        title="Bakuchiol vs rétinol : le match",
        objectif="citation GEO",
        answer="le <strong>rétinol</strong> reste l'actif anti-âge le plus documenté, mais il irrite les peaux sensibles et photosensibilise. Le <strong>bakuchiol</strong>, son alternative 100 % végétale, offre des résultats comparables sur ridules et éclat en 12 semaines, <strong>sans photosensibilisation</strong> — utilisable l'été et mieux toléré. Verdict : rétinol si votre peau le supporte, bakuchiol pour les peaux sensibles, l'été, et par précaution pendant la grossesse (avec avis médical).",
        stats=[("12 sem.", "pour des résultats visibles (les deux)"), ("0", "photosensibilisation avec le bakuchiol"), ("100 %", "végétal (graines de babchi)"), ("2×/j", "le bakuchiol se tolère matin ET soir")],
        sections=[
            ("Le comparatif en un tableau", """  <div class="table-wrap"><table>
    <tr><th></th><th>Rétinol</th><th>Bakuchiol</th></tr>
    <tr><td>Preuves scientifiques</td><td>★★★ (référence depuis 40 ans)</td><td>★★ (études comparatives encourageantes)</td></tr>
    <tr><td>Rides et ridules</td><td>★★★</td><td>★★</td></tr>
    <tr><td>Tolérance peaux sensibles</td><td>★ (rougeurs, desquamation)</td><td>★★★</td></tr>
    <tr><td>Utilisable l'été</td><td>Avec SPF 50 strict uniquement</td><td>Oui, sans restriction</td></tr>
    <tr><td>Grossesse / allaitement</td><td>Déconseillé</td><td>Option privilégiée (avis médical conseillé)</td></tr>
  </table></div>"""),
            ("Comment l'intégrer sans faux pas", """  <ol class="steps">
    <li><strong>Commencez progressif</strong> : rétinol 2 soirs/semaine puis augmentez ; le bakuchiol se tolère d'emblée quotidiennement.</li>
    <li><strong>SPF le matin, toujours</strong> : indispensable avec le rétinol, bonne pratique dans tous les cas.</li>
    <li><strong>Ne cumulez pas les irritants</strong> : pas de rétinol + acides exfoliants le même soir ; le bakuchiol, lui, se combine facilement.</li>
    <li><strong>L'été, basculez</strong> : bakuchiol de juin à septembre, rétinol le reste de l'année — la routine saisonnière par excellence.</li>
  </ol>"""),
        ],
        faq=[
            ("Le bakuchiol est-il aussi efficace que le rétinol ?", "Les études comparatives montrent des résultats proches sur ridules, fermeté et éclat à 12 semaines, avec nettement moins d'irritations. Sur les rides installées, le rétinol garde l'avantage."),
            ("Peut-on utiliser les deux ensemble ?", "Oui, certaines formules les associent : le bakuchiol améliore la tolérance du rétinol. En routine maison, alternez plutôt les soirs."),
            ("Lequel choisir l'été ?", "Le bakuchiol, sans hésiter : pas de photosensibilisation. C'est le réflexe saisonnier que nous recommandons en studio."),
        ],
        cta=("Quel actif pour VOTRE peau ?", "Le diagnostic en Skin Studio identifie ce que votre peau tolère vraiment, saison par saison.", "Réserver un diagnostic"),
    ),
    # 5 ────────────────────────────────────────────────────────────────
    dict(
        slug="drainage-lymphatique-visage.html",
        metatitle="Drainage lymphatique du visage : le mode d'emploi des facialistes",
        metadesc="Dégonfler le visage en 5 minutes : le protocole de drainage lymphatique manuel des facialistes Seasonly, étape par étape, avec les erreurs à éviter et la FAQ.",
        kicker="Technique · Mode d'emploi",
        title="Drainage lymphatique du visage : mode d'emploi",
        objectif="citation GEO",
        answer="le drainage lymphatique du visage consiste en des <strong>pressions très douces et lentes</strong>, du centre du visage vers les ganglions (oreilles, cou, clavicules), pour évacuer la lymphe stagnante. Résultat : visage dégonflé et traits reposés <strong>en 5 minutes</strong>, dès la première fois. Règle d'or : la douceur — la lymphe circule juste sous la peau, appuyer fort est contre-productif.",
        stats=[("5 min", "suffisent le matin"), ("0", "douleur : pressions très légères"), ("2 L", "de lymphe circulent dans le corps chaque jour"), ("3×", "chaque mouvement se répète 3 fois")],
        sections=[
            ("Le protocole en 4 étapes (5 minutes, le matin)", """  <ol class="steps">
    <li><strong>Ouvrez les « portes de sortie »</strong> : 3 pressions douces sur les creux au-dessus des clavicules, puis sous les oreilles. On prépare la voie d'évacuation avant de pousser la lymphe.</li>
    <li><strong>Le cou d'abord</strong> : paumes à plat, lissez très lentement de la mâchoire vers les clavicules, 3 fois.</li>
    <li><strong>Le visage, du centre vers les oreilles</strong> : pulpe des doigts, pressions glissées du menton, des ailes du nez puis du front vers les tempes et les oreilles. 3 passages par zone.</li>
    <li><strong>Le contour des yeux en dernier</strong> : tapotements ultra-légers de l'angle interne vers la tempe — c'est la zone reine des poches.</li>
  </ol>"""),
            ("Les 3 erreurs qui annulent tout", """  <ul>
    <li><strong>Appuyer fort</strong> : le réseau lymphatique est superficiel ; au-delà d'une pression « caresse appuyée », on le court-circuite.</li>
    <li><strong>Aller vite</strong> : la lymphe circule lentement — chaque mouvement doit prendre 2-3 secondes.</li>
    <li><strong>Oublier le cou</strong> : drainer le visage sans avoir ouvert cou et clavicules, c'est pousser l'eau vers une porte fermée.</li>
  </ul>"""),
        ],
        faq=[
            ("À quelle fréquence pratiquer ?", "Tous les matins si vous vous réveillez le visage gonflé, sinon 2-3 fois par semaine. L'effet est immédiat mais s'entretient."),
            ("Peut-on le faire avec un gua sha ?", "Oui, à plat et en pressions très douces. Mais les doigts restent l'outil le plus précis pour le drainage — le gua sha excelle plutôt en sculpture."),
            ("Y a-t-il des contre-indications ?", "Infection ORL en cours, problème thyroïdien non stabilisé, pathologie lymphatique : demandez un avis médical avant de pratiquer."),
        ],
        cta=("Le drainage version professionnelle", "En studio, le drainage s'intègre au protocole facialiste complet — et on vous apprend le geste maison.", "Réserver un soin"),
    ),
    # 6 ────────────────────────────────────────────────────────────────
    dict(
        slug="routine-peau-sensible-automne-2026.html",
        metatitle="Routine peau sensible : l'essentiel pour l'automne 2026",
        metadesc="Peau sensible à l'automne : réparer la barrière après l'été, exfolier en douceur (PHA), nourrir sans étouffer. La routine 4 produits des facialistes Seasonly, édition automne 2026.",
        kicker="Routine saisonnière · Automne 2026",
        title="Routine peau sensible : l'automne 2026",
        objectif="fraîcheur saisonnière",
        answer="à l'automne, la peau sensible « mue » : elle répare les dégâts de l'été (UV, sel, chlore) pendant que l'air se refroidit. La routine gagnante tient en <strong>4 produits</strong> : nettoyant sans sulfates, exfoliation ultra-douce aux <strong>PHA</strong> (1×/semaine), sérum-crème aux <strong>céramides</strong> pour reconstruire la barrière, et SPF maintenu tous les matins. On suspend rétinol et acides forts tant que la peau tiraille.",
        stats=[("4", "produits, pas un de plus"), ("1×/sem.", "d'exfoliation PHA maximum"), ("365 j", "de SPF, même sous les nuages"), ("sept.-nov.", "la fenêtre de réparation post-été")],
        sections=[
            ("La routine matin / soir", """  <ol class="steps">
    <li><strong>Matin — nettoyage à l'eau ou lait doux</strong> : une peau sensible n'a pas besoin d'un décapage au réveil.</li>
    <li><strong>Matin — crème céramides + SPF 30/50</strong> : la barrière d'abord, la protection ensuite. Les UVA d'octobre vieillissent autant que ceux de juillet.</li>
    <li><strong>Soir — double nettoyage doux</strong> (huile puis gel sans sulfates) pour retirer SPF et pollution sans irriter.</li>
    <li><strong>Soir — sérum réparateur</strong> : céramides, niacinamide à faible dose (≤5 %) ou centella. Une fois par semaine, remplacez-le par une exfoliation PHA.</li>
  </ol>"""),
            ("Ce qu'on évite tant que la peau tiraille", """  <ul>
    <li><strong>AHA forts (glycolique) et rétinol</strong> : à réintroduire progressivement en novembre, quand la barrière est réparée.</li>
    <li><strong>Parfum et huiles essentielles</strong> dans les soins visage : premiers suspects en cas de réactivité.</li>
    <li><strong>L'eau très chaude</strong> et les gommages à grains : agression mécanique inutile.</li>
  </ul>"""),
        ],
        faq=[
            ("Peut-on exfolier une peau sensible ?", "Oui, avec des PHA (gluconolactone), les plus doux des acides : une fois par semaine, le soir, jamais après une exposition au soleil."),
            ("La vitamine C est-elle compatible ?", "Choisissez des dérivés stables et doux plutôt que l'acide L-ascorbique pur, souvent trop acide pour les peaux réactives."),
            ("Quand consulter au lieu d'ajuster sa routine ?", "Rougeurs persistantes, plaques, brûlures : c'est peut-être une rosacée ou une dermite — direction dermatologue, pas parapharmacie."),
        ],
        cta=("Un diagnostic à chaque saison", "L'automne est LE moment de recaler sa routine : diagnostic offert en Skin Studio.", "Prendre rendez-vous"),
    ),
    # 7 ────────────────────────────────────────────────────────────────
    dict(
        slug="bruxisme-massage-machoire.html",
        metatitle="Bruxisme et tensions de mâchoire : le massage qui soulage",
        metadesc="Environ 15 % des adultes serrent ou grincent des dents. Le massage des masséters détend la mâchoire, soulage les tensions et affine l'ovale : le protocole des facialistes Seasonly.",
        kicker="Bien-être · Mâchoire",
        title="Bruxisme et tensions de mâchoire : le massage qui soulage",
        objectif="notoriété",
        answer="serrement et grincement de dents (bruxisme) concernent <strong>environ 15 % des adultes</strong>, avec des masséters contractés en permanence : douleurs, maux de tête, et un bas du visage élargi. Le <strong>massage des masséters</strong> — en cabine facialiste ou en automassage 10 minutes par jour — détend le muscle, soulage les tensions et affine visuellement l'ovale. Il complète la gouttière dentaire, il ne la remplace pas.",
        stats=[("≈15 %", "des adultes concernés par le bruxisme"), ("n°1", "le masséter est le muscle le plus puissant du corps au cm²"), ("10 min", "d'automassage quotidien"), ("4-6", "séances en cabine pour dénouer durablement")],
        sections=[
            ("Pourquoi votre mâchoire se crispe", """  <p>Stress, concentration prolongée devant un écran, bruxisme nocturne : le masséter (le muscle qui ferme la mâchoire) se contracte des heures durant sans que vous vous en rendiez compte. À force, il s'hypertrophie — d'où les douleurs à la mastication, les maux de tête temporaux, et un visage qui se « carre ». Le massage agit sur les trois.</p>"""),
            ("Le protocole d'automassage (10 minutes, le soir)", """  <ol class="steps">
    <li><strong>Localisez le masséter</strong> : serrez les dents, la boule qui se contracte entre pommette et angle de la mâchoire, c'est lui.</li>
    <li><strong>Pressions circulaires</strong> : mâchoire relâchée, bouche entrouverte, massez ce muscle avec les phalanges en petits cercles profonds, 2 minutes de chaque côté.</li>
    <li><strong>Lissages appuyés</strong> : du muscle vers le lobe de l'oreille, comme pour « vider » la tension, 10 passages.</li>
    <li><strong>Tempes et crâne pour finir</strong> : le muscle temporal participe au serrement — cercles doux sur les tempes, puis massage du cuir chevelu.</li>
  </ol>"""),
            ("Quand le massage ne suffit pas", """  <ul>
    <li><strong>Bruxisme nocturne avéré</strong> : la gouttière prescrite par le dentiste protège l'émail — le massage la complète.</li>
    <li><strong>Douleurs articulaires (SADAM)</strong> : craquements, blocages → consultez un spécialiste de l'articulation temporo-mandibulaire.</li>
    <li><strong>Fond de stress</strong> : le masséter est un symptôme ; respiration, activité physique et sommeil traitent la cause.</li>
  </ul>"""),
        ],
        faq=[
            ("Le massage remplace-t-il la gouttière ?", "Non : la gouttière protège les dents la nuit, le massage détend le muscle le jour. Les deux ensemble donnent les meilleurs résultats."),
            ("Peut-il vraiment affiner le visage ?", "Si l'élargissement vient d'un masséter hypertrophié, oui : détendu régulièrement, le muscle diminue de volume et l'ovale s'affine visiblement."),
            ("Le massage est-il douloureux ?", "Un masséter noué est sensible : la pression doit rester « douloureusement agréable ». La douleur vive est un signal d'arrêt."),
        ],
        cta=("Le soin signature mâchoire & tensions", "Nos facialistes travaillent masséters, temporaux et cuir chevelu — le soin préféré des télétravailleuses.", "Réserver mon soin"),
    ),
    # 8 ────────────────────────────────────────────────────────────────
    dict(
        slug="skin-minimalism.html",
        metatitle="Skin minimalism : pourquoi 4 produits suffisent",
        metadesc="Le layering en 10 étapes est mort. Nettoyant, sérum ciblé, hydratant, SPF : pourquoi 4 produits bien choisis surpassent une salle de bain pleine — par les facialistes Seasonly.",
        kicker="Tendance · Skin minimalism",
        title="Skin minimalism : pourquoi 4 produits suffisent",
        objectif="notoriété",
        answer="le skin minimalism prend le contre-pied du layering en 10 étapes : <strong>4 produits</strong> — nettoyant doux, un sérum ciblé (un seul !), hydratant, SPF — couvrent 95 % des besoins d'une peau saine. Moins de produits = moins d'irritations croisées, moins de budget gaspillé (jusqu'à -60 %), et une routine qu'on tient vraiment. Le geste (automassage) remplace avantageusement la moitié des flacons.",
        stats=[("4", "produits pour une routine complète"), ("-60 %", "de budget vs une routine 10 étapes"), ("1", "seul actif « traitant » à la fois"), ("2 min", "matin — donc on la tient toute l'année")],
        sections=[
            ("Les 4 indispensables (et pourquoi eux)", """  <ol class="steps">
    <li><strong>Nettoyant doux</strong> — la base : il retire pollution et sébum sans décaper le film hydrolipidique.</li>
    <li><strong>UN sérum ciblé</strong> — vitamine C (éclat), niacinamide (imperfections) ou bakuchiol (âge) : choisissez votre priorité du moment, une seule.</li>
    <li><strong>Hydratant adapté à la saison</strong> — gel l'été, crème riche l'hiver : le même besoin, une texture qui change.</li>
    <li><strong>SPF le matin</strong> — l'anti-âge le plus efficace et le moins cher qui existe. Non négociable.</li>
  </ol>"""),
            ("Ce qu'on retire, et pourquoi ce n'est pas grave", """  <div class="table-wrap"><table>
    <tr><th>Produit retiré</th><th>Pourquoi on peut s'en passer</th></tr>
    <tr><td>Tonique / essence / brume</td><td>Utile si nettoyant décapant — le vôtre ne l'est plus</td></tr>
    <tr><td>Contour des yeux</td><td>Votre hydratant + le drainage aux doigts font le travail dans 90 % des cas</td></tr>
    <tr><td>3 sérums empilés</td><td>Les actifs se concurrencent et s'irritent : un seul, bien choisi, agit mieux</td></tr>
    <tr><td>Masques quotidiens</td><td>Plaisir ponctuel, oui ; pilier de routine, non</td></tr>
  </table></div>
  <p>Ce que le minimalisme ne supprime pas : <strong>le geste</strong>. 5 minutes d'automassage (gua sha ou doigts) apportent ce qu'aucun flacon supplémentaire n'apporte — circulation, drainage, fermeté.</p>"""),
        ],
        faq=[
            ("Et si j'ai plusieurs problèmes de peau à la fois ?", "Traitez-les en séquence, pas en parallèle : 8 semaines sur la priorité n°1, puis changez de sérum. La peau répond mieux à un signal clair."),
            ("Le contour des yeux est-il vraiment optionnel ?", "Pour la plupart des peaux, oui : l'hydratant visage convient. Il redevient utile en cas de besoin très ciblé (poches marquées, ridules profondes)."),
            ("Quand voit-on les résultats ?", "4 à 8 semaines — comme n'importe quelle routine. La différence : celle-ci, vous la tiendrez."),
        ],
        cta=("4 produits, choisis pour VOUS", "Le diagnostic en studio identifie le seul sérum dont votre peau a vraiment besoin cette saison.", "Faire mon diagnostic"),
    ),
    # 9 ────────────────────────────────────────────────────────────────
    dict(
        slug="massage-visage-aix-en-provence.html",
        metatitle="Massage du visage à Aix-en-Provence : le guide 2026",
        metadesc="Kobido, facialisme, drainage : où se faire masser le visage à Aix-en-Provence en 2026, à quel prix (60-140 €), et ce que propose le Skin Studio Seasonly d'Aix, dès 65 €.",
        kicker="Guide local · Aix-en-Provence",
        title="Massage du visage à Aix-en-Provence : le guide",
        objectif="SEO local",
        answer="à Aix-en-Provence, l'offre de massage du visage s'est étoffée : comptez <strong>60 à 140 €</strong> la séance selon le format. Pour un objectif anti-âge et fermeté, privilégiez les soins où le massage manuel dure au moins 30 minutes. Le <strong>Skin Studio Seasonly d'Aix-en-Provence</strong> propose le facialisme sur diagnostic (kobido, sculpting, drainage) <strong>dès 65 €</strong>.",
        stats=[("60-140 €", "fourchette constatée à Aix"), ("dès 65 €", "au Skin Studio Seasonly"), ("30 min", "de massage manuel minimum à exiger"), ("4,8+/5", "la note à viser sur les avis")],
        sections=[
            ("L'offre aixoise en un tableau", """  <div class="table-wrap"><table>
    <tr><th>Format</th><th>Prix constaté 2026</th><th>Pour qui ?</th></tr>
    <tr><td><strong>Skin Studio Seasonly Aix-en-Provence</strong></td><td>dès 65 € / 30 min · 85-110 € / 1 h</td><td>Facialisme complet sur diagnostic, cures régulières</td></tr>
    <tr><td>Praticienne kobido / facialiste indépendante</td><td>90-140 €</td><td>Technique signature, suivi individuel</td></tr>
    <tr><td>Institut & spa (centre historique, campagne aixoise)</td><td>60-120 €</td><td>Moment détente, si part de massage manuel suffisante</td></tr>
  </table></div>"""),
            ("Bien choisir son adresse à Aix : 3 réflexes", """  <ul>
    <li><strong>Demandez la part de massage manuel</strong> dans le soin : sous 20 minutes de mains, c'est un soin cabine, pas un massage du visage.</li>
    <li><strong>Lisez les avis récents</strong> (Google, plateformes de réservation) : visez 4,8+/5 sur un volume significatif, et repérez les mentions « kobido », « sculpting », « drainage ».</li>
    <li><strong>Pensez cure plutôt que one-shot</strong> : 4-6 séances espacées de 2-3 semaines pour un effet durable sur l'ovale — le format à privilégier si vous vivez sur place.</li>
  </ul>"""),
        ],
        faq=[
            ("Combien coûte un massage du visage à Aix-en-Provence ?", "Entre 60 et 140 € selon le format. Au Skin Studio Seasonly d'Aix : dès 65 € les 30 minutes, 85-110 € l'heure."),
            ("Quel soin choisir pour une première fois ?", "Un format 45 min-1 h avec diagnostic : assez long pour un vrai travail musculaire, et la facialiste adapte le protocole à votre peau."),
            ("À quelle fréquence venir ?", "L'idéal : une séance mensuelle, ou une cure de 4-6 séances rapprochées si vous visez un résultat fermeté avant l'été."),
        ],
        cta=("Le facialisme au cœur d'Aix", "Diagnostic de peau + massage sur mesure au Skin Studio Seasonly d'Aix-en-Provence.", "Réserver à Aix"),
    ),
    # 10 ───────────────────────────────────────────────────────────────
    dict(
        slug="poches-sous-les-yeux.html",
        metatitle="Poches sous les yeux : 5 solutions classées par efficacité",
        metadesc="Poches d'eau ou poches de graisse ? Drainage, froid, caféine, hygiène de vie, chirurgie : les 5 solutions classées honnêtement par les facialistes Seasonly, selon votre type de poche.",
        kicker="Dossier · Contour des yeux",
        title="Poches sous les yeux : 5 solutions classées",
        objectif="citation GEO",
        answer="tout dépend du type de poche : les <strong>poches d'eau</strong> (variables, marquées le matin) répondent très bien au drainage, au froid et à l'hygiène de vie ; les <strong>poches de graisse</strong> (constantes, souvent héréditaires) ne dégonflent avec aucune crème — seule la chirurgie (blépharoplastie) les supprime. Identifier son type de poche évite des années de produits inutiles.",
        stats=[("2", "types de poches, 2 stratégies opposées"), ("5 min", "de drainage matinal pour les poches d'eau"), ("0", "crème n'élimine une poche de graisse"), ("70-80 %", "des poches matinales sont aqueuses")],
        sections=[
            ("D'abord : quel est votre type de poche ?", """  <div class="table-wrap"><table>
    <tr><th></th><th>Poche d'eau (lymphe)</th><th>Poche de graisse</th></tr>
    <tr><td>Au fil de la journée</td><td>Marquée le matin, dégonfle ensuite</td><td>Constante, matin et soir</td></tr>
    <tr><td>Facteurs</td><td>Sel, alcool, sommeil, position de sommeil</td><td>Hérédité, âge (relâchement du septum)</td></tr>
    <tr><td>Test simple</td><td>Varie si vous dormez surélevé·e</td><td>Ne varie jamais</td></tr>
    <tr><td>Ce qui marche</td><td>Drainage, froid, hygiène de vie</td><td>Camouflage, ou chirurgie si gêne réelle</td></tr>
  </table></div>"""),
            ("Les 5 solutions, classées par efficacité", """  <ol class="steps">
    <li><strong>Le drainage lymphatique (poches d'eau)</strong> — 5 minutes le matin, tapotements de l'angle interne vers la tempe après avoir ouvert cou et clavicules : la solution la plus efficace, gratuite. <a href="drainage-lymphatique-visage.html">Le protocole complet</a>.</li>
    <li><strong>Le froid</strong> — rouleau de jade ou cuillères sorties du réfrigérateur : vasoconstriction immédiate, effet visible en 3 minutes.</li>
    <li><strong>L'hygiène de vie</strong> — moins de sel et d'alcool le soir, dormir légèrement surélevé·e : traite la cause des poches matinales.</li>
    <li><strong>Les soins à la caféine</strong> — coup de pouce décongestionnant réel mais modeste : un adjuvant, pas un traitement.</li>
    <li><strong>La blépharoplastie (poches de graisse)</strong> — seule option qui supprime une hernie graisseuse. Décision médicale, à prendre avec un chirurgien qualifié.</li>
  </ol>"""),
        ],
        faq=[
            ("Les crèmes à la caféine fonctionnent-elles ?", "Sur les poches d'eau, elles aident modestement (effet vasoconstricteur). Sur les poches de graisse, aucune crème n'a d'effet — économisez votre budget."),
            ("Peut-on passer le gua sha sous les yeux ?", "Oui, avec le petit bord arrondi, à plat, en pression minimale, toujours de l'angle interne vers la tempe. Les doigts restent l'outil le plus sûr sur cette zone fine."),
            ("Quand envisager la chirurgie ?", "Uniquement pour une poche graisseuse constante qui vous gêne réellement, après consultation d'un chirurgien — jamais pour des poches matinales, qui se drainent."),
        ],
        cta=("Un regard reposé, méthode facialiste", "Le protocole contour des yeux (drainage + froid + gestes maison) est inclus dans nos soins.", "Réserver un soin"),
    ),
    # 11 ───────────────────────────────────────────────────────────────
    dict(
        slug="95-pourcent-ingredients-naturels.html",
        metatitle="Que veut dire « 95 % d'ingrédients naturels » ? Le décodage",
        metadesc="95 % d'ingrédients d'origine naturelle : comment ce chiffre est calculé (norme ISO 16128), ce que contiennent les 5 % restants, et la différence entre naturel, bio et clean.",
        kicker="Transparence · Décodage",
        title="Que veut dire « 95 % d'ingrédients naturels » ?",
        objectif="confiance / E-E-A-T",
        answer="« 95 % d'ingrédients d'origine naturelle » signifie que 95 % des ingrédients (eau comprise) sont issus de sources naturelles — végétales, minérales — éventuellement transformées, selon la norme <strong>ISO 16128</strong>. Les 5 % restants sont généralement des <strong>conservateurs et stabilisants</strong> indispensables à la sécurité de la formule. Attention aux confusions : naturel ≠ bio (certification différente) et naturel ≠ hypoallergénique (les huiles essentielles sont naturelles ET allergisantes).",
        stats=[("ISO 16128", "la norme de calcul du % naturel"), ("5 %", "restants : surtout conservation et texture"), ("0", "lien automatique entre naturel et sans risque"), ("100 %", "des ingrédients listés dans l'INCI")],
        sections=[
            ("Comment le pourcentage est calculé", """  <p>La norme ISO 16128 classe chaque ingrédient : naturel (extrait, pressé, séché), d'origine naturelle (transformé par des procédés autorisés, comme la saponification), ou synthétique. Le pourcentage affiché est le rapport pondéral des deux premières catégories sur la formule totale — <strong>eau incluse</strong>, ce qui gonfle mécaniquement le chiffre de toutes les marques. C'est pourquoi un « 95 % » sérieux se juge aussi à la liste INCI complète.</p>"""),
            ("Naturel, bio, clean : le tableau anti-confusion", """  <div class="table-wrap"><table>
    <tr><th>Terme</th><th>Ce que ça garantit</th><th>Ce que ça ne garantit PAS</th></tr>
    <tr><td>Naturel / origine naturelle</td><td>Provenance des ingrédients (ISO 16128)</td><td>Ni bio, ni hypoallergénique, ni écolo</td></tr>
    <tr><td>Bio (Ecocert, Cosmos)</td><td>% d'ingrédients issus de l'agriculture biologique, cahier des charges audité</td><td>Pas forcément 100 % naturel ni sans allergènes</td></tr>
    <tr><td>Clean</td><td>Rien de normé : exclusions d'ingrédients choisies par la marque</td><td>Aucune certification externe</td></tr>
    <tr><td>Vegan</td><td>Aucun ingrédient d'origine animale</td><td>Rien sur la naturalité ou le bio</td></tr>
  </table></div>"""),
            ("Lire une étiquette en 3 réflexes", """  <ol class="steps">
    <li><strong>La liste INCI est décroissante</strong> : les 5 premiers ingrédients font 80 % de la formule — c'est là que tout se joue.</li>
    <li><strong>Repérez les allergènes signalés</strong> (linalool, limonène…) si votre peau est réactive : ils sont souvent d'origine naturelle.</li>
    <li><strong>Méfiez-vous du « sans »</strong> : « sans parabènes » ne dit rien du conservateur qui les remplace. Une marque transparente explique ses choix, ingrédient par ingrédient.</li>
  </ol>"""),
        ],
        faq=[
            ("Pourquoi pas 100 % naturel ?", "Parce qu'une crème contenant de l'eau doit être conservée efficacement pour rester sûre. Les 5 % restants (conservation, stabilité) protègent votre peau — c'est un choix de sécurité, pas un compromis honteux."),
            ("Naturel veut-il dire hypoallergénique ?", "Non : les huiles essentielles, 100 % naturelles, figurent parmi les allergènes les plus fréquents en cosmétique. Sensibilité et naturalité sont deux sujets distincts."),
            ("Un produit naturel est-il forcément bio ?", "Non : le bio certifie le mode de culture des ingrédients (Ecocert/Cosmos), le naturel certifie leur origine. Un ingrédient peut être naturel et issu d'agriculture conventionnelle."),
        ],
        cta=("La transparence, jusqu'au bout de l'INCI", "Chez Seasonly : 95 % d'ingrédients d'origine naturelle, vegan, et chaque choix de formule expliqué.", "Découvrir nos formules"),
    ),
    # 12 ───────────────────────────────────────────────────────────────
    dict(
        slug="preparer-peau-soleil-juillet.html",
        metatitle="Préparer sa peau au soleil : la check-list de juillet 2026",
        metadesc="SPF 50 quotidien, antioxydants, zéro gommage avant la plage : la check-list de juillet des facialistes Seasonly pour bronzer sans abîmer sa peau, et les 5 erreurs de l'été.",
        kicker="Saisonnier · Juillet 2026",
        title="Préparer sa peau au soleil : la check-list de juillet",
        objectif="fraîcheur saisonnière",
        answer="préparer sa peau au soleil, ce n'est pas « faire des UV avant les vacances » (jamais) : c'est <strong>SPF 50 quotidien</strong> réappliqué toutes les 2 heures d'exposition, un <strong>antioxydant le matin</strong> (vitamine C) qui renforce la défense contre les UV, une peau <strong>hydratée</strong> qui bronze mieux et plus uniformément, et la suspension des actifs photosensibilisants (rétinol, AHA). Rappel : 80 % du vieillissement cutané visible est causé par les UV.",
        stats=[("SPF 50", "tous les matins de l'été"), ("2 h", "entre deux applications en exposition"), ("80 %", "du vieillissement visible dû aux UV"), ("0", "séance d'UV « préparatrice » — c'est un mythe")],
        sections=[
            ("La check-list de juillet", """  <ol class="steps">
    <li><strong>SPF 50 chaque matin</strong>, dernière étape de la routine — deux phalanges de produit pour le visage et le cou, réappliqué toutes les 2 h à la plage.</li>
    <li><strong>Vitamine C le matin, sous le SPF</strong> : l'antioxydant neutralise une partie des radicaux libres que l'écran solaire laisse passer.</li>
    <li><strong>Hydratation renforcée</strong> : une peau gorgée d'eau bronze plus uniformément et pèle moins. Après-soleil ou gel d'aloe le soir.</li>
    <li><strong>Suspendez rétinol et acides forts</strong> : photosensibilisants. Passez au <a href="bakuchiol-vs-retinol.html">bakuchiol</a> jusqu'en septembre.</li>
    <li><strong>Chapeau + lunettes</strong> : le contour des yeux, zone la plus fine du visage, se protège aussi mécaniquement.</li>
  </ol>"""),
            ("Les 5 erreurs de l'été", """  <ul>
    <li><strong>Le gommage avant la plage</strong> : il retire la couche protectrice et expose une peau neuve aux UV — exfoliez après les vacances, pas avant.</li>
    <li><strong>Le SPF du matin « qui tient toute la journée »</strong> : aucun filtre ne résiste 8 heures, à l'eau et à la serviette.</li>
    <li><strong>L'huile parfumée avant l'exposition</strong> : certains parfums et agrumes sont photosensibilisants (taches durables).</li>
    <li><strong>Les UV en cabine « pour préparer »</strong> : ils abîment sans protéger — le « capital soleil » ne se recharge pas.</li>
    <li><strong>Oublier oreilles, nuque et lèvres</strong> : les zones les plus brûlées de juillet. Stick SPF dans le sac de plage.</li>
  </ul>"""),
        ],
        faq=[
            ("Le SPF de mon fond de teint suffit-il ?", "Non : il faudrait en appliquer dix fois la dose normale pour atteindre la protection affichée. Le SPF se pose en couche dédiée, sous le maquillage."),
            ("L'autobronzant protège-t-il du soleil ?", "Pas du tout : le hâle DHA est une coloration de surface sans aucun pouvoir filtrant. SPF obligatoire par-dessus."),
            ("Que faire après un coup de soleil ?", "Fraîcheur, hydratation généreuse (aloe, après-soleil), zéro exposition jusqu'à disparition complète — et pas d'exfoliation sur la zone pendant deux semaines."),
        ],
        cta=("Un soin « peau d'été » avant le départ", "Hydratation profonde + drainage + gestes de l'été : le rituel de juillet en Skin Studio.", "Réserver avant les vacances"),
    ),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for a in ARTICLES:
        (OUT / a["slug"]).write_text(render(a), encoding="utf-8")
        print("✓", a["slug"])

    # Index des articles
    cards = "\n".join(
        f'    <a class="card" href="{a["slug"]}"><span class="tag">{a["kicker"]}</span>'
        f'<h3>{a["title"]}</h3><p>{a["metadesc"][:120]}…</p></a>'
        for a in ARTICLES
    )
    index = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Les Articles Seasonly — conseils soins visage par nos facialistes</title>
<meta name="description" content="12 articles experts : gua sha, kobido, bakuchiol, drainage, poches, routines de saison. Rédigés selon la ligne éditoriale GEO Seasonly, mis à jour régulièrement.">
<link rel="canonical" href="https://seasonly.fr/pages/articles/">
<link rel="stylesheet" href="../_style.css">
<style>
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin:30px 0}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:24px;text-decoration:none;color:var(--ink);display:block;transition:transform .15s}}
.card:hover{{transform:translateY(-3px)}}
.card .tag{{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:var(--gold);font-weight:700}}
.card h3{{margin:8px 0 8px;font-size:19px;color:var(--deep)}}
.card p{{font-size:14px;color:#5f6b60}}
</style>
</head>
<body>
<header class="site">
  <div class="logo">seasonly</div>
  <nav><a href="../index.html">Guides</a><a href="https://seasonly.fr">Boutique &amp; studios</a></nav>
</header>
<section class="hero">
  <div class="kicker">Le magazine des facialistes</div>
  <h1>Les Articles Seasonly</h1>
  <div class="answer">12 articles courts, chiffrés et honnêtes — produits par notre ligne éditoriale (et alimentés par notre robot Make, relus par nos facialistes). Un nouveau sujet toutes les 30 minutes en période de démo&nbsp;🌿</div>
  <p class="meta">Dernière mise à jour : {DATE_FR} · 12 articles en ligne</p>
</section>
<main>
  <div class="grid">
{cards}
  </div>
  <div class="cta">
    <h2>Du contenu à la cabine, il n'y a qu'un pas</h2>
    <p>Skin Studios à Paris, Aix-en-Provence et Bordeaux — dès 65 €.</p>
    <a class="btn" href="https://seasonly.fr">Réserver un soin</a>
  </div>
</main>
<footer>
  <span class="badge">95 % naturel</span><span class="badge">Vegan</span><span class="badge">Depuis 2018</span>
  <p style="margin-top:10px">© 2026 Seasonly — Hub éditorial « Les Articles ».</p>
</footer>
</body>
</html>
"""
    (OUT / "index.html").write_text(index, encoding="utf-8")
    print("✓ index.html —", len(ARTICLES), "articles générés dans", OUT)


if __name__ == "__main__":
    main()
