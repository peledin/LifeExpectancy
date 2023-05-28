import pandas as pd
from joblib import load

# Modell laden
rf = load("Models/random_forest_model.joblib")

# Laden Sie Ihre Daten
df = pd.read_csv("data/life_expectancy_cleaned.csv")

# Extrahieren Sie die eindeutigen Ländernamen und konvertieren Sie sie in eine Liste
country_list = df["Country"].unique().tolist()


def predict_life_expectancy(input_data):
    # Konvertieren Sie das Eingabedaten-Dict in einen DataFrame
    df = pd.DataFrame(input_data, index=[0])
    # Anwenden des One-Hot-Encodings auf die Eingabedaten
    df_encoded = pd.get_dummies(df)

    # Laden Sie die Liste der Features
    all_features = load("Models/feature_list.joblib")

    # Fügen Sie fehlende Spalten hinzu und füllen Sie sie mit Nullen
    for col in all_features:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    # Sortieren Sie die Spalten, um sicherzustellen, dass sie in der gleichen Reihenfolge wie in den Trainingsdaten sind
    df_encoded = df_encoded[all_features]

    # Entfernen Sie die Zielvariable aus den Eingabevariablen
    df_encoded = df_encoded.drop(columns=["Life expectancy"])

    # Vorhersage durchführen
    prediction = rf.predict(df_encoded)
    prediction = prediction * 100  # Zurückkonvertieren in Jahre

    return prediction


# Testen der Funktion
input_data = [
    {
        "Country": "Zimbabwe",
        "Year": 1999.0,
        "Status": "Developing",
        "Adult Mortality": 0.36288088642659283,
        "infant deaths": 0.034444444444444444,
        "Alcohol": 0.2,
        "percentage expenditure": 0.0036591348588773187,
        "Hepatitis B": 0.6530612244897959,
        "Measles ": 0.005438701498235015,
        " BMI ": 0.20973348783314022,
        "under-five deaths ": 0.0332,
        "Polio": 0.93125,
        "Total expenditure": 0.4521183981427742,
        "Diphtheria": 0.6494845360824741,
        "HIV/AIDS": 0.0,
        "GDP": 0.004888585012167692,
        "Population": 0.02607428879088441,
        " thinness  1-19 years": 0.6195652173913043,
        " thinness 5-9 years": 0.6035087719298246,
        "Income composition of resources": 0.1052742616033755,
        "Schooling": 0.88792270531400966,
    }
]

print(predict_life_expectancy(input_data))
