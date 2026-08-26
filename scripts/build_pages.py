from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
(ROOT / "articles").mkdir(exist_ok=True)

ARTICLES = [
    {
        "id": "marche-pub",
        "file": "articles/marche-pub.html",
        "nav": "marche",
        "label": "Marché pub France",
        "nav_label": "Marché",
        "title": "Le Social passe devant le Search",
        "chapo": "Le marché digital français atteint 6,69 Md€ au S1 2026. +12 %. Et pour la première fois, le Social dépasse le Search. La vidéo en est le seul moteur.",
        "lead": "Ce n'est pas une tendance. C'est un basculement. Le 36e Observatoire de l'e-pub SRI/UDECAM (9 juillet 2026) le confirme : la vidéo sociale capte désormais plus de budget publicitaire que les liens sponsorisés classiques. Pensez à ça comme à un changement de gravité — tout ce qui était secondaire devient central. La prévision annuelle reste à +11 %, soit un marché attendu à <strong>~13,9 Md€</strong> sur l'année.",
        "facts": [
            "Le Social progresse de <strong>+16 % à 2,22 Md€</strong> — soit 33 % du marché et 41 % de toute la croissance du semestre",
            "La vidéo représente <strong>64 % des revenus Social (+31 %, 1,42 Md€)</strong> — la croissance est exclusivement vidéo",
            "Le Retail Media atteint <strong>775 M€ (+18 %)</strong>, dont 77 % via le Retail Search (+24 %)",
            "La CTV s'impose comme <strong>1er support vidéo Display (51 %)</strong> des revenus vidéo Display ; la SVOD affiche +36 %",
            "Les acteurs français ne représentent plus que <strong>17 % du marché</strong> (+4 % seulement, contre +12 % pour le marché global)",
        ],
        "reco": "<strong>Pour Link :</strong> la vidéo sociale n'est plus un format complémentaire — c'est le cœur du marché. Proposer des formats vidéo natifs (Reels, TikTok, Shorts) à chaque client est une nécessité commerciale, pas une option.",
        "kpis": [
            ("6,7 Md€", "Marché digital S1 2026"),
            ("+12 %", "Croissance vs S1 2025"),
            ("83 %", "Capté par acteurs non-EU"),
        ],
        "card_title": "Le Social passe devant le Search",
        "card_text": "6,69 Md€ au S1 (+12 %). Pour la première fois, le Social dépasse le Search — porté exclusivement par la vidéo.",
        "featured": True,
    },
    {
        "id": "achat-media",
        "file": "articles/achat-media.html",
        "nav": "achat",
        "label": "IA & plateformes",
        "nav_label": "IA & médias",
        "title": "L'achat média passe en mode agentique : ce qui change pour les annonceurs",
        "chapo": "Google AI Max est le nouveau défaut pour les campagnes Search. Meta réécrit vos annonces en temps réel. L'humain se repositionne sur la stratégie — pas l'exécution.",
        "lead": "Depuis le 15 avril 2026, <strong>AI Max for Search est sorti de bêta</strong> et devient le type de campagne Search par défaut chez Google. Il combine matching sémantique (Gemini), personnalisation des textes et expansion d'URL — sans liste de mots-clés obligatoire. Côté Meta, juillet-août a été dense : lancement de <strong>Muse Image</strong> (génération d'images IA dans Advantage+), réécriture automatique des titres sur images uploadées, et déploiement du <strong>Generative Recommender</strong> (ranking LLM des annonces). Performance Max représente désormais <strong>45 % de toutes les conversions Google Ads</strong>.",
        "facts": [
            "Google AI Max annonce <strong>+7 % de conversions</strong> à CPA/ROAS similaire vs. search term matching seul (données Google internes)",
            "Meta Lattice : <strong>+12 % de qualité des annonces</strong>, +6 % de taux de conversion, +20 % d'efficacité capacitaire (Meta, jan. 2026)",
            "<strong>91 % des annonceurs Meta</strong> utilisent désormais Advantage+ (Business Insider, 2026)",
            "Migration DSA → AI Max repoussée à <strong>février 2027</strong>, mais ACA + broad match migrent en <strong>septembre 2026</strong>",
        ],
        "reco": "<strong>Pour Link :</strong> auditer les campagnes DSA clients avant septembre 2026 (migration automatique imminente). Tester AI Max sur 1-2 campagnes Search dès maintenant. La valeur ajoutée de l'agence se déplace vers la qualité des assets créatifs fournis aux algorithmes — pas l'exécution manuelle.",
        "kpis": [],
        "card_title": "L'achat média passe en mode agentique",
        "card_text": "AI Max devient le défaut Search. Meta réécrit les annonces en temps réel. La stratégie humaine prend le relais de l'exécution.",
        "featured": False,
    },
    {
        "id": "video-ia",
        "file": "articles/video-ia.html",
        "nav": "video",
        "label": "Production vidéo",
        "nav_label": "Vidéo",
        "title": "Vidéo IA — nouveaux outils, nouvelles obligations",
        "chapo": "Runway Gen-4.5, Kling 3.0 Omni, Veo 3.1 : la génération vidéo IA entre dans une phase professionnelle. Et depuis le 2 août 2026, l'IA Act impose l'étiquetage obligatoire.",
        "lead": "Imaginez un studio de production qui tient dans un navigateur. C'est à peu près là où en sont les outils vidéo IA en août 2026. Runway Gen-4.5 intègre des contrôles de caméra professionnels et 6 formats d'aspect ratio. Kling 3.0 Omni introduit l'AI Director — génération multi-plans avec transitions cinématiques — plus le lip-sync multilingue en 5 langues et des clips jusqu'à 15 secondes. L'écart de coût et de délai avec la production traditionnelle est désormais documenté, chiffré, et présentable aux clients.",
        "facts": [
            "Vidéo IA Essentiel (15–45 sec) : <strong>1 000–2 500 € HT</strong>, délai 3–7 jours (vs 3 000–5 000 € HT / 3–6 semaines en traditionnel)",
            "Vidéo IA Premium (90–180 sec + déclinaisons multilingues) : <strong>8 000–25 000 € HT</strong>, délai 3–4 semaines",
            "Déclinaisons multilingues : <strong>+30 à 50 %</strong> en production classique vs coût marginal quasi nul en IA",
            "Depuis le <strong>2 août 2026 (IA Act)</strong> : étiquetage « contenu généré par IA » obligatoire, consentements tracés, métadonnées C2PA — amendes jusqu'à <strong>15 M€ ou 3 % du CA mondial</strong>",
        ],
        "reco": "<strong>Pour Link :</strong> l'approche hybride (tournage socle + déclinaisons IA) est le positionnement optimal à présenter aux clients. Intégrer la conformité IA Act dans les devis et contrats dès maintenant — ce n'est plus optionnel.",
        "kpis": [],
        "card_title": "Vidéo IA : outils et obligations",
        "card_text": "Runway, Kling, Veo : le stack pro est là. Depuis le 2 août, l'IA Act impose l'étiquetage des contenus générés.",
        "featured": False,
    },
    {
        "id": "reseaux-sociaux",
        "file": "articles/reseaux-sociaux.html",
        "nav": "social",
        "label": "Réseaux sociaux",
        "nav_label": "Social",
        "title": "LinkedIn surprend, TikTok domine l'attention",
        "chapo": "LinkedIn affiche +15,2 % d'utilisateurs actifs — la plus forte croissance de tous les réseaux en France. TikTok, lui, capte 1h33 par jour.",
        "lead": "La France compte <strong>51,5 millions de comptes actifs</strong> sur les réseaux sociaux — 77,2 % de la population — pour un temps moyen de 12h32 par semaine. La surprise stratégique de 2026 ? LinkedIn. Sa croissance d'audience dépasse tous les autres réseaux, et son algorithme récompense massivement la vidéo verticale native. Pour les agences B2B, c'est une fenêtre d'opportunité à saisir maintenant, avant que tout le monde ne s'y engouffre.",
        "facts": [
            "TikTok : <strong>1h33/jour</strong> de temps moyen (1er réseau par temps d'attention) ; YouTube : 1h16 ; Instagram : 1h14",
            "LinkedIn : <strong>+15,2 % d'utilisateurs actifs</strong> en un an (vs +3,3 % pour TikTok) — 30 à 38 millions de membres en France",
            "Vidéo native LinkedIn (15–90 sec, portrait) : portée <strong>5 à 10× supérieure</strong> aux posts texte ; liens externes dans le corps = -40 à 60 % de portée",
            "YouTube touche <strong>84,4 % des internautes français</strong> ; YouTube Shorts cumule 200 milliards de vues quotidiennes mondiales",
        ],
        "reco": "<strong>Pour Link :</strong> proposer des formats 9:16 LinkedIn-first aux clients B2B est une opportunité immédiate. Sur TikTok et Shorts, les 3 premières secondes sont décisives — les scripts doivent être conçus pour l'attention, pas pour la narration classique.",
        "kpis": [],
        "card_title": "LinkedIn surprend, TikTok domine",
        "card_text": "LinkedIn +15,2 % d'actifs. TikTok capte 1h33/jour. La vidéo verticale native devient le format prioritaire.",
        "featured": False,
    },
    {
        "id": "rgpd",
        "file": "articles/rgpd.html",
        "nav": "rgpd",
        "label": "RGPD & cookies",
        "nav_label": "RGPD",
        "title": "La CNIL ne dort plus",
        "chapo": "Criteo condamné à 40 M€, définitivement. Depuis janvier 2026, un crawler automatisé de la CNIL contrôle les bandeaux cookies sans attendre de plainte.",
        "lead": "Pendant longtemps, la non-conformité cookies était un risque théorique. Un risque que beaucoup géraient en croisant les doigts. Ce temps est révolu. Le 4 mars 2026, le Conseil d'État a validé l'amende de <strong>40 M€ infligée à Criteo</strong> — faute de preuve de consentement valable. Et depuis janvier 2026, la CNIL a déployé un crawler automatisé qui scanne les sites français en continu. Pas besoin de plainte. Le robot passe, il voit, il signale.",
        "facts": [
            "<strong>23 sanctions simplifiées</strong> prononcées depuis janvier 2026 pour un total de 133 750 € cumulés via le crawler automatisé",
            "<strong>62 % des internautes français</strong> refusent les cookies non essentiels quand un vrai bouton « Refuser » est proposé (Didomi 2024)",
            "Durée maximale des cookies publicitaires : <strong>13 mois</strong> avec renouvellement obligatoire (CNIL, 1er janvier 2026)",
            "Le règlement ePrivacy a été formellement retiré (février 2025) ; le paquet Digital Omnibus est en trilogue — adoption incertaine avant <strong>2027</strong>",
        ],
        "reco": "<strong>Pour Link :</strong> audit de conformité cookies pour les sites clients, mise à jour des CMP, intégration du Google Consent Mode v2. Avec 62 % de refus cookies, les solutions analytics exemptées de consentement (Piano Analytics, Matomo) deviennent stratégiques.",
        "kpis": [],
        "card_title": "La CNIL ne dort plus",
        "card_text": "Amende Criteo confirmée (40 M€). Un crawler CNIL scanne les bandeaux cookies en continu, sans plainte.",
        "featured": False,
    },
]

SOURCES = [
    "SRI / UDECAM / Oliver Wyman — 36e Observatoire de l'e-pub, 9 juillet 2026 (via CB News, The Media Leader FR, Viuz, Siècle Digital)",
    "We Are Social / Meltwater — Digital Report France 2026 (janvier 2026) — Blog du Modérateur, Koredge.fr, Osmova.com",
    "CRÉDOC — Baromètre du numérique 2026, juin 2026",
    "HubSpot — State of Marketing 2026 ; Bpifrance — Rapport annuel mars 2026 (via DecisionIA.com)",
    "Metricool.com/fr — AI Overview France, 3 août 2026 ; Blog du Modérateur",
    "Obeevi.fr — Prix Vidéo IA 2026 : Grille Tarifaire, 2 février 2026",
    "UlazAI (mis à jour 18 août 2026) — Comparatif modèles vidéo IA ; Kling.ai blog ; FreeAcademy.ai",
    "Secure Privacy Blog FR — Consentement aux Cookies et RGPD en 2026, août 2026 ; CNIL (délibérations 2025-2026)",
    "ViralBrain.ai — LinkedIn Algorithm 2026 ; DataSlayer.ai, juillet 2026",
    "RGPDKit.fr — Bandeau cookies CNIL 2026, 11 août 2026 ; Agence Clova Blog (citant Didomi 2024)",
    "Règlement IA Act UE (entrée en vigueur 2 août 2026 pour les obligations d'étiquetage vidéo)",
    "Google Blog officiel — blog.google (AI Max for Search, avril &amp; juin 2026)",
    "Meta for Business / about.fb.com — Meta Lattice jan. 2026 ; Muse Image juillet 2026",
]

NAV = [
    ("home", "index.html", "Accueil"),
    ("marche", "articles/marche-pub.html", "Marché"),
    ("achat", "articles/achat-media.html", "IA & médias"),
    ("video", "articles/video-ia.html", "Vidéo"),
    ("social", "articles/reseaux-sociaux.html", "Social"),
    ("rgpd", "articles/rgpd.html", "RGPD"),
    ("portrait", "portrait.html", "Portrait"),
    ("sources", "sources.html", "Sources"),
]


def href(base: str, path: str) -> str:
    return f"{base}{path}"


def chrome(base: str, active: str, title: str, description: str) -> str:
    links = []
    for key, path, label in NAV:
        cls = ' class="is-active"' if active == key else ""
        links.append(f'        <a href="{href(base, path)}"{cls}>{label}</a>')
    nav_html = "\n".join(links)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="{href(base, "favicon.png")}" type="image/png">
  <link rel="apple-touch-icon" href="{href(base, "apple-touch-icon.png")}">
  <link rel="stylesheet" href="{href(base, "css/styles.css")}">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{href(base, "index.html")}">
        <span class="brand-name">keep the link</span>
        <span class="brand-tag">Les News</span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Ouvrir le menu" aria-expanded="false">
        <span></span>
      </button>
      <nav class="site-nav" aria-label="Navigation principale">
{nav_html}
        <a class="btn" href="https://link.fr/contact-agence-link/">Prendre RDV</a>
      </nav>
    </div>
  </header>
"""


def footer(base: str) -> str:
    links = "\n".join(
        f'            <li><a href="{href(base, path)}">{label}</a></li>'
        for _, path, label in NAV
    )
    return f"""  <section class="cta-band">
    <div class="container cta-inner">
      <div>
        <div class="cta-kicker">Prochain rendez-vous</div>
        <strong><span>Septembre</span> 2026</strong>
      </div>
      <a class="btn" href="https://link.fr/contact-agence-link/">Prendre RDV avec un expert →</a>
    </div>
  </section>
  <footer class="site-footer">
    <div class="waves" aria-hidden="true"></div>
    <div class="container">
      <div class="footer-inner">
        <div>
          <div class="footer-brand">Welcome <span>again.</span></div>
          <p>Agence Link · 127 rue Turenne, 33000 Bordeaux<br>www.link.fr</p>
        </div>
        <div>
          <h3>Le site</h3>
          <ul>
{links}
          </ul>
        </div>
        <div>
          <h3>Contact</h3>
          <ul>
            <li><a href="https://link.fr/contact-agence-link/">link.fr</a></li>
            <li>Édition #7 — Août 2026</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>keep the link · Les News</span>
        <span>Tous droits réservés</span>
      </div>
    </div>
  </footer>
  <script src="{href(base, "js/site.js")}"></script>
</body>
</html>
"""


def build_home() -> None:
    base = ""
    cards = []
    for art in ARTICLES:
        featured = " featured" if art["featured"] else ""
        cards.append(
            f"""      <a class="card{featured}" href="{art["file"]}">
        <div class="card-label">{art["label"]}</div>
        <h3>{art["card_title"]}</h3>
        <p>{art["card_text"]}</p>
        <span class="card-more">Lire l'article →</span>
      </a>"""
        )
    html = chrome(
        base,
        "home",
        "Les News | keep the link",
        "Veille webmarketing Link — édition août 2026 : marché pub, achat média IA, vidéo générative, réseaux sociaux et RGPD.",
    )
    html += f"""
  <section class="hero">
    <div class="waves" aria-hidden="true"></div>
    <div class="container hero-inner">
      <div>
        <div class="eyebrow">Édition #7 · Août 2026</div>
        <h1>Ce qui change vraiment <span>cet été.</span></h1>
        <p class="hero-lead">Août 2026 a tranché. La vidéo sociale dépasse le Search classique en France — pour la première fois. Google déploie son IA dans les résultats de recherche. L'IA Act entre en vigueur pour les productions vidéo. Et la CNIL surveille désormais les cookies en continu, sans attendre de plainte.</p>
        <div class="hero-actions">
          <a class="btn" href="articles/marche-pub.html">Lire l'édition</a>
          <a class="btn btn-ghost" href="portrait.html">Le portrait du mois</a>
        </div>
      </div>
      <dl class="hero-meta">
        <dt>Marché digital S1</dt>
        <dd>6,7 Md€</dd>
        <dt>Croissance</dt>
        <dd>+12 %</dd>
        <dt>IA Act vidéo</dt>
        <dd>2 août 2026</dd>
      </dl>
    </div>
  </section>
  <div class="topics">
    <div class="container">
      <ul class="topics-list">
        <li><a href="articles/marche-pub.html">Marché pub</a></li>
        <li><a href="articles/achat-media.html">Achat média</a></li>
        <li><a href="articles/video-ia.html">IA &amp; vidéo</a></li>
        <li><a href="articles/reseaux-sociaux.html">Réseaux sociaux</a></li>
        <li><a href="articles/rgpd.html">RGPD &amp; cookies</a></li>
      </ul>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="section-kicker">Au sommaire</div>
          <h2>Cinq sujets à retenir</h2>
        </div>
      </div>
      <p class="intro-text"><strong>Quatre signaux. Une seule direction :</strong> les agences qui combinent vidéo, IA maîtrisée et données propres prennent une longueur d'avance que les autres auront du mal à combler. Juillet–août 2026 : le Social dépasse le Search, l'achat média devient agentique, et la conformité (IA Act, cookies) n'est plus optionnelle.</p>
      <div class="kpi-row">
        <div class="kpi-card"><div class="kpi-value">6,7 Md€</div><div class="kpi-label">Marché digital S1 2026</div></div>
        <div class="kpi-card"><div class="kpi-value">+12 %</div><div class="kpi-label">Croissance vs S1 2025</div></div>
        <div class="kpi-card"><div class="kpi-value">83 %</div><div class="kpi-label">Capté par acteurs non-EU</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="card-grid five">
{chr(10).join(cards)}
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="section-kicker">Synthèse</div>
          <h2>Ce qu'il faut retenir en août</h2>
        </div>
      </div>
      <p class="intro-text">La vidéo sociale est officiellement le premier levier publicitaire digital en France — devant le Search classique. AI Overview transforme les règles du SEO dès maintenant. Et l'IA Act impose de nouvelles obligations de conformité pour toute production vidéo IA diffusée publiquement. Les agences qui maîtrisent ces trois dimensions simultanément — production vidéo, IA responsable, données propres — sont celles qui créeront de la valeur durable pour leurs clients.</p>
      <ul class="facts">
        <li><strong>1.</strong> Intégrer la vidéo native (9:16, formats courts) dans toutes les offres clients — Social, LinkedIn, YouTube Shorts</li>
        <li><strong>2.</strong> Auditer la visibilité des clients dans AI Overview et adapter les stratégies de contenu dès maintenant</li>
        <li><strong>3.</strong> Mettre en conformité les productions vidéo IA (IA Act) et les bandeaux cookies clients (crawler CNIL actif)</li>
      </ul>
    </div>
  </section>
  <section class="portrait-band">
    <div class="waves" aria-hidden="true"></div>
    <div class="container portrait-inner">
      <img class="avatar" src="images/gary-cadiz.png" alt="Gary Cadiz">
      <div>
        <div class="section-kicker">Qui sont-ils ?</div>
        <h2>Gary Cadiz</h2>
        <div class="portrait-role">Directeur commercial</div>
        <p>Surnom K Ten. Mantra : « Rien n'est jamais entièrement perdu ».</p>
      </div>
      <a class="btn" href="portrait.html">Voir le portrait</a>
    </div>
  </section>
"""
    html += footer(base)
    (ROOT / "index.html").write_text(html, encoding="utf-8")


def build_articles() -> None:
    for i, art in enumerate(ARTICLES):
        base = "../"
        prev_a = ARTICLES[i - 1] if i > 0 else None
        next_a = ARTICLES[i + 1] if i < len(ARTICLES) - 1 else None
        facts = "\n".join(f"            <li>{item}</li>" for item in art["facts"])
        kpis = ""
        if art["kpis"]:
            cells = "\n".join(
                f'            <div class="kpi-card"><div class="kpi-value">{value}</div><div class="kpi-label">{label}</div></div>'
                for value, label in art["kpis"]
            )
            kpis = f'<div class="kpi-row">\n{cells}\n          </div>'
        side = "\n".join(
            f'          <a href="{href(base, other["file"])}">{other["card_title"]}</a>'
            for other in ARTICLES
            if other["id"] != art["id"]
        )
        nav_prev = (
            f'<a href="{href(base, prev_a["file"])}">← {prev_a["nav_label"]}</a>'
            if prev_a
            else "<span></span>"
        )
        nav_next = (
            f'<a href="{href(base, next_a["file"])}">{next_a["nav_label"]} →</a>'
            if next_a
            else "<span></span>"
        )
        html = chrome(base, art["nav"], f"{art['title']} | keep the link", art["chapo"])
        html += f"""
  <section class="page-hero">
    <div class="waves" aria-hidden="true"></div>
    <div class="container page-hero-inner">
      <nav class="crumbs" aria-label="Fil d'Ariane">
        <a href="{href(base, "index.html")}">Accueil</a>
        <span>/</span>
        <span>{art["label"]}</span>
      </nav>
      <div class="eyebrow">{art["label"]} · Août 2026</div>
      <h1>{art["title"]}</h1>
      <p>{art["chapo"]}</p>
    </div>
  </section>
  <div class="container">
    <div class="article-layout">
      <article>
        {kpis}
        <p class="article-body">{art["lead"]}</p>
        <ul class="facts">
{facts}
        </ul>
        <div class="reco"><span class="reco-arrow">→</span><span>{art["reco"]}</span></div>
        <div class="article-nav">
          {nav_prev}
          {nav_next}
        </div>
      </article>
      <aside class="side-card">
        <h2>Dans cette édition</h2>
{side}
        <a href="{href(base, "portrait.html")}">Portrait · Gary Cadiz</a>
      </aside>
    </div>
  </div>
"""
        html += footer(base)
        (ROOT / art["file"]).write_text(html, encoding="utf-8")


def build_portrait() -> None:
    base = ""
    html = chrome(
        base,
        "portrait",
        "Gary Cadiz — Portrait | keep the link",
        "Portrait interne : Gary Cadiz, directeur commercial de l'agence Link.",
    )
    html += """
  <section class="page-hero">
    <div class="waves" aria-hidden="true"></div>
    <div class="container page-hero-inner">
      <nav class="crumbs" aria-label="Fil d'Ariane">
        <a href="index.html">Accueil</a>
        <span>/</span>
        <span>Portrait</span>
      </nav>
      <div class="eyebrow">Qui sont-ils ? · Édition #7</div>
      <div class="profile-hero">
        <img class="avatar" src="images/gary-cadiz.png" alt="Gary Cadiz">
        <div>
          <h1>Gary Cadiz</h1>
          <p>Directeur commercial</p>
        </div>
      </div>
      <dl class="profile-grid">
        <div class="profile-item"><dt>Surnom</dt><dd>K Ten</dd></div>
        <div class="profile-item"><dt>Son mantra</dt><dd>« Rien n'est jamais entièrement perdu »</dd></div>
        <div class="profile-item"><dt>Son plaisir coupable</dt><dd>Prendre la place de Junior au déjeuner</dd></div>
        <div class="profile-item"><dt>Son petit truc en plus</dt><dd>Jamais contre un match de bad(minton)</dd></div>
      </dl>
    </div>
  </section>
"""
    html += footer(base)
    (ROOT / "portrait.html").write_text(html, encoding="utf-8")


def build_sources() -> None:
    base = ""
    items = "\n".join(f"        <li>{source}</li>" for source in SOURCES)
    html = chrome(
        base,
        "sources",
        "Sources | keep the link",
        "Sources citées dans l'édition août 2026 de keep the link Les News.",
    )
    html += f"""
  <section class="page-hero">
    <div class="waves" aria-hidden="true"></div>
    <div class="container page-hero-inner">
      <nav class="crumbs" aria-label="Fil d'Ariane">
        <a href="index.html">Accueil</a>
        <span>/</span>
        <span>Sources</span>
      </nav>
      <div class="eyebrow">Édition #7 · Août 2026</div>
      <h1>Sources citées</h1>
      <p>Références utilisées pour l'édition d'août : observatoires, blogs plateformes et études marché.</p>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <ul class="sources">
{items}
      </ul>
    </div>
  </section>
"""
    html += footer(base)
    (ROOT / "sources.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build_home()
    build_articles()
    build_portrait()
    build_sources()
    geo = ROOT / "articles" / "geo.html"
    if geo.exists():
        geo.unlink()
    print("built")
