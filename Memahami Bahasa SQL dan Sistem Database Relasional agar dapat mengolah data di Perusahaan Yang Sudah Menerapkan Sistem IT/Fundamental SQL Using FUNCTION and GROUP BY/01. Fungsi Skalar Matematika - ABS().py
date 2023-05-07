SELECT
    studentid,
    firstname,
    lastname,
    semester1,
    semester2,
    ABS(markgrowth) AS markgrowth
FROM
    students;
