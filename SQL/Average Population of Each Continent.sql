select COUNTRY.CONTINENT , floor(avg(city.population)) from CITY join Country on
city.countrycode=country.code group by COUNTRY.CONTINENT ;
