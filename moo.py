import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import os

st.title('            AML DATA ENGINE               ')
uploadfile = st.file_uploader('Choose File', type = 'xlsx')
if uploadfile:
    df = pd.read_excel(uploadfile)
    #st.dataframe(df)
    #st.table(df)
    #dfc = st.cache
#if st.button("Data in the file"):
	#st.write (df.shape)
    #st.write(df['ID Type'].describe())
    #st.write(df.groupby(by=['ID Type']))
    
#if st.button('ID Types'):
   # st.write (df.groupby('ID Type')['Customer Number'].nunique('Transaction No'))

#opto = st.sidebar.selectbox(
 #  'START ANALYSIS',
  #('Email','phone')
#)

cal = st.multiselect("Select an option", ('ID TYPES','DATA IN THE FILE','NATIONALITY','REMITTER DETAILS','USER'))

if 'ID TYPES' in cal:
    st.write (df.groupby('ID Type')['Customer Number'].nunique('Transaction No'))

if 'DATA IN THE FILE' in cal:
    st.write (df.shape)

if 'NATIONALITY' in cal:
    st.write (df.pivot_table(df,index=['Remitter Nationality']))
    
if 'REMITTER DETAILS' in cal:
    st.write (df.pivot_table(df,index=['ID Type','Remitter Name']))
    
if 'USER' in cal:
   st.write (df.pivot_table(df,index=['User Code','LC Amt'],aggfunc={'LC Amt':np.sum}))
   
   
#complete untill now but needs work on 1. cache, 2. pivot tabel