# Azure e Entra ID — escopos, identidades e planos de acesso

## Gatilho e contexto mínimo

Identifique tenant, management group/subscription/resource group, recurso, principal, região e fonte de configuração. Diferencie papéis de diretório Entra de Azure RBAC. Pergunta central: **qual atribuição, credencial ou caminho de rede sustenta o acesso efetivo?**

## Árvores de investigação

### RBAC, Entra e workloads

- Reader no recurso → examine roles herdadas, grupos, roles customizadas, condições e deny assignments aplicáveis. Role mais restrita no filho não remove grant mais amplo no pai. `NotActions` subtrai da definição daquela role; não equivale a negação global contra outras atribuições.
- Acesso a dados → separe `Actions` de `DataActions` e mecanismos do serviço. Permissão administrativa pode permitir obter chaves ou alterar grants; ausência de DataAction direta não encerra a análise de caminhos indiretos.
- Conditional Access configurado → verifique estado de enforcement versus report-only, usuários/workloads abrangidos, aplicações, condições, exclusões e resultados de sign-in. Não extrapole política de usuários a service principals ou managed identities.
- Role elegível/PIM → diferencie elegibilidade de ativação vigente, requisitos de ativação, duração e logs. Não trate toda elegibilidade como privilégio já exercido, nem ignore o caminho de ativação.
- Managed identity ou aplicação → examine grants, credenciais/federação, consumidores e quem pode modificar o recurso que usa essa identidade. Ausência de segredo estático não elimina privilégio excessivo.

### Dados, rede e auditoria

- Storage sem acesso anônimo → examine também Shared Key, SAS, RBAC de dados, rede e consumidores. Bloquear anonimato não revoga SAS/chaves. Registre tipos/validade/escopo conhecidos sem revelar tokens.
- Key Vault → identifique modelo de autorização usado, grants e alcance de rede; não misture access policies e RBAC como se ambos governassem sempre a mesma operação.
- Private endpoint existente → confirme public network access, DNS usado pelo consumidor, rotas e acesso externo efetivo. A criação do endpoint privado não demonstra que o caminho público foi desabilitado.
- Azure Policy conforme → examine efeito, escopo, exclusões e avaliação atual. Uma auditoria de configuração não comprova autorização efetiva ou remediação aplicada.
- Activity Log presente → diferencie operações de gerenciamento, logs do recurso e sign-ins do Entra; valide diagnostic settings, destino, retenção e evento de dados quando necessário.

## Tratamento, validação e conclusão

Corrija atribuições, políticas, exposição ou credenciais no escopo que realmente concede acesso. Considere propagação, tokens/sessões e dependências de aplicações. Teste com principal e operação pertinentes o acesso legítimo e indevido, além da continuidade dos consumidores. Encerre com tenant/subscription e cobertura explícitos; encaminhe pipeline e federação para entrega/identidade.

## Erros a evitar

Tratar Reader local como redução de Contributor herdado; equiparar Azure RBAC e roles Entra; considerar report-only como proteção aplicada; presumir que private endpoint remove exposição pública.

## Referência de semântica

[Microsoft — funcionamento do Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview).
