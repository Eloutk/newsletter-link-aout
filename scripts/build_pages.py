from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
(ROOT / "articles").mkdir(exist_ok=True)

ARTICLES = [
    {
        "id": "marche-pub",
        "file": "articles/marche-pub.html",
        "nav": "marche",
        "label": "L'actu flash",
        "nav_label": "Marché",
        "title": "Le marché pub digital français franchit les 6,7 Md€ au S1 2026",
        "chapo": "+12 % de croissance, 6,689 Md€ de recettes : le digital confirme sa solidité. Mais 83 % du gâteau part chez Google, Meta, Amazon et TikTok.",
        "lead": "Le 36e Observatoire de l'e-pub (SRI/UDECAM/Oliver Wyman, 9 juillet 2026) confirme une dynamique solide, tirée par trois moteurs : le Social (+16 %), le Retail Media (+18 %) et la vidéo sous toutes ses formes. En face, le display classique recule (-5 %) et les éditeurs français perdent des parts. La prévision annuelle 2026 est fixée à <strong>~13,9 Md€</strong>.",
        "facts": [
            "Le <strong>Social représente 33 % du marché</strong> (2,22 Md€) et contribue à 41 % de la croissance du S1",
            "La <strong>vidéo sociale explose à +31 %</strong> et pèse 1,422 Md€, soit 64 % du levier Social",
            "Le <strong>programmatique vidéo atteint 78 %</strong> de part dans la vidéo (vs 75 % un an plus tôt)",
            "L'Édition &amp; Information est le <strong>seul segment en recul (-5 %)</strong>, à 251 M€",
        ],
        "kpis": [
            ("6,7 Md€", "Marché digital S1 2026"),
            ("+12 %", "Croissance vs S1 2025"),
            ("83 %", "Capté par acteurs non-EU"),
        ],
        "card_title": "Le marché digital franchit les 6,7 Md€",
        "card_text": "+12 % au S1, 6,689 Md€. La vidéo sociale et le retail media tirent la croissance. 83 % du gâteau part chez Google, Meta, Amazon et TikTok.",
        "featured": True,
    },
    {
        "id": "achat-media",
        "file": "articles/achat-media.html",
        "nav": "achat",
        "label": "IA &amp; plateformes",
        "nav_label": "IA",
        "title": "L'achat média passe en mode agentique : ce qui change pour les annonceurs",
        "chapo": "Google AI Max est le nouveau défaut pour les campagnes Search. Meta réécrit vos annonces en temps réel. L'humain se repositionne sur la stratégie, pas l'exécution.",
        "lead": "Depuis le 15 avril 2026, <strong>AI Max for Search est sorti de bêta</strong> et devient le type de campagne Search par défaut chez Google. Il combine matching sémantique (Gemini), personnalisation des textes et expansion d'URL — sans liste de mots-clés obligatoire. Côté Meta, juillet-août a été dense : lancement de <strong>Muse Image</strong> (génération d'images IA dans Advantage+), réécriture automatique des titres sur images uploadées, et déploiement du <strong>Generative Recommender</strong> (ranking LLM des annonces). Performance Max représente désormais <strong>45 % de toutes les conversions Google Ads</strong>.",
        "facts": [
            "Google AI Max annonce <strong>+7 % de conversions</strong> à CPA/ROAS similaire vs. search term matching seul (données Google internes)",
            "Meta Lattice : <strong>+12 % de qualité des annonces</strong>, +6 % de taux de conversion, +20 % d'efficacité capacitaire (Meta, jan. 2026)",
            "<strong>91 % des annonceurs Meta</strong> utilisent désormais Advantage+ (Business Insider, 2026)",
            "Migration DSA → AI Max repoussée à <strong>février 2027</strong>, mais ACA + broad match migrent en <strong>septembre 2026</strong>",
        ],
        "kpis": [],
        "card_title": "L'achat média passe en mode agentique",
        "card_text": "AI Max devient le défaut Search. Meta réécrit les annonces en temps réel. L'humain se repositionne sur la stratégie, pas l'exécution.",
        "featured": False,
    },
    {
        "id": "video-ia",
        "file": "articles/video-ia.html",
        "nav": "video",
        "label": "Production vidéo",
        "nav_label": "Vidéo",
        "title": "Génération vidéo IA : le stack professionnel est prêt",
        "chapo": "Veo 3.1, Runway Gen-4.5, Kling 3.0 : trois outils complémentaires qui couvrent 95 % des besoins d'une agence. La production vidéo IA est opérationnelle. Maintenant.",
        "lead": "La mise à jour Veo 3.1 (2 août 2026) intègre l'audio synchronisé natif sur tous les tiers, la sortie 4K et le couplage Gemini pour le prompting conversationnel. Elle réduit le temps de post-production audio d'environ <strong>40 %</strong>. Runway Gen-4.5 domine sur la cohérence des personnages (ELO 1 247 sur l'Artificial Analysis Video Arena). Kling 3.0 s'impose pour le volume social avec son mode storyboard multi-shots. À noter : <strong>l'API Sora 2 est en fin de vie en septembre 2026</strong> — ne plus intégrer dans les workflows.",
        "facts": [
            "<strong>Veo 3.1</strong> : audio natif synchronisé, 4K, 60s — idéal spots premium et assets Performance Max",
            "<strong>Kling 3.0</strong> : ~0,084 $/s, multi-shots, audio natif — idéal volume social (Reels, TikTok, Shorts)",
            "<strong>Runway Gen-4.5</strong> : ELO 1 247, meilleur score cohérence personnages — idéal brand content dirigé",
            "<strong>Sora 2 API</strong> : fin de vie septembre 2026 — migrer vers Veo 3.1 ou Kling 3.0 sans attendre",
        ],
        "kpis": [],
        "card_title": "Le stack vidéo IA est prêt",
        "card_text": "Veo 3.1, Runway Gen-4.5, Kling 3.0 : trois outils qui couvrent 95 % des besoins. L'API Sora 2 disparaît en septembre.",
        "featured": False,
    },
    {
        "id": "chatgpt-ads",
        "file": "articles/chatgpt-ads.html",
        "nav": "chatgpt",
        "label": "Nouvelles surfaces",
        "nav_label": "ChatGPT",
        "title": "ChatGPT Ads : OpenAI ouvre la publicité à 600 millions d'utilisateurs",
        "chapo": "OpenAI a officiellement annoncé l'arrivée de formats publicitaires dans ChatGPT. Une nouvelle surface d'inventaire premium, au cœur du moteur de recherche IA le plus utilisé au monde.",
        "lead": "Après des mois de spéculations, OpenAI a confirmé le lancement d'un programme publicitaire intégré à ChatGPT. Les annonces apparaîtront de façon contextuelle dans les réponses, ciblées selon l'intention de la requête — un modèle proche du Search, mais avec la profondeur conversationnelle en plus. Pour les annonceurs, c'est l'accès à une audience de <strong>600 millions d'utilisateurs actifs</strong> qui consultent ChatGPT comme premier réflexe d'information, avant même Google. <strong>Link est sur liste d'attente pour déployer cette solution en avant-première</strong> et accompagner ses clients dès l'ouverture du programme.",
        "facts": [
            "ChatGPT compte <strong>600 millions d'utilisateurs actifs</strong> dans le monde (OpenAI, 2026)",
            "Le format publicitaire est <strong>contextuel et conversationnel</strong> : l'annonce s'intègre dans la réponse selon l'intention de la requête",
            "OpenAI cible en priorité les <strong>annonceurs Search et Performance</strong> pour la phase de lancement",
            "<strong>Link est en liste d'attente</strong> pour accéder au programme en avant-première et tester les premiers formats",
        ],
        "kpis": [],
        "card_title": "ChatGPT Ads : 600 millions d'utilisateurs",
        "card_text": "OpenAI ouvre la pub dans ChatGPT. Link est en liste d'attente pour déployer la solution en avant-première.",
        "featured": False,
    },
]

SOURCES = [
    "SRI / UDECAM / Oliver Wyman — 36e Observatoire de l'e-pub, 9 juillet 2026 — sri-france.org",
    "The Media Leader FR — fr.themedialeader.com, 9 juillet 2026",
    "Siècle Digital — siecledigital.fr, 13 juillet 2026",
    "La Revue du Digital — larevuedudigital.com, juillet 2026",
    "Blog du Modérateur — blogdumoderateur.com, janvier 2026",
    "Google Blog officiel — blog.google (AI Max for Search, avril &amp; juin 2026)",
    "Meta for Business / about.fb.com — Meta Lattice jan. 2026 ; Muse Image juillet 2026",
    "AdAdvisor / AdMake AI Blog — Meta Ads updates août 2026",
    "CommonThread — commonthreadco.com, 2026",
    "Qwairy.co / GeoFast.fr — Google AI Overviews France, 22 juillet 2026",
    "Erlin.ai — Parts de trafic IA (ChatGPT, Gemini, DeepSeek), janvier 2026",
    "iaba.tech — Budget GEO France, 2026",
    "UlazAI — Veo 3.1 update, 2 août 2026 ; CreativeMarketing.ai — Veo 3.1 vs Runway, 17 juillet 2026",
    "Tech-Insider.org / PixVerse Blog — Runway Gen-4.5, Kling 3.0, 2026",
    "Lengow Blog — TikTok Shop France Q2 2026, juillet 2026",
    "J'ai un pote dans la com — CTV France, 31 mars 2026",
    "eMarketer / Digital Applied — Programmatique &amp; walled gardens, 2026",
    "Reworld MediaConnect / SRI — GEO x Créateurs, 21 juillet 2026",
    "Gartner via Search Engine Land — Baisse volume recherche traditionnel, 2026",
    "Ahrefs via Erlin.ai — Pages citées ChatGPT sans visibilité Google, 2026",
]

NAV = [
    ("home", "index.html", "Accueil"),
    ("marche", "articles/marche-pub.html", "Marché"),
    ("achat", "articles/achat-media.html", "IA"),
    ("video", "articles/video-ia.html", "Vidéo"),
    ("chatgpt", "articles/chatgpt-ads.html", "ChatGPT"),
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
            <li>Édition #7 , Août 2026</li>
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
        "Veille webmarketing Link, édition août 2026 : marché pub, achat média IA, vidéo générative et ChatGPT Ads.",
    )
    html += f"""
  <section class="hero">
    <div class="waves" aria-hidden="true"></div>
    <div class="container hero-inner">
      <div>
        <div class="eyebrow">Édition #7 · Août 2026</div>
        <h1>Ce qui change vraiment <span>cet été.</span></h1>
        <p class="hero-lead">L'été 2026 a été tout sauf calme : le marché pub digital français franchit les 6,7 Md€ au S1, Google lance ses AI Overviews en France, et la vidéo IA entre en production professionnelle. Ce mois-ci, on décrypte ce qui change vraiment pour votre business.</p>
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
        <dt>ChatGPT Ads</dt>
        <dd>600 M</dd>
      </dl>
    </div>
  </section>
  <div class="topics">
    <div class="container">
      <ul class="topics-list">
        <li><a href="articles/marche-pub.html">Marché pub</a></li>
        <li><a href="articles/achat-media.html">Achat média IA</a></li>
        <li><a href="articles/video-ia.html">Vidéo générative</a></li>
        <li><a href="articles/chatgpt-ads.html">ChatGPT Ads</a></li>
      </ul>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="section-kicker">Au sommaire</div>
          <h2>Quatre sujets à retenir</h2>
        </div>
      </div>
      <p class="intro-text">Juillet-août 2026 marque un tournant : <strong>le marché publicitaire digital français atteint 6,689 Md€ au S1</strong>, porté par la vidéo sociale (+31 %) et le retail media (+18 %). Pendant ce temps, Google déploie ses AI Overviews en France le 22 juillet — un séisme pour le SEO — et la génération vidéo IA passe du stade expérimental à la production professionnelle. L'achat média agentique redistribue les rôles entre humains et machines. <strong>Ce n'est plus une tendance à surveiller : c'est votre quotidien de demain.</strong></p>
      <div class="kpi-row">
        <div class="kpi-card"><div class="kpi-value">6,7 Md€</div><div class="kpi-label">Marché digital S1 2026</div></div>
        <div class="kpi-card"><div class="kpi-value">+12 %</div><div class="kpi-label">Croissance vs S1 2025</div></div>
        <div class="kpi-card"><div class="kpi-value">83 %</div><div class="kpi-label">Capté par acteurs non-EU</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="card-grid four">
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
      <p class="intro-text">Le marché croît, mais la valeur se concentre. L'achat média devient agentique, la vidéo IA entre en production professionnelle, et ChatGPT ouvre un nouvel inventaire pub. Les agences qui maîtrisent ces trois dimensions — assets créatifs, stack vidéo, nouvelles surfaces — sont celles qui créeront de la valeur durable pour leurs clients.</p>
      <ul class="facts">
        <li><strong>1.</strong> La vidéo est non négociable dans tout plan média 2026 — arbitrer plateformes globales et médias français</li>
        <li><strong>2.</strong> Auditer les campagnes DSA avant septembre 2026 et tester AI Max : la valeur se déplace vers les assets créatifs</li>
        <li><strong>3.</strong> Intégrer le stack Kling + Veo 3.1 + Runway, et anticiper ChatGPT Ads (Link est en liste d'attente)</li>
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
        "Gary Cadiz , Portrait | keep the link",
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
    for obsolete in ("geo.html", "reseaux-sociaux.html", "rgpd.html"):
        path = ROOT / "articles" / obsolete
        if path.exists():
            path.unlink()
    print("built")
