# Possibilities for games

| Format | What it would look like | Source or note |
|---|---|---|
| **RPG table with a master agent** | The channel is the table; one agent is the master, other agents are NPCs, humans play | Design rule: conversation with an NPC is private per player, and world events are the same for everyone [14] |
| **Persistent world with agents playing** | Agents and humans in the same universe | Gradient Bang: open space trading where ships, NPCs and systems are LLM agents [13] (source is a directory; check the repository) |
| **Mixed teams** | Each person brings their agent and the teams compete | Good format for a live stream or event |
| **Social deduction** | "Who here is human?" | Google presented at GDC lessons from human × bot matches and bot-only matches [17] |
| **Text MUD with agent NPC** | Text game with characters that really talk | Developer report from July 2026 [14] |
| **Course gamification** | Track as a mission; a tutor agent unlocks the next stage when the student delivers | Connects with the portal and the courses |

**What the sources say about limits:**
- In 2026, most games use a hybrid model: the rules and the game loop stay in classic code, and the agent handles dialogue and social interaction [15].
- Long NPC memory and computational cost are still the bottlenecks. An academic work concludes that models specialized for games tend to work better than generic ones [16].
- Memory by searching the history (RAG) is the most cited architecture [15].
