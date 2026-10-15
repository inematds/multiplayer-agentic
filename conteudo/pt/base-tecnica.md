# Possibilidades de base técnica

| Caminho | O que é | ➕ | ➖ |
|---|---|---|---|
| **Buzz (Block)** [1][2][3] | Espaço aberto (Apache-2.0) feito sobre o protocolo Nostr: cada humano e cada agente tem um par de chaves próprio. Agentes entram pelo Agent Client Protocol (ACP); Claude Code, Codex e goose são suportados. Pode ser hospedado aqui | Mais próximo do vídeo, aberto, identidade de agente nativa | Declarado inacabado, um relay por workspace, sem app de celular |
| **Matrix / Element + MindRoom** [7] | Cada agente vira uma conta Matrix e a conversa acontece em threads | Protocolo maduro, federado, criptografado, com apps de celular prontos | Mais peças para montar e operar |
| **Zulip ou Mattermost** [8] | Chats abertos maduros com API de bots. O Zulip organiza a conversa por "tópico" | Estáveis, com apps prontos | Agente é "bot", não membro de primeira classe. Na comparação de [8], o Mattermost aparece com recursos limitados na versão aberta |
| **Macro Chat** [8] | Chat, planejamento e git com agentes (Apache-2.0) | Também é agent-first | Pouco conhecido, pouca fonte |
| **nexor-agora** [6] | Pacote Python pequeno (MIT): humanos e sessões de Claude Code na mesma sala; a @menção acorda a sessão | Leve, bom de estudar | Projeto pequeno, maturidade incerta |
| **Construção própria** | Barramento de eventos e um painel web próprios | Sob medida para bots, filas e hooks já existentes | Refazer canais, busca e permissões custa caro |
| **Telegram como interface** | Usar os próprios grupos do Telegram como "canais", com a ponte Claude Code Channels [10] | Já está no celular e todo mundo já usa | Nenhuma visão consolidada; o Telegram vira gargalo |

Referências de conceito, sem uso direto: MeshAgent ("rooms" com contexto compartilhado, controle de acesso e rastreio) [9], Mastra Channels (agentes vivendo em Slack, Teams e Discord) [11], Claude Slack (canais para agentes via MCP) [12].
