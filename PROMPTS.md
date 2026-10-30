# Registro de Uso de Inteligência Artificial (PROMPTS.md)

Este documento registra todas as interações com ferramentas de Inteligência Artificial realizadas durante o desenvolvimento do projeto, em conformidade com as exigências do edital.

---

* **Integrante:** Pedro Paulo

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
