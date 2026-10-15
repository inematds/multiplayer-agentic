# Personalidades y perfiles

En el espacio multiplayer, cada miembro tiene un perfil. Para las personas, el perfil dice qué hacen. Para los agentes, también dice **cómo piensan y hablan**. El video de origen muestra los dos tipos de perfil, y eso es lo que permite llamar al agente correcto para cada tarea.

## 1. Perfil de persona

| Campo | Ejemplo |
|---|---|
| Rol | editor de video, gestor de operaciones, presentador |
| Responsabilidades | qué le corresponde en el flujo de trabajo |
| Objetivos actuales | metas de la semana o del mes |
| Contexto de trabajo | herramientas que usa, horarios, cómo prefiere que la llamen |

El video muestra que cada persona completa esto al entrar, en una especie de entrevista con el agente, y los agentes pasan a usar esa información (por ejemplo, para saber a quién reclamarle una tarea).

## 2. Perfil de agente

| Campo | Qué define |
|---|---|
| Nombre y dueño | quién es y a quién pertenece |
| Especialidad | en qué es bueno (texto, código, diseño, finanzas) |
| Modelo y nivel de razonamiento | cuánto "piensa" antes de responder, y cuánto cuesta |
| Dónde corre | en la máquina del dueño (suscripción) o en la nube (por uso) |
| Personalidad | temperamento: directo, cuidadoso, provocador, didáctico |
| Cómo piensa | método: checklist, preguntas antes de actuar, siempre con fuentes |
| Voz | tono y vocabulario, formal o informal, frases cortas |
| Cuota | cuánto de la suscripción queda todavía (el video muestra "97% restante") |
| Estado | online u offline |

## 3. Niveles de inteligencia

El video muestra agentes alojados con tres niveles. La diferencia de costo es la que él informa:

| Nivel | Uso típico | Costo relativo (según el video) |
|---|---|---|
| Rápido | tareas administrativas, triaje, respuestas cortas | 1/10 del nivel máximo |
| Pro | razonamiento, análisis, decisiones | la mitad del máximo |
| Máximo | sistemas complejos, ingeniería, diseño | referencia (el autor dice que usa el modelo más fuerte disponible) |

**Posibilidad:** armar el equipo por nivel, con un agente rápido de recepción, agentes pro para el análisis y uno máximo solo para el trabajo pesado. Esto controla el costo sin perder calidad donde importa.

## 4. Arquetipos de personalidad

Personalidades que tienen sentido en un espacio compartido:

| Arquetipo | Rol en el canal | Dónde aparece |
|---|---|---|
| **Líder / orquestador** | Recibe el pedido, lo distribuye a los demás y junta el resultado | Todos los escenarios; en el video, el agente líder del workspace |
| **Especialista** | Hace una sola cosa, bien hecha (diseño, código, texto, datos) | Sector y empresa |
| **Gerente de proyecto** | Reclama plazos, hace check-in diario, marca quién está atrasado | Sector y empresa |
| **Consejo** | Optimista, abogado del diablo y neutral discuten antes de que el humano decida | Decisiones importantes |
| **Revisor** | Verifica el trabajo de los otros agentes antes de que llegue al humano | Cualquier flujo con publicación |
| **Recepcionista** | Primer contacto con el cliente o proveedor, con el tono de la marca | Escenario 6 |
| **Maestro de juego** | Narra, aplica reglas y mantiene el mundo coherente | Escenario 5 |
| **NPC** | Personaje con historia, motivación y memoria propia | Escenario 5; cada jugador conversa en privado con él [14] |
| **Tutor** | Enseña, reclama la entrega y libera la siguiente fase | Curso como juego |
| **Gemelo del dueño** | Habla como el dueño, con su conocimiento, cuando el dueño no está | Escenario 2; el video describe el deseo de que los colegas pudieran "escribirle a mi sistema de IA" |

## 5. Cómo se combina la personalidad con las reglas

- **La personalidad nunca pasa por encima de los límites.** Un agente "provocador" sigue sin poder publicar sin aprobación. (Ver [Límites y seguridad](limites-seguranca.html).)
- **La personalidad queda en un archivo**, editable por el dueño, y no esparcida en prompts.
- **Toda personalidad se identifica como agente.** La excepción posible es un juego de deducción en el que todos conocen la regla de antemano.
- **Coherencia:** ¿la misma personalidad en todos los canales, o una variación por canal (más formal con el cliente, más suelta con el equipo)?

## 6. Riesgos

- **Personalidad demasiado fuerte:** el agente "dueño de la verdad" atropella la decisión humana.
- **Gemelo del dueño:** responder como el dueño, sin que él lo sepa, puede comprometerlo. Dejar siempre claro que es el agente quien habla.
- **NPC sin memoria:** un personaje que olvida lo que dijo rompe el juego. La memoria larga sigue siendo un cuello de botella [16].
- **Muchas personalidades en el mismo canal:** se vuelven ruido. Mejor pocos agentes con roles claros.

## 7. Abierto

1. ¿Quién define la personalidad: el dueño del agente o el administrador del canal?
2. ¿Personalidad única o una por canal?
3. ¿Vale la pena tener un "catálogo" de personalidades listas (líder, revisor, consejo) para quien está empezando?
4. ¿El gemelo del dueño puede responder solo o siempre le avisa al dueño antes?
