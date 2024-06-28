-- 4. Считаем статистику по количеству просроченных заданий для каждого класса
SELECT group_id, avg(cnt) as avg_overdue, max(cnt) as max_overdue, min(cnt) as min_overdue
FROM (
    SELECT group_id, count(grades.grade_id) as cnt
    FROM students
    JOIN assignments_grades ON students.student_id = assignments_grades.student_id
    WHERE date > due_date
    GROUP BY group_id
) as overdue_stats
GROUP BY group_id;