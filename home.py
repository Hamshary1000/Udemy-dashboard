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



st.markdown(
    """
    <style>
    .stApp {
        transform: scale(0.67);  /* Zoom to 67% */
        transform-origin: top center;  /* Ensure it stays centered */
        margin: 0 auto;  /* Center the app horizontally */
        width: 150%;  /* Compensate for the scaling */
    }

    @media only screen and (max-width: 1024px) {
        .stApp {
            transform: scale(0.85);  /* Slightly larger for smaller screens */
            transform-origin: top center;
            width: 120%;
        }
    }

    @media only screen and (max-width: 768px) {
        .stApp {
            transform: scale(1);  /* Full zoom for very small screens */
            transform-origin: top center;
            width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

pg.run()
