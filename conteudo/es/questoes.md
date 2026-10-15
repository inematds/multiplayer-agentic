# Preguntas de diseño abiertas

1. **Identidad.** ¿Agente como miembro de verdad, con clave propia como en Buzz [1], o como bot de un dueño?
2. **Agente hablando con agente.** ¿Permitido, permitido con tope de turnos, o solo con un humano mediando? Sin límite, los agentes pueden entrar en un bucle y gastar la suscripción.
3. **Permisos y seguridad.** Un mensaje escrito por otra persona en el canal puede inducir a tu agente a ejecutar algo (inyección de prompt). Controles posibles: el agente de cada persona solo obedece a su dueño, aprobación humana para cualquier acción externa, lista de acciones permitidas por canal.
4. **Disponibilidad.** El agente por suscripción depende de que la máquina esté encendida, como advierte el video. Opciones: máquina siempre encendida, VPS, o agente alojado (que paga por uso).
5. **Costo.** ¿Mostrar el crédito por persona, sala y agente, como en el video? La suscripción propia no tiene costo marginal, pero tiene límite semanal.
6. **Memoria.** ¿Memoria por canal, por agente o las dos? ¿Quién puede leer la memoria del agente de otra persona?
7. **Privacidad.** En el video, cada persona decide si comparte su propio Claude o Codex. Ese control tiene que existir.
8. **Ruido.** ¿Cómo evitar que el flujo de eventos quede ilegible? Opciones: filtros, resúmenes por agente, alertas solo de lo que pide acción.
