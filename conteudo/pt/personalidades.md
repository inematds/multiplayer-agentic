# Personalidades e perfis

No espaço multiplayer, cada membro tem um perfil. Para pessoas, o perfil diz o que ela faz. Para agentes, também diz **como ele pensa e fala**. O vídeo de origem mostra os dois tipos de perfil, e é isso que permite chamar o agente certo para cada tarefa.

## 1. Perfil de pessoa

| Campo | Exemplo |
|---|---|
| Papel | editor de vídeo, gestor de operações, apresentador |
| Responsabilidades | o que é dela no fluxo de trabalho |
| Objetivos atuais | metas da semana ou do mês |
| Contexto de trabalho | ferramentas que usa, horários, como prefere ser chamada |

O vídeo mostra que cada pessoa preenche isso ao entrar, numa espécie de entrevista com o agente, e os agentes passam a usar essas informações (por exemplo, para saber de quem cobrar uma tarefa).

## 2. Perfil de agente

| Campo | O que define |
|---|---|
| Nome e dono | quem é e a quem pertence |
| Especialidade | onde ele é bom (texto, código, design, finanças) |
| Modelo e nível de raciocínio | quanto "pensa" antes de responder, e quanto custa |
| Onde roda | na máquina do dono (assinatura) ou na nuvem (por uso) |
| Personalidade | temperamento: direto, cuidadoso, provocador, didático |
| Como pensa | método: checklist, perguntas antes de agir, sempre com fontes |
| Voz | tom e vocabulário, formal ou informal, frases curtas |
| Cota | quanto da assinatura ainda resta (o vídeo mostra "97% restante") |
| Status | online ou offline |

## 3. Níveis de inteligência

O vídeo mostra agentes hospedados com três níveis. A diferença de custo é a que ele informa:

| Nível | Uso típico | Custo relativo (segundo o vídeo) |
|---|---|---|
| Rápido | tarefas administrativas, triagem, respostas curtas | 1/10 do nível máximo |
| Pro | raciocínio, análise, decisões | metade do máximo |
| Máximo | sistemas complexos, engenharia, design | referência (o autor diz que usa o modelo mais forte disponível) |

**Possibilidade:** montar o time por nível, com um agente rápido de recepção, agentes pro para análise e um máximo só para o trabalho pesado. Isso controla custo sem perder qualidade onde ela importa.

## 4. Arquétipos de personalidade

Personalidades que fazem sentido num espaço compartilhado:

| Arquétipo | Papel no canal | Onde aparece |
|---|---|---|
| **Líder / orquestrador** | Recebe o pedido, distribui para os outros e junta o resultado | Todos os cenários; no vídeo, o agente líder do workspace |
| **Especialista** | Faz uma coisa só, bem feita (design, código, texto, dados) | Setor e empresa |
| **Gerente de projeto** | Cobra prazo, faz check-in diário, marca quem está atrasado | Setor e empresa |
| **Conselho** | Otimista, advogado do diabo e neutro discutem antes de o humano decidir | Decisões importantes |
| **Revisor** | Confere o trabalho dos outros agentes antes de chegar ao humano | Qualquer fluxo com publicação |
| **Recepcionista** | Primeiro contato com cliente ou fornecedor, com o tom da marca | Cenário 6 |
| **Mestre de jogo** | Narra, aplica regras e mantém o mundo coerente | Cenário 5 |
| **NPC** | Personagem com história, motivação e memória própria | Cenário 5; cada jogador conversa em privado com ele [14] |
| **Tutor** | Ensina, cobra entrega e libera a próxima fase | Curso como jogo |
| **Gêmeo do dono** | Fala como o dono, com o conhecimento dele, quando o dono não está | Cenário 2; o vídeo descreve o desejo de que colegas pudessem "escrever para o meu sistema de IA" |

## 5. Como a personalidade se combina com as regras

- **A personalidade nunca passa por cima dos limites.** Um agente "provocador" continua sem poder publicar sem aprovação. (Ver [Limites e segurança](limites-seguranca.html).)
- **A personalidade fica num arquivo**, editável pelo dono, e não espalhada em prompts.
- **Toda personalidade se identifica como agente.** A exceção possível é um jogo de dedução em que todos conhecem a regra antes.
- **Coerência:** a mesma personalidade em todos os canais, ou uma variação por canal (mais formal com cliente, mais solta com o time)?

## 6. Riscos

- **Personalidade forte demais:** o agente "dono da verdade" atropela a decisão humana.
- **Gêmeo do dono:** responder como o dono, sem ele saber, pode comprometê-lo. Sempre deixar claro que é o agente falando.
- **NPC sem memória:** personagem que esquece o que disse quebra o jogo. Memória longa ainda é um gargalo [16].
- **Muitas personalidades no mesmo canal:** viram ruído. Melhor poucos agentes com papéis claros.

## 7. Em aberto

1. Quem define a personalidade: o dono do agente ou o administrador do canal?
2. Personalidade única ou uma por canal?
3. Vale ter um "catálogo" de personalidades prontas (líder, revisor, conselho) para quem está começando?
4. O gêmeo do dono pode responder sozinho ou sempre avisa o dono antes?
