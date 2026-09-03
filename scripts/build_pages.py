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
        "title": "Le marché digital franchit les 6,7 Md€",
        "chapo": "+12 % au S1, 6,689 Md€. La vidéo sur les réseaux et la pub sur les sites marchands tirent la croissance. À eux seuls, quelques grands acteurs captent 83 % du gâteau.",
        "lead": "+12 % au S1, 6,689 Md€. La vidéo sur les réseaux et la pub sur les sites marchands tirent la croissance. À eux seuls, quelques grands acteurs captent 83 % du gâteau.",
        "facts": [],
        "kpis": [
            ("6,7 Md€", "Marché digital S1 2026"),
            ("+12 %", "Croissance vs S1 2025"),
            ("83 %", "Capté par acteurs non-EU"),
        ],
        "card_title": "Le marché digital franchit les 6,7 Md€",
        "card_text": "+12 % au S1, 6,689 Md€. La vidéo sur les réseaux et la pub sur les sites marchands tirent la croissance. À eux seuls, quelques grands acteurs captent 83 % du gâteau.",
        "featured": True,
    },
    {
        "id": "achat-media",
        "file": "articles/achat-media.html",
        "nav": "achat",
        "label": "IA &amp; plateformes",
        "nav_label": "IA",
        "title": "L'IA passe aux commandes, Link garde la main",
        "chapo": "Google et Meta automatisent de plus en plus le pilotage des campagnes. Surtout, un nouvel espace s'ouvre : la publicité dans ChatGPT, que Link peut déjà proposer, en avant-première.",
        "lead": "Google et Meta automatisent de plus en plus le pilotage des campagnes. Surtout, un nouvel espace s'ouvre : la publicité dans ChatGPT, que <strong>Link peut déjà proposer, en avant-première</strong>. Notre rôle reste le même : cadrer ces outils pour qu'ils servent vos résultats, pas l'inverse.",
        "facts": [],
        "kpis": [],
        "card_title": "L'IA passe aux commandes, Link garde la main",
        "card_text": "Google et Meta automatisent de plus en plus le pilotage des campagnes. Surtout, un nouvel espace s'ouvre : la publicité dans ChatGPT, que <strong>Link peut déjà proposer, en avant-première</strong>. Notre rôle reste le même : cadrer ces outils pour qu'ils servent vos résultats, pas l'inverse.",
        "featured": False,
    },
    {
        "id": "video-ia",
        "file": "articles/video-ia.html",
        "nav": "video",
        "label": "Production vidéo",
        "nav_label": "Vidéo",
        "title": "La vidéo pro, plus vite et moins chère",
        "chapo": "Produire une vidéo de qualité prend désormais quelques jours au lieu de quelques semaines, pour une fraction du budget.",
        "lead": "Produire une vidéo de qualité prend désormais quelques jours au lieu de quelques semaines, pour une fraction du budget. Ce qui fait la différence n'est plus l'outil, mais le regard : notre studio interne combine cette rapidité avec une vraie direction artistique. Résultat, des contenus qui vous ressemblent, déclinés pour tous les formats.",
        "facts": [],
        "kpis": [],
        "card_title": "La vidéo pro, plus vite et moins chère",
        "card_text": "Produire une vidéo de qualité prend désormais quelques jours au lieu de quelques semaines, pour une fraction du budget. Ce qui fait la différence n'est plus l'outil, mais le regard : notre studio interne combine cette rapidité avec une vraie direction artistique. Résultat, des contenus qui vous ressemblent, déclinés pour tous les formats.",
        "featured": False,
    },
]

SOURCES = [
    "SRI / UDECAM / Oliver Wyman, 36e Observatoire de l'e-pub, 9 juillet 2026, sri-france.org",
    "The Media Leader FR, fr.themedialeader.com, 9 juillet 2026",
    "Siècle Digital, siecledigital.fr, 13 juillet 2026",
    "La Revue du Digital, larevuedudigital.com, juillet 2026",
    "Blog du Modérateur, blogdumoderateur.com, janvier 2026",
    "Google Blog officiel, blog.google (AI Max for Search, avril &amp; juin 2026)",
    "Meta for Business / about.fb.com, Meta Lattice jan. 2026 ; Muse Image juillet 2026",
    "AdAdvisor / AdMake AI Blog, Meta Ads updates août 2026",
    "CommonThread, commonthreadco.com, 2026",
    "Qwairy.co / GeoFast.fr, Google AI Overviews France, 22 juillet 2026",
    "Erlin.ai, Parts de trafic IA (ChatGPT, Gemini, DeepSeek), janvier 2026",
    "iaba.tech, Budget GEO France, 2026",
    "UlazAI, Veo 3.1 update, 2 août 2026 ; CreativeMarketing.ai, Veo 3.1 vs Runway, 17 juillet 2026",
    "Tech-Insider.org / PixVerse Blog, Runway Gen-4.5, Kling 3.0, 2026",
    "Lengow Blog, TikTok Shop France Q2 2026, juillet 2026",
    "J'ai un pote dans la com, CTV France, 31 mars 2026",
    "eMarketer / Digital Applied, Programmatique &amp; walled gardens, 2026",
    "Reworld MediaConnect / SRI, GEO x Créateurs, 21 juillet 2026",
    "Gartner via Search Engine Land, Baisse volume recherche traditionnel, 2026",
    "Ahrefs via Erlin.ai, Pages citées ChatGPT sans visibilité Google, 2026",
]

NAV = [
    ("home", "index.html", "Accueil"),
    ("marche", "articles/marche-pub.html", "Marché"),
    ("achat", "articles/achat-media.html", "IA"),
    ("video", "articles/video-ia.html", "Vidéo"),
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
            <li>Édition #7 , Été 2026</li>
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
        "Veille webmarketing Link, édition été 2026 : marché pub, achat média, production vidéo et ChatGPT Ads.",
    )
    html += f"""
  <section class="hero">
    <div class="waves" aria-hidden="true"></div>
    <div class="container hero-inner">
      <div>
        <div class="eyebrow">Édition #7 · Été 2026</div>
        <h1>Ce qui change vraiment <span>cet été.</span></h1>
        <p class="hero-lead">Un marché publicitaire qui grandit, des outils qui deviennent plus simples, et de nouveaux espaces pour vos campagnes. On vous explique l'essentiel de la rentrée, clairement, et sans jargon.</p>
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
        <dt>Vidéo sociale</dt>
        <dd>+31 %</dd>
      </dl>
    </div>
  </section>
  <div class="topics">
    <div class="container">
      <ul class="topics-list">
        <li><a href="articles/marche-pub.html">Marché pub</a></li>
        <li><a href="articles/achat-media.html">Achat média</a></li>
        <li><a href="articles/video-ia.html">Production vidéo</a></li>
        <li><a href="articles/achat-media.html">ChatGPT Ads</a></li>
      </ul>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="section-head">
        <div>
          <div class="section-kicker">Au sommaire</div>
          <h2>Trois sujets à retenir</h2>
        </div>
      </div>
      <p class="intro-text">L'été 2026 marque un tournant simple à résumer : le marché publicitaire en ligne grandit (<strong>6,689 Md€ au premier semestre, +12 %</strong>), porté par la vidéo sur les réseaux et la pub sur les sites marchands. Les outils, eux, se simplifient, et de nouveaux espaces s'ouvrent, comme la publicité dans ChatGPT, que <strong>Link peut déjà activer pour vous</strong>. Ce n'est plus une tendance à surveiller : c'est votre quotidien de demain.</p>
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
          <h2>Ce qu'il faut retenir cet été</h2>
        </div>
      </div>
      <p class="intro-text">Le marché grandit, mais la valeur se déplace vers la vidéo et les sites marchands. Les outils se simplifient, et de nouveaux espaces publicitaires apparaissent. Les marques qui prennent de l'avance maintenant sont celles qui en récolteront les fruits.</p>
      <ul class="facts">
        <li><strong>1.</strong> La vidéo est incontournable dans tout plan média 2026, les réseaux sociaux en tête.</li>
        <li><strong>2.</strong> De nouveaux espaces s'ouvrent : Link peut déjà activer vos campagnes ChatGPT Ads.</li>
        <li><strong>3.</strong> L'IA accélère la production ; c'est la direction artistique humaine qui fait la différence.</li>
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
        facts_html = ""
        if art["facts"]:
            items = "\n".join(f"            <li>{item}</li>" for item in art["facts"])
            facts_html = f'<ul class="facts">\n{items}\n        </ul>'
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
        lead_html = ""
        if art["lead"] and art["lead"] != art["chapo"]:
            lead_html = f'<p class="article-body">{art["lead"]}</p>'
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
      <div class="eyebrow">{art["label"]} · Été 2026</div>
      <h1>{art["title"]}</h1>
      <p>{art["chapo"]}</p>
    </div>
  </section>
  <div class="container">
    <div class="article-layout">
      <article>
        {kpis}
        {lead_html}
        {facts_html}
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
        "Sources citées dans l'édition été 2026 de keep the link Les News.",
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
      <div class="eyebrow">Édition #7 · Été 2026</div>
      <h1>Sources citées</h1>
      <p>Références utilisées pour l'édition d'été : observatoires, blogs plateformes et études marché.</p>
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
    for obsolete in ("geo.html", "reseaux-sociaux.html", "rgpd.html", "chatgpt-ads.html"):
        path = ROOT / "articles" / obsolete
        if path.exists():
            path.unlink()
    print("built")
