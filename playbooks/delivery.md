# Entrega e ambientes de desenvolvimento — acesso ao caminho de produção

## Gatilho e contexto mínimo

Use para repositórios, CI/CD, runners, dependências, registries, artefatos, IaC e ambientes de desenvolvimento. Identifique plataforma, origem do código, gatilhos, identidade do job, runner, segredos, destino e vínculo commit → build → artefato → deployment. Pergunta central: **quem pode transformar entrada não confiável em execução privilegiada ou mudança de produção?**

## Árvores de investigação

### Repositório, gatilhos e runners

- Pipeline executa contribuição externa → trace evento, revisão efetivamente checkoutada, scripts/dependências executados e permissões/segredos disponíveis. Nome do evento sozinho não prova exploração; a combinação de código controlável e contexto privilegiado sustenta o risco.
- Branch protegido → verifique bypass, identidades autorizadas, required checks, revisões e permissão de modificar o próprio pipeline. Proteção nominal não garante integridade do artefato implantado.
- Runner self-hosted persistente → identifique reuso entre jobs/níveis de confiança, diretórios/cache, montagens, sockets, identidade de host e alcance de rede. Limpar workspace não demonstra eliminação de persistência em host/cache.
- Container no job → avalie modo privilegiado, socket do runtime, mounts de host e credenciais ambiente. Isolamento de processo não equivale a isolamento do host.

### Segredos e federação

- Credencial exposta em arquivo/log → registre metadados sanitizados, consumidores e permissões; recomende revogação/rotação, revisão de uso e remoção das fontes de exposição. Mascaramento de log não revoga credencial nem impede acesso pelo job.
- OIDC/federação habilitada → confira issuer, audience, subject/atributos e restrições a repositório, branch/environment e workflow conforme a plataforma. Curta duração não limita por si só quais jobs obtêm privilégios.
- Token de job muito amplo → identifique ações necessárias e permissões efetivas por etapa. Separe jobs de contribuição não confiável, build e deployment de acordo com a fronteira evidenciada, sem impor aprovações sem necessidade concreta.

### Dependências, artefatos e IaC

- SCA alerta → confronte manifest, lockfile, resolução/build e conteúdo do artefato implantado; registre dependência direta/transitiva e advisory verificado. Atualizar manifest sem regenerar resolução e rebuild pode deixar o runtime vulnerável.
- Artefato assinado/SBOM presente → verifique se o consumidor valida assinatura, identidade de origem e digest esperado. SBOM lista componentes; não prova ausência de vulnerabilidades ou origem confiável por si só.
- Tag mutável usada em deploy → vincule digest executado a build/revisão. Um scan limpo de outro digest não cobre o workload atual.
- IaC seguro, recurso inseguro → compare configuração desejada, plano/state, workspace, versão aplicada e runtime. O state pode conter segredos; solicite recortes sanitizados. Corrija fonte e reconcilie drift; não prescreva `apply` sem examinar mudanças e dependências.
- Desenvolvimento acessa produção → mapeie identidade, dados, rede e necessidade real. Proponha isolamento e privilégio mínimo verificáveis, mantendo os fluxos legítimos necessários.

## Tratamento, validação e conclusão

Corrija a fronteira que permite código/identidade indevida alcançar privilégio, segredo ou artefato confiável. Teste contribuição controlada sem segredos reais e confirme que ela não recebe acesso indevido; valide build/deploy legítimo, origem/digest e consumidores após rotação. Para runner persistente comprometido ou possivelmente contaminado, limpar somente código não é evidência suficiente de recuperação.

Conclua com cadeia de confiança rastreada, permissões residuais e jobs/ambientes não avaliados. Encaminhe permissões da identidade cloud ao provedor e comportamento do executável a aplicações.

## Erros a evitar

Tratar pipeline verde como seguro; considerar OIDC automaticamente restrito; confundir assinatura presente com verificação aplicada; substituir lockfile correto por manifest como evidência de runtime; reduzir o domínio a aconselhamento de programação.
