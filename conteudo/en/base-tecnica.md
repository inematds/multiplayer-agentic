# Technical base options

| Path | What it is | ➕ | ➖ |
|---|---|---|---|
| **Buzz (Block)** [1][2][3] | Open space (Apache-2.0) built on the Nostr protocol: every human and every agent has its own key pair. Agents join through the Agent Client Protocol (ACP); Claude Code, Codex and goose are supported. Can be hosted here | Closest to the video, open, native agent identity | Declared unfinished, one relay per workspace, no mobile app |
| **Matrix / Element + MindRoom** [7] | Each agent becomes a Matrix account and the conversation happens in threads | Mature, federated, encrypted protocol, with mobile apps ready | More pieces to assemble and run |
| **Zulip or Mattermost** [8] | Mature open chats with a bot API. Zulip organizes conversation by "topic" | Stable, with apps ready | The agent is a "bot", not a first-class member. In the comparison in [8], Mattermost shows limited features in the open version |
| **Macro Chat** [8] | Chat, planning and git with agents (Apache-2.0) | Also agent-first | Little known, few sources |
| **nexor-agora** [6] | Small Python package (MIT): humans and Claude Code sessions in the same room; an @mention wakes the session | Lightweight, good for study | Small project, uncertain maturity |
| **Build our own** | Our own event bus and web panel | Tailored to the bots, queues and hooks that already exist | Redoing channels, search and permissions is expensive |
| **Telegram as the interface** | Use the Telegram groups themselves as "channels", with the Claude Code Channels bridge [10] | Already on the phone and everyone already uses it | No consolidated view; Telegram becomes a bottleneck |

Concept references, not for direct use: MeshAgent ("rooms" with shared context, access control and tracing) [9], Mastra Channels (agents living in Slack, Teams and Discord) [11], Claude Slack (channels for agents via MCP) [12].
