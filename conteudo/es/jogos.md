# Posibilidades para juegos

| Formato | Cómo sería | Fuente u observación |
|---|---|---|
| **Mesa de rol con maestro-agente** | El canal es la mesa; un agente es el maestro, otros agentes son NPC, los humanos juegan | Regla de diseño: la conversación con un NPC es privada por jugador, y los eventos del mundo son iguales para todos [14] |
| **Mundo persistente con agentes jugando** | Agentes y humanos en el mismo universo | Gradient Bang: comercio espacial abierto en el que naves, NPC y sistemas son agentes LLM [13] (la fuente es un directorio; verificar en el repositorio) |
| **Equipos mixtos** | Cada persona trae su agente y los equipos compiten | Buen formato para transmisión en vivo o evento |
| **Deducción social** | "¿Quién aquí es humano?" | Google presentó en la GDC aprendizajes de partidas humano × bot y solo entre bots [17] |
| **MUD de texto con NPC agente** | Juego de texto con personajes que conversan de verdad | Relato de un desarrollador de julio de 2026 [14] |
| **Gamificación de curso** | La ruta como misión; un agente-tutor libera la siguiente fase cuando el alumno entrega | Se conecta con el portal y los cursos |

**Lo que dicen las fuentes sobre los límites:**
- En 2026, la mayoría de los juegos usa un modelo híbrido: las reglas y el loop del juego quedan en código clásico, y el agente se ocupa del diálogo y la interacción social [15].
- La memoria larga de los NPC y el costo computacional siguen siendo los cuellos de botella. Un trabajo académico concluye que los modelos especializados para juegos tienden a funcionar mejor que los genéricos [16].
- La memoria por búsqueda en el historial (RAG) es la arquitectura más citada [15].
