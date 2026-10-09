# Próximas entregas

## Antes de declarar a primeira versão validada

- Executar os 40 cenários independentes e o multi-turn de [TESTS.md](TESTS.md), com respostas e registros de ferramentas em sessões limpas.
- Corrigir falhas de decisão identificadas, repetir cenários afetados e registrar ambiente/modelo e cobertura em [VALIDATION.md](VALIDATION.md).
- Validar uso completo da instalação: carregamento, leitura condicional dos arquivos auxiliares, geração de artefatos e retomada por checkpoint.

## Aprofundamento orientado por evidências

- Containers/Kubernetes: admission, RBAC, isolamento, identidade de workloads, rede e diferenças entre manifesto e runtime.
- Active Directory/AD CS: caminhos de privilégio, trusts e configuração de certificados além da cobertura básica de identidade/Windows.
- Cloud: árvores específicas por serviço e cenários multicloud; ampliar a avaliação inicial de IAM, dados, rede e auditoria já implementada para AWS, Azure e GCP.
- Aplicações/ambientes de desenvolvimento: casos por runtime e plataforma de CI/CD, aplicações nativas, IPC e distribuição de atualizações, sempre partindo de achados do ambiente.
- Dados, telemetria e resiliência: módulos próprios para bancos de dados, detecção ponta a ponta, recuperação e requisitos de continuidade.
- Gestão de vulnerabilidades em escala e resposta a incidentes: correlação de campanhas de correção, evidências de comprometimento e fluxos especializados.

Cada expansão deve resolver uma lacuna observada, conter decisões condicionais e acrescentar cenários. Criar o módulo antes de anunciá-lo como disponível; manter regras gerais no CORE e formatos nos templates.
