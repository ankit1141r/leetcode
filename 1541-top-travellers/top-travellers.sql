with distancetravel as(
    select user_id,sum(distance) as travelled_distance
    from Rides
    group by user_id
)
select u.name,COALESCE(d.travelled_distance, 0) AS travelled_distance
from users u
left join distancetravel d
on u.id=d.user_id
order by travelled_distance desc,u.name;