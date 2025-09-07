select  
case
when (A+B)<=C or (B+C)<=A or (C+A)<=B  then 'Not A Triangle'
when A=B and B=C then 'Equilateral'
when (A=B and B!=C) or (B=C and B!=A) OR (A=C AND A!=B) then 'Isosceles'
WHEN (A!=B) AND (B!=C) AND (C!=A) THEN 'Scalene'
end
from Triangles;
