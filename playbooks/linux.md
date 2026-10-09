# Linux — configuração efetiva e redução de exposição

## Gatilho e contexto mínimo

Use para servidores, estações e workloads Linux. Identifique distribuição/build, função, forma de gestão, acesso administrativo, exposição e dependências. Pergunta central: **qual configuração ou privilégio efetivo permite o risco observado e onde corrigir sua causa?**

## Árvores de investigação

### SSH e acesso administrativo

- Uma linha em `sshd_config` permite senha → confirme versão, arquivo realmente usado, `Include`, blocos `Match` e parâmetros de inicialização. Para uma conexão específica, avalie a combinação usuário/origem/destino; não generalize a saída global.
- Senha efetivamente permitida → determine requisito de acesso, métodos alternativos, automação dependente e fatores adicionais. `PasswordAuthentication no` sozinho não exclui autenticação interativa por teclado/PAM; interprete `AuthenticationMethods` e opções efetivas da versão.
- Restrição aplicável → prepare na fonte de verdade e valide sintaxe antes de reload. Verifique acesso alternativo e recuperação; mantenha uma sessão existente enquanto testa **nova conexão** pelo caminho permitido e pelo caminho a negar.
- Login negado → diferencie política pretendida de chave inválida, conta bloqueada, origem incorreta ou falha de rede.

Exemplos de **coleta/validação**, apenas em host OpenSSH compatível e com contexto preenchido:

```sh
sshd -T -C user=<usuario>,addr=<ip-origem>,host=<host-origem>,laddr=<ip-destino>,lport=<porta>
sshd -t
```

São modelos, não comandos prontos: confirme binário, permissões e o arquivo/flags usados pelo serviço. `-T` interpreta configuração; não prova que o daemon em execução já a recarregou. `-t` valida sintaxe, não acesso funcional.

### Privilégios, serviços e permissões

- Regra sudo ampla ou `NOPASSWD` → avalie comando permitido, argumentos, arquivos graváveis e contexto do usuário. `NOPASSWD` isolado não prova escalada; um binário ou configuração controlável pelo usuário pode invalidar uma aparente restrição.
- Serviço privilegiado → relacione UID/capabilities, executável, unidade, drop-ins, arquivos de configuração e permissões de diretórios ancestrais. Arquivo gravável só sustenta impacto quando existe um consumidor/caminho de execução correspondente.
- Porta em escuta → confirme endereço/interface, namespace, processo e alcance externo. Loopback no host não descreve automaticamente publicação por proxy ou container.
- Correção candidata → reduza privilégio/escopo ou corrija propriedade na gestão central. Não remova serviço, aplique `chmod` recursivo ou desative conta sem identificar consumidor e dependência.

### Pacotes e auditoria

- CVE por versão aparente → confronte pacote instalado e revisão da distribuição com advisory/backport; confirme se o processo usa o binário atualizado ou precisa de reinício.
- Log ausente → confira serviço, evento gerado, permissões, forwarding, retenção e período da consulta. Ausência de arquivo não basta para concluir ausência de auditoria.

## Validação e conclusão

Verifique novamente o estado efetivo e o caminho que sustentava o achado; teste administração, automação e saúde do serviço. Se falhar, registre a falha e recupere/revise antes de ampliar. Encerre com causa tratada ou encaminhada, cobertura por host e risco residual; encaminhe fluxos para rede e permissões entre identidades para identidade.

## Erros a evitar

Confundir sintaxe válida com acesso preservado; alterar arquivo local gerenciado; confirmar CVE só por banner; declarar frota corrigida após testar um host.
