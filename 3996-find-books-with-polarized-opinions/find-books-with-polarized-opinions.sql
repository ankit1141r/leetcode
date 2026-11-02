# Write your MySQL query statement below
WITH stats AS (
    SELECT
        book_id,
        COUNT(*) AS total_sessions,
        MAX(session_rating) AS max_rating,
        MIN(session_rating) AS min_rating,
        SUM(
            CASE
                WHEN session_rating <= 2 OR session_rating >= 4
                THEN 1
                ELSE 0
            END
        ) AS extreme_ratings
    FROM reading_sessions
    GROUP BY book_id
)
SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,
    s.max_rating - s.min_rating AS rating_spread,
    ROUND(s.extreme_ratings / s.total_sessions, 2) AS polarization_score
FROM books b
JOIN stats s
    ON b.book_id = s.book_id
WHERE s.total_sessions >= 5
    AND s.max_rating >= 4
    AND s.min_rating <= 2
    AND s.extreme_ratings / s.total_sessions >= 0.6
ORDER BY polarization_score DESC,
         title DESC;