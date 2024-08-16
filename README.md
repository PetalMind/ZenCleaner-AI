
# File Classifier Project

## Overview
Ten projekt zawiera narzędzia do klasyfikacji plików na podstawie ich atrybutów takich jak rozmiar, rozszerzenie itp. Projekt składa się z kilku modułów, które umożliwiają zbieranie danych, ich wstępne przetwarzanie, trenowanie modelu klasyfikującego oraz ocenę jego skuteczności. 

## Pliki
- `collect_data.py`: Zbiera dane o plikach z wybranego katalogu, tworząc zestaw danych zawierający ścieżkę pliku, jego rozmiar, rozszerzenie oraz etykietę klasyfikacyjną.
- `preprocess_data.py`: Wstępnie przetwarza zebrane dane, konwertując i normalizując je, aby były odpowiednie do trenowania modelu.
- `train_model.py`: Trenuje model klasyfikacyjny na podstawie przetworzonych danych i zapisuje wytrenowany model do pliku.
- `evaluate_model.py`: Ocena skuteczności wytrenowanego modelu przy użyciu zestawu testowego danych.
- `predict.py`: Używa wytrenowanego modelu do przewidywania klasyfikacji nowych plików.

## Instalacja
Aby uruchomić projekt, upewnij się, że masz zainstalowane wszystkie wymagane pakiety. Możesz je zainstalować przy użyciu poniższego polecenia:

```bash
pip install -r requirements.txt
```

## Użycie

### 1. Zbieranie danych
Aby zebrać dane o plikach z konkretnego katalogu, uruchom `collect_data.py`:

```bash
python collect_data.py <ścieżka_do_katalogu> <etykieta>
```

Przykład:

```bash
python collect_data.py /path/to/junk 0
```

### 2. Wstępne przetwarzanie danych
Przetwarzanie zebranych danych:

```bash
python preprocess_data.py
```

### 3. Trenowanie modelu
Trenowanie modelu na przetworzonych danych:

```bash
python train_model.py
```

### 4. Ocena modelu
Ocena modelu przy użyciu zestawu testowego:

```bash
python evaluate_model.py
```

### 5. Przewidywanie
Przewidywanie klasyfikacji dla nowych plików:

```bash
python predict.py <ścieżka_do_pliku>
```

## Autorzy
- **Twoje Imię** - Główny developer

## Licencja
Ten projekt jest objęty licencją MIT - szczegóły w pliku LICENSE.
