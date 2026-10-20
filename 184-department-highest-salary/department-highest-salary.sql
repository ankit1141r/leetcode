# Write your MySQL query statement below
with fulltable as (
    select e.id,e.name as employee ,e.salary as salary,e.departmentId,d.name as department
    from employee e
    join department d 
    on e.departmentId=d.id
),
resulttable as(
     select department,employee,salary,
     rank() over(
        partition by department
        order by salary desc
     ) as r
     from fulltable  
)
select department,employee,salary
from resulttable
where r=1
order by employee;