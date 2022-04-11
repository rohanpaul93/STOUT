import pandas as pd
import numpy as np
import PIL as pil
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import hydralit as hy
########################################################################

### Visualization starts here
## importing all needed packages


import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

from matplotlib import rcParams


#To plot figs on jupyter
#%matplotlib inline
# figure size in inches
rcParams['figure.figsize'] = 16,8


df = pd.read_csv("loans_full_schema.csv", index_col=0)


########################################################### STREAM LIT STARTS HERE ##########################################
st.set_page_config(page_title="Casestudy", layout= "wide")

img1 = pil.Image.open('img.png')
##########################################################################################################################
col01, col02, col03 = st.columns([6,2,0.90])
col01.markdown("<h6 style='text-align: center; font-weight: bold; font-size:35pt; color: #033c5a; padding-top: 35px; '>STOUT CASE STUDY </h1>", unsafe_allow_html=True)
col02.image(img1,use_column_width= True)
col01.markdown("<h6 style='text-align: center; font-weight: bold; font-size:20pt; color: #033c5a; padding-top: 20px; '>Rohan Thekanath </h1>", unsafe_allow_html=True)

over_theme = {'txc_inactive': '#000000'}
app = hy.HydraApp(title='CaseStudy',
        hide_streamlit_markers=False,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )
@app.addapp(title='Case Study 1')
def CaseStudy1():
    my_expander1 = st.expander('', expanded=True)  
    #my_expander1.markdown("<p style='text-align: justify;'>This data set represents thousands of loans made through the Lending Club platform, which is a platform that allows individuals to lend to other individuals.</p>", unsafe_allow_html=True)

    my_expander1.header('Description and Issues:')
    my_expander1.markdown("* This data set contains loans which are already made and is not a dataset for loan applications.This data set represents thousands of loans made through the Lending Club platform, which is a platform that allows individuals to lend to other individuals.The data contains information about the loan and some demographics about the applicant.")
    my_expander1.markdown("* Some Issues that I noticed were that the data contained alot of missing values and also there were some variables with only 1 category.Some variables were also highly correlated and seemed redundant.")
    
    my_expander1.header('Visualizations:')
    my_expander1.subheader('1. State wise interest rate distribution')
    img2 = pil.Image.open('country_int_Rate.png')
    my_expander1.image(img2,use_column_width= True)
    
    my_expander1.markdown("* Here we can see that Texas has the highest interest rates.")
    my_expander1.markdown(" * The west cost also seems to have a higher interest rate as compared to the east coast.")
    
    my_expander1.subheader('2. Employee Length vs Interest Rate')
    emp_length = df.groupby('emp_length').mean()
    emp_length_df=pd.DataFrame(emp_length['interest_rate'])
    emp_length_df=emp_length_df.reset_index()
    #emp_length_df
    fig_1 = px.line(emp_length_df, x="emp_length", y="interest_rate")
    my_expander1.plotly_chart(fig_1,use_container_width=True)
    
    my_expander1.markdown("* The interest rate is high for customers who have less than 2 years of employment history")
    my_expander1.markdown("* Strangely the lowest interest rate are for people with with 7 and 4 years of work experience.")
    my_expander1.markdown("* People with 8 years of employment history also have a high interest rate as compared to others.")
    
    
    # We will look at loan_amount 
 
    plt.figure()

    my_expander1.subheader('3. Loan Amount distribution')
    #plt.subplot(121)
    g = sns.distplot(df["loan_amount"])
    g.set_xlabel("loan amount", fontsize=12)
    g.set_ylabel("Frequency Dist", fontsize=12)
    g.set_title("Frequency Distribuition")
    
    my_expander1.pyplot(plt,use_container_width=True)
    my_expander1.markdown("* This clearly looks like it is right skewed which means more number of number of loans are small ticket size as compared to big ticket sized loans.")

    my_expander1.subheader('4. Loan Status vs Loan amount')
    plt.figure(figsize = (12,14))

    plt.subplot(311)
    g = sns.countplot(x="loan_status", data=df)
    g.set_xticklabels(g.get_xticklabels(),rotation=45)
    g.set_xlabel("", fontsize=12)
    g.set_ylabel("Count", fontsize=15)
    g.set_title("Loan Status Count", fontsize=20)
    
    plt.subplot(312)
    g2 = sns.violinplot(x="loan_status", y="loan_amount", data=df)
    g2.set_xticklabels(g2.get_xticklabels(),rotation=45)
    g2.set_xlabel("Duration Distribuition", fontsize=15)
    g2.set_ylabel("loan amount", fontsize=15)
    g2.set_title("Loan Amount vs loan status", fontsize=20)
    
    plt.subplots_adjust(wspace = 0.2, hspace = 0.7,top = 0.9)
    
    plt.show()
    
    my_expander1.pyplot(plt,use_container_width=True)
    
    my_expander1.markdown("* The first plot is as expected. Current loans will be the maximum in this data set")
    my_expander1.markdown("* Here we can see that the loans with status like late and in-grace period have higher loan amounts.") 
    
    
    my_expander1.subheader('5. Loan Purpose vs Loan Amount')
    
    

    plt.figure(figsize = (12,8))
    
    plt.subplot(211)
    g = sns.countplot(x="loan_purpose",data=df,
                      palette='hls')
    g.set_xticklabels(g.get_xticklabels(),rotation=45)
    g.set_title("Application Type - Loan Amount", fontsize=20)
    g.set_xlabel("", fontsize=15)
    g.set_ylabel("Loan Amount", fontsize=15)
    
    plt.subplot(212)
    g1 = sns.violinplot(x="loan_purpose",y="loan_amount",data=df,
                   hue="application_type", split=True)
    g1.set_xticklabels(g1.get_xticklabels(),rotation=45)
    g1.set_title("Application Type - Loan Amount", fontsize=20)
    g1.set_xlabel("", fontsize=15)
    g1.set_ylabel("Loan Amount", fontsize=15)
    
    plt.subplots_adjust(wspace = 0.2, hspace = 0.8,top = 0.9)
    #plt.show()
    my_expander1.pyplot(plt,use_container_width=True)
    
    
    my_expander1.markdown("* One interesting fact is that the most loan is taken for debt_consolidation and credit cards as comapred to the other loan types. ")
    my_expander1.markdown("* Small business have the highest avg loan amount.") 
    
    
    my_expander1.subheader('6. Homeownership vs loan amount')
   
    plt.figure(figsize = (10,6))

    g = sns.violinplot(x="homeownership",y="loan_amount",data=df,
               kind="violin",
               split=True,palette="hls",
               hue="application_type")
    g.set_title("Homer Ownership - Loan Distribuition", fontsize=15)
    g.set_xlabel("", fontsize=15)
    g.set_ylabel("Loan Amount", fontsize=15)
    
    my_expander1.pyplot(plt,use_container_width=True)
    
    
    my_expander1.markdown("* People who have a mortage have a higher loan amount.") 
    
    
    my_expander1.subheader('7. Grades vs Interest rates')
    
    ## looking at interst rate vs grades
    grade = df.groupby('grade').mean()
    grade_df=pd.DataFrame(grade['interest_rate'])
    grade_df=grade_df.reset_index()
    
    fig = px.line(grade_df, x="grade", y="interest_rate")
    #fig.show()
    my_expander1.plotly_chart(fig,use_container_width=True)
    
       
    my_expander1.markdown("* This clearly shows that the grades are associated in some kind of order.") 
    my_expander1.markdown("* The higher grades have a higher interest rate. Probably riskier loans get a higher grade.")
    
    my_expander1.subheader('8. Verified Income vs Home ownership')
    
    grouped = df.groupby(['verified_income','homeownership']).mean()
    grouped_df=pd.DataFrame(grouped['interest_rate'])
    grouped_df=grouped_df.reset_index()
    
    fig = px.sunburst(grouped_df, path=[ 'verified_income','homeownership'], values='interest_rate',height=600)
    my_expander1.plotly_chart(fig,use_container_width=True)
    
    my_expander1.markdown("* Here we can see that people who have verified income and who are living on rent, their average interest rate seems to be the highest. Where as someone who does not have verified income and their home ownership status is on Mortgage, their average interst rate is the lowest.") 

    my_expander1.header('Model building:')
    my_expander1.markdown("* Since there was alot of work done for cleaning and preprocessing the date, I have linked jupyter notebooks below.")
    my_expander1.markdown("* Lasso, Ridge, Elastic net and XGboost have been tested to predict interest rate.")
    my_expander1.write("[Step 1](https://github.com/rohanpaul93/Stout/blob/main/step1_cleaning.ipynb)")
    my_expander1.write("[Step 2](https://github.com/rohanpaul93/Stout/blob/main/model_building.ipynb)")
    
    my_expander1.markdown("* If I had more time in hand, I would study all the variables in detail and try to do a bivariate analysis. Currently I went solely on the basis on The model importance from both regression and tree based method.")
    my_expander1.markdown("* I feel in this case creating interaction variables would do a good job.") 
   
@app.addapp(title='Case Study 2')
def CaseStudy2():
    st.write("[Source code + github link](https://github.com/rohanpaul93/Stout/blob/main/case_study_2.py)")
    my_expander2 = st.expander('Description', expanded=True)  
    my_expander2.markdown("<p style='text-align: justify;'>There is 1 dataset(csv) with 3 years worth of customer orders. There are 4 columns in the csv dataset: index, CUSTOMER_EMAIL(unique identifier as hash), Net_Revenue, and Year.</p>", unsafe_allow_html=True)
    
   
    my_expander2.header('1: Total Revenue.')
    
    code_1 = '''
    select sum(net_revenue) as total_revenue,year 
    from customer_orders 
    group by year 
    '''
    my_expander2.code(code_1, language='sql')
    
    my_expander2.markdown("Total Revenue for year 2015: **29036749.19**")
    my_expander2.markdown("Total Revenue for year 2016: **25730943.59**")
    my_expander2.markdown("Total Revenue for year 2017: **31417495.03**")
    
    
    my_expander2.header('2: New Customer Revenue.')
    
    code_2 = ''' 
    SELECT * 
    FROM(
		(
			SELECT SUM(net_revenue) AS NEW_CUSTOMER_REVENUE_2017 
			FROM customer_orders
			WHERE year = 2017 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year<2017)
		)
		JOIN 
		(
			SELECT SUM(net_revenue) AS NEW_CUSTOMER_REVENUE_2016
			FROM customer_orders WHERE year = 2016 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year<2016)
		) 
		ON 1=1 
		JOIN 
		(
			SELECT SUM(net_revenue) AS NEW_CUSTOMER_REVENUE_2015 
			FROM customer_orders WHERE year = 2015 AND customer_email NOT IN (SELECT DISTINCT customer_email FROM customer_orders WHERE year<2015)
		) 
		ON 1=1)
	)
    '''
    my_expander2.code(code_2, language='sql')
    
    my_expander2.markdown("New customer revenue for 2017: **28676607.64** ")
    my_expander2.markdown("New customer revenue for 2016: **18245491.01**")
    my_expander2.markdown("New customer revenue for 2015: **29036749.19**")
  
    my_expander2.header('3: Existing Customer Growth.')
    
    code_3 ='''
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
    '''     
    my_expander2.code(code_3, language='sql')
    
    my_expander2.markdown("Existing customer growth for year 2016: **20611.34** ")
    my_expander2.markdown("Existing customer growth for year 2017: **20335.46**")
    
    
    my_expander2.header('4: Revenue lost from Attrition.')
    
    code_4 ='''
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
    '''
    my_expander2.code(code_4, language='sql')
    
    my_expander2.markdown("Revenue lost from attrition for year 2017:  **$ 23110294.94**  ")
    my_expander2.markdown("Revenue lost from attrition for year 2016:  **$ 21571630.0** ")
    
    
    my_expander2.header('5: Existing Customer Revenue Current Year /Prior Year')
    
    code_5_1 ='''
    SELECT round(sum(net_revenue),2)  as revenue
	FROM customer_orders 
	where year = 2015 AND customer_email in (select customer_email from customer_orders where year = 2016)
    '''
    my_expander2.code(code_5_1, language='sql')
    
    my_expander2.markdown("Existing customer revenue for year 2015: **$ 7465117.12**  ")
    
    
    code_5_2 ='''
    SELECT round(sum(net_revenue),2)  as revenue
	FROM customer_orders 
	where year = 2016 AND customer_email in (select customer_email from customer_orders where year = 2017)
    '''
    my_expander2.code(code_5_2, language='sql')
    
    my_expander2.markdown("Existing customer revenue for year 2016: **$ $2620648.65**  ")
    
    code_5_3 ='''
    SELECT round(sum(net_revenue),2) 
	FROM customer_orders 
	where year = 2017 AND customer_email in (select customer_email from customer_orders where year = 2016)
    '''
    my_expander2.code(code_5_3, language='sql')
    
    my_expander2.markdown("Existing customer revenue for year 2017: **$ 2641259.99** ")
    
    
    my_expander2.header('6: Total Customers Current Year/previous year')
    
    code_6 ='''
    select count(distinct customer_email) as counts, year 
    from customer_orders
    group by year
    '''
    my_expander2.code(code_6, language='sql')
     
    my_expander2.markdown("Total customers in 2015: **231294**")
    my_expander2.markdown("Total customers in 2016: **204646**")
    my_expander2.markdown("Total customers in 2017: **249987**")  
    
    
    my_expander2.header('7: New Customers')
    
    code_7_1 ='''
    SELECT count(distinct customer_email) as cnt 
    FROM customer_orders 
    where year = 2016 and customer_email not in (select customer_email from customer_orders where year = 2015)
    '''
    my_expander2.code(code_7_1, language='sql')
    
    my_expander2.markdown("new customers in the year 2016: **145062**")

    code_7_2 ='''
    SELECT count(distinct customer_email) as cnt FROM customer_orders 
    where year = 2017 and customer_email not in (select customer_email from customer_orders where year = 2016)
    '''
    my_expander2.code(code_7_2, language='sql')
    
    my_expander2.markdown("New customers in the year 2017: **229028**")

    
    my_expander2.header('8: Lost Customers')
    
    code_8_1 ='''
    SELECT count(distinct customer_email) as cnt 
    FROM customer_orders 
    where year = 2015 and customer_email not in (select customer_email from customer_orders where year = 2016)
    '''
    my_expander2.code(code_8_1, language='sql')
   
    my_expander2.markdown("Customers lost in the year 2016: **171710**")
    
    
    code_8_2 = '''
    SELECT count(distinct customer_email) as cnt FROM customer_orders 
    where year = 2016 and customer_email not in (select customer_email from customer_orders where year = 2017)
    '''
    
    my_expander2.code(code_8_2, language='sql')
    
    my_expander2.markdown("Customers lost in the year 2017: **183687**")
    

                        
        
    
app.run()

