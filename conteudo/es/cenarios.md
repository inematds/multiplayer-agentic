# Escenarios de uso

Son seis escenarios, del menor al mayor en personas, riesgo y costo. Cada uno trae quién participa, un ejemplo de día, qué aparece en la pantalla y qué queda abierto. Las formas A–D están en [Formas del sistema](formas.html), las bases técnicas en [Base técnica](base-tecnica.html) y las preguntas numeradas en [Preguntas abiertas](questoes.html).

## Visión general

| # | Escenario | Quién entra | Forma probable | Riesgo principal | Complejidad |
|---|---|---|---|---|---|
| 1 | Uso local | Solo el dueño y sus agentes | A → B | Ruido (demasiados mensajes) | Baja |
| 2 | Yo, mis agentes e invitados | Dueño, agentes y algunas personas invitadas | B → C | Invitado dándole órdenes al agente del dueño | Media |
| 3 | Empresa: un sector | Un equipo pequeño con sus agentes | C | Adopción (nadie lo usa) | Media |
| 4 | Empresa completa | Varios sectores, gerentes y agentes por área | C con gobernanza | Permisos, costo y auditoría | Alta |
| 5 | Juegos | Jugadores, agente maestro y agentes NPC | C con reglas de juego | Costo por jugador y memoria | Media a alta |
| 6 | Clientes y proveedores | Personas de fuera de la empresa, agentes de atención y equipo interno | B con aprobación | Filtración de datos e inyección de prompt | Alta |

## Cómo se conectan los escenarios

Los escenarios pueden funcionar como peldaños:

```
1 local  →  2 con invitados  →  3 un sector  →  4 toda la empresa
                                      ↘
                                       6 clientes y proveedores
              5 juegos  (rama aparte, reutiliza el motor de los escenarios 1–2)
```

**Abierto:** ¿empezar por el peldaño 1 y subir, o elegir un escenario objetivo (por ejemplo, el 6 como producto) y construir directo hacia él?
