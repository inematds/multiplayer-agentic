# Cenário 6: Clientes e fornecedores

**Quem:** pessoas de fora (clientes, fornecedores, parceiros), agentes de atendimento e compras, e a equipe interna supervisionando.

**Um dia típico**
- **Cliente:** a mensagem chega pelo WhatsApp ou Telegram e cai no canal `#cliente-fulano`. O agente sugere a resposta e o humano libera ou assume.
- **Pedido:** o agente confirma prazo e estoque com o fornecedor no canal `#fornecedor-y`, onde o agente do fornecedor também pode estar.
- **Escalada:** reclamação ou valor alto vai direto para uma pessoa, com o histórico resumido.
- **Painel:** fila de atendimento, tempo de resposta e o que está esperando quem.

**Possibilidades**
- **6a — Atendimento supervisionado:** todo envio passa por aprovação humana. Mais seguro, mais lento.
- **6b — Autonomia por tipo:** perguntas simples o agente responde sozinho; o resto pede aprovação.
- **6c — Agente da empresa conversando com agente do fornecedor:** negociação de rotina entre agentes, e o humano aprova o fechamento.
- **6d — Portal do cliente:** o cliente vê o próprio canal (pedido, entrega, arquivos), sem ver nada interno.

**O que passa a ser obrigatório**
- Separação total entre canais externos e internos.
- Proteção contra injeção de prompt: mensagem de cliente é dado, nunca instrução.
- Registro do que foi enviado e de quem aprovou.
- Cuidado com dados pessoais (LGPD).

**Riscos:** um erro do agente chega direto ao cliente, vazamento de informação interna e tentativa de manipulação por quem está de fora.

**Faz sentido quando:** há volume de atendimento repetitivo e a equipe é pequena. Liga com os kits de atendimento (clínica, restaurante, hotel).
