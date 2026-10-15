# Use scenarios

There are six scenarios, from smallest to largest in people, risk and cost. Each one covers who takes part, an example day, what shows on screen and what stays open. Forms A–D are in [System forms](formas.html), the technical bases in [Technical base](base-tecnica.html) and the numbered questions in [Open questions](questoes.html).

## Overview

| # | Scenario | Who joins | Likely form | Main risk | Complexity |
|---|---|---|---|---|---|
| 1 | Local use | Only the owner and their agents | A → B | Noise (too many messages) | Low |
| 2 | Me, my agents and guests | Owner, agents and a few invited people | B → C | Guest giving orders to the owner's agent | Medium |
| 3 | Company: one department | A small team with its agents | C | Adoption (nobody uses it) | Medium |
| 4 | The whole company | Several departments, managers and agents per area | C with governance | Permissions, cost and audit | High |
| 5 | Games | Players, master agent and NPC agents | C with game rules | Cost per player and memory | Medium to high |
| 6 | Customers and suppliers | People outside the company, support agents and internal team | B with approval | Data leaks and prompt injection | High |

## How the scenarios connect

The scenarios can work as steps:

```
1 local  →  2 with guests  →  3 one department  →  4 whole company
                                      ↘
                                       6 customers and suppliers
              5 games  (separate branch, reuses the engine of scenarios 1–2)
```

**Open:** start at step 1 and climb, or pick a target scenario (for example, 6 as a product) and build straight for it?
