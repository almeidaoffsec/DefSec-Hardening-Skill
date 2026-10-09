# Defensive Security

Skill OpenCode de **segurança defensiva operacional**: um copiloto que acompanha e analisa junto ao operador o ambiente de trabalho, investiga vulnerabilidades, identifica correções e melhorias, prioriza riscos e verifica resultados.

O mesmo fluxo orienta todos os domínios:

`acompanhamento contínuo → evidência → hipótese → verificação → risco → correção/melhoria → validação`

## Cobertura implementada

O conteúdo operacional está em [SKILL.md](SKILL.md) e em 14 playbooks carregados sob demanda:

| Domínio | Cobertura inicial |
|---|---|
| [Assessment](playbooks/assessment.md) | Inventário parcial, contexto, caminhos de risco, evidências conflitantes e prioridade. |
| [Linux](playbooks/linux.md) | SSH efetivo, privilégios, serviços, permissões, pacotes e auditoria. |
| [Windows](playbooks/windows.md) | GPO/MDM, acesso remoto, privilégios, serviços e auditoria efetiva. |
| [Rede](playbooks/network.md) | Exposição, segmentação, fluxos necessários, controle de acesso e TLS. |
| [Identidade](playbooks/identity.md) | Permissões efetivas, MFA, contas de serviço, segredos e revogação. |
| [Cloud comum](playbooks/cloud.md) | Inventário, responsabilidade compartilhada, hierarquia, dados, drift e cobertura. |
| [AWS](playbooks/aws.md) | IAM/Organizations, S3, rede, KMS, CloudTrail e credenciais. |
| [Azure/Entra ID](playbooks/azure.md) | RBAC, Conditional Access, workloads, Storage, Key Vault, rede e auditoria. |
| [Microsoft 365](playbooks/m365.md) | Exchange Online, SharePoint/OneDrive/Teams: sharing, convidados, transporte, encaminhamento e consentimento OAuth. |
| [Google Workspace](playbooks/workspace.md) | Drive, Gmail, Admin console: compartilhamento, convidados, roteamento, verificação de apps e Context-Aware Access. |
| [GCP](playbooks/gcp.md) | IAM herdado, service accounts, Storage, rede, perímetros e auditoria. |
| [Aplicações](playbooks/applications.md) | Web/APIs, workers, serviços internos e desktop/mobile; fronteiras de confiança, autorização, entradas e runtime. |
| [Entrega e desenvolvimento](playbooks/delivery.md) | Repositórios, CI/CD, runners, dependências, artefatos, IaC e acesso entre ambientes. |
| [Compliance](playbooks/compliance.md) | Requisitos aplicáveis, evidências, cobertura, exceções e matriz de controles. |

A análise de aplicações e ambientes de desenvolvimento parte de evidências para identificar vulnerabilidades e propor correções. Código, configuração e resultados de ferramentas são insumos dessa investigação. Hardening e compliance também seguem esse objetivo, em vez de produzir checklists desvinculados do ambiente.

O trabalho é conjunto com o operador: o copiloto compartilha raciocínio e opções, integra hipóteses do operador como material a verificar e orienta coletas quando não tem acesso às ferramentas do ambiente. Condições funcionais que podem ser reforçadas entram como **melhorias**, rotuladas separadamente de defeitos de segurança, sem inflar um tipo no outro.

**Estado:** primeira implementação de conteúdo; a suíte comportamental ainda precisa ser executada. Consulte [VALIDATION.md](VALIDATION.md) para verificações reais e [Roadmap.md](Roadmap.md) para aprofundamentos pendentes. A existência de um playbook não comprova desempenho validado em todos os seus cenários.

## Instalação no OpenCode V2

Copie o conteúdo operacional para um diretório chamado `defensive-security`. O ID vem do caminho; `name` é o nome de exibição. `SKILL.md` na raiz deste repositório, por si só, não é uma instalação com esse ID.

Na raiz deste repositório, para uma instalação global:

```sh
dest="$HOME/.config/opencode/skills/defensive-security"
mkdir -p "$dest"
cp SKILL.md "$dest/SKILL.md"
cp -R playbooks references templates "$dest/"
```

Para instalação em um projeto, use como `dest` o caminho `<projeto>/.opencode/skills/defensive-security`. Ao atualizar, substitua os arquivos operacionais da versão anterior; os comandos acima sobrescrevem arquivos de mesmo nome. Preserve customizações locais antes da atualização.

Mantenha `playbooks/`, `references/` e `templates/` junto de `SKILL.md`. Não é necessário instalar o plano, instruções de manutenção ou expectativas dos testes. Não há dependências de aplicação, banco de dados ou scanner embutido.

Abra uma sessão no projeto de uso e invoque explicitamente:

```text
@defensive-security Analise estas evidências do ambiente, identifique possíveis
vulnerabilidades e priorize correções. Separe hipóteses de achados confirmados
e indique como verificar a eficácia de cada correção.
```

O OpenCode também pode selecionar a skill pela descrição. Para verificar descoberta a partir do projeto de uso, com Python 3 disponível:

```sh
location="$(python3 -c 'from pathlib import Path; from urllib.parse import quote; print(quote(str(Path.cwd()), safe=""))')"
opencode api get "/api/agent?location%5Bdirectory%5D=$location"
opencode api get "/api/skill?location%5Bdirectory%5D=$location"
```

Procure o ID `defensive-security` e confira a origem: uma instalação local pode prevalecer sobre uma global. No OpenCode v2.0.23 verificado, a consulta de agentes inicializa o registro; consultar skills antes disso pode retornar lista vazia. O parâmetro `location` evita usar o diretório padrão do servidor. A listagem comprova descoberta e conteúdo registrado, não execução dos cenários. Consulte a [documentação de skills V2](https://opencode.ai/v2/docs/skills) para descoberta e permissões.

## Uso com evidências

- **Linux:** “Este é o resultado efetivo de SSH e o fluxo de backup. Investigue exposição e sugira uma correção que preserve o backup.”
- **Cloud:** “Estas são policies, recursos expostos e limitações da coleta na conta AWS. Identifique caminhos de acesso indevido e a próxima verificação.”
- **Aplicação não web:** “Este worker recebe mensagens de vários tenants. Avalie produtores, identidade de execução e autorização no consumo.”
- **CI/CD:** “Este pipeline executa contribuições externas. Analise acesso a segredos, privilégios do runner e confiança no artefato de deploy.”
- **Validação:** “Aplicamos a correção, mas só testamos dois hosts. Avalie eficácia, funcionamento e cobertura restante.”

Informe o objetivo, escopo e material disponível; a skill solicita apenas lacunas que alteram a decisão. Acesso ao ambiente depende das ferramentas e permissões da sessão. Avaliar e sugerir não implica aplicar mudanças; execução ocorre quando solicitada no escopo definido.

Relatórios, matrizes, planos de remediação e checkpoints usam os [templates](templates/assessment-report.md) sob demanda. Para continuidade, peça um checkpoint e forneça-o explicitamente na nova sessão; a skill não possui persistência própria.

## Manutenção e verificação

Python **3.9+**, apenas biblioteca padrão, é necessário para o verificador do repositório; a skill não depende de Python:

```sh
python3 scripts/validate.py
git diff --check
```

O script verifica arquivos/links locais, blocos de código, referências do roteamento e estrutura/cobertura declarada dos cenários. O frontmatter local usa apenas `name` e `description`, ambos strings JSON entre aspas, um subconjunto de YAML; o script valida esse formato restrito, não YAML arbitrário. Não verifica URLs remotas, âncoras Markdown ou comportamento do modelo. `git diff --check` cobre o diff rastreado; o script também lê os documentos novos.

A regressão comportamental e o cenário multi-turn estão em [TESTS.md](TESTS.md). Alterações de playbook exigem cenários afetados; mudanças transversais exigem a suíte completa. Registre testes executados e limitações sem confundir revisão estrutural com aprovação comportamental.
