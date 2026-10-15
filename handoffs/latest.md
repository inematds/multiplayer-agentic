# Handoffs — trabalhos abertos

Cada linha é um assunto em andamento: leia o snapshot do assunto que for continuar. Gravado por handoff-grava.py.

<!-- handoff-indice:inicio -->
- `multiplayer-agentic` · handoffs/history/2026-10-15T215536Z-multiplayer-agentic.md · 15/10 18:55
<!-- handoff-indice:fim -->

---

Cópia integral do snapshot mais recente (handoffs/history/2026-10-15T215536Z-multiplayer-agentic.md):

# Handoff — 2026-10-15 — Conceito multiplayer agentic: site PT pronto, EN/ES traduzindo, falta publicar

## Projeto e escopo
Projeto ~/projetos/multiplayer-agentic (conceito, sem código de produto): sistema onde pessoas, agentes de IA e bots do Telegram dividem canais. O Nei pediu documento de discussão com possibilidades e fontes, 6 cenários, limites/segurança/personalidades, páginas de conteúdo além do guia, e publicar no portal e no grupo INEMA.AGENTES do Telegram. Não citar a ferramenta do vídeo de origem (Kylan).

## Objetivo atual
Publicar: repo inematds/multiplayer-agentic público + GitHub Pages (guia/ PT/EN/ES), card no portal (atualiza-portal, + EN/ES em translated-courses.ts) e tópico no INEMA.AGENTES (postar-telegram). Pronto = 3 URLs /guia/, /guia/en/, /guia/es/ respondendo 200, portal com push, tópico + MENU no Telegram.

## Estado aceito
- [confirmed] CONCEITO.md v0.3 com seções 1–12 + 17 fontes — CONCEITO.md
- [confirmed] Fonte das páginas PT: 17 .md + landing index.html (marcador @@CSS@@) — conteudo/pt/
- [confirmed] Gerador md→HTML (sidebar recolhível no celular, refs [n] linkam fontes.html#fN, prev/next) — tools/build.py, tools/estilo.css
- [confirmed] Site PT gerado em guia/ (18 páginas), layout ok 360–1920 sem rolagem horizontal — tools/checar.cjs
- [confirmed] Capa capa/capa.png, hero guia/assets/hero.png, 6 banners PT/EN/ES conferidos (texto certo) — guia/assets/
- [confirmed] README.md/.en/.es, CLAUDE.md (com Self-learning/Lessons), LESSONS.md, .github/workflows/pages.yml, .nojekyll

## Proposto / tentado, não confirmado
- [unverified] Traduções EN e ES por dois subagentes em segundo plano escrevendo conteudo/en/ e conteudo/es/ (34 de 36 arquivos existiam na última checagem) — aguardar notificação e conferir
- [?] build.py só roda completo quando en/ e es/ tiverem os 18 arquivos (senão FileNotFoundError); para PT só: python3 -c "import sys;sys.path.insert(0,'tools');import build;build.TXT={'pt':build.TXT['pt']};build.main()"

## Decisões e restrições
- Página = landing guia/index.html + páginas de conteúdo em guia/*.html (não um único guia) — pedido do Nei
- Kylan removido de tudo — pedido do Nei
- Autor dos commits inematds <inematds@gmail.com>; push de .github/workflows exige SSH (token gh inematds sem escopo workflow)
- Repo precisa ser público para Pages; o Nei pediu publicação

## Arquivos alterados
- Tudo em ~/projetos/multiplayer-agentic (projeto novo nesta sessão; ainda não é repo git)
- Fora do projeto: nenhum

## Memória e regras duráveis tocadas
- nenhuma

## Verificação
- Rodado: NODE_PATH=~/.npm-global/lib/node_modules node tools/checar.cjs pt → só restaram links para en/ e es/ (ainda inexistentes); rolagem horizontal corrigida (menu some abaixo de 1000px)
- Rodado: screenshots 1280 e 390 conferidos visualmente
- Não rodado: checar.cjs en es, build completo, git/push, Pages, portal, Telegram — dependem das traduções

## Estado em execução
- Processos em segundo plano: dois subagentes de tradução (EN e ES) — notificam ao terminar
- Servidores / portas: nenhum
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: nenhuma (publicação já pedida pelo Nei)

## Próxima ação exata
Ao terminarem as traduções: python3 tools/build.py && node tools/checar.cjs (todos OK) → git init, user inematds local, commit, gh repo create inematds/multiplayer-agentic --public, push via SSH, gh api pages build_type=workflow, conferir 3 URLs → skill atualiza-portal (+EN/ES) → skill postar-telegram no INEMA.AGENTES.

## Mapa de retomada
- CLAUDE.md — regras do projeto
- tools/build.py — como o site é gerado
- conteudo/pt/index.html — landing
- CONCEITO.md — documento inteiro

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim
