select p.product_name,sum(o.unit) as unit
from orders o
join products p
on o.product_id=p.product_id
where date_format(o.order_date,'%Y-%m')='2020-02'
group by p.product_id,p.product_name
having sum(o.unit)>=100 ;
