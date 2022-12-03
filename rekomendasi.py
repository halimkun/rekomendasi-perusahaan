import streamlit as st
from config import Config

class Rekomendasi:
    def __init__(self):
        self.option = Config().get_option()
    
    def main(self):
        st.title("Rekomendasi")
