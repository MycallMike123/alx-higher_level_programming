-- A script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- Don’t list rows without a name value
--Records should be listed by descending score
SELECT score, name FROM second_table WHERE NOT name='' ORDER BY score DESC;
