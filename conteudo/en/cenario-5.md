# Scenario 5: Games

**Who:** human players, a master agent (narrator or referee), NPC agents and, optionally, each player's agent playing along.

**Example sessions**
- **5a — RPG table:** the channel is the table. The master agent narrates, the NPCs respond and the players act. Each player talks to an NPC in private, but world events apply to everyone [14].
- **5b — Mixed teams:** each player brings their own agent, and the teams compete on a challenge (build something, solve a puzzle). Good for a live stream.
- **5c — Social deduction:** "who here is human?". There are GDC reports of human × bot matches [17].
- **5d — Persistent world:** a universe that keeps going when nobody is playing, with agents trading and exploring, like Gradient Bang [13].
- **5e — Course as a game:** a track becomes a mission, a tutor agent unlocks the next stage and the class sees the ranking.

**What shows on screen:** one channel per table or world, a game state panel (map, inventory, scoreboard) and the match history.

**Design rules according to the sources**
- The game logic stays in code, and the agent handles dialogue and social interaction [15].
- NPC memory comes from searching the history (RAG) [15]; long memory and cost are still the bottlenecks [16].

**Risks:** cost that grows per player, cheating (a player manipulating the master through a prompt) and slow responses.

**Makes sense when:** the goal is engagement, live streaming, community or teaching.
