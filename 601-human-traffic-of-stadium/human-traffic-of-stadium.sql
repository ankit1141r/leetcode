WITH cte AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM stadium
    WHERE people >= 100
),
grp_sizes AS (
    SELECT
        grp,
        COUNT(*) AS cnt
    FROM cte
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT
    c.id,
    c.visit_date,
    c.people
FROM cte c
JOIN grp_sizes g
    ON c.grp = g.grp
ORDER BY c.visit_date;