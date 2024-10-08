import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



data=pd.read_csv("udemy_courses-cleaned.csv")
df=data.copy()



#sidebar
st.sidebar.write('filter your data')
study_subject=st.sidebar.selectbox('choose subject',['Web Development','Business Finance','Musical Instruments','Graphic Design'])
# choosen_year=st.sidebar.slider('year',2011,2017)


#Body

#Row 1:

col1, col2 = st.columns((3, 7), gap='large')


with col1:        
    # Create a container for the card-like layout
    with st.container():
        # Using markdown with HTML for card-like styling
        st.markdown("""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #F9E400;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: 100%;  /* Ensure full width */
                text-align: center;
            ">
                <h3 style="margin: 0;">Content Duration</h3>
                <h1 style="margin: 0; ">{:,.0f}</h1>
            </div>
            """.format(df['content_duration'].sum()), unsafe_allow_html=True)
        
    fig = px.pie(df, values="content_duration", names="subject",title='Content Duration by subject')
    st.plotly_chart(fig, use_container_width=True)  # Ensure full width of the column
        


    


with col2:
    st.header('Content duration in Each duration category in each subject')
    ans2 = pd.pivot_table(data=df, columns='subject', index='duration_category', values='content_duration', aggfunc='sum')[study_subject]
    fig = px.bar(x=ans2.index, y=ans2)
    st.plotly_chart(fig, use_container_width=True)  # Ensure full width of the column


    


b1,b2 = st.columns(2,gap='medium')

with b1:
    st.header('Content Duration by level')
    ans3 = pd.pivot_table( data=df,columns='subject', index='level', values='content_duration', aggfunc='sum')[study_subject]
    fig = px.bar(x=ans3, y=ans3.index, orientation='h')
    st.plotly_chart(fig, use_container_width=True)


with b2:
    st.header('Content Duration each year in each subject')
    ans2 = pd.pivot_table(data=df, columns='subject', index='year', values='content_duration', aggfunc='sum')[study_subject]
    fig = px.bar(x=ans2.index, y=ans2)
    st.plotly_chart(fig, use_container_width=True)  # Ensure full width of the column
