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
    # Wczytaj przetworzone dane
    data = pd.read_csv(data_csv)
    
    # Podział na cechy (X) i etykiety (y)
    X = data[['size', 'extension']]
    y = data['label']
    
    # Podział danych na zestawy treningowe i testowe
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Trenowanie modelu
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Przewidywanie na zestawie testowym
    y_pred = model.predict(X_test)
    
    # Ocena modelu
    print(classification_report(y_test, y_pred))
    
    # Upewnij się, że katalog na model istnieje
    model_dir = os.path.dirname(model_output)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    # Zapisz model do pliku
    joblib.dump(model, model_output)
    print(f"Model został zapisany do '{model_output}'")

if __name__ == "__main__":
    train_model('data/file_data_preprocessed.csv', 'models/file_classifier.pkl')
