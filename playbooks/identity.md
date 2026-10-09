# Identidade — permissões efetivas e caminhos de acesso

## Gatilho e contexto mínimo

Identifique principal humano/workload, diretório ou provedor, recurso, ação, origem, grupos/roles, condições e ciclo de credenciais. Pergunta central: **qual identidade consegue realizar qual ação por qual caminho?**

## Decisões condicionais

- **Permissão direta restrita:** expanda grupos, roles herdadas, delegação, trusts, impersonation e políticas do recurso. Remover um grant direto não comprova remoção do acesso efetivo.
- **MFA configurado:** verifique usuários, aplicações, métodos/protocolos, exceções, condições e enforcement real. Política em modo de relatório não bloqueia. Separe identidades humanas de workloads e avalie os mecanismos adequados a cada uma.
- **Conta de serviço privilegiada:** identifique consumidores, permissões utilizadas, delegação e forma de autenticação antes de reduzir privilégios ou rotacionar. Prefira identidade de workload e credenciais de curta duração quando a plataforma e o fluxo permitirem.
- **Segredo exposto:** confirme tipo e escopo sem reproduzir seu valor; identifique validade, permissões, locais de exposição e consumidores. Proponha revogação/rotação e revisão de uso; apagar o texto do repositório não invalida a credencial nem elimina cópias históricas.
- **Usuário desativado:** verifique sessões, tokens, chaves, grants e contas relacionadas conforme o provedor. Não presuma revogação imediata de todos os acessos.
- **Exceção administrativa:** registre dono, motivo, escopo e validade conhecidos; examine controles compensatórios verificáveis. Uma conta de emergência exige análise de acesso e monitoramento, não remoção automática.

## Tratamento e validação

Proponha menor privilégio sustentado pelas ações necessárias e dependências conhecidas. Para mudanças, valide nova sessão/credencial: operação legítima permitida, operação indevida negada e acesso antigo revogado no escopo da correção. Logs devem associar resultado ao principal e recurso certos. Falha de login isolada pode ter causa alheia à política pretendida.

Conclua com caminhos efetivos cobertos e residuais, identidades não testadas e próximo objetivo. Use playbooks de provedor para semântica de IAM e entrega para consumidores em CI/CD.

## Erros a evitar

Equivaler role atribuída a toda permissão efetiva; declarar cobertura universal por MFA habilitado; considerar segredo removido como incidente resolvido; rotacionar sem conhecer consumidores.
