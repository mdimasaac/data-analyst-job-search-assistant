#!/usr/bin/env python
# coding: utf-8

# In[1]:

# https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text
def convert_pdf_to_txt(path):
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    from io import StringIO
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    # codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def get_scores(text):
    import pandas as pd
    querying = ["data","analy","sql","big data","query","entry","base","warehouse"] #A
    engineering = ["python","data","analy","machine","learn","etl","oop","pipe","tensor","engineer","nlp"] #B
    analysis = ["python","data","analy","eda","predict","machine","learn","test","explor","statisti"] #C
    model_building = ["python","data","analy","machine","learn","predict","ml","model","train"] #D
    scraping = ["python","data","analy","clean","mining","scrap","csv","json","api"] #E
    dashboarding = ["bi","power","data","analy","dashboard","tableau","report","visuali"] #F
    category = [querying, engineering, analysis, model_building, scraping, dashboarding]

    A,B,C,D,E,F = [],[],[],[],[],[]

    scores = [A,B,C,D,E,F]
    for score, cat in list(zip(scores, category)):
        sc = []
        for i in cat:
            if i in text.lower():
                sc.append(1)
        n = len(sc)/len(cat)
        score.append(round(n,2))
    df = pd.DataFrame()
    df["querying"] = A
    df["engineering"] = B
    df["analysis"] = C
    df["model_building"] = D
    df["scraping"] = E
    df["dashboarding"] = F
    return df

def read_pdf():
    import streamlit as st
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import pandas as pd
    

    st.header("_Data Analyst Job Search Assistant_")
    st.subheader("Upload your CV. Your personal skills will be analyzed.")
    st.write("NOTE: This feature is currently under development. It can work only if you send your CV to me beforehand.")
    st.markdown("Further Information: contact me at _mdimasaac@hotmail.com_")
    uploaded = st.file_uploader("Supported file format: pdf")
    if uploaded is not None:
        filename = uploaded.name
        text = convert_pdf_to_txt(filename)
        X_new = get_scores(text)
        col1, col2 = st.columns(2)
        with col1:
            open = st.button("Show Content")
            if open:
                st.write(text)
        with col2:
            show = st.button("Display Profile")
            if show:
                try:
                    st.write(X_new)
                    plt.style.use("dark_background")
                    barwidth=0.7
                    fig1, ax1 = plt.subplots(figsize=(20,8))
                    bars1 = X_new.iloc[0,0:6].values.tolist()
                    r1 = np.arange(len(bars1))
                    plt.bar(r1,bars1,color="red",width=barwidth,edgecolor="white",alpha=.4)
                    plt.xticks([r for r in range(len(bars1))],X_new.columns.tolist()[0:6])
                    ax1.tick_params(labelsize = 25)
                    st.pyplot(fig1)
                except:
                    st.write("profile not found")
            save = st.button("Save My Data")
            if save:
                    st.text("Saving data...")
                    time.sleep(2)
                    st.text("Successfully saved your data.")
                    time.sleep(.5)
                    st.text('Please proceed to the "Get Result" page.')
                    X_new.to_csv("set skills.csv", index = False)
