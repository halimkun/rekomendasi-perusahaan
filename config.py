class config:
    def __init__(self) :
        self.dataset = 'https://raw.githubusercontent.com/halimkun/rekomendasi-perusahaan/main/dataset/data_lulusan.csv'
        
        self.option = ["Beranda", "Rekomendasi","Bantuan", "Tentang" ]
        self.option_icon = ["house", "hr", "hand-index-thumb", "info-circle"]

    def get_dataset(self):
        return self.dataset

    def get_option(self):
        return self.option

    def get_option_icon(self):
        return self.option_icon
