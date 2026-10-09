# GCP — herança, service accounts e acesso aos dados

## Gatilho e contexto mínimo

Identifique organização/folders/projeto, recurso, região, principal e gestão por IaC. Pergunta central: **quais grants herdados, delegações e caminhos de rede permitem a ação observada?**

## Árvores de investigação

### IAM e service accounts

- Policy local restrita → examine allow policies herdadas da organização/folders/projeto, condições, deny policies e principal access boundaries quando aplicáveis. Grants locais não removem os herdados. Sem visibilidade dos pais, mantenha a conclusão de acesso incompleta.
- Organization Policy presente → identifique constraint, escopo, estado efetivo e suporte do serviço. Restrição de configuração não é concessão IAM nem comprova correção retroativa de todos os recursos.
- Service account sem chave → avalie quem pode impersoná-la, gerar tokens, anexá-la a workloads e alterar esses workloads. Ausência de chave exportada não elimina caminhos de uso privilegiado.
- Workload Identity Federation → confira issuer, audience, mapeamento/condições de atributos e bindings para os workloads esperados. Token de curta duração não compensa trust excessivamente amplo.

### Dados, rede e auditoria

- Bucket com grant público → examine `allUsers`/`allAuthenticatedUsers`, Public Access Prevention, herança e ACLs quando aplicáveis. Uniform bucket-level access centraliza o modelo de permissão; não significa que os grants IAM sejam privados. URL assinada delega acesso mesmo sem grant público.
- VM/serviço com entrada ampla → correlacione regras efetivas, políticas hierárquicas, targets/tags/service accounts, IPs, rotas, load balancer e listener. Regra sem correspondência ao recurso não demonstra exposição dele.
- VPC Service Controls configurado → identifique serviços protegidos, perímetro, ingress/egress, access levels e dry-run versus enforced. Perímetro não substitui IAM nem é garantia contra toda exfiltração.
- Cloud Audit Logs presente → diferencie categorias de auditoria e configuração por serviço/projeto, exclusões, roteamento, retenção e acesso. Não suponha que toda operação de leitura de dados esteja registrada por padrão.
- CMEK usado → examine permissões sobre a chave, localização e consumidores. Revogar/desabilitar chave pode impedir disponibilidade e recuperação sem tratar o grant excessivo na origem.

## Tratamento, validação e conclusão

Corrija o grant no nível que o origina e restrinja delegação/exposição conforme a necessidade do workload. Valide após propagação com principal, recurso e ação definidos: uso legítimo, acesso indevido e consumidores dependentes. Para chaves expostas, valide revogação e continuidade; não se limite à remoção do arquivo.

Conclua com projetos/regiões avaliados, herança conhecida e pendências. Encaminhe IaC/federação de pipeline para entrega e requisitos formais para compliance.

## Erros a evitar

Tratar binding local como override restritivo; presumir segurança pela ausência de chave; confundir uniform bucket-level access com bloqueio público; considerar perímetro em dry-run como enforcement.

## Referência de semântica

[Google Cloud — herança de allow policies](https://cloud.google.com/iam/docs/resource-hierarchy-access-control).
