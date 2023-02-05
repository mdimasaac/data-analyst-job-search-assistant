#!/usr/bin/env python
# coding: utf-8

# In[2]:


def input():
        import pandas as pd
        from sklearn import cluster, datasets
        from sklearn.preprocessing import MinMaxScaler
        import random
        from random import randint
        import numpy as np
        import streamlit as st
        import time
        from get_result import get_result
        import matplotlib.pyplot as plt
        

        a = ["_database queries_","_data extraction_","_logical query processing_","_database manipulation_",
                "_practical SQL operations_","_spark_", "_NoSQL_"] #7
        b = ["_deep learning_","_object-oriented-programming_","_natural language processing_","_building data pipeline_",
                "_ETL processes_","_AWS cloud_","_PySpark_", "_azure DevOps_", "_tensorflow_"] #9
        c = ["_data manipulation_","_exploratory data analysis_","_data remodeling_","_handling outliers_",
                "_inferential statistics, hypothesis testing_","_google analytics_","_statistic_", "_pivot table_"] #7
        d = ["_building regressor_","_building classifier_","_optimizing hyperparameter_","_clustering data_",
                "_feature selection_","_dimensionality reduction_","_analyzing imbalanced data_"] #7
        e = ["_web scraping_","_task simulation/automation_","_working with API_","_manipulating JSON data_",
                "_data cleaning_","_data entry_"] #6
        f = ["_tableau_","_power BI_","_dashboarding_","_making reports_","_presentation & communication_",
                "_team organization_","_ms excel power pivot_","_agile, scrum_"] #8
        st.header("Which of these tasks are you comfortable and confident working on?")
        t1,t2,t3,t4,t5,t6 = st.tabs(["Querying","Engineering","Analysis","Model Building","Scraping","Dashboarding"])
        with t1:
                st.subheader("Working with Databases")
                a0 = st.checkbox(a[0])
                a1 = st.checkbox(a[1])
                a2 = st.checkbox(a[2])
                a3 = st.checkbox(a[3])
                a4 = st.checkbox(a[4])
                a5 = st.checkbox(a[5])
                a6 = st.checkbox(a[6])
        with t2:
                st.subheader("Data Engineering Field")
                b0 = st.checkbox(b[0])
                b1 = st.checkbox(b[1])
                b2 = st.checkbox(b[2])
                b3 = st.checkbox(b[3])
                b4 = st.checkbox(b[4])
                b5 = st.checkbox(b[5])
                b6 = st.checkbox(b[6])
                b7 = st.checkbox(b[7])
                b8 = st.checkbox(b[8])
        with t3:
                st.subheader("Data Analyst Fundamentals")
                c0 = st.checkbox(c[0])
                c1 = st.checkbox(c[1])
                c2 = st.checkbox(c[2])
                c3 = st.checkbox(c[3])
                c4 = st.checkbox(c[4])
                c5 = st.checkbox(c[5])
                c6 = st.checkbox(c[6])
                c7 = st.checkbox(c[7])
        with t4:
                st.subheader("Machine Learning Much?")
                d0 = st.checkbox(d[0])
                d1 = st.checkbox(d[1])
                d2 = st.checkbox(d[2])
                d3 = st.checkbox(d[3])
                d4 = st.checkbox(d[4])
                d5 = st.checkbox(d[5])
                d6 = st.checkbox(d[6])
        with t5:
                st.subheader("Web Scraping Enthusiast")
                e0 = st.checkbox(e[0])
                e1 = st.checkbox(e[1])
                e2 = st.checkbox(e[2])
                e3 = st.checkbox(e[3])
                e4 = st.checkbox(e[4])
                e5 = st.checkbox(e[5])
        with t6:
                st.subheader("Delivering Result")
                f0 = st.checkbox(f[0])
                f1 = st.checkbox(f[1])
                f2 = st.checkbox(f[2])
                f3 = st.checkbox(f[3])
                f4 = st.checkbox(f[4])
                f5 = st.checkbox(f[5])
                f6 = st.checkbox(f[6])
                f7 = st.checkbox(f[7])

        na = (a0+a1+a2+a3+a4+a5+a6)/len(a)
        nb = (b0+b1+b2+b3+b4+b5+b6+b7+b8)/len(b)
        nc = (c0+c1+c2+c3+c4+c5)/len(c)
        nd = (d0+d1+d2+d3+d4+d5+d6)/len(d)
        ne = (e0+e1+e2+e3+e4+e5)/len(e)
        nf = (f0+f1+f2+f3+f4+f5+f6+f7)/len(f)

        df = pd.DataFrame()
        df["querying"] = [na]
        df["engineering"] = [nb]
        df["analysis"] = [nc]
        df["model_building"] = [nd]
        df["scraping"] = [ne]
        df["dashboarding"] = [nf]
        st.write(df)

        plt.style.use("dark_background")
        barwidth=0.7
        fig1, ax1 = plt.subplots(figsize=(20,8))
        bars1 = df.iloc[0,0:6].values.tolist()
        r1 = np.arange(len(bars1))
        plt.bar(r1,bars1,color="red",width=barwidth,edgecolor="white",alpha=.4)
        plt.xticks([r for r in range(len(bars1))],df.columns.tolist()[0:6])
        ax1.tick_params(labelsize = 25)
        st.pyplot(fig1)

        save = st.button("Save My Data")
        if save:
                st.text("Saving data...")
                time.sleep(2)
                st.text("Successfully saved your data.")
                time.sleep(.5)
                st.text('Please proceed to the "Get Result" page (see menu on the left)')
                df.to_csv("set skills.csv", index = False)

