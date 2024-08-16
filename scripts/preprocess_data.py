import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(input_csv, output_csv):
    """
    Funkcja przetwarza dane i zapisuje je do nowego pliku CSV.
    
    Args:
        input_csv (str): Ścieżka do wejściowego pliku CSV z danymi.
        output_csv (str): Ścieżka do wyjściowego pliku CSV z przetworzonymi danymi.
    """
    # Wczytaj dane z CSV
    data = pd.read_csv(input_csv)
    
    # Konwersja kolumny 'extension' na numeryczne wartości
    le = LabelEncoder()
    data['extension'] = le.fit_transform(data['extension'])
    
    # Zapisz przetworzone dane do nowego pliku CSV
    data.to_csv(output_csv, index=False)
    print(f"Przetworzone dane zostały zapisane do '{output_csv}'")

if __name__ == "__main__":
    preprocess_data('data/file_data.csv', 'data/file_data_preprocessed.csv')
