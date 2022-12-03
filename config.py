import pandas as pd

class Config:
    def __init__(self) :
        self.dataset = './dataset/data_lulusan.csv'
        self.option = ["Home", "Rekomendasi", "About" ]
        self.option_icon = ["house", "hr", "info-circle"]
    
    def get_dataset(self):
        return pd.read_csv(self.dataset)

    def get_option(self):
        return self.option

    def get_option_icon(self):
        return self.option_icon