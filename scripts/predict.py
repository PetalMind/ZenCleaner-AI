import os
import sys
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

def collect_file_data(directory):
    """
    Zbiera dane o plikach z podanego katalogu bez etykiet.
    
    Args:
        directory (str): Ścieżka do katalogu, z którego będą zbierane dane.
    
    Returns:
        pd.DataFrame: Dane o plikach w formacie DataFrame.
    """
    file_data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                extension = os.path.splitext(file)[1]
                file_data.append([filepath, size, extension])
            except FileNotFoundError:
                print(f"File not found: {filepath}")
            except PermissionError:
                print(f"Permission denied: {filepath}")
            except Exception as e:
                print(f"Error accessing file {filepath}: {e}")
    
    return pd.DataFrame(file_data, columns=['path', 'size', 'extension'])

def predict(model_path, directory):
    """
    Funkcja przewiduje klasyfikację plików w podanym katalogu.
    
    Args:
        model_path (str): Ścieżka do zapisanego modelu.
        directory (str): Ścieżka do katalogu z plikami do klasyfikacji.
    """
    # Sprawdzenie, czy plik modelu istnieje
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Sprawdzenie, czy katalog istnieje
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    # Wczytaj model
    model = joblib.load(model_path)
    
    # Zbierz dane o nowych plikach
    new_data = collect_file_data(directory)
    
    # Sprawdzenie, czy zebrano jakieś dane
    if new_data.empty:
        print("No files found in the directory.")
        return
    
    # Przekształć kolumnę 'extension' na wartości numeryczne
    le = LabelEncoder()
    new_data['extension'] = le.fit_transform(new_data['extension'])
    
    # Przewidywanie
    X_new = new_data[['size', 'extension']]
    predictions = model.predict(X_new)
    new_data['prediction'] = predictions
    
    # Wyświetlenie wyników
    print(new_data[['path', 'prediction']])

    # Zapisz wyniki do pliku CSV
    new_data.to_csv('data/predicted_files.csv', index=False)
    print("Wyniki klasyfikacji zostały zapisane do 'data/predicted_files.csv'")

if __name__ == "__main__":
    # Sprawdź, jakie flagi zostały przekazane
    if '--fullScan' in sys.argv:
        predict('models/file_classifier.pkl', '/')
    elif len(sys.argv) > 2 and sys.argv[1] == '--directory':
        directory = sys.argv[2]
        predict('models/file_classifier.pkl', directory)
    else:
        print("Usage: python3 scripts/predict.py --directory /path/to/directory")
        print("       python3 scripts/predict.py --fullScan")
