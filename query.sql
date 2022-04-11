•	Existing Customer Growth. To calculate this, use the Revenue of existing customers for current year –(minus) Revenue of existing customers from the previous year

SELECT  
(EXISTING_CUSTOMER_REVENUE_2017_16-EXISTING_CUSTOMER_REVENUE_2016_17) AS EXISTING_CUSTOMER_GROWTH_2016_2017,
(EXISTING_CUSTOMER_REVENUE_2016_15-EXISTING_CUSTOMER_REVENUE_2015_16) AS EXISTING_CUSTOMER_GROWTH_2015_2016
FROM(
		(
			SELECT SUM(net_revenue) AS EXISTING_CUSTOMER_REVENUE_2017_16 
			FROM customer_orders 
			WHERE year = 2017 AND customer_email IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year=2016)
		) 
		JOIN 
		(
			SELECT SUM(net_revenue) AS EXISTING_CUSTOMER_REVENUE_2016_17
			FROM customer_orders 
			WHERE year IN (2016) AND customer_email IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year=2017)
		) 
		ON 1=1 
		JOIN 
		(
			SELECT SUM(net_revenue) AS EXISTING_CUSTOMER_REVENUE_2016_15 
			FROM customer_orders 
			WHERE year IN (2016) AND customer_email IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year=2015)
		) 
		ON 1=1
		JOIN 
		(
			SELECT SUM(net_revenue) AS EXISTING_CUSTOMER_REVENUE_2015_16
			FROM customer_orders 
			WHERE year IN (2015) AND customer_email IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year=2016)
		) 
		ON 1=1
	)
	
	
#################################################



SELECT  
Attrition_from_17_16,Attrition_from_16_15
FROM(
		(
			SELECT SUM(net_revenue) AS Attrition_from_17_16 
			FROM customer_orders 
			WHERE year = 2016 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year=2017)
		) 
		JOIN 
		(
			SELECT SUM(net_revenue) AS Attrition_from_16_15
			FROM customer_orders 
			WHERE year IN (2015) AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year=2016)
		) 
		ON 1=1 
		
	)
	
	
##########################################

select count(distinct customer_email) as counts,year from customer_orders
group by year 