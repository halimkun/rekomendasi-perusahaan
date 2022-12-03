import streamlit as st
from streamlit_option_menu import option_menu

from config import Config
from home import Home
from about import About
from rekomendasi import Rekomendasi

# page config
st.set_page_config(
    page_title="Streamlit Option Menu",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="expanded",
)


# initial main page
def main():
    # sidebar
    with st.sidebar:
        selected_menu = option_menu(
            menu_title=False,
            options=Config().get_option(),
            default_index=0,
            orientation="horizontal",
            icons=Config().get_option_icon(),
            styles={
                "nav-link": {"--hover-color": "#5e497c", "transition": "all 0.2s ease-in-out", "text-align": "left"},
            }
        )

    if selected_menu == "Home":
        Home().main()
    elif selected_menu == "Rekomendasi":
        Rekomendasi().main()
    elif selected_menu == "About":
        About().main()


# render page
main()
