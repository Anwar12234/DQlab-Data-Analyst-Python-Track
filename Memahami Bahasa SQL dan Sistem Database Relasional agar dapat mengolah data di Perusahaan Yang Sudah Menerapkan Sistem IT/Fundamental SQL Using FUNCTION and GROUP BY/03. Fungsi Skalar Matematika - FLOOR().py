SELECT
    studentid,
    firstname,
    lastname,
    FLOOR(semester1) AS semester1,
    FLOOR(semester2) AS semester2,
    markgrowth
FROM
    students;
