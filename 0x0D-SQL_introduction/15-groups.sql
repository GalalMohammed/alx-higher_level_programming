-- a script list number of records with same score in table second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
