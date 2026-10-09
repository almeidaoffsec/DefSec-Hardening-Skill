# Google Workspace — colaboração, compartilhamento e verificação de apps

## Gatilho e contexto mínimo

Use para Drive, Gmail, Admin console e suítes de colaboração. Identifique domínio, OUs/unidades envolvidas, grupos, workloads e origem da configuração. Pergunta central: **quem alcança quais dados por qual caminho e o que limita esse acesso?**

Identidade de diretório, service accounts e permissões Google seguem [GCP](gcp.md) quando o contexto é cloud; identidade de usuários e grupos segue [Identidade](identity.md). Este playbook trata dos limites dos workloads de colaboração.

## Decisões condicionais

- **Compartilhamento fora do domínio habilitado:** verifique o escopo real por OU/unidade organizacional — configuração de domínio, por OU e por unidade compartilhada se sobrepõem. Habilitado não comprova exposição: identifique arquivos/unidades com links "anyone" e conteúdo alcançável.
- **Link "anyone" encontrado no Drive:** registre unidade, conteúdo, expiração e data conhecidas. Link ativo em conteúdo sensível sustenta achado; link expirado/revogado não. Não presuma audiência limitada à intenção de quem compartilhou.
- **Compartilhamento por unidade compartilhada:** relacione membros, permissões por nível e limites de compartilhamento da unidade. Acesso legítimo de membro não é achado; ausência de revisão de membros pode ser melhoria.
- **Regras de roteamento/allowlist no Gmail:** rastreie condição, remetentes/destinatários e efeito (bypass de spam, modificação, encaminhamento). Allowlist existente não prova aplicação em todo o domínio; verifique efeito com mensagem representativa.
- **Encaminhamento automático:** identifique origem (usuário, regra, destino), domínio de destino e conteúdo alcançável. Encaminhamento ativo é exposição a verificar; permissão sem uso é configuração a revisar.
- **App OAuth com verificação pendente/limite:** separe escopos concedidos, alcance (usuários afetados) e status de verificação. App não verificado com escopos amplos sustenta hipótese de risco; verificação não elimina avaliação de escopos e necessidade de uso.
- **Context-Aware Access configurado:** confira níveis aplicados por usuário/grupo/dispositivo e modo de enforcement versus apenas relatório. Nível configurado sem aplicação efetiva não restringe acesso.

## Tratamento, validação e conclusão

Corrija na origem: configuração de compartilhamento no nível que governa a OU/unidade, regras de Gmail no Admin console, acesso de apps revisado nos controles de acesso de apps. Links desativados não comprovam perda de acesso por cópias/destinatários anteriores — teste em janela controlada quando aplicável.

Para bloquear app OAuth em uso, identifique consumidores e função real antes: bloquear interrompe fluxos dependentes. Valide acesso controlado e funcionamento dos fluxos legítimos após a mudança.

Conclua com escopo por workload (Drive, Gmail, Admin) e cobertura de OUs/unidades avaliadas. Encaminhe identidade de diretório e service accounts para [Identidade](identity.md)/[GCP](gcp.md).

## Erros a evitar

Declarar vazamento pelo compartilhamento habilitado sem conteúdo alcançável; tratar configuração de domínio como estado efetivo por OU/unidade; confirmar abuso pela existência de escopo concedido; bloquear app sem mapear consumidores legítimos.
