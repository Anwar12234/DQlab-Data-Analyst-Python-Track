SELECT
    customername,
    contactname,
    city,
    postalcode
FROM
    customers
UNION
SELECT
    suppliername,
    contactname,
    city,
    postalcode
FROM
    suppliers;
