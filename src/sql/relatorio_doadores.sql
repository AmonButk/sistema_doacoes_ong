-- Relatório 3: Listagem de Doadores
-- Relatório auxiliar para conferência de registros
SELECT d.cpf,
       d.nome,
       d.email,
       d.telefone
  FROM doadores d
 ORDER BY d.nome
