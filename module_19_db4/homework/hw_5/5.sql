-- 5. Анализируем все группы по определенным критериям
SELECT group_id, count(student_id) as total_students, avg(grade) as avg_grade,
    sum(case when grade is null then 1 else 0 end) as students_did_not_submit_work,
    sum(case when date > due_date then 1 else 0 end) as students_overdue,
    count(distinct case when grade is null then student_id end) as students_retries
FROM assignments_grades
GROUP BY group_id;