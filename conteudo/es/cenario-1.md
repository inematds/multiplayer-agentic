# Escenario 1: Uso local: yo y mis agentes

**Quién:** solo el dueño. Del otro lado: los bots de Telegram, las sesiones de Claude Code y Codex, las colas y los timers.

**Un día típico**
- 06:00 la cola en español publica un video → evento "publicado" con enlace.
- 08:00 advviral genera el radar → evento con vista previa y botón "ver".
- 10:00 llega un pedido por el bot v3 → evento "pedido recibido", luego "agente X lo tomó", luego "terminó".
- 14:00 una sesión de Claude se traba → evento de alerta.
- 21:00 resumen del día: qué entró, qué salió y qué falló.

**Qué aparece en la pantalla**
- Canales por origen: `#telegram`, `#agentes`, `#colas`, `#publicaciones`, `#alertas`.
- Filtros por agente, bot y período; solo se destaca lo que pide acción.

**Posibilidades**
- **1a:** panel de solo lectura (forma A).
- **1b:** panel en el que se puede responder a un bot o llamar a un agente (forma B).
- **1c:** sin panel nuevo, usando un grupo privado de Telegram como flujo [10].

**Abierto:** ¿cuánto ruido es aceptable? ¿Hace falta un agente que resuma el flujo?

**Tiene sentido cuando:** el problema es "no sé qué está corriendo ni qué llegó".
