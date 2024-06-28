-- 2. Выбираем 10 лучших учеников с самым высоким средним баллом
SELECT full_name, avg(grade) as avg_grade
FROM students
JOIN assignments_grades ON students.student_id = assignments_grades.student_id
GROUP BY full_name
ORDER BY avg_grade DESC
LIMIT 10;