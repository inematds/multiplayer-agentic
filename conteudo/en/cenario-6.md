# Scenario 6: Customers and suppliers

**Who:** outside people (customers, suppliers, partners), support and purchasing agents, and the internal team supervising.

**A typical day**
- **Customer:** the message arrives through WhatsApp or Telegram and lands in the `#customer-fulano` channel. The agent suggests the reply and the human releases it or takes over.
- **Order:** the agent confirms lead time and stock with the supplier in the `#supplier-y` channel, where the supplier's agent may also be present.
- **Escalation:** a complaint or high value goes straight to a person, with the history summarized.
- **Panel:** support queue, response time and what is waiting on whom.

**Possibilities**
- **6a — Supervised support:** every outgoing message goes through human approval. Safer, slower.
- **6b — Autonomy by type:** simple questions the agent answers alone; the rest asks for approval.
- **6c — Company agent talking to supplier agent:** routine negotiation between agents, and the human approves the closing.
- **6d — Customer portal:** the customer sees their own channel (order, delivery, files), without seeing anything internal.

**What becomes mandatory**
- Total separation between external and internal channels.
- Protection against prompt injection: a customer message is data, never instruction.
- A record of what was sent and who approved it.
- Care with personal data (LGPD).

**Risks:** an agent error reaches the customer directly, leak of internal information and manipulation attempts by outsiders.

**Makes sense when:** there is a volume of repetitive support and the team is small. Connects with the support kits (clinic, restaurant, hotel).
