# Escenario 6: Clientes y proveedores

**Quién:** personas de afuera (clientes, proveedores, aliados), agentes de atención y compras, y el equipo interno supervisando.

**Un día típico**
- **Cliente:** el mensaje llega por WhatsApp o Telegram y cae en el canal `#cliente-fulano`. El agente sugiere la respuesta y el humano la libera o toma el control.
- **Pedido:** el agente confirma plazo y stock con el proveedor en el canal `#proveedor-y`, donde el agente del proveedor también puede estar.
- **Escalamiento:** un reclamo o un monto alto va directo a una persona, con el historial resumido.
- **Panel:** cola de atención, tiempo de respuesta y qué está esperando a quién.

**Posibilidades**
- **6a — Atención supervisada:** todo envío pasa por aprobación humana. Más seguro, más lento.
- **6b — Autonomía por tipo:** las preguntas simples el agente las responde solo; el resto pide aprobación.
- **6c — Agente de la empresa conversando con agente del proveedor:** negociación de rutina entre agentes, y el humano aprueba el cierre.
- **6d — Portal del cliente:** el cliente ve su propio canal (pedido, entrega, archivos), sin ver nada interno.

**Qué pasa a ser obligatorio**
- Separación total entre canales externos e internos.
- Protección contra inyección de prompt: el mensaje de un cliente es dato, nunca instrucción.
- Registro de lo que se envió y de quién lo aprobó.
- Cuidado con los datos personales (LGPD).

**Riesgos:** un error del agente llega directo al cliente, filtración de información interna e intento de manipulación por parte de quien está afuera.

**Tiene sentido cuando:** hay volumen de atención repetitiva y el equipo es pequeño. Se conecta con los kits de atención (clínica, restaurante, hotel).
