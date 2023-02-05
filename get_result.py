#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_data():
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    import numpy as np
    # read clean file
    X = pd.read_csv("data clean.csv")
    # split categorical numerical
    X_num = X.select_dtypes(np.number)
    X_cat = X.select_dtypes(object)
    # scale the numerical
    scaler = MinMaxScaler().fit(X_num)
    X_scaled = scaler.transform(X_num)
    X_scaled = pd.DataFrame(X_scaled, columns = X_num.columns)
    return X_scaled, X_cat

def build_model(X_scaled,X_cat):
    import pandas as pd
    from sklearn import cluster
    # make a column "total score"
    X_scaled["total"] = X_scaled["querying"] + X_scaled["engineering"] + X_scaled["analysis"] + X_scaled["model_building"] + X_scaled["scraping"] + X_scaled["dashboarding"]
    # drop rows that has less than specific number
    X_scaled = X_scaled.drop(X_scaled[X_scaled["total"] < .4].index)
    # kmeans to make clusters
    kmeans = cluster.KMeans(n_clusters=37)
    kmeans.fit(X_scaled)
    clusters = kmeans.predict(X_scaled)
    pred = clusters.tolist()
    # put the cluster label to each row
    X_scaled["category"] = pred
    X_cat = X_cat.reset_index(drop=True)
    X_processed = pd.concat([X_scaled, X_cat], axis = 1)
    return X_processed

# get random row from a dataframe
def getrandom(df):
    import random
    from random import randint
    import pandas as pd
    x = df.shape[0]-1
    x = random.randint(0,x)
    rec_job = df.iloc[x,:]
    return rec_job


# In[ ]:


def get_result():
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import cluster
    
    import plotly.express as px
    import plotly.graph_objects as go
    import random
    from random import randint
    import time
    from st_aggrid import AgGrid as aggrid

    X_scaled, X_cat = read_data()
    X_new = pd.read_csv("set skills.csv")
    kmeans = cluster.KMeans(n_clusters=37)
    kmeans.fit(X_scaled)
    pred_new = kmeans.predict(X_new).tolist()
    X_new["category"] = pred_new
    X_new["job_title"] = ["your skills"]
    X_processed = build_model(X_scaled, X_cat)
    X_new["total"] = X_new.sum(axis = 1)
    selection = X_processed[X_processed["category"] == pred_new[0]]
    recommendation = getrandom(selection)
    recommendation = pd.DataFrame(recommendation).T
    st.header("_Data Analyst Job Search Assistant_")
    st.text("Thank you for using our service.")
    st.text("Please click the button below to get your job recommendation.")
    open = st.button("Find a Job Recommendation")
    if open:
        index = recommendation.index.values.tolist()[0]
        jobinfo = pd.read_csv("data clean with url.csv")
        jobinfo = jobinfo.iloc[index,0:4]
        st.subheader(jobinfo[2])
        # generate_report(X_processed, X_new, pred_new)
        plt_vars = ["querying","engineering","analysis","model_building","scraping","dashboarding"]
        fig1 = go.Figure()
        fig1.add_trace(go.Scatterpolar(r = pd.Series(recommendation.loc[(recommendation.loc[:,plt_vars].index.values.tolist()[0]), plt_vars].values),
                        theta = plt_vars, fill = "toself", name = "Recommended for You"))
        fig1.add_trace(go.Scatterpolar(r = pd.Series(X_new.loc[0, plt_vars].values),
                        theta = plt_vars, fill = "toself", name = "Your Profile"))

        fig1.update_layout(polar=dict(radialaxis=dict(visible=True)),template="plotly_dark",showlegend=True)
        plt.legend(bbox_to_anchor=(1.02,1), loc = "upper left", borderaxespad=0)
        st.plotly_chart(fig1)

        plt.style.use('dark_background')
        barwidth= 0.4
        fig2, ax2 = plt.subplots(figsize=(20,20))
        bars1 = recommendation.iloc[0,0:6].values.tolist()
        bars2 = X_new.iloc[0,0:6].values.tolist()
        r1 = np.arange(len(bars1))
        r2 = [x + barwidth for x in r1]
        plt.bar(r1,bars1,color = "blue", width=barwidth,edgecolor="white",label="recommended for you", alpha=.5)
        plt.bar(r2,bars2,color = "red", width=barwidth, edgecolor="white", label="your preferences", alpha=.5)
        plt.xticks([r+barwidth/2 for r in range(len(bars1))],recommendation.columns.tolist()[0:6])
        plt.legend(bbox_to_anchor=(1.02,1), loc = "upper left", borderaxespad=0, prop = {"size":30})
        ax2.tick_params(labelsize = 25)
        st.pyplot(fig = fig2)
        
        t1,t2 = st.tabs(["Job Description","Job Details"])
        with t1:
            st.write("Job description:")
            st.write(jobinfo[1])
        with t2:
            st.write("URL:")
            st.write(jobinfo[0])
            st.write("Job title:")
            st.write(jobinfo[2])
            st.write("Company:")
            st.write(jobinfo[3])
    
    more = st.button("See More Similar Jobs")
    if more:
        table = selection.loc[:,["job_title","comp_name","city"]]
        st.write(table)


