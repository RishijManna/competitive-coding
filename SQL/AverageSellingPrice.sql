
-- Link ->  https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50

-- solution
  
select id,movie,description ,rating from Cinema where
id%2!=0 and description!='boring' 
order by rating desc
