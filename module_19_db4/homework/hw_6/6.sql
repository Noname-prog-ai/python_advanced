-- 6. Выводим среднюю оценку за задания, где нужно было что-то прочитать и выучить
SELECT avg(grade) as avg_grade
FROM assignments
JOIN assignments_grades ON assignments.assisgnment_id = assignments_grades.assisgnment_id
WHERE assignment_text LIKE '%прочитать%' OR assignment_text LIKE '%выучить%';