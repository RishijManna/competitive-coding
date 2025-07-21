-- Link -> https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50

-- Solution
select id,movie,description ,rating from Cinema where
id%2!=0 and description!='boring' 
order by rating desc
