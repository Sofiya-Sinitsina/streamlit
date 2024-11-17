import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
import os
from PIL import Image

image = Image.open('img/logo_d.png')

st.set_page_config(initial_sidebar_state='collapsed', page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "img", "logo_d.svg")

pages = ["Home", "Project1", "Project2", "Project3"]



styles = {
    "nav": {
        "background-color": "#581845",
    },
    "img": {
        "position": "absolute",
        "left": "-0px",
        "font-size": "15px",
        "top": "4px",
        "width": "2rem",
        "height": "2rem",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "#ffffff",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background_color": "rgba(105, 114, 255, 0.25)",
        "color": "#FFC300"
    },
    "hover": {
        "background_color": "rgba(255, 255, 255, 0.35)",
        "color": "#FFC300"
    }
}

page = navbar(pages, styles=styles, logo_path=logo_path,)

if page == "Home":
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()