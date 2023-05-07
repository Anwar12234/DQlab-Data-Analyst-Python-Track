SELECT
    studentid,
    firstname,
    lastname,
    CEILING(semester1) AS semester1,
    CEILING(semester2) AS semester2,
    markgrowth
FROM
    students;
