
# ZenCleaner-AI Project

## Overview
ZenCleaner-AI to projekt umożliwiający klasyfikację plików na podstawie ich atrybutów, takich jak rozmiar, rozszerzenie itp. Projekt składa się z kilku modułów, które umożliwiają zbieranie danych, ich wstępne przetwarzanie, trenowanie modelu klasyfikującego oraz ocenę jego skuteczności. Projekt jest szczególnie użyteczny do segregacji plików na potrzebne i śmieciowe.

## Wymagania
- Python 3.8 lub nowszy
- Pakiety wymienione w `requirements.txt`

## Instalacja
1. Sklonuj repozytorium na swoje lokalne środowisko:
    ```bash
    git clone git clone https://github.com/PetalMind/ZenCleaner-AI.git

    ```
2. Przejdź do katalogu projektu:
    ```bash
    cd ZenCleaner-AI
    ```
3. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

## Struktura katalogów i plików

```
ZenCleaner-AI/
├── data/                           # Katalog na zbiory danych
│   ├── junk_files/                 # Przykładowe pliki śmieciowe do treningu
│   ├── necessary_files/            # Przykładowe pliki potrzebne do treningu
│   └── file_data.csv               # Plik CSV z połączonymi danymi plików (rozmiar, rozszerzenie, label)
│
├── models/                         # Katalog na zapisane modele
│   └── file_classifier.pkl         # Zapisany model klasyfikujący pliki
│
├── notebooks/                      # Katalog na notatniki Jupyter do eksploracji i prototypowania
│   └── data_exploration.ipynb      # Notatnik do wstępnej eksploracji danych
│
├── scripts/                        # Katalog na skrypty Pythona
│   ├── collect_data.py             # Skrypt do zbierania danych o plikach
│   ├── preprocess_data.py          # Skrypt do wstępnego przetwarzania danych
│   ├── train_model.py              # Skrypt do trenowania modelu AI
│   ├── evaluate_model.py           # Skrypt do oceny modelu na zestawie testowym
│   └── predict.py                  # Skrypt do przewidywania na nowych danych
│
├── requirements.txt                # Lista wymaganych bibliotek Pythona
├── README.md                       # Plik README z opisem projektu i instrukcją obsługi
└── .gitignore                      # Plik gitignore dla plików i katalogów, które nie powinny trafić do repozytorium
```

## Opis poszczególnych plików i katalogów

- **data/**: Katalog, w którym przechowywane są zbiory danych. Pliki treningowe są podzielone na dwie kategorie: `junk_files/` (pliki śmieciowe) i `necessary_files/` (pliki potrzebne). Plik `file_data.csv` przechowuje dane zebrane z obu katalogów w formie tabelarycznej.
  
- **models/**: Katalog przeznaczony na zapisane modele. Główny model klasyfikujący pliki jest zapisany jako `file_classifier.pkl`.

- **notebooks/**: Katalog zawierający notatniki Jupyter, które będą używane do eksploracji danych i prototypowania modelu. Notatnik `data_exploration.ipynb` zawiera wstępną analizę danych.

- **scripts/**: Katalog zawierający skrypty Pythona:
  - `collect_data.py`: Skrypt do zbierania danych o plikach z katalogów z plikami śmieciowymi i potrzebnymi.
  - `preprocess_data.py`: Skrypt do wstępnego przetwarzania danych (np. transformacja rozszerzeń plików na wartości numeryczne).
  - `train_model.py`: Skrypt do trenowania modelu na zebranych danych.
  - `evaluate_model.py`: Skrypt do oceny wydajności modelu na zestawie testowym.
  - `predict.py`: Skrypt do przewidywania klas plików na nowych danych.

- **requirements.txt**: Plik zawierający listę wszystkich bibliotek Pythona, które są potrzebne do uruchomienia projektu, takich jak `numpy`, `pandas`, `scikit-learn`.

- **README.md**: Plik z opisem projektu, instrukcją instalacji, sposobem uruchamiania skryptów i innymi ważnymi informacjami dla użytkownika lub programisty.

- **.gitignore**: Plik konfiguracyjny dla Git, który określa, które pliki i katalogi mają być ignorowane przez system kontroli wersji (np. katalog `__pycache__`, pliki tymczasowe, dane wyjściowe itp.).

## Użycie

### 1. Zbieranie danych
Aby zebrać dane o plikach z konkretnego katalogu, uruchom `collect_data.py`. Skrypt ten przeszukuje wskazany katalog i zbiera informacje o plikach, takie jak rozmiar, rozszerzenie oraz przypisaną etykietę (np. 0 = śmieciowy, 1 = potrzebny).

```bash
python scripts/collect_data.py <ścieżka_do_katalogu> <etykieta>
```

Przykład:

```bash
python scripts/collect_data.py data/junk_files 0
python scripts/collect_data.py data/necessary_files 1
```

### 2. Wstępne przetwarzanie danych
Przed trenowaniem modelu, dane muszą zostać przetworzone. Skrypt `preprocess_data.py` wykonuje normalizację i konwersję danych do formatu odpowiedniego dla modelu.

```bash
python scripts/preprocess_data.py
```

### 3. Trenowanie modelu
Skrypt `train_model.py` trenuje model klasyfikujący na podstawie przetworzonych danych. Używa on algorytmu Random Forest, aby nauczyć się klasyfikować pliki.

```bash
python scripts/train_model.py
```

Model zostanie zapisany w katalogu `models/`.

### 4. Ocena modelu
Po zakończeniu trenowania modelu możesz ocenić jego skuteczność przy użyciu skryptu `evaluate_model.py`, który generuje raport z dokładnością modelu, precyzją, czułością i miarą F1.

```bash
python scripts/evaluate_model.py
```

### 5. Przewidywanie
Aby przewidzieć klasyfikację nowych plików, użyj skryptu `predict.py`. Skrypt ten wczytuje wytrenowany model i dokonuje przewidywań dla nowych danych.

```bash
python scripts/predict.py <ścieżka_do_pliku>
```

### Przykładowe użycie
Przykład pełnego przepływu pracy:
```bash
# Zbieranie danych
python scripts/collect_data.py data/necessary_files 1
python scripts/collect_data.py data/junk_files 0

# Przetwarzanie danych
python scripts/preprocess_data.py

# Trenowanie modelu
python scripts/train_model.py

# Ocena modelu
python scripts/evaluate_model.py

# Przewidywanie
python scripts/predict.py /path/to/new_file.txt
```

## Testowanie
Aby przetestować cały pipeline, można napisać skrypty testowe lub użyć pytest do testowania poszczególnych modułów. Upewnij się, że dane testowe są odpowiednio przygotowane w katalogu `data/`.

## Autorzy
- **Dominik** - Główny developer

## Licencja
Ten projekt jest objęty licencją MIT - szczegóły w pliku LICENSE.
