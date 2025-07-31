
-- https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50
select query_name,round(avg(rating/position),2) as quality,round(avg(if (rating<3,1,0))*100,2) as poor_query_percentage from Queries
group by query_name
