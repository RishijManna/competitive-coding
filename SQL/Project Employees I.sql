-- Link https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50

select Project.project_id, round(avg(Employee.experience_years),2) as average_years 
from Project left join Employee on Project.employee_id = Employee.employee_id
group by  Project.project_id
