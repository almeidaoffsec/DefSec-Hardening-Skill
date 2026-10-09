# Registro de validação

## Verificações de 2026-10-08

Ambiente: Linux, Python **3.14.7**, OpenCode **v2.0.23**. Primeira implementação de conteúdo. Os cenários de [TESTS.md](TESTS.md) estão especificados; a aprovação comportamental permanece pendente. Nenhum modelo foi executado como agente avaliado nestas verificações.

| Verificação | Resultado | Evidência / limite |
|---|---|---|
| Validador estrutural | APROVADO | `python3 scripts/validate.py`: 26 documentos, 14 playbooks e 46 cenários estruturados; links locais, frontmatter restrito, blocos e cobertura declarada válidos. Reexecutado após a adição de M365/Workspace. |
| Casos negativos do validador | APROVADO | Em cópia temporária: link quebrado, frontmatter inválido, ID duplicado, campo ausente, bloco não fechado e playbook sem rota/cenário foram rejeitados. Cópia íntegra passou. |
| Whitespace do diff | APROVADO | `git diff --check` sem erros; nesta execução os arquivos ainda eram não rastreados, por isso a verificação de Markdown novo foi feita pelo script. |
| Descoberta no OpenCode V2 | APROVADO | Instalação local padrão em projeto temporário, sem `skills` explícito no config. API retornou ID `defensive-security`, caminho correto, nome, descrição e corpo idêntico ao `SKILL.md` sem frontmatter. |
| T01–T45 e M01 | NÃO EXECUTADO | Requerem sessões limpas sem acesso às expectativas; nenhum resultado comportamental é presumido. |

## Evidência da descoberta

O conteúdo operacional foi copiado para `.opencode/skills/defensive-security/` em um repositório Git temporário. Consultas feitas via `opencode api get`, primeiro `/api/agent`, depois `/api/skill`, com query `location[directory]` codificada para o diretório temporário. A inicialização de agentes foi necessária no runtime verificado: a listagem de skills anterior retornava vazia. Sem `location`, a API usou o diretório padrão do servidor, não o diretório do comando.

Registro local temporário: `/tmp/opencode/defensive-security-install-wux5avnr/discovery-result.json`. Asserções verificaram ID, origem, nome, descrição e igualdade do corpo registrado com o arquivo de origem. Os arquivos auxiliares foram incluídos na cópia; sua leitura condicional por um modelo ainda depende da regressão comportamental. Os comandos reproduzíveis de descoberta estão no [README](README.md).

Fixtures temporárias dos casos negativos: `/tmp/opencode/defensive-security-validator-pgzf8vhf`. Os diretórios temporários não são artefatos versionados nem persistência garantida.

## Pendências

Executar T01–T45 e M01 e registrar versão da skill, ambiente/modelo, respostas e leituras de ferramentas. Também validar geração de arquivos e retomada real de checkpoint. Revisão textual ou descoberta bem-sucedida não altera o status dos cenários.
