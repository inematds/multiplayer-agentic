# Scenario 2: Me, my agents and guests

**Who:** the owner, their agents and 1 to 5 guests (partner, editor, collaborator, advanced student). A guest can bring their own agent, as in the video.

**A typical day**
- The guest joins the `#project-x` channel and asks the owner's agent about progress.
- The agent answers with what it knows about the project, without showing the rest of the owner's machine.
- The guest connects their Claude, and the two agents split the task (one writes, the other reviews).
- Anything that goes outside (publish, send, delete) waits for the owner to approve in the thread.

**What changes compared with scenario 1**
- **Who can do what** now exists: the guest talks, but cannot make the owner's agent execute anything.
- The guest sees only the channels they were invited to.
- Cost: each agent runs on its own owner's subscription, as in the video.

**Possibilities**
- **2a:** the guest only talks, and the owner's agent answers in read-only mode.
- **2b:** the guest can request tasks, and the owner approves each one.
- **2c:** guest with their own agent, in a shared channel with a cap on turns between agents.

**Risks:** prompt injection coming from the guest's message ([question 3](questoes.html)) and privacy of the owner's memory (question 6).

**Makes sense when:** there is a partnership or a two-person project and the exchange today happens over WhatsApp, with screenshots.
