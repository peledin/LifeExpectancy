import pandas as pd


def load_data():
    # Laden der vorverarbeiteten Daten
    X_train = pd.read_csv("../data/X_train.csv")
    X_test = pd.read_csv("../data/X_test.csv")
    y_train = pd.read_csv("../data/y_train.csv")
    y_test = pd.read_csv("../data/y_test.csv")

    return X_train, X_test, y_train, y_test
