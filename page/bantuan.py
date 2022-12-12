import streamlit as st


class bantuan:
    def __init__(self):
        pass

    def main(self):
        st.title("Cara Penggunaan")
        '''
            cara menggunakan aplikasi ini, silahkan ikuti langkah-langkah berikut:
        '''

        with st.expander("Siapkan Dataset"):
            st.markdown('''
                Dataset yang digunakan dalam aplikasi ini, harus berformat csv, dan memiliki kolom-kolom sebagai berikut:
                
                | Kolom | Keterangan |
                |---|---|
                | Nomor | digunakan untuk menandai data |
                | Nama | digunakan dalam sistem rekomendasi |
                | Nilai Siswa | Nilai yang digunakan bisa berapapun, sesuai data yang dimiliki |
                | Target | digunakan untuk menentukan target dari data yang dimiliki, target ini akan menjadi hasil dari sistem rekomendasi, dengan kata lain, target ini akan menjadi hal yang direkomendasikan |

                <br />

                pastikan urutan kolom sesuai dengan yang telah ditentukan, jika tidak sesuai, maka aplikasi tidak akan dapat berjalan dengan baik. untuk lebih lengkapnya, silahkan perhatikan gambar berikut:
            ''', unsafe_allow_html=True)
        
        with st.expander("Simpan dataset dalam format csv"):
            st.markdown('''
                untuk dapat menyimpan dataset dalam format csv, silahkkan ikuti langkah-langkah berikut sesuai dengan aplikasi office yang digunakan, atau bisa juga menggunakan aplikasi lain yang dapat menyimpan file dalam format csv.
            ''', unsafe_allow_html=True)
        
        with st.expander("Upload dataset"):
            st.markdown('''
                Dataset yang telah disiapkan, kemudian diupload ke aplikasi ini. 

                Pada menu rekomendasi, terdapat fitur upload dataset, dengen demikian data yang sudah disiapkan dapat digunakan dalam memberikan rekomendasi. data dapat berupa data apapun, baik itu data lulusan yang sudah bekerja atau lulusan yang melanjutkan pendidikan ke jenjang yang lebih tinggi.
            ''', unsafe_allow_html=True)

            st.info('''
                pastikan dataset yang diupload sudah sesuai dengan format yang telah ditentukan pada __Poin 1__
            ''')

        with st.expander("Inputkan nilai-nilai yang diperoleh"):
            st.markdown('''
                Setelah dataset yang digunakan telah diupload, kemudian nilai-nilai dari siswa atau mahasiswa yang akan diberikan rekomendasi diinputkan kedalam tempat yang telah disediakan, nilai tersebut akan digunakan untuk perhitungan matematis dan untuk memperoleh hasil rekomendasi.
            ''', unsafe_allow_html=True)

            st.info('''
                pastikan field yang sudah disediakan sudah terisi semua sebelum menekan tombol __Rekomendasikan__
            ''')