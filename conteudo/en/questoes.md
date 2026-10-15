# Open design questions

1. **Identity.** Agent as a real member, with its own key as in Buzz [1], or as one owner's bot?
2. **Agent talking to agent.** Allowed, allowed with a turn cap, or only with a human mediating? Without a limit, agents can loop and burn the subscription.
3. **Permission and security.** A message written by another person in the channel can induce your agent to execute something (prompt injection). Possible safeguards: each person's agent only obeys its owner, human approval for any external action, a list of allowed actions per channel.
4. **Availability.** An agent on a subscription depends on the machine being on, as the video warns. Options: an always-on machine, VPS, or hosted agent (which pays per use).
5. **Cost.** Show credit per person, room and agent, as in the video? Your own subscription has no marginal cost, but has a weekly limit.
6. **Memory.** Memory per channel, per agent or both? Who can read another person's agent memory?
7. **Privacy.** In the video, each person decides whether to share their own Claude or Codex. This control needs to exist.
8. **Noise.** How to keep the event flow from becoming unreadable? Options: filters, summaries per agent, alerts only for what needs action.
