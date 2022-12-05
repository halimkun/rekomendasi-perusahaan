import streamlit as st
from config import config
from model import model
import pandas as pd
from sklearn import tree

class rekomendasi:
    def __init__(self):
        self.option = config().get_option()
        self.widget = []
    
    def main(self):
        st.title("Rekomendasi")

        col1, col2 = st.columns(2)

        col1.markdown('''<div style="font-size:1.2rem; font-weight: bold;">Upload Dataset</div>''', unsafe_allow_html=True)
        df = col1.file_uploader("", type=['csv'], help="Upload file dataset, hanya file csv yang diperbolehkan.", accept_multiple_files=False)
        
        if df is not None:
            df = model.prepared_dataset(self, df)

            nilai = df.columns[:-1]
            target = df.columns[-1]

            nilai_input = []
            col2.markdown('''<div style="font-size:1.2rem; font-weight: bold; ">Input Nilai</div>''', unsafe_allow_html=True)
            for i in range(len(nilai)):
                nilai_input.append(col2.number_input(nilai[i], min_value=0, max_value=100, help="Masukkan nilai"))

            col2.write("")
            if col2.button("Rekomendasikan"):
                nilai_input = pd.DataFrame(nilai_input)

                # polygon style
                st.markdown('''<style>
                    .polygon {
                        width: 0;
                        height: 0;
                        border-left: 50px solid transparent;
                        border-right: 50px solid transparent;
                        border-bottom: 100px solid #5e497c;
                    }
                </style>''', unsafe_allow_html=True)

                result = model.calculate(self, df[nilai], df[target], nilai_input)
                
                col1.markdown('''---''')
                col1.markdown('''<div style="font-size:1.2rem; font-weight: bold; ">Hasil Rekomendasi</div>''', unsafe_allow_html=True)
                col1.markdown(f'''<div style="font-size:1rem; color: #5e497c;">{result['predict'][0]}</div>''', unsafe_allow_html=True)
                col1.markdown('''<br />''', unsafe_allow_html=True)
                col1.markdown('''<div style="font-size:1.2rem; font-weight: bold; ">Detail</div>''', unsafe_allow_html=True)
                col1.markdown(f'''<div style="font-size:1rem;">Akurasi: <code>{result['train_score']}</code></div>''', unsafe_allow_html=True)