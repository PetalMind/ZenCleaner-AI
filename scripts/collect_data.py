import os
import pandas as pd

def collect_file_data(directory, label):
    """
    Funkcja zbiera dane o plikach z podanego katalogu.
    
    Args:
        directory (str): Ścieżka do katalogu, z którego będą zbierane dane.
        label (int): Etykieta plików (0 = śmieciowy, 1 = potrzebny).
    
    Returns:
        pd.DataFrame: Dane o plikach w formacie DataFrame.
    """
    file_data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            extension = os.path.splitext(file)[1]
            file_data.append([filepath, size, extension, label])
    
    return pd.DataFrame(file_data, columns=['path', 'size', 'extension', 'label'])

def main():
    # Zdefiniuj ścieżki do katalogów
    junk_dir = 'data/junk_files/'
    necessary_dir = 'data/necessary_files/'
    
    # Zbierz dane z katalogów
    data_junk = collect_file_data(junk_dir, 0)
    data_necessary = collect_file_data(necessary_dir, 1)
    
    # Połącz dane w jeden DataFrame
    data = pd.concat([data_junk, data_necessary])
    
    # Upewnij się, że katalog 'data/' istnieje
    output_dir = 'data/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Zapisz dane do pliku CSV
    data.to_csv(os.path.join(output_dir, 'file_data.csv'), index=False)
    print("Dane zostały zapisane do 'file_data.csv'")

if __name__ == "__main__":
    main()
