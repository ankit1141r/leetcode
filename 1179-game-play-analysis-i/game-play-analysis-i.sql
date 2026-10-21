# Write your MySQL query statement below
with resulttable as(
    select player_id,event_date,
    row_number() over(
        partition by player_id
        order by event_date
    ) as rn
    from Activity
)
select player_id,event_date as first_login
from resulttable
where rn=1;