# Catálogo de referências

Este catálogo organiza fontes; não adota uma baseline pelo operador nem declara controles atendidos. Não contém cópias de benchmarks. Selecione documento, edição e perfil conforme produto/versão, função, escopo e requisito aplicável.

## Referências técnicas consultadas na implementação

Consulta realizada em **2026-10-08**. São páginas de documentação contínua, sem edição normativa fixada; revalide a semântica relevante quando usá-las em uma avaliação. A consulta destas páginas não verifica todas as recomendações de todos os serviços.

| Fonte | Tema coberto | Versão / perfil | Limite |
|---|---|---|---|
| [AWS IAM — policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) | Relação entre políticas de identidade/recurso, boundaries e controles organizacionais | Documentação online; sem perfil normativo | Casos específicos dependem do principal, serviço, tipo de policy e contexto. |
| [Azure RBAC — overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) | Atribuições, escopos, herança, ações de gerenciamento/dados e avaliação | Documentação online; sem perfil normativo | Não substitui documentação de Entra, Conditional Access ou autorização própria do serviço. |
| [GCP IAM — resource hierarchy](https://cloud.google.com/iam/docs/resource-hierarchy-access-control) | Herança e união de allow policies | Documentação online; sem perfil normativo | Deny policies, condições e outras restrições exigem consulta específica. |

## Seleção de baseline no ambiente

Conforme o pedido, considerar requisitos organizacionais/contratuais/regulatórios, baseline de fornecedor, CIS Benchmarks ou DISA STIG para configuração; CIS Controls, NIST CSF e ISO/IEC 27001/27002 para objetivos/controles; PCI DSS quando aplicável. Nenhuma edição dessas famílias foi selecionada ou auditada nesta implementação. Requisitos legais como LGPD dependem do contexto jurídico/organizacional, além de controles técnicos.

Registrar para cada referência realmente usada:

| Nome / fonte acessível | Edição / versão | Produto / versões | Perfil / função | Consulta | Aplicabilidade / limitações |
|---|---|---|---|---|---|
| <documento e URL ou referência fornecida> | <verificada ou pendente> | <escopo> | <perfil> | <data conhecida> | <justificativa e acesso> |

Sem acesso ao documento necessário, solicitar o trecho ou registrar a pendência. Não reconstruir IDs, requisitos ou regras de auditoria por memória. Guardar apenas metadados e referências suficientes à rastreabilidade.
