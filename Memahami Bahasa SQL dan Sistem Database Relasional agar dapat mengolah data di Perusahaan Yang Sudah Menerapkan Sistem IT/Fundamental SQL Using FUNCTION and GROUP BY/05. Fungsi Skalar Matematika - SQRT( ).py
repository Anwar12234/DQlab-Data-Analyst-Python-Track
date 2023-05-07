SELECT
    studentid,
    firstname,
    lastname,
    SQRT(semester1) AS semester1,
    semester2,
    markgrowth
FROM
    students;
