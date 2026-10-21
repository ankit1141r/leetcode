select customer_number
from orders
group by customer_number
having count(customer_number)=(
    select max(rn)
    from(
        select 
    row_number() over(
        partition by customer_number
    ) as rn
    from orders
    ) as maxid
);
