import streamlit as st
# st.title('Hi there')

st.set_page_config(page_title=None, page_icon=None,
                   layout="wide",
                   initial_sidebar_state="expanded")


about_page = st.Page(
    "views/1_about.py",
    title="About",
    icon="😎",
    default=True,
)
overview = st.Page(
    "views/2_overview.py",
    title="Overview",
    icon="👀",
)

sales = st.Page(
    "views/3_sales.py",
    title="Sales",
    icon="🛒",
)
subscribers = st.Page(
    "views/4_subscribers.py",
    title="Subscribers",
    icon="👦",
)
content = st.Page(
    "views/5_content.py",
    title="Content",
    icon="🎞",
)

courses = st.Page(
    "views/6_courses.py",
    title="Courses",
    icon="🖼",
)


# Navigation 
pg = st.navigation(pages=[about_page, overview,sales,subscribers,content,courses])

# --- SHARED ON ALL PAGES ---

st.logo("assets/Udemy New.png")
st.sidebar.markdown("Made with ❤️ by [Hamshary](www.linkedin.com/in/mohamed-elhamshary-0825811a4)")

pg.run()
