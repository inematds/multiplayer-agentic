# Cenário 2: Eu, meus agentes e convidados

**Quem:** o dono, os agentes dele e de 1 a 5 convidados (sócio, editor, parceiro, aluno avançado). Um convidado pode trazer o próprio agente, como no vídeo.

**Um dia típico**
- O convidado entra no canal `#projeto-x` e pergunta ao agente do dono sobre o andamento.
- O agente responde com o que sabe do projeto, sem mostrar o resto da máquina do dono.
- O convidado conecta o Claude dele, e os dois agentes dividem a tarefa (um escreve, o outro revisa).
- Qualquer coisa que saia para fora (publicar, enviar, excluir) espera o dono aprovar no thread.

**O que muda em relação ao cenário 1**
- Passa a existir **quem pode o quê**: o convidado conversa, mas não manda o agente do dono executar.
- O convidado vê apenas os canais para os quais foi chamado.
- Custo: cada agente roda na assinatura do próprio dono, como no vídeo.

**Possibilidades**
- **2a:** o convidado só conversa, e o agente do dono responde em modo leitura.
- **2b:** o convidado pode pedir tarefas, e o dono aprova cada uma.
- **2c:** convidado com o próprio agente, em canal compartilhado e com teto de turnos entre agentes.

**Riscos:** injeção de prompt vinda da mensagem do convidado ([questão 3](questoes.html)) e privacidade da memória do dono (questão 6).

**Faz sentido quando:** há uma parceria ou um projeto em dupla e a troca hoje acontece por WhatsApp, com prints.
