#!/usr/bin/env python3
"""Divide o CONCEITO.md em páginas de conteúdo (conteudo/pt/*.md). Rodar uma vez; depois edite os .md."""
import re, pathlib

raiz = pathlib.Path(__file__).resolve().parent.parent
txt = (raiz / "CONCEITO.md").read_text()

secoes = re.split(r"^## ", txt, flags=re.M)
cab = {}
for s in secoes[1:]:
    titulo, _, corpo = s.partition("\n")
    cab[titulo.strip()] = corpo.strip()

def pega(prefixo):
    for k, v in cab.items():
        if k.startswith(prefixo):
            return k, v
    raise KeyError(prefixo)

def limpa(t):
    t = re.sub(r"\n---\s*$", "", t.strip()).strip()
    return t

links = {
    "seção 3": "[formas do sistema](formas.html)",
    "seção 4": "[base técnica](base-tecnica.html)",
    "seção 5": "[questões em aberto](questoes.html)",
    "seção 6": "[cenários](cenarios.html)",
    "seção 9": "[caso INEMA](caso-inema.html)",
}
def troca(t):
    for a, b in links.items():
        t = t.replace(a, b)
    return t

out = raiz / "conteudo" / "pt"
out.mkdir(parents=True, exist_ok=True)
def grava(nome, titulo, corpo):
    (out / f"{nome}.md").write_text(f"# {titulo}\n\n{troca(limpa(corpo))}\n")

k1, v1 = pega("1."); k2, v2 = pega("2.")
grava("conceito", "A ideia", f"## {k1[3:]}\n\n{limpa(v1)}\n\n## {k2[3:]}\n\n{limpa(v2)}")
for pre, nome in [("3.", "formas"), ("4.", "base-tecnica"), ("5.", "questoes"),
                  ("7.", "empresas"), ("8.", "jogos")]:
    k, v = pega(pre)
    grava(nome, k[3:], v)
k9, v9 = pega("9."); k10, v10 = pega("10.")
grava("caso-inema", k9[3:], f"{limpa(v9)}\n\n## {k10[4:]}\n\n{limpa(v10)}")
_, vf = pega("Fontes")
grava("fontes", "Fontes", vf)

# cenários: visão geral + uma página por cenário
_, v6 = pega("6.")
partes = re.split(r"^### ", v6, flags=re.M)
intro = partes[0]
geral = ""
liga = ""
for p in partes[1:]:
    t, _, c = p.partition("\n")
    t = t.strip()
    m = re.match(r"Cenário (\d) — (.*)", t)
    if m:
        grava(f"cenario-{m.group(1)}", f"Cenário {m.group(1)}: {m.group(2)}", c)
    elif t.startswith("Visão geral"):
        geral = limpa(c)
    elif t.startswith("Como os cenários"):
        liga = limpa(c)
grava("cenarios", "Cenários de uso",
      f"{limpa(intro)}\n\n## Visão geral\n\n{geral}\n\n## Como os cenários se ligam\n\n{liga}")
print(sorted(p.name for p in out.iterdir()))
