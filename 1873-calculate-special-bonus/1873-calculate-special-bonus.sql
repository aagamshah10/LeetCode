SELECT employee_id,
case when employee_id%2 <>0 and name not like 'M%' then salary 
ELSE 0
END as bonus
FROM Employees
ORDER BY employee_id