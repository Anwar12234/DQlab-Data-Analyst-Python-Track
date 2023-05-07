SELECT
    studentid,
    substring_index(Email, '@', 1) AS name
FROM
    students;
