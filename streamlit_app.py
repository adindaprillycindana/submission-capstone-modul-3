import streamlit as st

# --- Page Setup ---

about_page = st.Page(
    page = "views/about_us.py",
    title = "About Us",
    icon = ":material/account_circle:",
    default=True,
)

project_1_page =st.Page(
    page="views/model_deploy.py",
    title = "Prediction Model",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP  ---
pg = st.navigation(pages=[about_page, project_1_page])

# --- SHARED ON ALL PAGES ---
st.logo("assets/terra_h.png",size='large')
st.sidebar.text('Made with 💚 by The Data Science Team')

# --- RUN NAVIGATION ---
pg.run()