import os
import pandas as pd
from sklearn.metrics import classification_report
import joblib

def evaluate_model(model_path, data_csv):
    """
    Funkcja ocenia zapisany model AI na nowym zestawie danych.
    
    Args:
        model_path (str): Ścieżka do zapisanego modelu.
        data_csv (str): Ścieżka do przetworzonego pliku CSV z danymi.
    """
    print(f"🔍 Rozpoczynanie oceny modelu...")

    # Sprawdzenie, czy plik modelu istnieje
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"❗ Model file not found: {model_path}")
    
    print(f"📦 Wczytywanie modelu z pliku: {model_path}")
    # Wczytaj model
    model = joblib.load(model_path)
    
    # Sprawdzenie, czy plik danych istnieje
    if not os.path.exists(data_csv):
        raise FileNotFoundError(f"❗ Data file not found: {data_csv}")
    
    print(f"📥 Wczytywanie danych z pliku: {data_csv}")
    # Wczytaj dane
    data = pd.read_csv(data_csv)
    
    print("🔄 Podział danych na cechy (X) i etykiety (y)...")
    # Podział na cechy (X) i etykiety (y)
    X = data[['size', 'extension']]
    y = data['label']
    
    print("🔍 Przeprowadzanie predykcji na danych...")
    # Przewidywanie na danych
    y_pred = model.predict(X)
    
    print("📊 Generowanie raportu z oceny modelu...")
    # Ocena modelu
    print(classification_report(y, y_pred))
    print("✅ Ocena modelu została zakończona.")

if __name__ == "__main__":
    evaluate_model('models/file_classifier.pkl', 'data/file_data_preprocessed.csv')
