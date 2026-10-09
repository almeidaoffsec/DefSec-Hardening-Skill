# Windows — política efetiva, privilégios e serviços

## Gatilho e contexto mínimo

Identifique edição/build, servidor ou estação, função, domínio/tenant, GPO/MDM, contexto usuário/computador e meios de administração. Pergunta central: **qual política ou permissão efetiva permite a exposição e qual fonte a governa?**

## Decisões condicionais

- **Política local diverge do esperado:** obtenha resultado efetivo de GPO/MDM para o usuário/computador e momento relevantes, além de herança, filtros, exceções e conflito entre fontes. Uma edição local pode ser revertida no próximo refresh. Corrija a fonte que prevalece e valide propagação.
- **RDP/WinRM/SMB exposto:** relacione listener, perfil de firewall, alcance de rede, autenticação, grupos autorizados e função do host. Porta acessível não comprova acesso anônimo; serviço bloqueado de uma origem não prova bloqueio global.
- **Conta ou grupo privilegiado:** expanda associações e direitos efetivos, identifique contas de serviço e uso operacional. Remover uma associação não elimina necessariamente outros caminhos de privilégio ou sessões já abertas.
- **Serviço/tarefa executa privilegiado:** correlacione identidade de execução, permissões no executável, configuração, diretórios e gatilho. Caminho sem aspas só sustenta exploração se houver interpretação vulnerável e escrita em caminho candidato por identidade pertinente; não conclua pelo formato isolado.
- **Build associado a CVE:** verifique edição, atualização cumulativa instalada, advisory e reboot pendente. Preserve distinção entre correção instalada e binário/estado efetivo.
- **Auditoria habilitada sem eventos:** examine política avançada efetiva, geração de evento controlado, canal, forwarding e retenção. SACL e contexto do objeto podem ser necessários dependendo do evento.

## Coleta orientada

Em Windows compatível, `gpresult /r` é uma coleta resumida de GPO; a cobertura depende de identidade e privilégios. `auditpol /get /category:*` consulta a política de auditoria. Esses resultados não abrangem automaticamente MDM, toda precedência ou entrega dos logs; peça evidência adicional conforme a pergunta.

## Tratamento e validação

Trate a origem GPO/MDM ou gestão do serviço; teste primeiro em conjunto representativo. Defina acesso alternativo e recuperação para restrições de administração. Valide política resultante após propagação, novo acesso permitido/negado, funcionamento de serviços e evento de auditoria quando aplicável.

Conclua com identidade, host, escopo de política e cobertura explícitos. Encaminhe grupos/herança para identidade, alcance para rede e controles formais para compliance. Investigação aprofundada de AD/AD CS exige evidências e referências específicas além deste playbook.

## Erros a evitar

Considerar política local como efetiva; confundir GPO configurada com aplicada; interromper conta de serviço por estar privilegiada; concluir escalada por caminho sem aspas sem verificar as condições.
