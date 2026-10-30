# Registro de Uso de Inteligência Artificial (PROMPTS.md)

Este documento registra todas as interações com ferramentas de Inteligência Artificial realizadas durante o desenvolvimento do projeto, em conformidade com as exigências do edital.

---

## Integrante: Pedro Paulo

* **Prompt 1 (Análise do edital)**
  > "Estou com esse plano de implementação para um trabalho academico e preciso fazer a minha parte para conclusão do projeto. Analise esse arquivo e me diga o que exatamente posso adiantar para concluir minha etapa do preojeto (Minha parte consta no arquivo com o nome de 'Pedro Paulo', item E))."
* **O que foi feito com a resposta:**
  Identificação dos 6 arquivos de responsabilidade de Pedro Paulo (`src/sql/relatorio_arrecadacao_por_campanha.sql`, `src/sql/relatorio_doacoes.sql`, `src/sql/relatorio_doadores.sql`, `src/reports/relatorios.py`, `src/utils/config.py` e `src/utils/splash_screen.py`) e entendimento de que sua etapa pode ser realizada de forma independente dos outros módulos.

* **Prompt 2 (Construção do projeto)**
  > "Ok! Agr quero que você construa a minha parte do trabalho seguindo exatamente o plano proposto, passo a passo! Caso encontre alguma divergencia ou tenha alguma dúvida, me informe que ditarei o caminho a ser seguido. Faça tudo desde o começo. Crie as pastas com os nomes exatos, arquivos e afins..."
* **O que foi feito com a resposta:**
  Geração e criação dos arquivos da Seção 5.1-E do contrato técnico, com implementação das consultas SQL obrigatórias (sumarização e junção), classe `Relatorio` com exibição via DataFrame, menus padronizados em `config.py` e tela de abertura com contagens dinâmicas no banco em `splash_screen.py`.



## Integrante: Ricardo

* **Prompt 1 (Análise do Edital):**
  > "Analise este edital e separe as datas de entrega e os itens obrigatórios que o projeto deve conter."

* **Prompt 2 (Definição de Escopo e Tarefas):**
  > "Com base no PDF do Plano de Implementação C2 de Banco de Dados, estruture e detalhe apenas as etapas e tarefas sob a responsabilidade do Ricardo. Se faltar alguma informação ou houver impedimentos para a execução, indique o que é necessário."

* **Prompt 3 (Melhorias na Documentação):**
  > "Forneça 5 sugestões práticas de como posso melhorar e enriquecer o arquivo README.md do projeto."

* **Prompt 4 (Comandos de Terminal e Git):**
  > "Quais são os comandos de terminal necessários para clonar um repositório, adicionar ficheiros, fazer o commit e realizar o push para o GitHub?"

---

## Integrante: Maria Vitória

* **Prompt 1 (Estrutura do Controller de Doações em Python):**
  > "Com base no exemplo `controller_pedido.py` do professor, como estruturo em Python a classe `Controller_Doacao` usando o `OracleQueries` para executar os comandos de insert (com a sequence `DOACOES_ID_DOACAO_SEQ`), update, delete e o select com join na tabela de doadores?"

* **Prompt 2 (Validação de Dados e Tratamento de Erros em Python):**
  > "Me mostre como criar funções em Python para validar o valor da doação (aceitando vírgula ou ponto) e a data no formato DD/MM/AAAA no terminal, tratando erros caso o usuário digite um valor inválido."

* **Prompt 3 (Refatoração e Limpeza de Comentários):**
  > "Revise o código do `controller_doacao.py` para manter apenas comentários necessários que expliquem a lógica, documentar as funções e usar nomes de variáveis autoexplicativos."

* **Prompt 4 (Testes no Oracle e Fluxo de Commits):**
  > "Quais passos devo seguir para testar os métodos do controller conectando no banco Oracle local e como organizar o envio dessas alterações em commits separados no Git?"

---

## Amon: Prompts de configuração do repositório, scripts SQL, integração e testes na VM

### Prompt A1: Fork, colaboradores e primeiros passos no GitHub
- **Ferramenta/Fonte:** Claude (Anthropic)
- **Integrante:** Amon
- **Prompt utilizado:**
> "Sou Amon e faço parte de um grupo que está desenvolvendo o trabalho descrito no PDF anexo (Python + Oracle, sem ORM, SQL em string concatenada). Minha parte está na seção 6 (Divisão de tarefas) e o contrato técnico na seção 5.1. Pode me explicar como fazer a parte de hoje, focando no fork e no GitHub?" (depois: "é minha primeira vez usando o GitHub, não sei onde digito esse bash")
- **O que o grupo fez com a resposta:** Seguimos o passo a passo para fazer o fork, renomear o repositório para `sistema_doacoes_ong`, adicionar o professor `howardroatti` e os 4 colegas como colaboradores, instalar o Git for Windows (Git Bash), clonar o repositório e configurar `user.name` e `user.email` para os commits ficarem vinculados a cada conta.

### Prompt A2: Limpeza dos arquivos do tema antigo (pedidos)
- **Ferramenta/Fonte:** Claude (Anthropic)
- **Integrante:** Amon
- **Prompt utilizado:**
> "Dei `git ls-files` no repositório após clonar e configurar nome e e-mail" (colando a lista de arquivos) "me instrua exatamente o que mandar no bash para continuar."
- **O que o grupo fez com a resposta:** Executamos os `git rm` indicados para remover models, controllers, relatórios SQL e demais arquivos do tema "pedidos" do projeto de exemplo, mantendo `oracle_queries.py`, `authentication.oracle`, `requirements.txt` e os `__init__.py`. Em seguida, criamos `sql/create_tables_doacoes.sql` e fizemos commit e push.

### Prompt A3: Scripts de exemplo e resolução de merge
- **Ferramenta/Fonte:** Claude (Anthropic)
- **Integrante:** Amon
- **Prompt utilizado:**
> "Um outro membro do grupo fez um commit, então imagino que eu tenho que fazer um pull. Me diga o que mandar no bash para a próxima parte" (enviando o PDF do passo a passo de integração), e depois um print do Vim aberto durante o `git pull`: "fechei o bash e abri de novo, como proceder?"
- **O que o grupo fez com a resposta:** Criamos `sql/inserting_samples_records.sql` (6 doadores e 15 doações em 3 campanhas) e `src/create_tables_and_records.py`, e fizemos um commit por arquivo. Concluímos o merge pendente com `git commit --no-edit`, configuramos `core.editor` para não abrir o Vim novamente e confirmamos no `git log` que tudo estava no GitHub.

### Prompt A4: Análise das pendências do grupo e criação do `principal.py`
- **Ferramenta/Fonte:** Claude (Anthropic)
- **Integrante:** Amon
- **Prompt utilizado:**
> "Vou mandar um relatório que outro membro do grupo fez sobre o que ainda falta no projeto. Analisando esse relatório, diga se algo que falta irá interferir com alguma parte minha e realize os próximos passos de acordo."
- **O que o grupo fez com a resposta:** Identificamos que a falta do `src/reports/relatorios.py` impedia o teste do `principal.py`. Conferimos `config.py` e `splash_screen.py` (aceitar argumento em `clear_console`, ordem 3 = Atualizar e 4 = Remover no menu), criamos o `src/principal.py` com menus em laço e `ler_inteiro` para proteger contra entradas inválidas, validamos a sintaxe e fizemos commit e push.

### Prompt A5: Teste na VM (cx_Oracle, venv e login do Oracle)
- **Ferramenta/Fonte:** Claude (Anthropic)
- **Integrante:** Amon
- **Prompt utilizado:**
> "Abri a máquina virtual pela primeira vez, em tese o código está todo completo. Me mande o que digitar no terminal agora para realizar o teste." (depois, com prints dos erros: `No module named 'cx_Oracle'`, `externally-managed-environment`, `No module named 'pkg_resources'` e `ORA-01017`)
- **O que o grupo fez com a resposta:** Criamos um ambiente virtual (`venv`) na VM, instalamos o `cx_Oracle` com `--no-build-isolation` e o `pandas` separadamente (sem alterar o `requirements.txt` do repositório) e corrigimos o `authentication.oracle` apenas localmente, sem quebra de linha no final, para resolver o `ORA-01017`. O script `create_tables_and_records.py` passou a executar com `Records successfully generated!`, e então rodamos a bateria de testes do `principal.py` e gravamos o vídeo demonstrativo.

---

### Integrante Gabriel:
* **Prompt 1 (Plano de Implementação e Divisão do Grupo):**
  > "Eu e meu grupo temos um trabalho de banco de dados para entregar. Analise cuidadosamente o edital 'C2 edital desenvolvimento' e monte um plano de implementação para o grupo, seguindo o edital e escolhendo um tema de menor complexidade. Os membros são: Amon, Gabriel, Maria Vitória, Pedro Paulo e Ricardo."
  * **Uso:** revisei e levei ao grupo, que validou o tema, a divisão de tarefas e o contrato técnico de nomes de tabelas, classes e métodos.
  
* **Prompt 2 (Classes Model e Controller_Doador):**
  > "Com base no arquivo 'plano de implementação' que está localizado nos meus downloads, quero que você faça as tarefas destinadas ao membro Gabriel Ridolfi, explique o que foi feito em cada uma para eu implementar."
  * **Uso:** a IA gerou `doadores.py`, `doacoes.py` e `controller_doador.py` seguindo o contrato técnico e o padrão do projeto do professor. Estudei a explicação de cada método, em especial a verificação de FK antes de excluir o doador.

* **Prompt 3 (Ambiente local para testes):**
  > "Pode baixar o Python e o Oracle e abra o código gerado para eu  poder conferir."
  * **Uso:** instalei o Python e o Oracle XE no meu computador e testei o controller contra o banco: inserção, CPF repetido, atualização, exclusão simples e exclusão com doações (respondendo N e depois S). Tudo funcionou.

* **Prompt 4 (Guia da Reunião de Integração):** *(resumo — feito em outra máquina, texto original não preservado)*
  > Pedi um passo a passo para a reunião de integração, com a ordem dos commits de cada integrante, checklists de conferência do código e a bateria de testes.
  * **Uso:** conduzi a reunião com o guia.

* **Prompt 5 (Revisão cruzada dos arquivos do grupo):**
  > "Analise a pasta 'revisar codigo' e, com base nas regras do PDF 'passo a passo reuniao', veja se as classes estão conversando entre si ou se há algum erro. Não precisa testar ainda, só cheque nomes de classes, métodos, variáveis, tudo que possa interromper a comunicação em um teste futuro."
  * **Uso:** a revisão confirmou que o código dos colegas estava de acordo com o contrato. Também apontou ajustes menores, como a leitura de CPF com pontuação no `controller_doacao.py`.
---
