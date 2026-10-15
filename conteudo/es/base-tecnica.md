# Posibilidades de base técnica

| Camino | Qué es | ➕ | ➖ |
|---|---|---|---|
| **Buzz (Block)** [1][2][3] | Espacio abierto (Apache-2.0) construido sobre el protocolo Nostr: cada humano y cada agente tiene su propio par de claves. Los agentes entran por el Agent Client Protocol (ACP); Claude Code, Codex y goose son compatibles. Se puede alojar aquí | Lo más cercano al video, abierto, identidad de agente nativa | Declarado inacabado, un relay por workspace, sin app de celular |
| **Matrix / Element + MindRoom** [7] | Cada agente se vuelve una cuenta Matrix y la conversación ocurre en threads | Protocolo maduro, federado, cifrado, con apps de celular listas | Más piezas para armar y operar |
| **Zulip o Mattermost** [8] | Chats abiertos maduros con API de bots. Zulip organiza la conversación por "tema" | Estables, con apps listas | El agente es un "bot", no un miembro de primera clase. En la comparación de [8], Mattermost aparece con funciones limitadas en la versión abierta |
| **Macro Chat** [8] | Chat, planificación y git con agentes (Apache-2.0) | También es agent-first | Poco conocido, pocas fuentes |
| **nexor-agora** [6] | Paquete pequeño de Python (MIT): humanos y sesiones de Claude Code en la misma sala; la @mención despierta la sesión | Liviano, bueno para estudiar | Proyecto pequeño, madurez incierta |
| **Construcción propia** | Un bus de eventos y un panel web propios | A la medida de los bots, colas y hooks que ya existen | Rehacer canales, búsqueda y permisos sale caro |
| **Telegram como interfaz** | Usar los propios grupos de Telegram como "canales", con el puente Claude Code Channels [10] | Ya está en el celular y todos ya lo usan | Ninguna vista consolidada; Telegram se vuelve un cuello de botella |

Referencias de concepto, sin uso directo: MeshAgent ("rooms" con contexto compartido, control de acceso y trazabilidad) [9], Mastra Channels (agentes que viven en Slack, Teams y Discord) [11], Claude Slack (canales para agentes vía MCP) [12].
