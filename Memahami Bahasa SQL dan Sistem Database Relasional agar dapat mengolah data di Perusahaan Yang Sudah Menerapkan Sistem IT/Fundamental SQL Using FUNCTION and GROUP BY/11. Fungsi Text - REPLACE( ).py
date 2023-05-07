SELECT
    studentid,
    email,
    REPLACE(email, 'yahoo', 'gmail') AS new_email
FROM
    students;
