import streamlit as st
from streamlit_option_menu import option_menu

from config import config
from home import home
from about import about
from rekomendasi import rekomendasi
from bantuan import bantuan

# page config
st.set_page_config(
    page_title="Streamlit Option Menu",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# initial main page
def main():
    # sidebar
    with st.sidebar:
        selected_menu = option_menu(
            menu_title=False,
            options=config().get_option(),
            default_index=0,
            orientation="horizontal",
            icons=config().get_option_icon(),
            styles={
                "nav-link": {"--hover-color": "#9580ff82", "transition": "all 0.2s ease-in-out", "display": "flex"},
            }
        )

    if selected_menu == "Beranda":
        home().main()
    elif selected_menu == "Rekomendasi":
        rekomendasi().main()
    elif selected_menu == "Bantuan":
        bantuan().main()
    elif selected_menu == "Tentang":
        about().main()


# render page
main()
