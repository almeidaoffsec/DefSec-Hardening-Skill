# Rede — alcance, segmentação e dependências

## Gatilho e contexto mínimo

Identifique origem, destino, protocolo/porta, direção, ambiente, fluxo necessário, plano de gerenciamento e pontos de controle. Pergunta central: **quem consegue alcançar o quê, por qual caminho e com qual impacto?**

## Decisões condicionais

- **Serviço dito público:** correlacione DNS, endereço, listener, balanceador/proxy, NAT, rotas e filtragem. Inclua IPv4/IPv6 quando presentes. Regra permissiva não prova um caminho completo; IP privado não exclui publicação por intermediário.
- **Segmentação declarada:** identifique caminhos alternativos, peering, VPN, trânsito e controle no destino. Teste a origem realmente representativa; resultado a partir do host do agente pode não representar o segmento avaliado.
- **Timeout ou acesso negado:** diferencie falta de rota, serviço indisponível, resolução incorreta, autenticação e bloqueio pelo controle esperado. Busque logs/contadores e um fluxo de controle positivo para atribuir causa.
- **Fluxo desnecessário confirmado:** restrinja origem/destino e plano de gerenciamento na fonte de verdade. Considere conexões estabelecidas, comportamento stateful/stateless, DNS, portas efêmeras e caminho de retorno conforme a plataforma.
- **Mudança interrompe aplicação:** registre falha funcional, identifique dependência afetada e regra/caminho causador. Recupere o fluxo necessário com escopo mínimo; não mantenha uma mudança indisponibilizante como validada.

## Evidência e tratamento

Monte uma matriz pequena `origem → destino/serviço → necessário? → controle esperado → observado → período`. Utilize configuração efetiva e testes de conexão contextualizados, sem varreduras extensas quando um fluxo específico resolve a pergunta.

Para TLS, correlacione ponto de terminação, hostname, cadeia, versões/protocolos e eventual tráfego posterior ao proxy. Certificado válido na borda não comprova proteção de todos os saltos.

## Validação e conclusão

Teste pelo menos o fluxo permitido necessário e o fluxo indevido nas condições relevantes; confirme saúde do serviço e observabilidade da decisão de bloqueio. Registre segmentos e famílias de endereços cobertos. Conclua quando alcance e dependências estiverem demonstrados, ou explicite a observação faltante. Encaminhe controles específicos de rede cloud ao provedor correspondente.

## Erros a evitar

Equiparar porta fechada a controle eficaz; desconsiderar caminho alternativo ou IPv6; aplicar bloqueio indiscriminado; atribuir um erro de autenticação à segmentação.
