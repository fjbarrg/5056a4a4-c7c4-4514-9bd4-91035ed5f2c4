/*
 SECTION: Group exercises
 DESCRIPTION: Write a valid SQL query to solve each problem.
 */

-- A) Get all the unique department names.
-- SELECT DISTINCT department FROM course;
-- B) Get the top 10 female students (first_name, last_name, age, gpa) with the best GPA scores and order by age (asc).
-- SELECT first_name, last_name, age, gpa FROM student WHERE gender = 'female' ORDER BY gpa DESC, age ASC LIMIT 10;
-- C) Count the number of male/female students that are at least 25 years old.
-- SELECT gender, count(gender) FROM student WHERE age > 24 GROUP BY gender;
-- D) Get the number of male/female students that were accepted
-- SELECT gender, count(gender) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id WHERE enrollment.approved =1 GROUP BY gender;
-- E) Get the min, average, and max GPA of the accepted male students that are less than 20 years old.
-- SELECT max(gpa), min(gpa), avg(gpa)  FROM student INNER JOIN enrollment ON student.id = enrollment.student_id WHERE student.gender = 'male' AND student.age < 20 AND enrollment.approved = 1;
-- SELECT gender, max(gpa), min(gpa), avg(gpa)  FROM student INNER JOIN enrollment ON student.id = enrollment.student_id WHERE student.gender = 'male' AND student.age < 20 AND enrollment.approved = 1 GROUP BY gender;
-- SELECT * FROM (SELECT gender, max(gpa), min(gpa), avg(gpa) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id WHERE student.age < 20 AND enrollment.approved = 1 GROUP BY gender) gender_aggregate WHERE gender_aggregate.gender = 'male';
-- F) Get the number of enrollments to courses that take longer than 2 years to finalize.
-- SELECT count(*) FROM course INNER JOIN enrollment ON course.id = enrollment.course_id WHERE course.years > 2 AND enrollment.approved = 1;
-- G) Get the number of male/female student that will take a course from the 'Statistics' department.
-- SELECT gender, count(*) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id INNER JOIN course on enrollment.course_id = course.id WHERE LOWER(course.department) = 'statistics' GROUP BY student.gender; -- WHERE LOWER(course.department) LIKE 'stat%';

/*
 SECTION: Individual exercises
 DESCRIPTION: Write a valid SQL query to solve each problem.
 */

-- A) Count the number of courses per department
-- SELECT department, count(*) FROM course GROUP BY course.department; -- WHERE LOWER(course.department) LIKE 'stat%';
-- B) How many male/female students were accepted?
-- SELECT gender, count(*) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id WHERE enrollment.approved = 1 GROUP BY student.gender;
-- C) How many students were accepted per course?
-- SELECT course.name, count(*) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id INNER JOIN course on enrollment.course_id = course.id WHERE enrollment.approved =1 GROUP BY course.name;
-- D) What's the average age and gpa per course?
-- SELECT course.name, avg(age), avg(gpa) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id INNER JOIN course on enrollment.course_id = course.id GROUP BY course.name;
-- E) Get the average number of years the enrolled (approved) female student will study.
-- SELECT avg(course.years) FROM student INNER JOIN enrollment ON student.id = enrollment.student_id INNER JOIN course on enrollment.course_id = course.id WHERE enrollment.approved = 1 AND student.gender = 'female';

