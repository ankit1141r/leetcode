# Write your MySQL query statement belowwith \
with fulltable as(
    select
     t.id,t.client_id,t.driver_id,t.city_id,t.status,t.request_at
     from trips t
     join users c
     on t.client_id=c.users_id
     join users d
     on t.driver_id=d.users_id
     WHERE c.banned = 'No'
      AND d.banned = 'No'
      AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
     
),
resulttable AS (
    SELECT request_at,
           count(*) AS total_requests,
           sum(case when status='Completed' THEN 1 ELSE 0 END) AS VALID_REQUESTS
           
    FROM fulltable
    GROUP BY request_at
)
SELECT 
request_at as `Day`,round((1-(VALID_REQUESTS/total_requests)),2) as 'Cancellation Rate'
FROM resulttable
ORDER BY request_at;