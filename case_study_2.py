# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:02:05 2022

@author: rohan
"""

import pandas as pd
import numpy as np
import pandasql as ps
import datetime
from datetime import datetime

customer_orders = pd.read_csv('customer_orders.csv')

###  •	Total revenue for the current year
q1="select sum(net_revenue) as total_revenue,year from customer_orders group by year "
question_1= ps.sqldf(q1)

print("Total Revenue for year 2015: 29036749.19")
print("Total Revenue for year 2016: 25730943.59")
print("Total Revenue for year 2017: 31417495.03")


### •	New Customer Revenue e.g. new customers not present in previous year only

q2 = "SELECT * FROM((SELECT SUM(net_revenue) AS NEW_CUSTOMER_REVENUE_2017 FROM customer_orders WHERE year = 2017 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year<2017)) JOIN (SELECT SUM(net_revenue) AS NEW_CUSTOMER_REVENUE_2016 FROM customer_orders WHERE year = 2016 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year<2016)) ON 1=1 JOIN (SELECT SUM(net_revenue) AS NEW_CUSTOMER_REVENUE_2015 FROM customer_orders WHERE year = 2015 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year<2015)) ON 1=1)"
question_2= ps.sqldf(q2)

print("New customer revenue for 2017: 28676607.64 ")
print("New customer revenue for 2016: 18245491.01")
print("New customer revenue for 2015: 29036749.19 ")

### •	Existing Customer Growth. To calculate this, use the Revenue of existing customers for current year –(minus) Revenue of existing customers from the previous year

q3 = """SELECT  
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
	)"""

question_3= ps.sqldf(q3)

print("Existing customer growth for year 2016: 20611.34")
print("Existing customer growth for year 2017: 20335.46")
### •	Revenue lost from attrition

q4 ="""
SELECT  
Attrition_from_17_16,Attrition_from_16_15
FROM (
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

"""

question_4= ps.sqldf(q4)

print("Revenue lost from attrition for year 2017:  $ 23110294.94 ")
print("Revenue lost from attrition for year 2016:  $ 21571630.0")



### •	Existing Customer Revenue Current Year /Prior Year
q5_2015 ="""
SELECT round(sum(net_revenue),2) 
	FROM customer_orders 
	where year = 2015 AND customer_email in (select distinct customer_email from customer_orders where year = 2016)
"""
existing_cust_rev_2015 =ps.sqldf(q5_2015)
print("Existing customer revenue for year 2015: $7465117.12")


q5_2016 ="""
SELECT round(sum(net_revenue),2) 
	FROM customer_orders 
	where year = 2016 AND customer_email in (select customer_email from customer_orders where year = 2017)
"""
existing_cust_rev_2016 =ps.sqldf(q5_2016)

print("Existing customer revenue for year 2016: $2620648.65")

q5_2017 ="""
SELECT round(sum(net_revenue),2) 
	FROM customer_orders 
	where year = 2017 AND customer_email in (select customer_email from customer_orders where year = 2016)
"""
existing_cust_rev_2017 =ps.sqldf(q5_2017)

print("Existing customer revenue for year 2017: $2641259.99 ")

### •	Total Customers Current Year/previous year

q6 = """
select count(distinct customer_email) as counts, year from customer_orders
group by year 
"""
total_customers =ps.sqldf(q6)

print("Total customers in 2015: 231294")
print("Total customers in 2016: 204646")
print("Total customers in 2017: 249987")   



### •	New Customers

q7_2016 ="""
SELECT count(distinct customer_email) as cnt 
FROM customer_orders 
where year = 2016 and customer_email not in (select customer_email from customer_orders where year = 2015);
"""
new_customers_2016 = ps.sqldf(q7_2016)
print("new customers in the year 2016: 145062")

q7_2017 ="""
SELECT count(distinct customer_email) as cnt FROM customer_orders 
                 where year = 2017 and customer_email not in (select customer_email from customer_orders where year = 2016)
"""
new_customers_2017 = ps.sqldf(q7_2017)

print("New customers in the year 2017: 229028")
### •	Lost Customers


q8_2016 ="""
SELECT count(distinct customer_email) as cnt 
FROM customer_orders 
where year = 2015 and customer_email not in (select customer_email from customer_orders where year = 2016)
"""
lost_custoers_2016 = ps.sqldf(q8_2016)
print("Customers lost in the year 2016: 171710")

q8_2017 ="""
SELECT count(distinct customer_email) as cnt FROM customer_orders 
                 where year = 2016 and customer_email not in (select customer_email from customer_orders where year = 2017)
"""
lost_custoers_2017 = ps.sqldf(q8_2017)
print("Customers lost in the year 2017: 183687")
