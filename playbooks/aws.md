# AWS — permissões, exposição e controles efetivos

## Gatilho e contexto mínimo

Use após identificar conta, região/serviço e principal no [contexto cloud](cloud.md). Inclua organização/OU, trusts entre contas e gestão por IaC quando relevantes. Pergunta central: **qual principal pode executar qual ação sobre qual recurso e por qual caminho?**

## Árvores de investigação

### IAM e Organizations

- Policy com `Allow` amplo → identifique principal, ações, recursos e condições, políticas de identidade/recurso, boundaries, políticas de sessão e controles organizacionais aplicáveis (SCP/RCP). `Deny` explícito aplicável prevalece; ausência de `Deny` não concede acesso.
- SCP permite ação → trate como limite organizacional, não concessão de permissão. Confirme a quais contas/principais ela se aplica; não presuma alcance universal.
- Acesso entre contas → correlacione trust/resource policy e permissões do chamador. Para role, examine quem pode assumi-la e quais condições restringem a sessão. Diferencie grant para role de grant para sessão ao avaliar boundaries e políticas de recurso; não reduza todos os casos a uma interseção simplista.
- Simulação permite/nega → registre contexto e limitações de policies/serviços representados. Confirme resultado efetivo por evidência operacional apropriada; falha por KMS, rede ou recurso ausente não prova que IAM bloqueou a ação.

### S3, rede e criptografia

- Bucket policy parece pública → examine Block Public Access nos níveis aplicáveis, access points, Object Ownership/ACLs quando habilitadas e acesso efetivo ao objeto relevante. URL pré-assinada delega acesso; não é sinônimo de bucket público.
- Security group abre administração → correlacione associação à interface, IP/endpoint público, rotas, NACL e listener. Considere regras IPv6 e acesso por balanceador ou transitividade de rede. Regra aberta isolada confirma configuração permissiva, não alcance pela internet.
- Dados criptografados → avalie key policy, grants, permissões IAM e consumidores. Criptografia não corrige autorização excessiva; remover acesso à chave pode interromper workloads, backups e recuperação.

### Telemetria e credenciais

- CloudTrail presente → confira escopo de contas/regiões, seletores e categorias de eventos, destino/retenção e entrega. Não infira eventos de dados somente por eventos de gerenciamento habilitados.
- Access key em pipeline/repositório → relacione principal, grants, uso conhecido e consumidores; proponha revogação/rotação e revisão de atividade. Apagar o segredo não revoga acesso. Avalie federação de workload com trust restrito ao contexto esperado.

## Tratamento, validação e conclusão

Restrinja grants/trusts/exposição na fonte de verdade, mantendo operações necessárias. Teste acesso legítimo e indevido ao **mesmo recurso/ação** relevante, com identidades e condições registradas. Verifique que a correção não apenas mudou o erro de IAM para erro de KMS/rede. Registre contas/regiões e recursos não cobertos; encaminhe dependências do pipeline para entrega.

## Erros a evitar

Declarar acesso por uma policy isolada; usar SCP como grant; declarar S3 público sem avaliar controles efetivos; concluir cobertura de dados pelo simples funcionamento do CloudTrail.

## Referência de semântica

[AWS IAM — avaliação de políticas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html). Consulte os casos específicos vinculados na documentação quando tipo de principal/policy alterar a avaliação.
