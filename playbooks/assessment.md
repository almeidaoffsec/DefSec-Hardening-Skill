# Assessment — do inventário ao próximo objetivo

## Gatilho e contexto mínimo

Use para ambiente desconhecido, inventário parcial, múltiplos domínios ou priorização inicial. Identifique objetivo, ativos incluídos, função de negócio, criticidade, exposição e origem/idade do inventário. Pergunta central: **qual condição pode produzir impacto relevante e qual evidência permite decidir?**

## Decisões condicionais

1. **Pedido amplo sem plataforma:** use os dados existentes; pergunte plataforma/função e exposição do ativo prioritário. Não entregue comandos para um SO presumido. Se houver vários ambientes, comece por um fluxo ou ativo crítico e explicite a cobertura.
2. **Inventário incompleto:** registre conhecidos e desconhecidos; relacione ativo → serviço → identidade → dados → dependências. Diferencie ativo não inventariado de ativo inexistente. Uma lista de portas não substitui inventário de identidades ou serviços gerenciados.
3. **Alerta de vulnerabilidade:** identifique produto/build, fonte do alerta, condição detectada e evidência de alcance. Se baseado em banner, busque pacote efetivo, backport/advisory e condição vulnerável. Registre a vulnerabilidade como hipótese até haver sustentação suficiente.
4. **Exposição confirmada:** identifique quem alcança o serviço, por qual caminho e com quais privilégios. Se o impacto depende de outra permissão ou configuração, registre essa ligação como hipótese separada. Reduzir exposição pode ser mitigação intermediária sem corrigir a causa.
5. **Achados concorrentes:** priorize combinações de exposição, privilégio e criticidade. Uma vulnerabilidade grave em componente inacessível e uma administração pública sem proteção exigem decisões contextualizadas, não apenas ordenação por score.
6. **Evidências conflitantes:** compare momento, identidade, ambiente e versão antes de substituir conclusões. Falta de permissão na coleta deixa a questão aberta; busque uma evidência alternativa que responda à mesma pergunta.
7. **Possível comprometimento:** registre o indicador e sua origem; priorize alcance, identidades e preservação de evidências. Evite que reinstalação, limpeza de logs ou rotação descoordenada elimine a possibilidade de entender o ocorrido. Encaminhe a resposta a incidentes conforme os recursos disponíveis, sem declarar intrusão por uma exposição isolada.

## Evidência e tratamento

Use inventário com fonte/período, configuração efetiva, fluxos, permissões, avisos do fornecedor e resultados de testes contextualizados. Relacione cada coleta a uma decisão. Para logging, valide geração de um evento conhecido, entrega, consulta e janela de retenção antes de interpretar ausência de alertas. Para backup, configuração de job não comprova restauração; peça evidência de recuperação e dependências testadas.

Produza um mapa inicial pequeno, achados correlacionados, lacunas e correções candidatas. Distinga **defeitos** (vulnerabilidade, exposição, lacuna de controle) de **melhorias** (condição funcional que pode ser reforçada, simplificada ou verificada); rotule cada item como um ou outro e preserve a distinção na priorização, sem inflar melhoria a risco confirmado. Escolha o próximo playbook pelo dado que precisa ser interpretado, sem executar uma lista universal de ferramentas.

## Validação e conclusão

Após a correção, repita a verificação nas mesmas condições relevantes e teste o fluxo necessário à função do ativo. Registre cobertura e itens restantes. Encerre a avaliação inicial quando houver escopo rastreável, prioridade justificada e um próximo objetivo verificável; ausência de inventário completo não impede uma conclusão pontual.

## Erros a evitar

- Confundir scanner limpo com ambiente seguro ou ausência de comprometimento.
- Transformar lacuna de visibilidade em vulnerabilidade confirmada.
- Gerar checklist genérico sem relacionar itens às evidências do ambiente.
