
-- Link ->  https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50

-- solution
  
# Write your MySQL query statement below
select Prices.product_id, 
ifnull(ROUND(SUM(Prices.price*UnitsSold.units) / SUM(UnitsSold.units), 2),0) AS average_price from Prices left join UnitsSold on 
Prices.product_id=UnitsSold.product_id and UnitsSold.purchase_date between Prices.start_date and Prices.end_date
group by Prices.product_id 
