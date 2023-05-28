# LifeExpectancy

Dieses Projekt beinhaltet die Erstellung von Modellen zur Vorhersage der Lebenserwartung basierend auf verschiedenen Merkmalen. Der Datensatz stammt von [Kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who?resource=download)

## Über das Projekt

Dieses Projekt wurde von [Dino Pelesevic](https://github.com/peledin), [Noemi Ryf](https://github.com/ryfnoe) und [Jay-Leo Nagel](https://github.com/jayzing00) im Rahmen des Moduls `Python-Grundlagen & Anwendung in Data Science (2023-FS)` an der [ZHAW](https://www.zhaw.ch/en/university/) erstellt.

## Struktur

Dieses Projekt besteht aus verschiedenen Komponenten:

- Models: Dieser Ordner enthält verschiedene vorher trainierte Modelle zur Vorhersage der Lebenserwartung, einschließlich random_forest_model.joblib, gradient_boosting_model.joblib, linear_regression_model.joblib und feature_list.joblib​​.
- app: In diesem Ordner befindet sich die app.py-Datei, die ein Flask-basiertes Webanwendungsskript ist. Es lädt das trainierte Modell und die Daten, ermöglicht Vorhersagen basierend auf den Eingabedaten und gibt die Vorhersage als JSON zurück​​.
- data: Dieser Ordner enthält die Datensätze, die für das Training des Modells verwendet wurden.
- src: In diesem Ordner befinden sich die Python-Notebooks zur Erstellung der Modelle, das Notebook für die Bereinigung des Datensatzes, sowie das Notebook für die Anwendung der XAI-Techniken.

## Installation

Um dieses Projekt zu klonen und lokal auszuführen, führen Sie die folgenden Schritte aus:

- Klonen Sie das Repository auf Ihren lokalen Rechner

```bash
git clone https://github.com/peledin/LifeExpectancy.git
```

- Installieren Sie die benötigten Python-Pakete mit dem folgenden Befehl

```bash
pip install -r requirements.txt.
```
