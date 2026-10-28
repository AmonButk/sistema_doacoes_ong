-- Relatório 2: Doações detalhadas (Junção)
-- Atende ao requisito 6.a.1.ii do edital
SELECT d.id_doacao,
       TO_CHAR(d.data_doacao, 'DD/MM/YYYY') AS data_doacao,
       dd.nome AS nome_doador,
       d.campanha,
       d.valor
  FROM doacoes d
 INNER JOIN doadores dd
    ON d.cpf = dd.cpf
 ORDER BY d.id_doacao
