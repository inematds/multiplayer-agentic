# Escenario 5: Juegos

**Quién:** jugadores humanos, un agente maestro (narrador o árbitro), agentes NPC y, opcionalmente, el agente de cada jugador jugando junto.

**Ejemplos de partida**
- **5a — Mesa de rol:** el canal es la mesa. El agente maestro narra, los NPC responden y los jugadores actúan. Cada jugador conversa con un NPC en privado, pero los eventos del mundo valen para todos [14].
- **5b — Equipos mixtos:** cada jugador lleva su propio agente, y los equipos compiten en un desafío (construir algo, resolver un enigma). Bueno para transmisiones en vivo.
- **5c — Deducción social:** "¿quién aquí es humano?". Hay relatos de la GDC sobre partidas humano × bot [17].
- **5d — Mundo persistente:** universo que continúa cuando nadie está jugando, con agentes negociando y explorando, como Gradient Bang [13].
- **5e — Curso como juego:** la ruta se vuelve misión, un agente-tutor libera la siguiente fase y el grupo ve el ranking.

**Qué aparece en la pantalla:** un canal por mesa o mundo, un panel del estado del juego (mapa, inventario, marcador) y el historial de la partida.

**Reglas de diseño según las fuentes**
- La lógica del juego queda en código, y el agente se ocupa del diálogo y la interacción social [15].
- La memoria de los NPC viene de búsqueda en el historial (RAG) [15]; la memoria larga y el costo siguen siendo los cuellos de botella [16].

**Riesgos:** costo que crece por jugador, trampa (jugador manipulando al maestro por prompt) y lentitud de respuesta.

**Tiene sentido cuando:** el objetivo es engagement, transmisión en vivo, comunidad o enseñanza.
