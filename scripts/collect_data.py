import os
import sys
import pandas as pd
from tqdm import tqdm

def collect_file_data(directory, label):
    """
    Funkcja zbiera dane o plikach z podanego katalogu.
    
    Args:
        directory (str): Ścieżka do katalogu, z którego będą zbierane dane.
        label (int): Etykieta plików (0 = śmieciowy, 1 = potrzebny).
    
    Returns:
        pd.DataFrame: Dane o plikach w formacie DataFrame.
        int: Liczba plików, do których brak było uprawnień.
        int: Całkowita liczba odczytanych plików.
        int: Liczba plików, których nie można było przetworzyć.
    """
    file_data = []
    total_files = 0
    permission_errors = 0
    processing_errors = 0
    
    # Zliczanie wszystkich plików w katalogu
    total_file_count = sum(len(files) for _, _, files in os.walk(directory))

    with tqdm(total=total_file_count, desc=f"Przetwarzanie {directory}") as pbar:
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    size = os.path.getsize(filepath)
                    extension = os.path.splitext(file)[1]
                    file_data.append([filepath, size, extension, label])
                    total_files += 1
                except PermissionError:
                    permission_errors += 1
                except Exception:
                    processing_errors += 1
                
                # Aktualizacja paska postępu
                pbar.update(1)
    
    return pd.DataFrame(file_data, columns=['path', 'size', 'extension', 'label']), permission_errors, total_files, processing_errors

def main():
    # Sprawdź, czy flaga --FullScan została podana
    full_scan = '--FullScan' in sys.argv
    
    if full_scan:
        # Jeśli --FullScan jest włączona, ustaw directory na '/'
        print("🚀 Rozpoczynanie pełnego skanowania dysku...")
        junk_dir = '/'
        necessary_dir = '/'
    else:
        # Zdefiniuj ścieżki do katalogów
        junk_dir = 'data/junk_files/'
        necessary_dir = 'data/necessary_files/'
    
    # Zbierz dane z katalogów
    print("🔍 Zbieranie danych o plikach śmieciowych...")
    data_junk, permission_errors_junk, total_files_junk, processing_errors_junk = collect_file_data(junk_dir, 0)
    print("🔍 Zbieranie danych o plikach potrzebnych...")
    data_necessary, permission_errors_necessary, total_files_necessary, processing_errors_necessary = collect_file_data(necessary_dir, 1)
    
    # Połącz dane w jeden DataFrame
    print("🔄 Łączenie danych...")
    data = pd.concat([data_junk, data_necessary])
    
    # Upewnij się, że katalog 'data/' istnieje
    output_dir = 'data/'
    if not os.path.exists(output_dir):
        print(f"📂 Tworzenie katalogu: {output_dir}")
        os.makedirs(output_dir)
    
    # Zapisz dane do pliku CSV
    output_file = os.path.join(output_dir, 'file_data.csv')
    print(f"💾 Zapisywanie danych do pliku: {output_file}")
    data.to_csv(output_file, index=False)
    print("\n✅ Dane zostały zapisane do 'file_data.csv'")
    
    # Wyświetlenie podsumowania
    total_files = total_files_junk + total_files_necessary
    permission_errors = permission_errors_junk + permission_errors_necessary
    processing_errors = processing_errors_junk + processing_errors_necessary
    print(f"📊 Podsumowanie skanowania: Odczytane pliki: {total_files} | Brak uprawnień do plików: {permission_errors} | Pliki nieprzetworzone: {processing_errors}")

if __name__ == "__main__":
    main()
