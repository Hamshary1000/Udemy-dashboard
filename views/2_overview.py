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
# st.table(df.head())

#sidebar
st.write('')
st.write('')
st.sidebar.write('filter your data')
# study_subject=st.sidebar.selectbox('choose subject',[None,'Web Development','Business Finance','Musical Instruments','Graphic Design'])
choosen_year=st.sidebar.slider('year',2011,2017)












#Body


#Row1
a1, a2, a3, a4 = st.columns(4, gap='small')

# Define a common card width
card_width = "100%"

with a1:
    filtered_data = df[df['year'] == choosen_year]

    with st.container():
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #F5004F;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Num of courses</h3>
                <h1 style="margin: 0;">{filtered_data['course_id'].size}</h1>
            </div>
            """, unsafe_allow_html=True)

with a2:
    with st.container():
        filtered_data = df[df['year'] == choosen_year]
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #7C00FE;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Sales</h3>
                <h1 style="margin: 0;">${filtered_data['profit'].sum():,.0f}</h1>
            </div>
            """, unsafe_allow_html=True)

with a3:
    with st.container():
        filtered_data = df[df['year'] == choosen_year]
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #F9E400;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Content Duration</h3>
                <h1 style="margin: 0;">{filtered_data['content_duration'].sum():,.0f}</h1>
            </div>
            """, unsafe_allow_html=True)

with a4:
    with st.container():
        filtered_data = df[df['year'] == choosen_year]
        st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                background-color: #FFAF00;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                width: {card_width};
                text-align: center;
            ">
                <h3 style="margin: 0;">Subscribers</h3>
                <h1 style="margin: 0;">{filtered_data['num_subscribers'].sum()}</h1>
            </div>
            """, unsafe_allow_html=True)



#Row2
st.write('')
st.write('')

c1, c2 = st.columns((4,6))

with c1:
    st.header(f'Paid vs Free Courses {choosen_year}')
    # Count the occurrences of paid vs free courses
    filtered_data = df[df['year'] == choosen_year]

    ans1 = filtered_data['is_paid'].value_counts().reset_index()
    ans1.columns = ['is_paid', 'count']
    
    # Create a pie chart using Plotly Express
    fig = px.pie(ans1, values='count', names='is_paid')
    
    # Display the pie chart in Streamlit
    st.plotly_chart(fig)

with c2:
    st.header(f'Total profit made by each subject in each year {choosen_year}')
    ans2=pd.pivot_table(df, index='subject', columns='year', values='profit', aggfunc='sum')[choosen_year]


    fig= px.bar(
    
    x=ans2.index,
    y=ans2,
   )
    st.plotly_chart(fig)


#Row2
st.write('')
st.write('')

b1, b2 = st.columns((4,6))



with b1:
    pivot_table = pd.pivot_table(df, index='subject', columns='year', values='num_lectures', aggfunc='sum')
    filtered_data = pivot_table[choosen_year].reset_index()
    st.subheader(f'Num of lectures {choosen_year}')
    fig = px.imshow(filtered_data.set_index('subject').T, color_continuous_scale='Rainbow')
    st.plotly_chart(fig)


with b2:
    pivot_table = pd.pivot_table(df, index='subject', columns='year', values='num_subscribers', aggfunc='sum')
    filtered_data = pivot_table[choosen_year].reset_index()
    st.subheader(f'Num of subscribers {choosen_year}')
    fig = px.treemap(filtered_data, path=['subject'], values=choosen_year)
    st.plotly_chart(fig)
