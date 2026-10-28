-- Relatório 1: Arrecadação por campanha (Sumarização)
-- Atende ao requisito 6.a.1.i do edital
SELECT d.campanha,
       COUNT(1) AS qtd_doacoes,
       SUM(d.valor) AS total_arrecadado,
       ROUND(AVG(d.valor), 2) AS media
  FROM doacoes d
 GROUP BY d.campanh
 ORDER BY total_arrecadado DESC
