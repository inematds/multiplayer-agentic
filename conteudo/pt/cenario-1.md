# Cenário 1: Uso local: eu e meus agentes

**Quem:** só o dono. Do outro lado: os bots do Telegram, as sessões de Claude Code e Codex, as filas e os timers.

**Um dia típico**
- 06:00 a fila em espanhol publica um vídeo → evento "publicado" com link.
- 08:00 o advviral gera o radar → evento com prévia e botão "ver".
- 10:00 um pedido chega pelo bot v3 → evento "pedido recebido", depois "agente X pegou", depois "terminou".
- 14:00 uma sessão de Claude trava → evento de alerta.
- 21:00 resumo do dia: o que entrou, o que saiu e o que falhou.

**O que aparece na tela**
- Canais por origem: `#telegram`, `#agentes`, `#filas`, `#publicações`, `#alertas`.
- Filtros por agente, bot e período; destaque só para o que pede ação.

**Possibilidades**
- **1a:** painel só de leitura (forma A).
- **1b:** painel em que dá para responder um bot ou chamar um agente (forma B).
- **1c:** sem painel novo, usando um grupo privado do Telegram como fluxo [10].

**Em aberto:** quanto barulho é aceitável? É preciso um agente que resuma o fluxo?

**Faz sentido quando:** o problema é "não sei o que está rodando nem o que chegou".
