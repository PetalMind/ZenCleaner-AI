
# File Classifier Project

## Overview
Ten projekt zawiera narzędzia do klasyfikacji plików na podstawie ich atrybutów, takich jak rozmiar, rozszerzenie itp. Projekt składa się z kilku modułów, które umożliwiają zbieranie danych, ich wstępne przetwarzanie, trenowanie modelu klasyfikującego oraz ocenę jego skuteczności. Projekt jest szczególnie użyteczny do segregacji plików na potrzebne i śmieciowe.

## Wymagania
- Python 3.8 lub nowszy
- Pakiety wymienione w `requirements.txt`

## Instalacja
1. Sklonuj repozytorium na swoje lokalne środowisko:
    ```bash
    git clone https://github.com/twoje-repozytorium/file-classifier.git
    ```
2. Przejdź do katalogu projektu:
    ```bash
    cd file-classifier
    ```
3. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

## Struktura katalogów
Struktura katalogów projektu wygląda następująco:
```
file-classifier/
├── data/
│   ├── raw/               # Surowe dane zebrane z katalogów
│   ├── processed/         # Przetworzone dane gotowe do trenowania modelu
├── models/                # Zapisane modele AI
├── notebooks/             # Notebooki Jupyter do eksploracji danych i testowania modeli
├── src/                   # Główne skrypty projektu
│   ├── collect_data.py    # Zbieranie danych o plikach
│   ├── preprocess_data.py # Przetwarzanie danych
│   ├── train_model.py     # Trenowanie modelu
│   ├── evaluate_model.py  # Ocena modelu
│   └── predict.py         # Przewidywanie za pomocą modelu
└── README.md              # Dokumentacja projektu
```

## Użycie

### 1. Zbieranie danych
Aby zebrać dane o plikach z konkretnego katalogu, uruchom `collect_data.py`. Skrypt ten przeszukuje wskazany katalog i zbiera informacje o plikach, takie jak rozmiar, rozszerzenie oraz przypisaną etykietę (np. 0 = śmieciowy, 1 = potrzebny).

```bash
python collect_data.py <ścieżka_do_katalogu> <etykieta>
```

Przykład:

```bash
python collect_data.py /path/to/junk 0
```

### 2. Wstępne przetwarzanie danych
Przed trenowaniem modelu, dane muszą zostać przetworzone. Skrypt `preprocess_data.py` wykonuje normalizację i konwersję danych do formatu odpowiedniego dla modelu.

```bash
python preprocess_data.py
```

### 3. Trenowanie modelu
Skrypt `train_model.py` trenuje model klasyfikujący na podstawie przetworzonych danych. Używa on algorytmu Random Forest, aby nauczyć się klasyfikować pliki.

```bash
python train_model.py
```

Model zostanie zapisany w katalogu `models/`.

### 4. Ocena modelu
Po zakończeniu trenowania modelu możesz ocenić jego skuteczność przy użyciu skryptu `evaluate_model.py`, który generuje raport z dokładnością modelu, precyzją, czułością i miarą F1.

```bash
python evaluate_model.py
```

### 5. Przewidywanie
Aby przewidzieć klasyfikację nowych plików, użyj skryptu `predict.py`. Skrypt ten wczytuje wytrenowany model i dokonuje przewidywań dla nowych danych.

```bash
python predict.py <ścieżka_do_pliku>
```

### Przykładowe użycie
Przykład pełnego przepływu pracy:
```bash
# Zbieranie danych
python collect_data.py /path/to/good_files 1
python collect_data.py /path/to/junk_files 0

# Przetwarzanie danych
python preprocess_data.py

# Trenowanie modelu
python train_model.py

# Ocena modelu
python evaluate_model.py

# Przewidywanie
python predict.py /path/to/new_file.txt
```

## Testowanie
Aby przetestować cały pipeline, można napisać skrypty testowe lub użyć pytest do testowania poszczególnych modułów. Upewnij się, że dane testowe są odpowiednio przygotowane w katalogu `data/`.

## Autorzy
- **Dominik** - Główny developer

## Licencja
Ten projekt jest objęty licencją MIT - szczegóły w pliku LICENSE.
