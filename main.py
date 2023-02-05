#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.preprocessing import MinMaxScaler
import random
from random import randint
import time
from input import input
from get_result import get_result
from read_pdf import read_pdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# In[158]:

def read_data():
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

# In[3]:

from PIL import Image

def main():
    options = ['0. Introduction','1. Load Dataset','2.1. Set Skills','2.2. Upload your CV','3. Get Result','Stop']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if (choice == "0. Introduction"):
        st.header("_Data Analyst Job Search Assistant_")
        t1,t2,t3,t4 = st.tabs(["1","2","3","4"])
        with t1:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Bootcamp Final Project")
                st.text("A presentation by:")
                st.markdown("**Muhammad Dimas Abdul Aziz Cakradewa**")
                st.markdown("**Data Analytics** Course, Full-Time, Nov 22 - Feb 23")
            with col2:
                st.text("")
            with col3:
                st.markdown("<h4 style='text-align: left; color: gray;'> Powered by:</h4>",unsafe_allow_html=True )
                st.image("./ironhack.png", width = 180)
        with t2:
            st.subheader("Things to do while searching for jobs:")
            st.markdown("- <h5>See job requirements</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Tasks at work</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Expectations</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Company profile</h5>", unsafe_allow_html=True)
        with t3:
            st.subheader("Things this _Job Search Assistant_ does for you:")
            st.markdown("- <h5>Load data from job market database</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Take your skill profile</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Give you job recommendation(s)</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Compare your profile with the job recommendation</h5>", unsafe_allow_html=True)
        with t4:
            st.subheader("Things this _Job Search Assistant_ doesn't do:")
            st.markdown("- <h5>Generate your CV</h5>", unsafe_allow_html=True)
            st.markdown("- <h5>Send formally-written emails to the company</h5>", unsafe_allow_html=True)
    
    elif (choice == "1. Load Dataset"):
        st.header("_Data Analyst Job Search Assistant_")
        readfile = st.button("Load Dataset")
        if readfile:
            X_scaled, X_cat = read_data()
            st.write("Loading data from database. Please wait..")
            time.sleep(2)
            st.write("Job offer database successfully loaded. Ready to run calculations.")
            time.sleep(1)
            st.write("Preview of available job offers from the dataset:")
            time.sleep(2)
            st.write(X_cat.sample(n=5))
            time.sleep(1)
            st.write("Successfully loaded dataset.")
            time.sleep(2)
            st.write("Please proceed to the 'Set Skills' page (see menu on the left)")
        pass

    elif (choice == "2.1. Set Skills"):
        input()
        pass
    
    elif (choice == '2.2. Upload your CV'):
        read_pdf()
        pass

    elif (choice == "3. Get Result"):
        get_result()
        pass

    else:
        st.subheader("Good luck on searching for jobs!")
        st.write("You're going to nail it. Best of luck.")
        time.sleep(15)
        st.stop()

main()
