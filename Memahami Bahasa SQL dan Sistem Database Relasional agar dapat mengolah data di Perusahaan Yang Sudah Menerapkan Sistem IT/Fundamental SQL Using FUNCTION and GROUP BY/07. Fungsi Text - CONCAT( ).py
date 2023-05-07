SELECT
    studentid,
    CONCAT(firstname, lastname) AS name,
    semester1,
    semester2,
    markgrowth
FROM
    students;
