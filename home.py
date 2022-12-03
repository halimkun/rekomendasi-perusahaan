import streamlit as st
from config import Config

class Home:
    def __init__(self):
        self.option = Config().get_option()

    def main(self):
        st.markdown('''# Sistem Rekomendasi''')
        st.markdown('''
            Aplikasi yang dapat memberikan rekomendasi untuk para lulusan SMK, aplikasi ini memerlukan data lulusan tahun terdahulu untuk dapat memberikan rekomendasi, aplikasi ini dibuat dengan menggunakan algoritma **_Data Mining_** yaitu **_Decision Tree_** untuk memberikan rekomendasi peruahaan yang sesuai dengan kemampuan lulusan.
        ''')
        st.dataframe(Config().get_dataset())
