# Cenário 5: Games

**Quem:** jogadores humanos, um agente mestre (narrador ou árbitro), agentes NPC e, opcionalmente, o agente de cada jogador jogando junto.

**Exemplos de partida**
- **5a — Mesa de RPG:** o canal é a mesa. O mestre-agente narra, os NPCs respondem e os jogadores agem. Cada jogador conversa com um NPC em privado, mas os eventos do mundo valem para todos [14].
- **5b — Times mistos:** cada jogador leva o próprio agente, e os times disputam um desafio (construir algo, resolver um enigma). Bom para live.
- **5c — Dedução social:** "quem aqui é humano?". Há relatos da GDC de partidas humano × bot [17].
- **5d — Mundo persistente:** universo que continua quando ninguém está jogando, com agentes negociando e explorando, como o Gradient Bang [13].
- **5e — Curso como jogo:** trilha vira missão, um agente-tutor libera a próxima fase e a turma vê o ranking.

**O que aparece na tela:** um canal por mesa ou mundo, um painel do estado do jogo (mapa, inventário, placar) e o histórico da partida.

**Regras de design segundo as fontes**
- A lógica do jogo fica em código, e o agente cuida de diálogo e interação social [15].
- A memória dos NPCs vem de busca no histórico (RAG) [15]; memória longa e custo ainda são os gargalos [16].

**Riscos:** custo que cresce por jogador, trapaça (jogador manipulando o mestre por prompt) e lentidão de resposta.

**Faz sentido quando:** o objetivo é engajamento, live, comunidade ou ensino.
