# Write your MySQL query statement below
WITH user_stats AS (
    SELECT
        user_id,
        COUNT(*) AS prompt_count,
        AVG(tokens) AS avg_tokens
    FROM prompts
    GROUP BY user_id
)


SELECT
    s.user_id,
    s.prompt_count,
    ROUND(s.avg_tokens, 2) AS avg_tokens
FROM user_stats s
WHERE s.prompt_count >= 3
  AND EXISTS (
        SELECT 1
        FROM prompts p
        WHERE p.user_id = s.user_id
          AND p.tokens > s.avg_tokens
    )
ORDER BY avg_tokens DESC, user_id ASC;