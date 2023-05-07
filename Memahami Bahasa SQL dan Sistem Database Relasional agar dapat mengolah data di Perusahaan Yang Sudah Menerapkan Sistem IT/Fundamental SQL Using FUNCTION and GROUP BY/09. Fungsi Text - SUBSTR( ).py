SELECT
    studentid,
    substr(firstname, 2, 3) AS initial
FROM
    students;
