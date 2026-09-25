# Write your MySQL query statement below
-- Step 1: Aggregate daily totals
WITH daily AS (
    SELECT visited_on,
           SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

-- Step 2: Compute 7-day moving average
SELECT d.visited_on,
       SUM(d2.amount) AS amount,
       ROUND(SUM(d2.amount) / 7, 2) AS average_amount
FROM daily d
JOIN daily d2
  ON d2.visited_on BETWEEN DATE_SUB(d.visited_on, INTERVAL 6 DAY) AND d.visited_on
GROUP BY d.visited_on
HAVING COUNT(d2.visited_on) = 7
ORDER BY d.visited_on;
