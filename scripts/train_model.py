import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(data_csv, model_output):
    """
    Funkcja trenuje model AI na przetworzonych danych.
    
    Args:
        data_csv (str): Ścieżka do przetworzonego pliku CSV z danymi.
        model_output (str): Ścieżka do pliku, w którym model będzie zapisany.
    """
    print("🚀 Rozpoczynanie treningu modelu...")

    # Wczytaj przetworzone dane
    print(f"📥 Wczytywanie danych z pliku: {data_csv}")
    data = pd.read_csv(data_csv)
    
    # Podział na cechy (X) i etykiety (y)
    print("🔄 Podział danych na cechy i etykiety...")
    X = data[['size', 'extension']]
    y = data['label']
    
    # Podział danych na zestawy treningowe i testowe
    print("✂️ Podział danych na zestaw treningowy i testowy...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Trenowanie modelu
    print("🏋️‍♂️ Trenowanie modelu RandomForest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Przewidywanie na zestawie testowym
    print("🔍 Przewidywanie wyników na zestawie testowym...")
    y_pred = model.predict(X_test)
    
    # Ocena modelu
    print("📊 Generowanie raportu z oceny modelu...")
    print(classification_report(y_test, y_pred))
    
    # Upewnij się, że katalog na model istnieje
    model_dir = os.path.dirname(model_output)
    if not os.path.exists(model_dir):
        print(f"📂 Tworzenie katalogu na model: {model_dir}")
        os.makedirs(model_dir)
    
    # Zapisz model do pliku
    print(f"💾 Zapisywanie modelu do pliku: {model_output}")
    joblib.dump(model, model_output)
    print(f"✅ Model został zapisany do '{model_output}'")

if __name__ == "__main__":
    train_model('data/file_data_preprocessed.csv', 'models/file_classifier.pkl')
