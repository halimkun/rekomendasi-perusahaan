import streamlit as st
from config import config

class about:
    def __init__(self):
        self.option = config().get_option()
    
    def main(self):
        st.title("About")

        st.markdown('''
            Aplikasi rekomendasi yang dibuat untuk membantu siswa atau mahasiswa dalam memilih jurusan yang sesuai dengan kompentensi semasa menempuh pendidikan, aplikasi ini memanfaatkan metode decision tree untuk menghasilkan rekomendasi. untuk dapat menggunakan aplikasi ini, diharapkan pengguna sudah memiliki dataset yang sesuai dengan format yang telah ditentukan.

            dalam aplikasi ini, pengguna dapat mengupload dataset yang telah disiapkan, kemudian menginputkan nilai-nilai yang diperoleh semasa menerima pendidikan, lalu aplikasi akan memberikan rekomendasi jurusan yang sesuai dengan nilai-nilai yang telah diinputkan.

            untuk lebih lengkap mengenai cara penggunaan aplikasi ini, silahkan klik tombol bantuan yang ada di sebelah kiri.
        ''', unsafe_allow_html=True)