# Aplicações — análise de vulnerabilidades no contexto de execução

## Gatilho e contexto mínimo

Use para aplicações web/APIs, serviços internos, workers/filas, aplicações desktop/mobile e componentes executáveis. Identifique função, versão/build implantado, dados, entradas, identidade de execução, dependências e limites de confiança. Pergunta central: **qual entrada ou identidade pode atravessar uma fronteira de confiança e causar impacto?**

Analise código/configuração quando necessários para sustentar ou refutar um achado. Parta do ambiente observado e proponha correção para o problema identificado, sem transformar a avaliação em orientação genérica de desenvolvimento.

## Árvores de investigação

### Autenticação, autorização e isolamento

- Autenticação presente → verifique autorização por ação, objeto, tenant e contexto no componente que realiza a operação. Ocultar botão/rota no cliente não aplica autorização no servidor/serviço.
- API rejeita usuário indevido em uma rota → examine rotas alternativas, métodos, operações em lote e processamento assíncrono pertinentes. Não conclua que todos os objetos/tenants estão isolados pelo resultado de um caso.
- Worker/serviço interno confia em mensagem → identifique produtores autorizados, validação de contexto/tenant, consumidor e permissões do processo. Rede privada não torna mensagem confiável.
- Desktop/mobile valida no cliente → identifique o que o usuário controla localmente e onde a decisão é novamente aplicada. Considere IPC, armazenamento local e atualização; o modelo não depende de existir endpoint HTTP.

### Entradas, execução e dados

- Alerta de injeção/execução → rastreie entrada controlável, transformações/validação e operação sensível (consulta, shell, parser, arquivo, template). Código suspeito sem caminho atingível permanece hipótese; mitigação existente precisa ser avaliada no contexto certo.
- Caminho de arquivo fornecido externamente → avalie normalização, diretório permitido, links e permissões do consumidor. Uma verificação textual de prefixo não comprova confinamento efetivo.
- URL controlável → identifique destinos alcançáveis pelo processo, redirecionamentos, resolução e credenciais ambiente. Não use acesso real a metadados/segredos como teste padrão; prefira destino controlado que verifique a fronteira necessária.
- Sessão/token/segredo → avalie armazenamento, escopo, validade, revogação e exposição por logs/erros. Valor codificado ou ofuscado continua recuperável conforme o contexto; não o reproduza no relatório.
- Dependência vulnerável → relacione versão resolvida, artefato implantado, advisory e caminho de uso. Falta de alcance demonstrado não apaga o componente vulnerável: separe presença da vulnerabilidade de explorabilidade no ambiente.

### Runtime e implantação

- Código corrigido → confirme commit/build, imagem/artefato efetivo e rollout; não conclua pelo branch ou PR fechado.
- Serviço em container → examine usuário, mounts, capacidades, sockets expostos, segredos e publicação de portas. Container isolado nominalmente não comprova fronteira segura; a análise avançada de orquestrador requer dados específicos.
- Dados de produção em ambiente de teste → identifique conteúdo, acesso, destino de logs/backups e necessidade; proponha redução de exposição e substituição/mascaramento com validação de utilidade.

## Correção e validação

Relacione a correção à causa: autorização no ponto decisório, restrição do consumidor, configuração segura, atualização de componente ou redução de privilégios/exposição. Mitigação na borda pode reduzir alcance sem eliminar o defeito. Use amostras e identidades controladas, evitando leitura desnecessária de dados reais.

Defina um teste que reproduza a condição indevida com efeito controlado e um teste do fluxo legítimo; inclua variantes que exercitem a fronteira corrigida. Valide no build efetivamente implantado e registre cobertura. Conclua com evidência, condição de exploração, impacto, correção e risco residual; encaminhe artefatos/dependências para entrega, credenciais para identidade e acesso cloud ao provedor.

## Erros a evitar

Limitar a avaliação a WebApps; confirmar exploração apenas por padrão de código; orientar implementação sem achado; considerar WAF ou rede privada prova de ausência de vulnerabilidade; validar só o caso bloqueado.
