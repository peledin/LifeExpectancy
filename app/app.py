from flask import Flask, render_template, request, jsonify
import pandas as pd
from joblib import load

app = Flask(__name__, template_folder="templates")

# Modell laden
rf = load("../Models/random_forest_model.joblib")

# Laden der Daten
df = pd.read_csv("../data/life_expectancy_cleaned.csv")

# Eindeutige Ländernamen extrahieren und in eine Liste konvertieren
country_list = df["Country"].unique().tolist()


def predict_life_expectancy(input_data):
    # Konvertiere das Eingabedaten-Dict in einen DataFrame
    df = pd.DataFrame(input_data, index=[0])
    # Anwenden des One-Hot-Encodings auf die Eingabedaten
    df_encoded = pd.get_dummies(df)

    # Liste der Features laden
    all_features = load("../Models/feature_list.joblib")

    # Füge fehlende Spalten hinzu und fülle sie mit Nullen
    for col in all_features:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    # Sortiere die Spalten, um sicherzustellen, dass sie in der gleichen Reihenfolge wie in den Trainingsdaten sind
    df_encoded = df_encoded[all_features]

    # Entferne die Zielvariable aus den Eingabevariablen
    df_encoded = df_encoded.drop(columns=["Life expectancy"])

    # Vorhersage durchführen
    prediction = rf.predict(df_encoded)
    prediction = prediction * 100  # Zurückkonvertieren in Jahre

    return prediction


@app.route("/")
def home():
    return render_template("index.html", country_list=country_list)


def convert_to_float(val):
    try:
        return float(val)
    except ValueError:
        return val


@app.route("/predict", methods=["POST"])
def predict():
    # Extrahiere die Daten aus der Anfrage
    data = request.form.to_dict()
    data = {k: [convert_to_float(v)] for k, v in data.items()}

    # Vorhersage durchführen
    prediction = predict_life_expectancy(data)

    # Verwandle die Vorhersage in JSON und gib sie zurück
    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    app.run(debug=True)
