SELECT Product.product_name,Sales.price,Sales.year
FROM Sales 
JOIN Product 
ON Sales.product_id = Product.product_id