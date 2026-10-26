# Write your MySQL query statement below
with result_table as(
select user_id,time_stamp as last_stamp,row_number() over(
    partition by user_id
    order by time_stamp desc
) as rn
from Logins
WHERE YEAR(time_stamp) = 2020
)
select user_id,last_stamp from result_table
where rn=1
;