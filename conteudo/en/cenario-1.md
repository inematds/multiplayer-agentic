# Scenario 1: Local use: me and my agents

**Who:** only the owner. On the other side: the Telegram bots, the Claude Code and Codex sessions, the queues and the timers.

**A typical day**
- 06:00 the Spanish queue publishes a video → "published" event with a link.
- 08:00 advviral generates the radar → event with a preview and a "view" button.
- 10:00 a request arrives through bot v3 → "request received" event, then "agent X picked it up", then "finished".
- 14:00 a Claude session hangs → alert event.
- 21:00 daily summary: what came in, what went out and what failed.

**What shows on screen**
- Channels by source: `#telegram`, `#agents`, `#queues`, `#publications`, `#alerts`.
- Filters by agent, bot and period; highlight only what needs action.

**Possibilities**
- **1a:** read-only panel (form A).
- **1b:** panel where you can reply to a bot or call an agent (form B).
- **1c:** no new panel, using a private Telegram group as the flow [10].

**Open:** how much noise is acceptable? Is an agent needed to summarize the flow?

**Makes sense when:** the problem is "I don't know what is running or what arrived".
