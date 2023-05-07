SELECT
    studentid,
    firstname,
    lastname,
    MOD(semester1, 2) AS semester1,
    semester2,
    EXP(markgrowth)
FROM
    students;
