import pandas as pd

from sklearn.model_selection import train_test_split
from config import config
from sklearn import tree

class model:
    def __init__(self):
        pass

    def prepared_dataset(self, df):
        # check df passed
        if df is None:
            return None
        else:
            df = pd.read_csv(df)

            df.dropna(inplace=True)
            df = df.reset_index(drop=True)
            df.columns = df.columns.str.strip()

            df.drop(['No', 'Nama'], axis=1, inplace=True)

            return df.astype(str)

    def calculate(self, nilai_df, target_df, nilai_input_df):
        if nilai_df is None or target_df is None or nilai_input_df is None:
            return None
        else:
            # split dataset
            X_train, X_test, y_train, y_test = train_test_split(nilai_df.values, target_df, test_size=0.26, random_state=2)

            # make model
            model = tree.DecisionTreeClassifier(
                criterion='entropy',
                max_depth=3, 
                max_leaf_nodes=3
            )

            # fit 
            clf = model.fit(X_train, y_train)

            # train model
            train_score = model.score(X_train, y_train)
            test_score = model.score(X_test, y_test)

            # predict
            predict = model.predict(nilai_input_df.T)

            # dot data
            dot_data = tree.export_graphviz(
                clf, out_file=None, 
                feature_names=nilai_df.columns, 
                class_names=y_train.values,  
                filled=True, rounded=True,  
                special_characters=True
            )

            return {
                'train_score': train_score,
                'test_score': test_score,
                'predict': predict,
                'plot_tree': dot_data
            }