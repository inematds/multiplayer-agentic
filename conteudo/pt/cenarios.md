# Cenários de uso

São seis cenários, do menor para o maior em pessoas, risco e custo. Cada um traz quem participa, um exemplo de dia, o que aparece na tela e o que fica em aberto. As formas A–D estão em [Formas do sistema](formas.html), as bases técnicas em [Base técnica](base-tecnica.html) e as questões numeradas em [Questões em aberto](questoes.html).

## Visão geral

| # | Cenário | Quem entra | Forma provável | Risco principal | Complexidade |
|---|---|---|---|---|---|
| 1 | Uso local | Só o dono e os agentes dele | A → B | Ruído (muita mensagem) | Baixa |
| 2 | Eu, meus agentes e convidados | Dono, agentes e algumas pessoas convidadas | B → C | Convidado mandando no agente do dono | Média |
| 3 | Empresa: um setor | Uma equipe pequena com seus agentes | C | Adoção (ninguém usa) | Média |
| 4 | Empresa inteira | Vários setores, gestores e agentes por área | C com governança | Permissão, custo e auditoria | Alta |
| 5 | Jogos | Jogadores, agente mestre e agentes NPC | C com regras de jogo | Custo por jogador e memória | Média a alta |
| 6 | Clientes e fornecedores | Pessoas de fora da empresa, agentes de atendimento e equipe interna | B com aprovação | Vazamento de dados e injeção de prompt | Alta |

## Como os cenários se ligam

Os cenários podem funcionar como degraus:

```
1 local  →  2 com convidados  →  3 um setor  →  4 empresa toda
                                      ↘
                                       6 clientes e fornecedores
              5 games  (ramo à parte, reaproveita o motor dos cenários 1–2)
```

**Em aberto:** começar pelo degrau 1 e subir, ou escolher um cenário-alvo (por exemplo, o 6 como produto) e construir direto para ele?
