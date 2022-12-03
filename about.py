import streamlit as st
from config import Config

class About:
    def __init__(self):
        self.option = Config().get_option()
    
    def main(self):
        st.title("About")
