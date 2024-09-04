import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title=None, page_icon=None,
                   layout="wide",
                   initial_sidebar_state="expanded")

data=pd.read_csv("udemy_courses-cleaned.csv")
df=data.copy()



#sidebar
st.sidebar.write('filter your data')
study_subject=st.sidebar.selectbox('choose subject',['Web Development','Business Finance','Musical Instruments','Graphic Design'])
# choosen_year=st.sidebar.slider('year',2011,2017)



#Body
a1, a2, a3, a4 = st.columns(4, gap='small')

# Define a common card width
card_width = "100%"

with a1:
    with st.container():
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #EF5A6F;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Num of courses</h3>
                <h1 style="margin: 0;">{df['course_id'].size}</h1>
            </div>
            """, unsafe_allow_html=True)

with a2:
    with st.container():
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #AD49E1;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">num of levels</h3>
                <h1 style="margin: 0;">{df['level'].nunique():,.0f}</h1>
            </div>
            """, unsafe_allow_html=True)

with a3:
    with st.container():
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #D4BDAC;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Num of web courses</h3>
                <h1 style="margin: 0;">⬆ {df['subject'].value_counts()[0]:,.0f}</h1>
            </div>
            """, unsafe_allow_html=True)

with a4:
    with st.container():
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #536493;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Num of Graphic courses </h3>
                <h1 style="margin: 0;">⬇ {df['subject'].value_counts()[3]}</h1>
            </div>
            """, unsafe_allow_html=True)


col1,col2=st.columns(2,gap='small')
with col1:
    st.write('')
    st.header('Total courses by level')
    ans3 = pd.pivot_table( data=df,columns='subject', index='level', values='course_id', aggfunc='sum')[study_subject]
    fig = px.bar(x=ans3.index, y=ans3)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write('')
    st.header('Total courses by year')
    ans3 = pd.pivot_table( data=df,columns='subject', index='year', values='course_id', aggfunc='sum')[study_subject]
    fig = px.bar(x=ans3.index, y=ans3)
    st.plotly_chart(fig, use_container_width=True)




st.write('')
st.header('Growth of courses over years')
ans3=df.pivot_table(columns='subject',index='year',values='course_id',aggfunc='size') 
fig = px.line(ans3, 
                  x=ans3.index, 
                  y=ans3.columns, 
                  labels={'value': 'Number of Courses', 'year': 'Year'}
                  )
st.plotly_chart(fig, use_container_width=True)
    
