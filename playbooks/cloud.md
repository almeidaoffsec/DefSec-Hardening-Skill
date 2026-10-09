# Cloud — escopo, hierarquia e responsabilidade

## Gatilho e contexto mínimo

Use para AWS, Azure, GCP ou ambiente híbrido/multicloud. Identifique provedor, partição/cloud quando pertinente, organização/tenant, contas/subscriptions/projetos, regiões, serviços, identidade de coleta e modelo de gestão. Pergunta central: **qual combinação de acesso, exposição e configuração produz risco neste escopo cloud?**

## Decisões condicionais

- **Inventário de uma única conta/região:** registre alcance e paginação/filtros da coleta; serviços globais e recursos em outros escopos podem ficar fora. Falta de permissão em uma API limita visibilidade, não prova inexistência.
- **Serviço gerenciado:** identifique responsabilidades de cliente e provedor para configuração, identidades, dados, rede e recuperação. Serviço gerenciado não elimina vulnerabilidades de configuração do cliente.
- **Política local restritiva:** obtenha políticas herdadas e do recurso, condições, exceções e caminhos entre contas/tenants/projetos. Use a semântica específica do provedor; não traduza nomes de roles como se os modelos fossem equivalentes.
- **Dados considerados privados:** verifique plano de controle e plano de dados, grants públicos, credenciais delegadas/temporárias, endpoints e acesso por intermediários. Criptografia em repouso não impede leitura por identidade autorizada indevidamente.
- **Postura indicada por ferramenta:** correlacione finding com recurso atual, regra/versão, data e cobertura. Estado arquivado/suprimido não significa corrigido. Score agregado não substitui caminho de risco.
- **IaC diverge do console:** identifique workspace/state, versão aplicada, overlays e mudanças fora do pipeline. Corrija a fonte de verdade e planeje reconciliação; um template seguro não comprova runtime seguro.
- **Auditoria/backup habilitado:** verifique categorias, recursos/regiões, destino, acesso, retenção e teste real de entrega/restauração. Registro administrativo não cobre necessariamente acesso aos dados.

## Encaminhamento e tratamento

Leia somente o provedor pertinente: [AWS](aws.md), [Azure](azure.md) ou [GCP](gcp.md). Em multicloud, mantenha escopos e identidades separados e correlacione trusts/federação quando a evidência mostrar conexão. Use [entrega](delivery.md) quando pipeline/IaC controlar a configuração e [identidade](identity.md) para ciclo de credenciais.

Priorize exposição de dados e administração, permissões com grande alcance e caminhos entre ambientes. Proponha redução de risco na origem; mudanças organizacionais podem afetar muitos workloads e exigem validação representativa das dependências reais.

## Validação e conclusão

Registre principal, recurso, ação, região e momento de cada teste. Compare operação legítima e indevida, propagação da política e saúde dos consumidores. Valide restauração quando recuperação fizer parte da correção; snapshot existente não basta. Conclua com limites de visibilidade e escopos ainda não avaliados.

## Erros a evitar

Aplicar checklist de um provedor a outro; presumir que uma conta representa a organização; considerar configuração gerenciada automaticamente segura; confundir controle-plane auditado com toda atividade de dados registrada.
