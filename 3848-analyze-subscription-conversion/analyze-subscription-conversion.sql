WITH converted_users AS (
    SELECT user_id
    FROM UserActivity
    GROUP BY user_id
    HAVING SUM(activity_type = 'free_trial') > 0
       AND SUM(activity_type = 'paid') > 0
)

SELECT 
    ua.user_id,
    ROUND(AVG(CASE WHEN activity_type = 'free_trial'
                   THEN activity_duration END), 2) AS trial_avg_duration,
    ROUND(AVG(CASE WHEN activity_type = 'paid'
                   THEN activity_duration END), 2) AS paid_avg_duration
FROM UserActivity ua
JOIN converted_users cu
    ON ua.user_id = cu.user_id
GROUP BY ua.user_id
ORDER BY ua.user_id;