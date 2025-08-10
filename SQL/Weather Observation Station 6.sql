--https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true

select distinct(city) from station where city like 'A%' or  city like 'E%' or city like 'I%'  or city like 'O%'  or city like 'U%';
