import streamlit as st


st.set_page_config(page_title=None, page_icon=None,
                   layout="wide",
                   initial_sidebar_state="expanded")

   

#Body



st.image('assets/Udemy New.png')



   



    # Center the text
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.title('About This App')
    
    st.write("""
    Welcome to the **Udemy Competitive Analysis Dashboard**! This app is designed to provide valuable insights into the Udemy course marketplace,
    helping you understand trends, performance metrics, and competitive dynamics across various subjects and categories.
    """)
    
    st.subheader('Purpose')
    
    st.write("""
    The primary goal of this app is to analyze the Udemy dataset, which includes information on courses such as:
    - **Course Title**
    - **Price**
    - **Number of Subscribers**
    - **Number of Reviews**
    - **Content Duration**
    - **Course Level**
    - **Subject**
    - **Profit**
    - **Published Date** """)
    
    
    st.subheader('With this data, the app aims to:')

    st.write("""        
    1. **Identify Market Trends**: Understand which subjects and course types are popular among learners.
    2. **Evaluate Competitive Position**: Analyze how different courses and instructors are performing relative to each other.
    3. **Profitability Analysis**: Assess which courses are generating the most revenue and why.
    4. **Content Strategy**: Discover which course attributes (e.g., level, duration, price) contribute to higher engagement and profitability.
    """)
