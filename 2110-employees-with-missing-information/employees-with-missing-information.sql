# Write your MySQL query statement below
with result_table as(select e.employee_id as employee_id from employees e
left join salaries s
on e.employee_id=s.employee_id
where salary is null

union

select s.employee_id as employee_id from salaries s
left join employees e
on s.employee_id=e.employee_id
where name is null)
select * from result_table
order by  employee_id
;