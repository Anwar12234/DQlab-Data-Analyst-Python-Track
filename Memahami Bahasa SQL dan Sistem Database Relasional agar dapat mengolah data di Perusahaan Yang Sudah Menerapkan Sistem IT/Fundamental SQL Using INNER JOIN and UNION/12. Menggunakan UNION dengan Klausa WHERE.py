SELECT
    *
FROM
    tabel_a
WHERE
    kode_pelanggan = 'dqlabcust03'
UNION
SELECT
    *
FROM
    tabel_b
WHERE
    kode_pelanggan = 'dqlabcust03';
