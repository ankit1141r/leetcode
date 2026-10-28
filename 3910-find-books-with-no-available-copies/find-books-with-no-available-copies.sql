# Write your MySQL query statement below
WITH borrowed AS (
    SELECT
        book_id,
        COUNT(*) AS current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
)
SELECT
    l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    b.current_borrowers
FROM library_books l
JOIN borrowed b
    ON l.book_id = b.book_id
WHERE b.current_borrowers = l.total_copies
ORDER BY b.current_borrowers DESC, l.title ASC;