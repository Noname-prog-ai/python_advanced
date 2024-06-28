-- 3. Находим всех учеников преподавателя, который задает самые простые задания
SELECT full_name
FROM students
WHERE teacher_id = (
    SELECT teacher_id
    FROM teachers
    JOIN assignments ON teachers.teacher_id = assignments.teacher_id
    JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
    GROUP BY full_name
    ORDER BY avg_grade DESC
    LIMIT 1
);