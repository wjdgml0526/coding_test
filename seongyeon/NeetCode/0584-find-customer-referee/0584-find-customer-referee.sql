# Write your MySQL query statement below
SELECT id, name, referee_id
FROM Customer
WHERE referee_id <> 2 OR referee_id is null;