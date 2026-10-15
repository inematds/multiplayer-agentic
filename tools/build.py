#!/usr/bin/env python3
"""Gera as páginas de conteúdo do guia a partir de conteudo/<lang>/*.md.

PT -> guia/<pagina>.html · EN -> guia/en/<pagina>.html · ES -> guia/es/<pagina>.html
O guia/index.html (landing) é escrito à mão e não é tocado aqui.
Uso: python3 tools/build.py
"""
import html, pathlib, re
import markdown

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CSS = (RAIZ / "tools" / "estilo.css").read_text()
REPO = "https://github.com/inematds/multiplayer-agentic"
SLUG = "multiplayer-agentic"

ORDEM = ["conceito", "formas", "base-tecnica", "questoes", "limites-seguranca", "personalidades", "cenarios",
         "cenario-1", "cenario-2", "cenario-3", "cenario-4", "cenario-5", "cenario-6",
         "empresas", "jogos", "caso-inema", "fontes"]

TXT = {
    "pt": dict(html="pt-BR", dir="", guia="Guia", conceito="Conceito", cenarios="Cenários",
               fontes="Fontes", paginas="Páginas", ant="Anterior", prox="Próxima",
               tema="Alternar tema", nota="Documento de conceito em discussão"),
    "en": dict(html="en", dir="en/", guia="Guide", conceito="Concept", cenarios="Scenarios",
               fontes="Sources", paginas="Pages", ant="Previous", prox="Next",
               tema="Toggle theme", nota="Concept document under discussion"),
    "es": dict(html="es", dir="es/", guia="Guía", conceito="Concepto", cenarios="Escenarios",
               fontes="Fuentes", paginas="Páginas", ant="Anterior", prox="Siguiente",
               tema="Cambiar tema", nota="Documento de concepto en discusión"),
}

EXTRA = """
  .doc{display:grid;grid-template-columns:240px minmax(0,1fr);gap:40px;padding:40px 22px 60px}
  .side{position:sticky;top:80px;align-self:start;font-size:.9rem;max-height:calc(100vh - 100px);overflow:auto}
  .side summary{display:block;margin-bottom:.6em;cursor:pointer;list-style:none}
  .side summary::-webkit-details-marker{display:none}
  @media(max-width:860px){.side summary:after{content:" ▾"}.side[open] summary:after{content:" ▴"}}
  .side a{display:block;color:var(--mut);padding:.32em .6em;border-radius:8px;border-left:2px solid transparent}
  .side a:hover{color:var(--txt)}
  .side a.on{color:var(--txt);background:var(--bg2);border-left-color:var(--amb)}
  .side a.sub{padding-left:1.4em;font-size:.86rem}
  article{max-width:76ch;min-width:0}
  article h1{font-size:clamp(1.8rem,4vw,2.6rem);font-weight:800;letter-spacing:-.025em;margin-bottom:.6em}
  article h2{font-size:1.45rem;font-weight:800;margin:1.8em 0 .5em}
  article h3{font-size:1.12rem;margin:1.5em 0 .4em}
  article p,article li{line-height:1.7}
  article ul,article ol{padding-left:1.3em}
  article li{margin:.25em 0}
  article blockquote{margin:1em 0;padding:.6em 1em;border-left:3px solid var(--amb);background:var(--bg2);border-radius:0 10px 10px 0;color:var(--mut)}
  article hr{border:none;border-top:1px solid var(--line);margin:2em 0}
  article code{background:var(--bg2);border:1px solid var(--line);border-radius:6px;padding:.05em .35em;font-size:.88em}
  article pre code{background:none;border:none;padding:0}
  article a{text-decoration:underline;text-decoration-color:rgba(226,162,59,.45);text-underline-offset:3px}
  article a.ref{text-decoration:none;font-size:.82em;vertical-align:.15em}
  .tbl{overflow-x:auto;margin:1.2em 0;border:1px solid var(--line);border-radius:12px}
  .tbl table{border-collapse:collapse;width:100%;font-size:.9rem}
  .tbl th,.tbl td{padding:.6em .8em;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
  .tbl th{background:var(--bg2);font-family:Sora;font-weight:600}
  .tbl tr:last-child td{border-bottom:none}
  .pn{display:flex;justify-content:space-between;gap:12px;margin-top:3em;padding-top:1.5em;border-top:1px solid var(--line)}
  .pn a{display:block;border:1px solid var(--line);border-radius:12px;padding:.8em 1em;max-width:48%;text-decoration:none;color:var(--txt)}
  .pn a:hover{border-color:var(--amb)}
  .pn small{display:block;color:var(--mut);font-size:.78rem}
  ol.fontes li{margin:.7em 0;overflow-wrap:anywhere}
  ol.fontes li:target{background:rgba(226,162,59,.12);border-radius:8px}
  @media(max-width:860px){.doc{grid-template-columns:1fr;gap:18px}.side{position:static;max-height:none;border:1px solid var(--line);border-radius:12px;padding:12px}}
"""


def titulo(md):
    m = re.match(r"#\s+(.+)", md)
    return m.group(1).strip() if m else "?"


def render(md, nome):
    md = re.sub(r"^#\s+.+\n", "", md, count=1)
    corpo = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "toc"])
    corpo = re.sub(r"<table>", '<div class="tbl"><table>', corpo)
    corpo = corpo.replace("</table>", "</table></div>")
    # citações [n] -> link para a página de fontes
    if nome != "fontes":
        corpo = re.sub(r"\[(\d{1,2})\]", r'<a class="ref" href="fontes.html#f\1">[\1]</a>', corpo)
    else:
        n = [0]
        def li(_):
            n[0] += 1
            return f'<li id="f{n[0]}">'
        corpo = corpo.replace("<ol>", '<ol class="fontes">', 1)
        corpo = re.sub(r"<li>", li, corpo)
        corpo = re.sub(r"(?<![\"'>])(https?://[^\s<]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', corpo)
    return corpo


def pagina(lang, nome, titulos):
    t = TXT[lang]
    md = (RAIZ / "conteudo" / lang / f"{nome}.md").read_text()
    tit = titulos[nome]
    corpo = render(md, nome)
    i = ORDEM.index(nome)
    lado = []
    for p in ORDEM:
        cls = "on" if p == nome else ""
        if p.startswith("cenario-"):
            cls = (cls + " sub").strip()
        lado.append(f'<a class="{cls}" href="{p}.html">{html.escape(titulos[p])}</a>')
    ant = ORDEM[i - 1] if i > 0 else None
    prox = ORDEM[i + 1] if i < len(ORDEM) - 1 else None
    pn = '<div class="pn">'
    pn += (f'<a href="{ant}.html"><small>← {t["ant"]}</small>{html.escape(titulos[ant])}</a>'
           if ant else f'<a href="./"><small>← {t["guia"]}</small>{t["guia"]}</a>')
    pn += (f'<a href="{prox}.html" style="text-align:right"><small>{t["prox"]} →</small>{html.escape(titulos[prox])}</a>'
           if prox else "<span></span>")
    pn += "</div>"
    pre = "../" if lang != "pt" else ""
    seletor = {
        "pt": f'<a class="on" href="{nome}.html">PT</a><a href="en/{nome}.html">EN</a><a href="es/{nome}.html">ES</a>',
        "en": f'<a href="../{nome}.html">PT</a><a class="on" href="{nome}.html">EN</a><a href="../es/{nome}.html">ES</a>',
        "es": f'<a href="../{nome}.html">PT</a><a href="../en/{nome}.html">EN</a><a class="on" href="{nome}.html">ES</a>',
    }[lang]
    base = f"https://inematds.github.io/{SLUG}/guia/"
    return f"""<!DOCTYPE html>
<html lang="{t['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(tit)} — Multiplayer Agentic</title>
<meta name="description" content="Multiplayer Agentic · {html.escape(tit)} · {t['nota']}">
<link rel="alternate" hreflang="pt-BR" href="{base}{nome}.html">
<link rel="alternate" hreflang="en" href="{base}en/{nome}.html">
<link rel="alternate" hreflang="es" href="{base}es/{nome}.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
{CSS}{EXTRA}</style>
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="./"><span class="emoji">🎮</span> Multiplayer Agentic</a>
  <span class="sep">|</span>
  <span class="clubpro">
    <a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a>
    <span class="sep">-</span>
    <a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a>
  </span>
  <div class="links">
    <a class="sec" href="./">{t['guia']}</a>
    <a class="sec" href="conceito.html">{t['conceito']}</a>
    <a class="sec" href="cenarios.html">{t['cenarios']}</a>
    <a class="sec" href="fontes.html">{t['fontes']}</a>
    <span class="lang">{seletor}</span>
    <button class="tgl" id="themeToggle" aria-label="{t['tema']}" title="{t['tema']}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">GitHub</a>
  </div>
</div></nav>
<div class="wrap doc">
  <details class="side" id="side"><summary class="chip">{t['paginas']}</summary>{''.join(lado)}</details>
  <article>
    <h1>{html.escape(tit)}</h1>
{corpo}
{pn}
  </article>
</div>
<footer>
  <div class="wrap">
    <p>Multiplayer Agentic · {t['nota']} ·
      <a href="{REPO}">inematds/multiplayer-agentic</a> ·
      <a href="https://inema.club">INEMA.CLUB</a></p>
  </div>
</footer>
<script>
  (function(){{
    var sd=document.getElementById('side'); if(sd && innerWidth>860) sd.open=true;
    var KEY='{SLUG}-theme';
    var b=document.body, t=document.getElementById('themeToggle');
    if(localStorage.getItem(KEY)==='light'){{ b.classList.add('light'); t.textContent='☀️'; }}
    t.addEventListener('click',function(){{
      var light=b.classList.toggle('light');
      t.textContent=light?'☀️':'🌙';
      localStorage.setItem(KEY, light?'light':'dark');
    }});
  }})();
</script>
</body>
</html>
"""


def main():
    for lang, t in TXT.items():
        src = RAIZ / "conteudo" / lang
        if not src.exists():
            print(f"[{lang}] sem conteudo/{lang}, pulado")
            continue
        titulos = {n: titulo((src / f"{n}.md").read_text()) for n in ORDEM}
        dest = RAIZ / "guia" / t["dir"]
        dest.mkdir(parents=True, exist_ok=True)
        for n in ORDEM:
            (dest / f"{n}.html").write_text(pagina(lang, n, titulos))
        idx = src / "index.html"
        if idx.exists():
            (dest / "index.html").write_text(idx.read_text().replace("@@CSS@@", CSS))
        print(f"[{lang}] {len(ORDEM)} páginas em guia/{t['dir']}")


if __name__ == "__main__":
    main()
